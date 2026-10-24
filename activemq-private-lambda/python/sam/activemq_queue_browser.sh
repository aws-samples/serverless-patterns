#!/bin/bash

# This script can be used to browse messages in the ActiveMQ queue
# It uses the activemq command-line tool installed on the EC2 instance

/home/ec2-user/activemq_client/apache-activemq-5.18.6/bin/activemq browse --amqurl "ssl://ACTIVEMQ_BROKER_ENDPOINT_ONE" --user ACTIVEMQ_BROKER_ADMIN_USER --password ACTIVEMQ_BROKER_PASSWORD ACTIVEMQ_QUEUE_NAME

/home/ec2-user/activemq_client/apache-activemq-5.18.6/bin/activemq browse --amqurl "ssl://ACTIVEMQ_BROKER_ENDPOINT_TWO" --user ACTIVEMQ_BROKER_ADMIN_USER --password ACTIVEMQ_BROKER_PASSWORD ACTIVEMQ_QUEUE_NAME
