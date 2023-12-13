#!/bin/sh

printf "Sending HTTP GET request to: %s ...\n" "${TARGET_ENDPOINT_URL}"
while true; do
    curl --max-time 10 -sS -X GET "${TARGET_ENDPOINT_URL}"
    printf "\n"
    sleep 5
done
