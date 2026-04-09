#!/bin/bash
set -e

echo "============================================"
echo " CVE-2024-52012 — Apache Solr Zip Slip Lab"
echo "============================================"
echo ""
echo " Solr 9.7.0 (standalone) on :8984"
echo " Vulnerable proxy on :8983"
echo ""

# Ensure configset directory exists
mkdir -p /var/solr/data/configsets

# Start the vulnerable proxy in the background
python3 /opt/vuln_proxy.py &
PROXY_PID=$!

# Give the proxy a moment to bind
sleep 1

echo "[*] Proxy started (PID $PROXY_PID)"
echo "[*] Starting Solr..."

# Start Solr on port 8984 (the proxy on 8983 is the exploit target)
exec solr-foreground -p 8984
