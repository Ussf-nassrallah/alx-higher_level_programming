#!/bin/bash
# script that sends a JSON POST request to a URL, and display res
url = "$1"; curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$url"
