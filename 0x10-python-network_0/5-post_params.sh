#!/usr/bin/env bash

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Define the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with parameters and display the body of the response
curl -s -X POST -d "email=$email&subject=$subject" "$1"
