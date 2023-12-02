#!/bin/bash
# Use curl to send a request and display the size of the response body in bytes
curl -so /dev/null -w '%{Size_Download}\n' $1
