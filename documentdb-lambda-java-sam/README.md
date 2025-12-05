# Java AWS Lambda Amazon DocumentDB Streams consumer, using AWS SAM

This pattern is an example of a AWS Lambda function written in Java that consumes messages from Amazon DocumentDB Streams. The pattern demonstrates how a SAM project can be configured to deploy an AWS Lambda function written in Java with an Amazon DocumentDB event trigger. The pattern demonstrates how Amazon DocumentDB streams can be parsed in an AWS Lambda function and the parsed content output to an Amazon DynamoDB table. The pattern provides an AWS CloudFormation template to install and set-up an Amazon DocumentDB cluster. The CloudFormation template also installs an Amazon EC2 instance with tools necessary to configure the Amazon DocumentDB cluster to generate Amazon DocumentDB streams and configuration needed by a Java producer that can generate the Amazon DocumentDB streams.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/src/main/java - Code for the application's Lambda function that will listen for Amazon DocumentDB Streams messages and write them to a Amazon DynamoDB table
- documentdb_streams_message_sender_json/src/main/java - Code for adding documents in a Amazon DocumentDB collection that generate Amazon DocumentDB stream records
- documentdb_streams_consumer_dynamo_sam/template_original.yaml - A template that defines the application's Lambda function to be used by SAM to deploy the function
- DocumentDBAndMongoClientEC2.yaml - An AWS CloudFormation template file that can be used to deploy an Amazon DocumentDB cluster and also deploy an Amazon EC2 instance with all prerequisites installed, so you can directly build and deploy the Lambda function and test it out.
- connect_to_mongo_shell.sh - A shell script that can be used to connect to the Amazon DocumentDB cluster using the mongosh tool
- docdb_db_collection.sh - A shell script that will be used to create a database and a collection inside the Amazon DocumentDB cluster. The lambda function's event listener will be configured to listen for change stream events on this database and collection
- java_keystore_script.sh - A shell script that will be used to create a Java keystore file that will be required by the Sender program that will connect to the Amazon DocumentDB cluster and insert JSON documents in the created collection, which generate stream records for the Lambda function. The Java keystore is required to programmatically connect to the Amazon DocumentDB cluster
- mongodb-org-8.0.repo - This file is required to install mongosh tool on the EC2 instance. mongosh is a command-line tool used to connect to the Amazon DocumentDB cluster to perform administrative tasks, and CRUD operations on the Amazon DocumentDB cluster
- mongodbcolcreate.js - This file will be used to create a database and a collection inside the Amazon DocumentDB cluster. In order to programatically use the mongosh tool, a .js file needs to be passed as a --file argument to mongosh.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the Cloudformation template to create the Amazon DocumentDB Cluster and Client Amazon EC2 instance

* [Run the Cloudformation template using the file DocumentDBAndMongoClientEC2.yaml] - You can go to the AWS Cloudformation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the Cloudformation stack to be created. This CloudFormation template will create an Amazon DocumentDB cluster. It will also create an EC2 instance that you can use as a client.

* [Connect to the EC2 instance] - Once the CloudFormation stack is created, you can go to the EC2 console and connect to the instance using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab. In case you are using SSM Instance connect, you are not initially placed in the home directory. If you connect as ssm-user, you need to sudo su to ec2-user for this to work.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running post creation. 

The EC2 instance that was created by running the CloudFormation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications.

* [Check if the database and cluster are available] - Once you are inside the EC2 instance, you should be in the /home/ec2-user folder. cd to the mongoshell folder and then run ./connect_to_mongo_shell.sh. This connects the mongosh tool to the Amazon DocumentDB cluster created by the CloudFormation template. Once inside the mongosh, you can issue commands like show dbs to see if the database was created, use <database name> to switch to the created database, and then show collections to see if the collection was created. If you did not modify the defaults in the CloudFormation template, then the name of the database should be DocumentDBJavaLambdaDB and the name of the collection should be DocumentDBJavaLambdaCollection


## Pre-requisites to Deploy the sample Lambda function

* Java - On the EC2 machine, we have installed the version of Java that you selected. We have installed Amazon Corrretto JDK of the version that you had selected at the time of specifying the input parameters in the Cloudformation template. At the time of publishing this pattern, only Java versions 11, 17 and 21 are supported by AWS SAM
* Maven - On the EC2 machine, we have installed Maven (https://maven.apache.org/install.html)
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

We have also cloned the Github repository for serverless-patterns on the EC2 machine already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/documentdb-lambda-java-sam
    ```

## Use the SAM CLI to build and deploy the lambda function

Make sure you are connected to the EC2 instance as mentioned in the "Connect to the EC2 instance" step above

Build your application with the `sam build` command.

```bash
cd documentdb_streams_consumer_dynamo_sam
sam build
```

The SAM CLI installs dependencies defined in `documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

```

## Test the build locally

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

You should see a response such as the below:

```
***** Begin sam local invoke response *****

Mounting                                                                                                                                               
/home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_consumer_dynamo_sam/.aws-sam/build/LambdaDocumentDBStreamsConsumerJava
Function as /var/task:ro,delegated, inside runtime container                                                                                           
SAM_CONTAINER_ID: c0e42e24e4e3d1e515960af9eaecd1a59d11f8cb03f640bd4b789635e97a5edb                                                                     
START RequestId: cd50e0ee-7859-4d70-8265-a0b3afa7ce7a Version: $LATEST
Picked up JAVA_TOOL_OPTIONS: -XX:+TieredCompilation -XX:TieredStopAtLevel=1
Begin Event *************Message = DocumentDBStreamMessage [eventSourceArn=arn:aws:rds:us-west-2:123456789012:cluster:lambdaeventsourcedocumentdbcluster, eventSource=aws:docdb, events=[EventElement [event=EventEvent [_id=_ID [_data=0164ad054b0000000a010000000a0000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060683, i=10]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-1], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-1, firstname=John, lastname=Doe, street=4 B Blue Ridge Blvd, city=Brighton, county=Livingston, state=MI, zip=48116, homePhone=810-292-9388, cellPhone=810-374-9840, email=josephine_darakjy@darakjy.org, company="Chanay, Jeffrey A Esq", website=http://www.chanayjeffreyaesq.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000201000000020000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=2]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-2], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-2, firstname=John, lastname=Doe, street=8 W Cerritos Ave #54, city=Bridgeport, county=Gloucester, state=NJ, zip=8014, homePhone=856-636-8749, cellPhone=856-264-4130, email=art@venere.org, company="Chemel, James L Cpa", website=http://www.chemeljameslcpa.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000301000000030000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=3]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-3], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-3, firstname=John, lastname=Doe, street=639 Main St, city=Anchorage, county=Anchorage, state=AK, zip=99501, homePhone=907-385-4412, cellPhone=907-921-2010, email=lpaprocki@hotmail.com, company=Feltz Printing Service, website=http://www.feltzprintingservice.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000401000000040000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=4]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-4], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-4, firstname=Jane, lastname=Doe, street=34 Center St, city=Hamilton, county=Butler, state=OH, zip=45011, homePhone=513-570-1893, cellPhone=513-549-4561, email=donette.foller@cox.net, company=Printing Dimensions, website=http://www.printingdimensions.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000501000000050000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=5]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-5], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-5, firstname=John, lastname=Doe, street=3 Mcauley Dr, city=Ashland, county=Ashland, state=OH, zip=44805, homePhone=419-503-2484, cellPhone=419-800-6759, email=simona@morasca.com, company="Chapman, Ross E Esq", website=http://www.chapmanrosseesq.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000601000000060000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=6]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-6], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-6, firstname=John, lastname=Doe, street=7 Eads St, city=Chicago, county=Cook, state=IL, zip=60632, homePhone=773-573-6914, cellPhone=773-924-8565, email=mitsue_tollner@yahoo.com, company=Morlong Associates, website=http://www.morlongassociates.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000701000000070000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=7]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-7], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-7, firstname=John, lastname=Doe, street=7 W Jackson Blvd, city=San Jose, county=Santa Clara, state=CA, zip=95111, homePhone=408-752-3500, cellPhone=408-813-1105, email=leota@hotmail.com, company=Commercial Press, website=http://www.commercialpress.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000801000000080000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=8]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-8], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-8, firstname=John, lastname=Doe, street=5 Boston Ave #88, city=Sioux Falls, county=Minnehaha, state=SD, zip=57105, homePhone=605-414-2147, cellPhone=605-794-4895, email=sage_wieser@cox.net, company=Truhlar And Truhlar Attys, website=http://www.truhlarandtruhlarattys.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000901000000090000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=9]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-9], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-9, firstname=Jane, lastname=Doe, street=228 Runamuck Pl #2808, city=Baltimore, county=Baltimore City, state=MD, zip=21224, homePhone=410-655-8723, cellPhone=410-804-4694, email=kris@gmail.com, company="King, Christopher A Esq", website=http://www.kingchristopheraesq.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]], EventElement [event=EventEvent [_id=_ID [_data=0164ad054c0000000a010000000a0000503c], clusterTime=ClusterTime [$timestamp=Timestamp [t=1689060684, i=10]], documentKey=DocumentKey [_id=TestMessage11-07-11-2023-07-07-47-10], fullDocument=FullDocument [_id=TestMessage11-07-11-2023-07-07-47-10, firstname=Jane, lastname=Doe, street=2371 Jerrold Ave, city=Kulpsville, county=Montgomery, state=PA, zip=19443, homePhone=215-874-1229, cellPhone=215-422-8694, email=minna_amigon@yahoo.com, company="Dorl, James J Esq", website=http://www.dorljamesjesq.com], ns=NS [db=DocumentDBStreamsLambdaTriggerDB, coll=Customer], operationType=insert]]]]EventSource = aws:docdbEventSourceARN = arn:aws:rds:us-west-2:123456789012:cluster:lambdaeventsourcedocumentdbclusterStarting a new message **************EventIDData = 0164ad054b0000000a010000000a0000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-1ClusterTimeTimeStampT = 1689060683ClusterTimeTimeStampI = 10CustomerID = TestMessage11-07-11-2023-07-07-47-1CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 4 B Blue Ridge BlvdCustomerCity = BrightonCustomerCounty = LivingstonCustomerState = MICustomerZip = 48116CustomerHomePhone = 810-292-9388CustomerCellPhone = 810-374-9840CustomerEmail = josephine_darakjy@darakjy.orgCustomerCompany = "Chanay, Jeffrey A Esq"CustomerWebsite = http://www.chanayjeffreyaesq.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000201000000020000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-2ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 2CustomerID = TestMessage11-07-11-2023-07-07-47-2CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 8 W Cerritos Ave #54CustomerCity = BridgeportCustomerCounty = GloucesterCustomerState = NJCustomerZip = 8014CustomerHomePhone = 856-636-8749CustomerCellPhone = 856-264-4130CustomerEmail = art@venere.orgCustomerCompany = "Chemel, James L Cpa"CustomerWebsite = http://www.chemeljameslcpa.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000301000000030000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-3ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 3CustomerID = TestMessage11-07-11-2023-07-07-47-3CustomerFirstname = JaneCustomerLastname = DoeCustomerStreet = 639 Main StCustomerCity = AnchorageCustomerCounty = AnchorageCustomerState = AKCustomerZip = 99501CustomerHomePhone = 907-385-4412CustomerCellPhone = 907-921-2010CustomerEmail = lpaprocki@hotmail.comCustomerCompany = Feltz Printing ServiceCustomerWebsite = http://www.feltzprintingservice.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000401000000040000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-4ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 4CustomerID = TestMessage11-07-11-2023-07-07-47-4CustomerFirstname = JaneCustomerLastname = DoeCustomerStreet = 34 Center StCustomerCity = HamiltonCustomerCounty = ButlerCustomerState = OHCustomerZip = 45011CustomerHomePhone = 513-570-1893CustomerCellPhone = 513-549-4561CustomerEmail = donette.foller@cox.netCustomerCompany = Printing DimensionsCustomerWebsite = http://www.printingdimensions.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000501000000050000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-5ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 5CustomerID = TestMessage11-07-11-2023-07-07-47-5CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 3 Mcauley DrCustomerCity = AshlandCustomerCounty = AshlandCustomerState = OHCustomerZip = 44805CustomerHomePhone = 419-503-2484CustomerCellPhone = 419-800-6759CustomerEmail = simona@morasca.comCustomerCompany = "Chapman, Ross E Esq"CustomerWebsite = http://www.chapmanrosseesq.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000601000000060000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-6ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 6CustomerID = TestMessage11-07-11-2023-07-07-47-6CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 7 Eads StCustomerCity = ChicagoCustomerCounty = CookCustomerState = ILCustomerZip = 60632CustomerHomePhone = 773-573-6914CustomerCellPhone = 773-924-8565CustomerEmail = mitsue_tollner@yahoo.comCustomerCompany = Morlong AssociatesCustomerWebsite = http://www.morlongassociates.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000701000000070000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-7ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 7CustomerID = TestMessage11-07-11-2023-07-07-47-7CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 7 W Jackson BlvdCustomerCity = San JoseCustomerCounty = Santa ClaraCustomerState = CACustomerZip = 95111CustomerHomePhone = 408-752-3500CustomerCellPhone = 408-813-1105CustomerEmail = leota@hotmail.comCustomerCompany = Commercial PressCustomerWebsite = http://www.commercialpress.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000801000000080000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-8ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 8CustomerID = TestMessage11-07-11-2023-07-07-47-8CustomerFirstname = JohnCustomerLastname = DoeCustomerStreet = 5 Boston Ave #88CustomerCity = Sioux FallsCustomerCounty = MinnehahaCustomerState = SDCustomerZip = 57105CustomerHomePhone = 605-414-2147CustomerCellPhone = 605-794-4895CustomerEmail = sage_wieser@cox.netCustomerCompany = Truhlar And Truhlar AttysCustomerWebsite = http://www.truhlarandtruhlarattys.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000901000000090000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-9ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 9CustomerID = TestMessage11-07-11-2023-07-07-47-9CustomerFirstname = JaneCustomerLastname = DoeCustomerStreet = 228 Runamuck Pl #2808CustomerCity = BaltimoreCustomerCounty = Baltimore CityCustomerState = MDCustomerZip = 21224CustomerHomePhone = 410-655-8723CustomerCellPhone = 410-804-4694CustomerEmail = kris@gmail.comCustomerCompany = "King, Christopher A Esq"CustomerWebsite = http://www.kingchristopheraesq.comFinishing a new message **************Starting a new message **************EventIDData = 0164ad054c0000000a010000000a0000503cOperationType = insertDatabase = DocumentDBStreamsLambdaTriggerDBCollection = CustomerDocumentKeyID = TestMessage11-07-11-2023-07-07-47-10ClusterTimeTimeStampT = 1689060684ClusterTimeTimeStampI = 10CustomerID = TestMessage11-07-11-2023-07-07-47-10CustomerFirstname = JaneCustomerLastname = DoeCustomerStreet = 2371 Jerrold AveCustomerCity = KulpsvilleCustomerCounty = MontgomeryCustomerState = PACustomerZip = 19443CustomerHomePhone = 215-874-1229CustomerCellPhone = 215-422-8694CustomerEmail = minna_amigon@yahoo.comCustomerCompany = "Dorl, James J Esq"CustomerWebsite = http://www.dorljamesjesq.comFinishing a new message **************End Event ***************END RequestId: 717b4978-4112-4f63-947f-bb9552482687
REPORT RequestId: 717b4978-4112-4f63-947f-bb9552482687  Init Duration: 0.03 ms  Duration: 1106.27 ms    Billed Duration: 1107 ms        Memory Size: 512 MB    Max Memory Used: 512 MB

***** End sam local invoke response *****
```


## Deploy the sample application


To deploy your application for the first time, run the following in your shell. Make sure the shell variable $AWS_REGION is set. If not, replace $AWS_REGION with the region in which you are deploying the AWS Lambda function:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name documentdb-lambda-java-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to AWS CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter StreamsProducerDocumentDBCluster**: The name of the Amazon DocumentDB Cluster that was created by the AWS CloudFormation template
* **Parameter StreamsProducerDocumentDBDatabase**: The name of the Amazon DocumentDB database that will generate streaming events to be consumed by the AWS Lambda function
* **Parameter StreamsProducerDocumentDBCollection**: The name of the Amazon DocumentDB collection that will generate streaming events to be consumed by the AWS Lambda function
* **Parameter SecretsManagerARN**: The ARN of the Amazon Secrets Manager secret that has the username and password to connect to the Amazon DocumentDB cluster
* **Parameter Subnet1**: The first of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter Subnet2**: The second of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter Subnet3**: The third of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter SecurityGroup**: The security group of the AWS Lambda function. This can be the same as the security group of the EC2 machine that was created by the AWS CloudFormation template
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well
    
**Note: In case you want to deploy the Lambda function by pointing to an existing DocumentDB Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the above parameters accordingly**


## Test the application

Once the lambda function is deployed, send some Amazon DocumentDB Streams messages by inputting documents in the Database and Collection that have been configured on the lambda function's event listener.

For your convenience, a Java program and a shell script has been created on the EC2 machine that was provisioned using Cloudformation.

```
cd /home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_message_sender_json

chmod +x commands.sh
```

You should see a script called commands.sh. Run that script by passing a random string and a number between 1 and 500. Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

```
[ec2-user@ip-10-0-0-126 ~]$ sh ./commands.sh firstBatch 10
```

You should see output similar to what is shown below:

Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-1
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-1
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-2
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-2
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-3
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-3
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-4
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-4
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-5
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-5
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-6
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-6
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-7
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-7
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-8
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-8
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-9
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-9
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-10
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-10


Once the messages have been sent, check Amazon Cloudwatch Logs and you should see messages for the Amazon Cloudwatch Log Group with the name of the deployed AWS Lambda function. The name of the Amazon Cloudwatch Log Group is /aws/lambda/<Name of the AWS Lambda function>

When you run the above script, it inputs JSON records into the Amazon DocumentDB cluster in the database and collection that were created. This results in the Amazon DocumentDB streams publishing every document. The AWS Lambda function listens on the published Amazon DocumentDB streams messages

The AWS Lambda code parses the Amazon DocumentDB streams messages and outputs the fields in the messages to Amazon Cloudwatch logs.

The lambda function also inputs each record into a Amazon DynamoDB table called DocumentDBStreamsConsumerDynamoDBTableJava (if you did not modify the default name in the sam template.yaml file)

You can go to the Amazon DynamoDB console and view the records.

You can also use the aws cli command below to view the count of records inserted into Amazon DynamoDB

```
aws dynamodb scan --table-name DocumentDBStreamsConsumerDynamoDBTableJava --select "COUNT"

```



## Cleanup

You can first clean-up the AWS Lambda function by running `sam delete`

```
cd /home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_consumer_dynamo_sam
sam delete

```
Confirm the delete by selecting Y at both prompts.
AWS SAM confirms the stack deletion with the "Deleted successfully" message in the terminal.

Next you need to delete the Amazon CloudFormation template containing the Amazon DocumentDB cluster and the Amazon EC2 instance. Open the Amazon CloudFormation console, select the stack, then choose Delete. The delete will take some time.