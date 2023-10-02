#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
 and displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    base_url = sys.argv[1]
    res = requests.get(base_url)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
