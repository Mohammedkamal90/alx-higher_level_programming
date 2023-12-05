#!/bin/bash
# Use curl to send a POST request with parameters and display the body of the response
curl -s -X POST -d "email=Test@gmail.com&subject=I will always be here for PLD" "$1"
