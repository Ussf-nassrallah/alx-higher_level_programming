#!/bin/bash
# script that sends a GET req to the URL, and displays the body of the res
url="$1" hv="X-School-User-Id"; curl -s "$url" -H "$hv: 98"
