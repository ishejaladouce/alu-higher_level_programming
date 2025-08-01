#!/bin/bash
# Fetch URL following redirects and show body only if final status code is 200
response=$(curl -s -L -w "%{http_code}" "$1")
body=${response::-3}
code=${response: -3}
if [ "$code" == "200" ]; then
    echo -n "$body"
fi
