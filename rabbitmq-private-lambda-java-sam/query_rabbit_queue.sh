#!/bin/bash

original_broker_endpoint="RABBITMQ_BROKER_ENDPOINT"

amqps_prefix="amqps://"

# Remove the prefix from the beginning of the string
broker_endpoint_without_amqps="${original_broker_endpoint#$amqps_prefix}"

# Print the result
echo "original_broker_endpoint: $original_broker_endpoint"
echo "broker_endpoint_without_amqps: $broker_endpoint_without_amqps"

port_suffix=":5671"
broker_endpoint_without_port="${broker_endpoint_without_amqps%${port_suffix}}"
echo "broker_endpoint_without_port: $broker_endpoint_without_port"
            
https_prefix="https://"

rabbitmq_https_broker_endpoint="$https_prefix$broker_endpoint_without_port"
echo "rabbitmq_https_broker_endpoint=$rabbitmq_https_broker_endpoint"

curl -sL -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/vhosts/RABBITMQ_VIRTUAL_HOST

curl -sL -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/exchanges/RABBITMQ_VIRTUAL_HOST/RABBITMQ_EXCHANGE

curl -sL -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/queues/RABBITMQ_VIRTUAL_HOST/RABBITMQ_QUEUE_NAME

curl -sL -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/bindings/RABBITMQ_VIRTUAL_HOST/e/RABBITMQ_EXCHANGE/q/RABBITMQ_QUEUE_NAME