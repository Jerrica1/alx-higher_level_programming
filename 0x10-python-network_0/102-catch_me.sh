#!/bin/bash
# Displays 'You got me!' when makes request to 0.0.0.0:5000/catch_me
curl -X PUT -L -H "Origin: HolbertonSchool" -s 0.0.0.0:5000/catch_me -d 'user_id=98'
