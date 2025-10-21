#!/bin/bash

# Pass a random string as the first command-line argument to this shell script. It will be used to uniquely identify a batch of messages
# Pass an integer as the second command-line argument to this shell script < 500. For example if you want to send 100 messages, pass 100
# Example sh commands.sh firstbatch 100

java -classpath /home/ec2-user/serverless-patterns/rabbitmq-private-lambda-java-sam/rabbitmq_message_sender_json/target/json-rabbitmq-producer-0.0.1-SNAPSHOT.jar rabbitmq.producer.JsonRabbitMQProducer RABBITMQ_BROKER_ENDPOINT RABBITMQ_VIRTUAL_HOST RABBITMQ_EXCHANGE RABBITMQ_QUEUE_NAME $1 $2