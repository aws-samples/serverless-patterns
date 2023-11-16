sudo yum -y install java-11 
wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz 
tar -xzf kafka_2.12-2.8.1.tgz 
rm -rf kafka_2.12-2.8.1.tgz 
cd ./kafka_2.12-2.8.1/libs 
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.1/aws-msk-iam-auth-1.1.1-all.jar 
cd ../bin 
touch client.properties 
echo "security.protocol=SASL_SSL 
 sasl.mechanism=AWS_MSK_IAM 
  sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required; 
 sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler " > client.properties