#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
hd="Origin: HolbertonSchool"; curl -sL -X PUT -H "$hd" -d "user_id=98" 0.0.0.0:5000/catch_me
