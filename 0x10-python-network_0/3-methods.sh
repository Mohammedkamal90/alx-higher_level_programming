#!/bin/bash
# Use curl to send an OPTIONS request and display the allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
