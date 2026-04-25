<p align="center">
  <a href="https://securelayer7.net">
    <img src="https://avatars.githubusercontent.com/u/14994455?v=4" alt="SecureLayer7" width="150"/>
  </a>
</p>

<h1 align="center">SecureLayer7 Research</h1>

<p align="center">
  <a href="#published-research"><img src="https://img.shields.io/badge/CVEs_Analyzed-25-red?style=for-the-badge"/></a>
  <a href="#published-research"><img src="https://img.shields.io/badge/Critical-13-darkred?style=for-the-badge"/></a>
  <a href="#published-research"><img src="https://img.shields.io/badge/High-12-orange?style=for-the-badge"/></a>
  <a href="https://blog.securelayer7.net"><img src="https://img.shields.io/badge/Blog-securelayer7.net-blue?style=for-the-badge"/></a>
</p>

---

## About

> SecureLayer7's research team focuses on identifying, analyzing, and responsibly disclosing vulnerabilities across widely-used software. This repository serves as a centralized archive of our published CVE research, proof-of-concept exploits, and lab environments.

---

## Published Research

| # | Published | CVE ID | Product | Type | Severity | Analysis |
|:-:|-----------|--------|---------|------|:--------:|----------|
| 1 | 2023-09-24 | CVE-2023-38831 | WinRAR | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Zero-Day RCE via DarkMe](https://blog.securelayer7.net/analysis-of-cve-2023-38831-zero-day-vulnerability-in-winrar) |
| 2 | 2023-12-11 | CVE-2023-22518 | Atlassian Confluence | Auth Bypass | ![Critical](https://img.shields.io/badge/-Critical_9.1-red) | [Authentication Bypass](https://blog.securelayer7.net/confluence-authentication-bypass/) |
| 3 | 2024-01-10 | CVE-2023-26360 | Adobe ColdFusion | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Unauthenticated RCE](https://blog.securelayer7.net/unauthorized-rce-in-adobe-coldfusion/) |
| 4 | 2024-01-30 | CVE-2020-9496 / CVE-2023-49070 / CVE-2023-51467 | Apache OFBiz | RCE + Auth Bypass | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Multiple Vulnerabilities](https://blog.securelayer7.net/ofbiz-authentication-bypass-cve-2023-51467/) |
| 5 | 2024-03-11 | CVE-2024-23897 | Jenkins | Arbitrary File Read | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Arbitrary File Read](https://blog.securelayer7.net/arbitrary-file-read-in-jenkins/) |
| 6 | 2024-05-24 | CVE-2023-39143 | PaperCut | RCE | ![High](https://img.shields.io/badge/-High_8.4-orange) | [Remote Code Execution](https://blog.securelayer7.net/analysis-of-papercut-rce/) |
| 7 | 2024-06-05 | CVE-2024-27348 | Apache HugeGraph | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Sandbox Bypass RCE](https://blog.securelayer7.net/remote-code-execution-in-apache-hugegraph/) |
| 8 | 2024-06-19 | CVE-2024-25065 | Apache OFBiz | Path Traversal | ![High](https://img.shields.io/badge/-High_7.5-orange) | [Auth Bypass via Path Traversal](https://blog.securelayer7.net/security-bypass-in-apache-ofbiz/) |
| 9 | 2024-07-02 | CVE-2024-31204 / CVE-2024-30270 | Mailcow | XSS + Path Traversal | ![High](https://img.shields.io/badge/-High_8.0-orange) | [XSS & Path Traversal](https://blog.securelayer7.net/xss-and-path-traversal-exploits-in-mailcow/) |
| 10 | 2024-08-01 | CVE-2024-39877 | Apache Airflow | Code Execution | ![High](https://img.shields.io/badge/-High_8.8-orange) | [Jinja2 Template Injection](https://blog.securelayer7.net/arbitrary-code-execution-in-apache-airflow/) |
| 11 | 2024-08-22 | CVE-2024-22263 | Spring Cloud Data Flow | Arbitrary File Write | ![High](https://img.shields.io/badge/-High_8.8-orange) | [Arbitrary File Writing](https://blog.securelayer7.net/spring-cloud-data-flow-exploit/) |
| 12 | 2024-09-26 | CVE-2024-38856 | Apache OFBiz | RCE | ![High](https://img.shields.io/badge/-High_8.2-orange) | [File Read to RCE](https://blog.securelayer7.net/cve-2024-38856-apache-ofbiz-rce/) |
| 13 | 2025-12-05 | CVE-2025-55182 | React / Next.js | Prototype Pollution | ![Critical](https://img.shields.io/badge/-Critical_10.0-red) | [Prototype Pollution](https://blog.securelayer7.net/cve-2025-55182/) |
| 14 | 2025-12-21 | CVE-2025-68613 | n8n | RCE (Expression Injection) | ![Critical](https://img.shields.io/badge/-Critical_9.9-red) | [Expression Injection RCE](https://blog.securelayer7.net/cve-2025-68613-n8n-rce-exploitation/) |
| 15 | 2026-02-04 | CVE-2026-25049 | n8n | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.4-red) | [Remote Code Execution](https://blog.securelayer7.net/cve-2026-25049/) |
| 16 | 2026-03-02 | Pending | IPVanish VPN (macOS) | Local Privilege Escalation | ![High](https://img.shields.io/badge/-High_8.8-orange) | [macOS Privilege Escalation](https://blog.securelayer7.net/ipvanish-vpn-macos-privilege-escalation/) |
| 17 | 2026-03-02 | — | DeepChat (Electron) | RCE via XSS / `openExternal` | ![Critical](https://img.shields.io/badge/-Critical-red) | [openExternal RCE via XSS](https://blog.securelayer7.net/deepchat-openexternal-rce-via-xss-in-electron/) |
| 18 | 2026-03-06 | CVE-2026-22708 / CVE-2026-25253 | OpenClaw | Prompt Injection + Auth Bypass | ![High](https://img.shields.io/badge/-High_8.8-orange) | [ClawdBot VS Code Trojan & OpenClaw Risks](https://blog.securelayer7.net/clawdbot-vs-code-trojan-openclaw-security/) |
| 19 | 2026-03-19 | CVE-2026-22729 | Spring AI (PgVectorStore) | JSONPath Injection | ![High](https://img.shields.io/badge/-High_8.6-orange) | [JSONPath Injection](https://blog.securelayer7.net/cve-2026-22729-jsonpath-injection-spring-ai-pgvectorstore/) |
| 20 | 2026-03-19 | CVE-2026-22730 | Spring AI (MariaDB Vector Store) | SQL Injection | ![High](https://img.shields.io/badge/-High_8.8-orange) | [SQL Injection](https://blog.securelayer7.net/cve-2026-22730-sql-injection-spring-ai-mariadb/) |
| 21 | 2026-03-23 | CVE-2026-24291 | Windows Registry | Privilege Escalation | ![Critical](https://img.shields.io/badge/-Critical-red) | [RegPwn](https://blog.securelayer7.net/cve-2026-24291-regpwn-windows-privilege-escalation/) |
| 22 | 2026-03-26 | CVE-2024-54676 | Apache OpenMeetings | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Deserialization RCE](https://blog.securelayer7.net/cve-2024-54676-apache-openmeetings-openjpa-rce/) |
| 23 | 2026-03-31 | CVE-2025-59489 | Unity Hub (macOS) | DyLib Injection / TCC Bypass | ![High](https://img.shields.io/badge/-High_8.4-orange) | [TCC Bypass via DyLib Injection](https://blog.securelayer7.net/cve-2025-59489-unity-hub-macos-tcc-bypass-dylib-injection/) |
| 24 | 2026-04-09 | CVE-2024-52012 | Apache Solr | Path Traversal RCE | ![Critical](https://img.shields.io/badge/-Critical-red) | [Zip Slip RCE](https://blog.securelayer7.net/cve-2024-52012-apache-solr-zip-slip-rce-attack/) |
| 25 | 2026-04-20 | CVE-2025-57738 | Apache Syncope | Groovy Injection RCE | ![High](https://img.shields.io/badge/-High_7.2-orange) | [Groovy Injection RCE](https://blog.securelayer7.net/cve-2025-57738-apache-syncope-groovy-rce/) |

---

## Contact

| | |
|:--|:--|
| **Website** | [securelayer7.net](https://securelayer7.net) |
| **Blog** | [blog.securelayer7.net](https://blog.securelayer7.net) |
| **Twitter** | [@securelayer7](https://twitter.com/securelayer7) |
| **Disclosure** | Coordinated 90-day responsible disclosure policy |

---

<p align="center">
  <sub>All research is conducted responsibly. Vulnerabilities are reported to vendors before public disclosure.</sub>
</p>
