#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    base_url = sys.argv[1]
    try:
        with urllib.request.urlopen(base_url) as res:
            data = res.read()
            print(data.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
