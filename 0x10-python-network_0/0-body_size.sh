#!/usr/bin/env bash
# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send a request and display the size of the response body in bytes
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

if [ -z "$size" ]; then
  echo "Failed to retrieve the size of the body."
else
  echo "$size"
fi
