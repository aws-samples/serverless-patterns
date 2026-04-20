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

echo "########## Begin verifying if Virtual Host has been created ##########"

curl -sL -u rabbitmqadmin:rabbitmqPassword123 -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/vhosts/RabbitMQVirtualHost | jq .

echo "########## End verifying if Virtual Host has been created ##########"

echo "########## Begin verifying if Exchange has been created ##########"

curl -sL -u rabbitmqadmin:rabbitmqPassword123 -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/exchanges/RabbitMQVirtualHost/RabbitMQExchange | jq .

echo "########## End verifying if Exchange has been created ##########"

echo "########## Begin verifying if Queue has been created ##########"

curl -sL -u rabbitmqadmin:rabbitmqPassword123 -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/queues/RabbitMQVirtualHost/RabbitMQJavaLambdaQueue | jq .

echo "########## End verifying if Queue has been created ##########"

echo "########## Begin verifying if Queue has been bound to exchange ##########"

curl -sL -u rabbitmqadmin:rabbitmqPassword123 -H "Accept: application/json" $rabbitmq_https_broker_endpoint/api/bindings/RabbitMQVirtualHost/e/RabbitMQExchange/q/RabbitMQJavaLambdaQueue | jq .

echo "########## End verifying if Queue has been bound to exchange ##########"