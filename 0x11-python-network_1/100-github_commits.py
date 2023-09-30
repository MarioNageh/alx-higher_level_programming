#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    headers = {"Accept": "application/vnd.github.v3+json",
               "X-GitHub-Api-Version": "2022-11-28",
               }
    response = requests.get(url, headers=headers)
    body = response.json()
    body = body[:10]
    try:
        for commit in body:
            print(commit.get("sha"), end=": ")
            print(commit.get("commit").get("author").get("name"))
    except Exception as e:
        pass
