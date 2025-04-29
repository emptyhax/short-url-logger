#!/bin/bash

URL="http://localhost:5000/new"
TARGET_URL="https://github.com/slyhax"

curl -X POST $URL \
    -H "Content-Type: application/json" \
    -d "{\"url\": \"$TARGET_URL\"}"

