#!/bin/bash

#This command can be used to find messages in the queue created for the Lambda function
#Modify the below command to use the activemq client to execute other commands on the cluster

/home/ec2-user/activemq_client/apache-activemq-5.18.6/bin/activemq browse --amqurl ACTIVEMQ_BROKER_ENDPOINT_ONE --user ACTIVEMQ_BROKER_ADMIN_USER --password ACTIVEMQ_BROKER_PASSWORD ACTIVEMQ_QUEUE_NAME


#Uncomment and use the below command if you get a "Broker not available at:" message with the first broker endpoint

#/home/ec2-user/activemq_client/apache-activemq-5.18.6/bin/activemq browse --amqurl ACTIVEMQ_BROKER_ENDPOINT_TWO --user ACTIVEMQ_BROKER_ADMIN_USER --password ACTIVEMQ_BROKER_PASSWORD ACTIVEMQ_QUEUE_NAME