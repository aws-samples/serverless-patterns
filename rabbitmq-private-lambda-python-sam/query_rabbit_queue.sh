#!/bin/bash

# Retrieve RabbitMQ credentials from Secrets Manager
AWS_REGION=${AWS_REGION:-us-west-2}
SECRET_JSON=$(aws secretsmanager get-secret-value --secret-id AmazonRabbitMQCredentials --region "$AWS_REGION" --query SecretString --output text)
RABBITMQ_ADMIN_USER=$(echo "$SECRET_JSON" | jq -r .username)
RABBITMQ_PASSWORD=$(echo "$SECRET_JSON" | jq -r .password)

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

curl -sL -u "$RABBITMQ_ADMIN_USER:$RABBITMQ_PASSWORD" -H "Accept: application/json" "$rabbitmq_https_broker_endpoint/api/vhosts/RABBITMQ_VIRTUAL_HOST" | jq .

echo "########## End verifying if Virtual Host has been created ##########"

echo "########## Begin verifying if Exchange has been created ##########"

curl -sL -u "$RABBITMQ_ADMIN_USER:$RABBITMQ_PASSWORD" -H "Accept: application/json" "$rabbitmq_https_broker_endpoint/api/exchanges/RABBITMQ_VIRTUAL_HOST/RABBITMQ_EXCHANGE" | jq .

echo "########## End verifying if Exchange has been created ##########"

echo "########## Begin verifying if Queue has been created ##########"

curl -sL -u "$RABBITMQ_ADMIN_USER:$RABBITMQ_PASSWORD" -H "Accept: application/json" "$rabbitmq_https_broker_endpoint/api/queues/RABBITMQ_VIRTUAL_HOST/RABBITMQ_QUEUE_NAME" | jq .

echo "########## End verifying if Queue has been created ##########"

echo "########## Begin verifying if Queue has been bound to exchange ##########"

curl -sL -u "$RABBITMQ_ADMIN_USER:$RABBITMQ_PASSWORD" -H "Accept: application/json" "$rabbitmq_https_broker_endpoint/api/bindings/RABBITMQ_VIRTUAL_HOST/e/RABBITMQ_EXCHANGE/q/RABBITMQ_QUEUE_NAME" | jq .

echo "########## End verifying if Queue has been bound to exchange ##########"
