#!/bin/bash
# Displays body of response after being sent POST request
curl -sd 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
