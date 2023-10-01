#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
  displays the value of the X-Request-Id
"""


import sys
import urllib.request


def fetch_url():
    """ fetch url and displays the value of the X-Request-Id  """
    base_url = sys.argv[1]
    with urllib.request.urlopen(base_url) as response:
        headers = response.headers
        print(headers['X-Request-Id'])

if __name__ == "__main__":
    fetch_url()