#!/bin/bash
# Fetch URL with redirects, show body only if final status is 200
response=$(curl -s -L -w "%{http_code}" "$1"); body=${response::-3}; code=${response: -3}; [ "$code" == "200" ] && echo "$body"
