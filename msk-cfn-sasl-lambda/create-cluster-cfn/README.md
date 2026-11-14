# Deploy CloudFormation Stack

- Login to AWS Console
- Go to CloudFormation
- Select `Create stack` / `Standard`
- On next page, select `Upload a template file`
- Click on `Choose File` and select `MSKSampleStack.yml`
- Give a stack name, for example `MSKStack`.
- Under `Parameters`:
  - `EnvType` defaults to `Provisioned`, which SASL/SCRAM needs. Choose `Serverless` only for a serverless cluster with IAM auth.
  - `MSKKafkaVersion` defaults to `4.1.x.kraft`.
- Click `Next`
- Select the check box that allows CloudFormation to create IAM resources, click `Next` again, and on next page, click `Submit`

You can deploy the same template from the AWS CLI instead:

```
aws cloudformation deploy --template-file MSKSampleStack.yml --stack-name MSKStack --capabilities CAPABILITY_IAM
```

The template deploys following key resources - 

- VPC 
- 3 private subnets and 1 public subnet, with a NAT gateway
- Security groups. The MSK cluster accepts connections from the Kafka client instance and from itself.
- A Kafka client EC2 instance (Amazon Linux 2023) in a private subnet, with Amazon Corretto 21, the Apache Kafka 4.1.2 client and the Amazon MSK IAM auth library installed. It has no public IP address and no SSH access. You connect with AWS Systems Manager Session Manager.
- Custom KMS key to use with the secret for SCRAM authentication
- Secret manager secret for SCRAM authentication, named `AmazonMSK_<stack name>_Credentials`
- Private certificate authority for MTLS authentication

The secret, KMS alias and MSK configuration names include the stack name, so you can deploy the template more than once in the same Region.

After the CloudFormation stack is deployed, move on to next step. 

# Basic Set up

The provisioned MSK cluster is set up to work with all three authentication mechanisms - TLS, SASL/SCRAM, and IAM. The serverless cluster uses IAM only.

## Connect to the Kafka client instance

The `KafkaClientInstanceId` stack output has the instance ID. Connect in one of these ways:

- In the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), select the instance, choose **Connect**, choose the **Session Manager** tab, then choose **Connect**.
- From your terminal, with the [Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) installed:

    ```
    aws ssm start-session --target <KafkaClientInstanceId>
    ```

Session Manager signs you in as `ssm-user`. Switch to `ec2-user`, which has the Kafka client in `~/kafka`:

```
sudo su - ec2-user
cd ~/kafka
```

The instance role gives the AWS CLI on the instance access to this stack's cluster, so you don't need to configure credentials.

## Get the bootstrap brokers

- Run this command to get the MSK cluster's ARN. Replace `MSKStack` with your stack name. For a serverless cluster, use `MSKStack-serverless-cluster`.

    ```
    CLUSTER_ARN=$(aws kafka list-clusters-v2 --cluster-name-filter MSKStack-cluster --query 'ClusterInfoList[0].ClusterArn' --output text)
    ```

- Run this command to get the bootstrap broker strings:

    ```
    aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN
    ```

# Test authentication mechanisms

## IAM 

The client instance already has the Amazon MSK IAM auth library in `~/kafka/libs` and an IAM client configuration in `~/kafka/client_iam.properties`.

- Get the IAM bootstrap brokers:

    ```
    BOOTSTRAP_IAM=$(aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN --query 'BootstrapBrokerStringSaslIam' --output text)
    ```

- Create a Kafka topic:

    ```
    ./bin/kafka-topics.sh --create --bootstrap-server $BOOTSTRAP_IAM --command-config client_iam.properties --replication-factor 3 --partitions 1 --topic MSKTutorialTopicIAM
    ```

- You should get a response like this - 

    `Created topic MSKTutorialTopicIAM.`

## Mutual TLS

Here's the documentation based on which following instructions are created - https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html

- Get the ARN of the private certificate authority from the `CertificateAuthorityArn` stack output:

    ```
    PCA_ARN=<CertificateAuthorityArn>
    ```

- Run the following command to use the JVM trust store to create your client trust store.

    ```
    cp $(dirname $(readlink -f $(which java)))/../lib/security/cacerts ~/kafka.client.truststore.jks
    ```

- Run the following command to create a private key for your client. 

    ```
    keytool -genkey -keystore ~/kafka.client.keystore.jks -validity 300 -storepass storepass -keypass storepass -dname "CN=dn" -alias Example-Alias -storetype pkcs12
    ```

- Run the following command to create a certificate request with the private key you created in the previous step

    ```
    keytool -keystore ~/kafka.client.keystore.jks -certreq -file ~/client-cert-sign-request -alias Example-Alias -storepass storepass -keypass storepass
    ```

- Open the `~/client-cert-sign-request` file and ensure that it starts with -----BEGIN CERTIFICATE REQUEST----- and ends with -----END CERTIFICATE REQUEST-----. If it starts with -----BEGIN NEW CERTIFICATE REQUEST-----, delete the word NEW (and the single space that follows it) from the beginning and the end of the file.

- Run the following command to sign your certificate request. You can change the validity value if you want. Here we use 300 as an example.

    ```
    CERT_ARN=$(aws acm-pca issue-certificate --certificate-authority-arn $PCA_ARN --csr fileb://$HOME/client-cert-sign-request --signing-algorithm "SHA256WITHRSA" --validity Value=300,Type="DAYS" --query CertificateArn --output text)
    ```

- Run the following command to get the certificate that AWS Private CA signed for you, followed by its certificate chain, in one file:

    ```
    aws acm-pca get-certificate --certificate-authority-arn $PCA_ARN --certificate-arn $CERT_ARN --query '[Certificate, CertificateChain]' --output text > ~/signed-certificate-from-acm
    ```

- Run the following command on the client machine to add this certificate to your keystore so you can present it when you talk to the MSK brokers.

    ```
    keytool -keystore ~/kafka.client.keystore.jks -import -file ~/signed-certificate-from-acm -alias Example-Alias -storepass storepass -keypass storepass
    ```

- If you get a prompt like this - `Install reply anyway? [no]:`, enter yes, and press enter.

- Create a TLS client configuration:

```
cat > client_tls.properties <<EOF
security.protocol=SSL
ssl.truststore.location=/home/ec2-user/kafka.client.truststore.jks
ssl.keystore.location=/home/ec2-user/kafka.client.keystore.jks
ssl.keystore.password=storepass
ssl.key.password=storepass
EOF
```

- Create a test topic using the bootstrap server for TLS (BootstrapBrokerStringTls):

    ```
    BOOTSTRAP_TLS=$(aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN --query 'BootstrapBrokerStringTls' --output text)
    ./bin/kafka-topics.sh --create --bootstrap-server $BOOTSTRAP_TLS --command-config client_tls.properties --replication-factor 3 --partitions 1 --topic MSKTutorialTopicTLS
    ```

- You should see a message like this - 
    ```
    Created topic MSKTutorialTopicTLS.
    ```

# SASL/SCRAM authentication

Here's the documentation based on which following instructions are created - https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html

- Create a SASL/SCRAM client configuration with the user name and password from the `CredentialsSecretArn` secret. The instance role can read only this secret.

```
SECRET_ARN=<CredentialsSecretArn>
aws secretsmanager get-secret-value --secret-id $SECRET_ARN --query SecretString --output text \
  | jq -r '"security.protocol=SASL_SSL\nsasl.mechanism=SCRAM-SHA-512\nsasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username=\"" + .username + "\" password=\"" + .password + "\";"' \
  > client_sasl.properties
chmod 600 client_sasl.properties
```

- Retrieve the SASL/SCRAM bootstrap brokers:

    ```
    BOOTSTRAP_SCRAM=$(aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN --query 'BootstrapBrokerStringSaslScram' --output text)
    ```

- Run following command to create a topic:

    ```
    ./bin/kafka-topics.sh --create --bootstrap-server $BOOTSTRAP_SCRAM --replication-factor 3 --partitions 1 --topic DemoSASLTopic --command-config client_sasl.properties
    ```

You should see a message like this: 
_Created topic DemoSASLTopic._

**Start the producer**
Run the below command to start the producer. Once the producer is running, you can send messages by typing some text inputs.

```
./bin/kafka-console-producer.sh --bootstrap-server $BOOTSTRAP_SCRAM --topic DemoSASLTopic --producer.config client_sasl.properties
```

Go to the msk-cfn-sasl-lambda pattern README to see how to consume the topic using AWS Lambda.


# References
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html

https://docs.aws.amazon.com/msk/latest/developerguide/create-topic.html

https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#configure-clients-for-iam-access-control

https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html

https://github.com/aws/aws-msk-iam-auth/releases/tag/v2.2.0

https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html
