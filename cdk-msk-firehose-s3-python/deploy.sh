echo "Deploy MSK S3 Delivery Stack using CDK"


export BUCKET_NAME="msk-kdf-s3-bucket-2398479823749879"
source .venv/bin/activate pip3
pip3 install -r requirements.txt

echo "Deploy MSK Serverless Stack"
cdk synth MSKServerLessStack
cdk deploy MSKServerLessStack


echo "Create the Topic in MSK Cluster by logging into the EC2 Instance Created using SSM connect\n\n"

echo "Execute the following Commands and then enter Y to proceed further for creating the KDF S3 stack \n\n"

echo "
      cd ssm-user
      export bs=<my-endpoint>
      <path-to-your-kafka-installation>/bin/kafka-topics.sh --bootstrap-server $bs --command-config client.properties --create --topic msk-kdf-s3-topic --partitions 6
      <path-to-your-kafka-installation>/bin/kafka-topics.sh --bootstrap-server  $bs --command-config client.properties --list
      <path-to-your-kafka-installation>/bin/kafka-console-producer.sh --bootstrap-server $bs --producer.config client.properties --topic msk-src-pattern"

read -p "Acknowledge that the Topic has been Created by pressing any key to Proceed further " yes

echo "Deploy KDF Stack"
cdk synth MSKKdfS3Stack
cdk deploy MSKKdfS3Stack