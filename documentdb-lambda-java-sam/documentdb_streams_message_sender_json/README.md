# documentdb-streams-message-sender

This project contains source code and supporting files for a Java application that you can use to input records into a streams enabled DocumentDB database/collection, such that DocumentDB streams can generate messages that can in turn be consumed by a Lambda function

- documentdb_streams_message_sender/src/main/java - Code for the application.
- documentdb_streams_message_sender/Commands - A file that contains the command to run this application so DocumentDB Streams messages can be generated to invoke the corresponding Lambda function

## Set-up and run this application

The steps required before this application can be run are

1) Install and configure a DocumentDB cluster (use AWS console or a Cloudformation template) - for detailed instructions look at the AWS documentation - https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html

2) Use the command wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem to download the global-bundle.pem file needed to connect to the DocumentDB cluster

3) Create a database and a collection in the DocumentDB cluster (Use standard MongoDB commands - https://www.mongodb.com/basics/create-database)

4) Create a Java Truststore as documented in the "Connecting with TLS Enabled" section of the document - https://docs.aws.amazon.com/documentdb/latest/developerguide/connect_programmatically.html - Look at the Java tab for detailed instructions

5) Create a secret in AWS Secrets Manager called AmazonDocumentDBCredentials - Choose a secret of type "Credentials for Amazon DocumentDB database" when creating the secret. Provide the username and password to connect to the DocumentDB database as had been specified at the time of cluster creation. Name this secret AmazonDocumentDBCredentials

6) Create another secret of type "Other type of secret" in AWS Secrets Manager called AmazonDocumentDBTruststore - In this secret, create two secret keys - 

	a) truststore - location of the truststore created in Step 4
	b) truststorepassword - the password for the truststore
	
7) Use the command specified in the documentdb_streams_message_sender/Commands file to generate DocumentDB Streams messages that can be consumed by the Lambda function. The command specified in the Commands file takes four parameters

	a) The DocumentDB database created in Step 3
	b) The DocumentDB collection created in Step 3
	c) A Unique String that can be used to identify the batch of DocumentDB Streams messages that will be generated
	d) The number of DocumentDB Streams messages to generate as part of this batch
	
8) If a Lambda function consumer of the DocumentDB Streams messages has already been deployed, then you should be able to see the content of the messages in the Lambda function logs in Cloudwatch