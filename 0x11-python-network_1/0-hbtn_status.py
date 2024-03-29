#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


def fetch_url():
    """ fetch url and display the response """
    base_url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(base_url) as response:
        data = response.read()
        # display the response
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode()}")


if __name__ == "__main__":
    fetch_url()
