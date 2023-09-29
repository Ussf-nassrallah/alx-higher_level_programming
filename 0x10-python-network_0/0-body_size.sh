#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
#  and displays the size of the body of the response

url="$1"
key="Content-Length:"
curl -sI "$url" | grep "$key" | cut -d " " -f 2
