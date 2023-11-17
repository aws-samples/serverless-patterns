cd ../software/FirehoseTransformationLambda
mvn clean
cd ../../infrastructure
mvn clean
cdk synth
cdk deploy