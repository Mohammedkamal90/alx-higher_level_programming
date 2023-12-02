#!/bin/bash
#print status
curl -so /dev/null -w "%{Http_code}" $1
