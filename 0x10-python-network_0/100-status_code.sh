#!/usr/bin/env bash
# Check if URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send request and display only status code of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$status_code"
