#!/usr/bin/env python3
"""Enable GitHub Pages - pass token as first argument"""
import sys, json, urllib.request, urllib.error

if len(sys.argv) < 2:
    print("Usage: python3 enable_pages.py <github_token>")
    sys.exit(1)

TOKEN = sys.argv[1]
REPO = "xiaohao7023/dupes-seo"

# Enable Pages
data = json.dumps({"source": {"branch": "main", "path": "/"}, "build_type": "actions"}).encode()
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json", "User-Agent": "Mozilla/5.0", "X-GitHub-Api-Version": "2022-11-28"}

try:
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/pages", data=data, headers=headers, method="POST")
    resp = urllib.request.urlopen(req)
    print("Pages enabled:", resp.read().decode())
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"POST ({e.code}): {body}")
    if e.code in (409, 422):
        # Already exists, try PUT to update
        req2 = urllib.request.Request(f"https://api.github.com/repos/{REPO}/pages", data=data, headers=headers, method="PUT")
        try:
            resp2 = urllib.request.urlopen(req2)
            print("Pages updated:", resp2.read().decode())
        except urllib.error.HTTPError as e2:
            print(f"PUT ({e2.code}): {e2.read().decode()}")

# Check status
try:
    req3 = urllib.request.Request(f"https://api.github.com/repos/{REPO}/pages", headers=headers)
    resp3 = urllib.request.urlopen(req3)
    info = json.loads(resp3.read().decode())
    print(f"\nURL: {info.get('html_url', 'N/A')}")
    print(f"Status: {info.get('status', 'N/A')}")
    print(f"Source: {info.get('source', {}).get('branch', 'N/A')}")
except urllib.error.HTTPError as e:
    print(f"GET ({e.code}): {e.read().decode()}")
