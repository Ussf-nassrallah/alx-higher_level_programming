#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""

import sys
import requests


def fetch_url():
    base_url = sys.argv[1]
    res = requests.get(base_url)
    print(res.headers.get('X-Request-Id'))


if __name__ == "__main__":
    fetch_url()
