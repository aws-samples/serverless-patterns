#!/bin/bash

external_api_url=https://example.com
service1_url=https://example.com/service1
service2_url=https://example.com/service2

while true; do
  current_time=$(date +"%T")
  echo "[$current_time] Sending requests ..."
  curl "$external_api_url"
  echo -e ""
  curl "$service1_url"
  echo -e ""
  curl "$service2_url"
  echo -e ""
  echo -e "----------------------------------------"
  sleep 5
done
