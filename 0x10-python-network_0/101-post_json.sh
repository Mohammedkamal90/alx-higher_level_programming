#!/bin/bash
# Use curl to send a JSON POST request and display the body of the response
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
