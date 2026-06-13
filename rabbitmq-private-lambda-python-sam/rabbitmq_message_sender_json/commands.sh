#!/bin/bash

# Pass a random string as the first command-line argument to this shell script. It will be used to uniquely identify a batch of messages
# Pass an integer as the second command-line argument to this shell script < 500. For example if you want to send 100 messages, pass 100
# Example sh commands.sh firstbatch 100

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


java -classpath /home/ec2-user/serverless-patterns/rabbitmq-private-lambda-java-sam/rabbitmq_message_sender_json/target/json-rabbitmq-producer-0.0.1-SNAPSHOT.jar rabbitmq.producer.JsonRabbitMQProducer $broker_endpoint_without_port RABBITMQ_VIRTUAL_HOST RABBITMQ_EXCHANGE RABBITMQ_QUEUE_NAME $1 $2