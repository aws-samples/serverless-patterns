cd ../software/KinesisLambdaClient
mvn clean package
cd ../../infrastructure
mvn clean compile
cdk synth
cdk deploy