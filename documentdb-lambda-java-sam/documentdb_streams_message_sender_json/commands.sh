#!/bin/bash

# Pass a random string as the first command-line argument to this shell script. It will be used to uniquely identify a batch of messages
# Pass an integer as the second command-line argument to this shell script < 500. For example if you want to send 100 messages, pass 100
# Example sh commands.sh firstbatch 100

java -classpath /home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_message_sender_json/target/json-documentdb-producer-0.0.1-SNAPSHOT.jar documentdb.streams.producer.DocumentDBStreamsProducer DOCDB_DATABASE DOCDB_COLLECTION $1 $2