#!/bin/bash
# Displays body from POST request of a JSON file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
