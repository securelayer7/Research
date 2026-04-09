#!/usr/bin/env python3
"""
CVE-2024-52012 Vulnerable Proxy
Replicates the exact behavior of FileSystemConfigSetService.uploadFileToConfig:
  - Receives ZIP via ConfigSet Upload API
  - Extracts entries WITHOUT path sanitization (Zip Slip)
  - All other requests are proxied to real Solr
"""

import http.server
import urllib.request
import urllib.error
import urllib.parse
import zipfile
import io
import os
import json
import sys

SOLR_BACKEND = "http://localhost:8984"
CONFIGSET_BASE = "/var/solr/data/configsets"


class VulnHandler(http.server.BaseHTTPRequestHandler):

    def handle_configset_upload(self, params):
        """Mimics FileSystemConfigSetService.uploadFileToConfig — NO path validation."""
        name = params.get("name", ["default"])[0]
        config_dir = os.path.join(CONFIGSET_BASE, name)
        os.makedirs(config_dir, exist_ok=True)

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            zf = zipfile.ZipFile(io.BytesIO(body))
            written = []
            for entry in zf.namelist():
                # ============================================================
                # VULNERABLE: os.path.join resolves ".." without validation!
                # This is the exact behavior of the unpatched Solr code:
                #   Path file = configDir.resolve(filePath);
                #   Files.write(file, data);
                # ============================================================
                file_path = os.path.normpath(os.path.join(config_dir, entry))
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "wb") as f:
                    f.write(zf.read(entry))
                written.append(file_path)
                print(f"[VULN] Wrote: {file_path}", flush=True)

            resp = json.dumps({
                "responseHeader": {"status": 0, "QTime": 1},
                "success": {"files_written": written},
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json;charset=utf-8")
            self.send_header("Content-Length", str(len(resp)))
            self.end_headers()
            self.wfile.write(resp)

        except Exception as e:
            resp = json.dumps({"responseHeader": {"status": 500}, "error": {"msg": str(e), "code": 500}}).encode()
            self.send_response(500)
            self.send_header("Content-Type", "application/json;charset=utf-8")
            self.end_headers()
            self.wfile.write(resp)

    # --- request routing ---------------------------------------------------

    def _is_configset_upload(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        return (
            parsed.path == "/solr/admin/configs"
            and params.get("action", [""])[0].upper() == "UPLOAD"
        )

    def do_POST(self):
        if self._is_configset_upload():
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            self.handle_configset_upload(params)
        else:
            self._proxy()

    def do_GET(self):
        self._proxy()

    def do_PUT(self):
        self._proxy()

    def do_DELETE(self):
        self._proxy()

    def do_HEAD(self):
        self._proxy()

    # --- transparent reverse proxy to real Solr ----------------------------

    def _proxy(self):
        url = SOLR_BACKEND + self.path
        headers = {k: v for k, v in self.headers.items() if k.lower() not in ("host",)}

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else None

        req = urllib.request.Request(url, data=body, headers=headers, method=self.command)
        try:
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
                self.send_response(resp.status)
                for k, v in resp.getheaders():
                    if k.lower() not in ("transfer-encoding", "connection"):
                        self.send_header(k, v)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception:
            self.send_response(502)
            self.end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(f"[proxy] {self.address_string()} - {format % args}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    os.makedirs(CONFIGSET_BASE, exist_ok=True)
    server = http.server.HTTPServer(("0.0.0.0", 8983), VulnHandler)
    print(f"[*] Vulnerable ConfigSet proxy on :8983 -> Solr on :8984", flush=True)
    print(f"[*] ConfigSet base: {CONFIGSET_BASE}", flush=True)
    server.serve_forever()
