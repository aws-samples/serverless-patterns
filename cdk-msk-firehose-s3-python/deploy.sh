echo "Deploy MSK S3 Delivery Stack using CDK"

source ./venv/bin/activate pip3
pip3 install -r requirements.txt

echo "Deploy MSK Serverless Stack"
cdk deploy MSKServerLessStack

echo "Deploy KDF Stack"
cdk deploy MSKKdfS3Stack