#!/bin/bash
# script that sends a GET req to the URL, and displays the body of the res
url="$1"; curl -s "$url" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
