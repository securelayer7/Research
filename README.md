<p align="center">
  <img src="assets/banner.png" alt="SecureLayer7 Research Lab" width="800"/>
</p>

<p align="center">
  <b>Vulnerability Research & CVE Analysis</b><br>
  <sub>SecureLayer7 Security Research Team</sub>
</p>

<p align="center">
  <a href="#published-research"><img src="https://img.shields.io/badge/CVEs_Analyzed-14-red?style=for-the-badge"/></a>
  <a href="#published-research"><img src="https://img.shields.io/badge/Critical-9-darkred?style=for-the-badge"/></a>
  <a href="#published-research"><img src="https://img.shields.io/badge/High-5-orange?style=for-the-badge"/></a>
  <a href="https://blog.securelayer7.net"><img src="https://img.shields.io/badge/Blog-securelayer7.net-blue?style=for-the-badge"/></a>
</p>

---

## About

> SecureLayer7's research team focuses on identifying, analyzing, and responsibly disclosing vulnerabilities across widely-used software. This repository serves as a centralized archive of our published CVE research, proof-of-concept exploits, and lab environments.

---

## Published Research

| # | CVE ID | Product | Type | Severity | Analysis |
|:-:|--------|---------|------|:--------:|----------|
| 1 | CVE-2023-38831 | WinRAR | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Zero-Day RCE via DarkMe](https://blog.securelayer7.net/analysis-of-cve-2023-38831-zero-day-vulnerability-in-winrar) |
| 2 | CVE-2023-22518 | Atlassian Confluence | Auth Bypass | ![Critical](https://img.shields.io/badge/-Critical_9.1-red) | [Authentication Bypass](https://blog.securelayer7.net/confluence-authentication-bypass/) |
| 3 | CVE-2023-26360 | Adobe ColdFusion | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Unauthenticated RCE](https://blog.securelayer7.net/unauthorized-rce-in-adobe-coldfusion/) |
| 4 | CVE-2020-9496 / CVE-2023-49070 / CVE-2023-51467 | Apache OFBiz | RCE + Auth Bypass | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Multiple Vulnerabilities](https://blog.securelayer7.net/ofbiz-authentication-bypass-cve-2023-51467/) |
| 5 | CVE-2024-23897 | Jenkins | Arbitrary File Read | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Arbitrary File Read](https://blog.securelayer7.net/arbitrary-file-read-in-jenkins/) |
| 6 | CVE-2023-39143 | PaperCut | RCE | ![High](https://img.shields.io/badge/-High_8.4-orange) | [Remote Code Execution](https://blog.securelayer7.net/analysis-of-papercut-rce/) |
| 7 | CVE-2024-27348 | Apache HugeGraph | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Sandbox Bypass RCE](https://blog.securelayer7.net/remote-code-execution-in-apache-hugegraph/) |
| 8 | CVE-2024-25065 | Apache OFBiz | Path Traversal | ![High](https://img.shields.io/badge/-High_7.5-orange) | [Auth Bypass via Path Traversal](https://blog.securelayer7.net/security-bypass-in-apache-ofbiz/) |
| 9 | CVE-2024-38856 | Apache OFBiz | RCE | ![High](https://img.shields.io/badge/-High_8.2-orange) | [File Read to RCE](https://blog.securelayer7.net/cve-2024-38856-apache-ofbiz-rce/) |
| 10 | CVE-2024-22263 | Spring Cloud Data Flow | Arbitrary File Write | ![High](https://img.shields.io/badge/-High_8.8-orange) | [Arbitrary File Writing](https://blog.securelayer7.net/spring-cloud-data-flow-exploit/) |
| 11 | CVE-2024-39877 | Apache Airflow | Code Execution | ![High](https://img.shields.io/badge/-High_8.8-orange) | [Jinja2 Template Injection](https://blog.securelayer7.net/arbitrary-code-execution-in-apache-airflow/) |
| 12 | CVE-2024-31204 / CVE-2024-30270 | Mailcow | XSS + Path Traversal | ![High](https://img.shields.io/badge/-High_8.0-orange) | [XSS & Path Traversal](https://blog.securelayer7.net/xss-and-path-traversal-exploits-in-mailcow/) |
| 13 | CVE-2024-54676 | Apache OpenMeetings | RCE | ![Critical](https://img.shields.io/badge/-Critical_9.8-red) | [Deserialization RCE](CVE-2024-54676/) |

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
