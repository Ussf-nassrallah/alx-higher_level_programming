#!/bin/bash
# script that sends a GET req to the URL, and displays the body of the response
url="$1"; curl -sfL "$url"
