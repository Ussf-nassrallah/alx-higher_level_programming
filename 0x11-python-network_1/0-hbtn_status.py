# !/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

base_url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(base_url) as response:
    data = response.read()

# print output
print("Body response:")
print(f"    - type: {type(data)}")
print(f"    - content: {data}")
print(f"    - utf8 content: {data.decode()}")