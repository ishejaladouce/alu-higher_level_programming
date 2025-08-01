#!/bin/bash
# Display body only if HTTP status code is 200
response=$(curl -s -w "%{http_code}" "$1"); echo "${response::-3}" | { [ "${response: -3}" == "200" ] && cat; }
