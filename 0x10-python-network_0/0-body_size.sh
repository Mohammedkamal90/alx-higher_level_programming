#!/usr/bin/env bash
# Use curl to send a request and display the size of the response body in bytes
curl -s1 "$1" | wc -c
