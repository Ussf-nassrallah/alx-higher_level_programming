#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


def fetch_url():
    base_url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(base_url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")


if __name__ == "__main__":
    fetch_url()
