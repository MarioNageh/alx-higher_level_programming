#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url)
    print(req.headers["X-Request-Id"])
