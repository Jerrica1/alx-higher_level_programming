#!/bin/bash
# Displays the status of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
