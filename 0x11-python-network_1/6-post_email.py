#!/usr/bin/python3
"""
script that takes in a URL and an email address,
 sends a POST request to the passed URL with the email as a parameter,
  and finally displays the body of the response.
"""

import sys
import requests


def post_email():
    base_url = sys.argv[1]
    values = {'email': sys.argv[2]}
    res = requests.post(base_url, data=values)
    print(res.text)


if __name__ == "__main__":
    post_email()