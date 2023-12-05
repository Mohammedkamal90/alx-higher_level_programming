#!/bin/bash
# Use curl to send an OPTIONS request and display the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
