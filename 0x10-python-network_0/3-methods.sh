#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
url="$1" key="Allow:"; curl -sI "$url" | grep "$key" | cut -d " " -f 2-
