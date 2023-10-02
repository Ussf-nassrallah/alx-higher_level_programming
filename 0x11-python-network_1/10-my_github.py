#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
  and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    base_url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    res = requests.get(base_url, auth=auth)
    user_id = res.json().get('id')

    print(user_id)
