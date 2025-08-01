#!/bin/bash
# Send request to URL and display body size in bytes
curl -s "$1" | wc -c
