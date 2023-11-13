echo "Destroy MSK S3 Delivery Stack using CDK"

source ./venv/bin/activate pip3
pip3 install -r requirements.txt

echo "Destroy KDF Stack"
cdk destroy MSKKdfS3Stack

echo "Deploy MSK Serverless Stack"
cdk destroy MSKServerLessStack

