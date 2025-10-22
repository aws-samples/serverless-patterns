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

curl -i -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -X PUT $rabbitmq_https_broker_endpoint/api/vhosts/RABBITMQ_VIRTUAL_HOST
            
curl -i -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -X PUT -H "Content-type: application/json" -d '{"type": "fanout", "durable": true, "auto_delete": false, "internal": false}' $rabbitmq_https_broker_endpoint/api/exchanges/RABBITMQ_VIRTUAL_HOST/RABBITMQ_EXCHANGE
            
curl -i -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -X PUT -H "Content-type: application/json" -d '{"durable": true, "auto_delete": false}' $rabbitmq_https_broker_endpoint/api/queues/RABBITMQ_VIRTUAL_HOST/RABBITMQ_QUEUE_NAME
            
curl -i -u RABBITMQ_BROKER_ADMIN_USER:RABBITMQ_BROKER_PASSWORD -X POST -H "Content-type: application/json" -d '{"routing_key": "RABBITMQ_EXCHANGE-RABBITMQ_QUEUE_NAME"}' $rabbitmq_https_broker_endpoint/api/bindings/RABBITMQ_VIRTUAL_HOST/e/RABBITMQ_EXCHANGE/q/RABBITMQ_QUEUE_NAME