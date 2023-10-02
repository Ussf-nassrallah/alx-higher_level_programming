#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
  to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    base_url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    values = {'p': letter}
    res = requests.post(base_url, data=values)
    try:
        data = res.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
