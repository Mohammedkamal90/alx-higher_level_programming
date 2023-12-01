#!/usr/bin/env bash
# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send a GET request and display the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | {
  read -r status_code
  if [ "$status_code" -eq 200 ]; then
    curl -s "$1"
  fi
}
