#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""


import sys
import requests


if __name__ == "__main__":
    rep_name = sys.argv[1]
    owner_name = sys.argv[2]
    base_url = f"https://api.github.com/repos/{owner_name}/{rep_name}/commits"

    res = requests.get(base_url)
    commits = res.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                commits[index].get('sha'),
                commits[index].get("commit").get("author").get("name")
            ))
    except IndexError:
        pass
