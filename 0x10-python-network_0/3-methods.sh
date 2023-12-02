#!/bin/bash

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send an OPTIONS request and display the allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
