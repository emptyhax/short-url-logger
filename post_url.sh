#!/bin/bash

URL="http://localhost:5000/new"
TARGET_URL="https://discord.com/"

curl -X POST $URL \
    -H "Content-Type: application/json" \
    -d "{\"url\": \"$TARGET_URL\"}"

