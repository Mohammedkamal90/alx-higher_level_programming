#!/usr/bin/env bash
# Check if both URL and filename are provided as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <URL> <filename>"
  exit 1
fi

# Read the file contents
json_data=$(cat "$2" 2>/dev/null)

# Check if the file contains valid JSON
if jq -e . >/dev/null 2>&1 <<<"$json_data"; then
  # Use curl to send a JSON POST request and display the body of the response
  curl -sX POST -H "Content-Type: application/json" -d "$json_data" "$1"
else
  echo "Not a valid JSON"
fi
