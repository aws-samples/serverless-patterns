# Deploy Cloudformation Stack

- Login to AWS Console
- Go to CloudFormation
- Select `Create stack` / `Standard`
- On next page, select `Upload a template file`
- Click on `Choose File` and select `MSKSampleStack.yml`
- Give a stack name, for example `MSKStack`.
- Under `Parameters` for `EnvType`, select `Serverless` for serverless MSK cluster, or `Provisoned` for provisoned MSK cluster.
- Click `Next`
- Click `Next` again, and on next page, click `Submit`

The template deploys following key resources - 

- VPC 
- 3 private subnets and 1 public subnet
- Security group
- A Cloud9 environment
- Custom KMS key to use with the secret for SCRAM authentication
- Secret manager secret for SCRAM authentication
- Private certificate authority for MTLS authentication

After cloudofrmation stack is deployed, move on to next step. 
# Basic Set up

The MSK cluster is set up to work with all three authentication mechanisms - TLS, SASL/SCRAM, and IAM. There are some basic set up steps that are required to test all three mechanisms. 


- Open cloud 9 instance and open terminal.

- Download Apache Kafka. 

    ```
    wget https://downloads.apache.org/kafka/3.4.1/kafka_2.13-3.4.1.tgz
    ```

If this version (2.13-3.4.1) is not available anymore, please download latest Apache Kafka version that is MSK supports from https://downloads.apache.org/kafka/.

Review this page to get a list of Apache Kafka versions supported by MSK - https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html

- Unzip the package you just downloaded

    ```
    tar -xzf kafka_2.13-3.4.1.tgz
    ```


# Test authetication mechanisms

## IAM 

- Go to the kafka_2.13-3.4.1/libs/ directory, then run the following command to download the Amazon MSK IAM JAR file. 

    ```
    cd kafka_2.13-3.4.1/libs/ 
    wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.6/aws-msk-iam-auth-1.1.6-all.jar
    ```

- Under kafka_2.13-3.4.1/bin directory create a new file with name `client.properties` and add following content in that file - 

```
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

- Go to terminal and run following commands. Replace AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY with your long term credentials for the account where you deployed the stack. 

```
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
```

```
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```

- Run this command to get MSK cluster's ARN  -

    ```
    aws kafka  list-clusters-v2 --cluster-name-filter <YOUR CLUSTER NAME>  --query 'ClusterInfoList[0].ClusterArn'
    ```

- Run  this command to get the bootstrap broker links -

    ```
    aws kafka get-bootstrap-brokers --cluster-arn <ARN_FROM_LAST_STEP>
    ```

- Get the value of BootstrapBrokerStringSaslIam, and pick the first url from that, for example - b-3.<clustername>.<id>.c9.kafka.us-east-1.amazonaws.com:9098

- Open terminal and cd to kafka_2.13-3.4.1/bin directory

    ```
    cd ~/environment/kafka_2.13-3.4.1/bin
    ```

- Run this command to create a Kafka topic 

    ```
    ./kafka-topics.sh --create --bootstrap-server <BootstrapBrokerStringSaslIam> --command-config client.properties --replication-factor 3 --partitions 1 --topic MSKTutorialTopicIAM
    ```

- You should get a response like this - 

    `Created topic MSKTutorialTopicIAM.`

## Mutual TLS

Here's the documentation based on which following instructions are created - https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html


- In Cloud9 terminal, cd to `environment` directory
    ```
    cd ~/environment/
    ```

- Run the following command to use the JVM trust store to create your client trust store. Adjust JVM path if needed.
    ```
    cp /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.321.x86_64/jre/lib/security/cacerts kafka.client.truststore.jks
    ```

- Run the following command to create a private key for your client. 

    ```
    keytool -genkey -keystore kafka.client.keystore.jks -validity 300 -storepass storepass -keypass storepass -dname "CN=dn" -alias Example-Alias -storetype pkcs12
    ```

- Run the following command to create a certificate request with the private key you created in the previous step

    ```
    keytool -keystore kafka.client.keystore.jks -certreq -file client-cert-sign-request -alias Example-Alias -storepass storepass -keypass storepass
    ```

- Open the /environment/client-cert-sign-request file and ensure that it starts with -----BEGIN CERTIFICATE REQUEST----- and ends with -----END CERTIFICATE REQUEST-----. If it starts with -----BEGIN NEW CERTIFICATE REQUEST-----, delete the word NEW (and the single space that follows it) from the beginning and the end of the file.

- Run the following command to sign your certificate request. Replace Private-CA-ARN with the ARN of your PCA. You can change the validity value if you want. Here we use 300 as an example. Replace Private-CA-ARN with the ARN of the certificate authority deployed via cloudformation. 

    ```
    aws acm-pca issue-certificate --certificate-authority-arn Private-CA-ARN --csr fileb://client-cert-sign-request --signing-algorithm "SHA256WITHRSA" --validity Value=300,Type="DAYS"
    ```

- You should receive a response like below. Make a note of CertificateArn
    ```
    {
        "CertificateArn": "<ARN>"
    }
    ```

- Run the following command to get the certificate that AWS Private CA signed for you. Replace Certificate-ARN with the ARN you obtained from the response to the previous command.

    ```
    aws acm-pca get-certificate --certificate-authority-arn Private-CA-ARN --certificate-arn Certificate-ARN
    ```

- From the JSON result of running the previous command, copy the strings associated with Certificate and CertificateChain. Paste these two strings in a new file named signed-certificate-from-acm. Paste the string associated with Certificate first, followed by the string associated with CertificateChain. Replace the \n characters with new lines. The following is the structure of the file after you paste the certificate and certificate chain in it.
```
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----            
```

- Run the following command on the client machine to add this certificate to your keystore so you can present it when you talk to the MSK brokers.

    ```
    keytool -keystore kafka.client.keystore.jks -import -file signed-certificate-from-acm -alias Example-Alias -storepass storepass -keypass storepass
    ```

- If you get a prompt like this - `Install reply anyway? [no]:`, enter yes, and press enter.

- Open kafka_2.13-3.4.1/bin/client.properties, and comment out existing list by adding # in front of each line.

- Add following lines after existing lines.

```
security.protocol=SSL
ssl.truststore.location=/home/ec2-user/environment/kafka.client.truststore.jks
ssl.keystore.location=/home/ec2-user/environment/kafka.client.keystore.jks
ssl.keystore.password=storepass
ssl.key.password=storepass
```

- Run following command to create a test topic from kafka_2.13-3.4.1/bin directory in terminal. Use the bootstrap server for TLS (BootstrapBrokerStringTls) from the list obtained in IAM section. -

    ```
    ./kafka-topics.sh --create --bootstrap-server b-1.mskstackcluster.97lslp.c9.kafka.us-east-1.amazonaws.com:9094 --command-config client.properties --replication-factor 3 --partitions 1 --topic MSKTutorialTopicTLS
    ```

- You should see a message like this - 
    ```
    Created topic MSKTutorialTopicTLS.
    ```

# SASL/SCRAM authentication

Here's the documentation based on which following instructions are created - https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html

- Under `/environment`, create a new file `users_jaas.conf`

- Add following content to this file -

```
KafkaClient {
   org.apache.kafka.common.security.scram.ScramLoginModule required
   username="<username from secret manager>"
   password="<password from secret manager>";
};
```
Replace the values for username and password to the values present in secret manager secret, that was deployed with cloudformation stack.

- Use the following command to export your JAAS config file as a KAFKA_OPTS environment parameter.

    ```
    export KAFKA_OPTS=-Djava.security.auth.login.config=/home/ec2-user/environment/users_jaas.conf
    ```

- Create a file named kafka.client.truststore.jks in a ./tmp directory.

    ```
    cp /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.321.x86_64/jre/lib/security/cacerts /tmp/kafka.client.truststore.jks
    ```

- In the root directory of your Apache Kafka installation, create a client properties file called client_sasl.properties with the following contents. This file defines the SASL mechanism and protocol.

```
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512
ssl.truststore.location=<path-to-keystore-file>/kafka.client.truststore.jks
```

- Retrieve your bootstrap brokers string with the following command. Replace ClusterArn with the Amazon Resource Name (ARN) of your cluster:

    ```
     aws kafka get-bootstrap-brokers --cluster-arn ClusterArn
    ```

- Run following command to create a topic. Replace `BootstrapBrokerStringSaslScram` with the value that you retrieved in the previous step.

    ```
    cd ~/environment/kafka_2.13-3.4.1/
    
    ./bin/kafka-topics.sh --create --bootstrap-server BootstrapBrokerStringSaslScram --replication-factor 3 --partitions 1 --topic DemoSASLTopic --command-config client_sasl.properties
    ```

You should see a message like this: 
_Created topic DemoSASLTopic._

**Start the producer**
Run the below command to start the producer, once the producer is running, you can send topics by typing some text inputs. `BootstrapBrokerStringSaslScram` with the value that you retrieved in the previous step.

```
./bin/kafka-console-producer.sh --broker-list BootstrapBrokerStringSaslScram --topic DemoSASLTopic --producer.config client_sasl.properties

```

Go to msk-sasl-sram-lambda pattern how to consume the topics using AWS Lambda events.


# References
https://docs.aws.amazon.com/cloud9/latest/user-guide/credentials.html

https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html

https://docs.aws.amazon.com/msk/latest/developerguide/create-topic.html

https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#configure-clients-for-iam-access-control

https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html

https://github.com/aws/aws-msk-iam-auth/releases/tag/v1.1.6

https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html
