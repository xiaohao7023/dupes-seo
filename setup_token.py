#!/usr/bin/env python3
"""Setup: write GitHub token to file. Run this with the token as argument."""
import sys
if len(sys.argv) < 2:
    print("Usage: python3 setup_token.py <token>")
    sys.exit(1)
with open("/home/guotuzi/.github_token", "w") as f:
    f.write(sys.argv[1].strip())
print("Token saved.")
