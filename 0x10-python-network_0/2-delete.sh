#!/usr/bin/env bash
# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send a DELETE request and display the body of the response
curl -X DELETE -s "$1"
