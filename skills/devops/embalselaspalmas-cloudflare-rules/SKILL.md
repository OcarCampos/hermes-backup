---
name: embalselaspalmas-cloudflare-rules
description: Cloudflare WAF firewall rules for embalselaspalmas.cl — geoblock CL-only + block WordPress attack vectors
---

# Embalses Las Palmas — Cloudflare Firewall Rules

Cloudflare WAF rules applied to embalselaspalmas.cl (WordPress site) after bot registration attack and security hardening.

## Rules Applied

### 1. Geoblock — Block International Traffic
**Purpose:** Site serves local CL community only, not worldwide.

```
(ip.src.country ne "CL" and not cf.client.bot)
```
**Action:** Block

### 2. Block XML-RPC & User Enumeration Endpoints
**Purpose:** Close known WordPress attack vectors used for bot intrusion.

```
(http.request.uri.path contains "/xmlrpc.php") or (http.request.uri.path contains "/wp-json/wp/v2/users" and http.request.method eq "POST")
```
**Action:** Block

## Context
- Bots were registering on the site → plugins updated, users deleted
- Open ends found during security review — not related to registration vector
- Decision made to geoblock entirely to CL to prevent future abuse
- Research done on best Cloudflare approach for geoblocking

## Verification
After applying rules in Cloudflare → Security panel → Firewall Rules:
1. Test from non-CL IP (or Cloudflare IP checker) — should get 403
2. Test `/xmlrpc.php` — should be blocked regardless of country
3. Test `/wp-json/wp/v2/users` POST — should be blocked
