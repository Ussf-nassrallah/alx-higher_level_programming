#!/bin/bash
# Bash script that sends a DELETE request to the URL
url="$1"; curl -s "$url" -X DELETE
