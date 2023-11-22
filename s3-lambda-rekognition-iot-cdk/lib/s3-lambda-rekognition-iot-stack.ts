import {Stack, StackProps,  } from 'aws-cdk-lib';
import *  as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import * as eventsources from 'aws-cdk-lib/aws-lambda-event-sources';
import * as iam from 'aws-cdk-lib/aws-iam';
import { CfnOutput } from 'aws-cdk-lib'; 
import { Construct } from 'constructs';


export class PPEIoTViolations extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    //create new S3 bucket
    const bucket = new s3.Bucket(this, 'images-bucket', {
    })


  const lambdaFunction = new lambda.Function(this, 'lambdaFunction', {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset(path.join(__dirname,'ppeDetectionFunction/')),
    handler: 'lambda_function.lambda_handler',
    environment: {
      'TOPIC': 'Bittle1/sub',
      'MESSAGE': 'khi',
      'MIN_CONFIDENCE': '80',
      'REQUIRED_PPE': '["HAND_COVER","FACE_COVER"]'
    }

})

bucket.grantRead(lambdaFunction)

// Grant Lambda function to call Rekognition detect labels
lambdaFunction.role?.attachInlinePolicy(
  new iam.Policy(this, 'rekognitionDetectLabelsPolicy', {
    statements: [
      new iam.PolicyStatement({
        actions: ['rekognition:DetectProtectiveEquipment','iot:Publish'],
        resources: ['*'],
      })
    ],
  }),
);


  // add S3 event to lambda function
  lambdaFunction.addEventSource(new eventsources.S3EventSource(bucket, {
    events: [s3.EventType.OBJECT_CREATED],
  }))

  // output S3 bucket name

  new CfnOutput(this, 'bucketName', {
    value: bucket.bucketName,
    description: 'The name of the s3 bucket created.',
  });


}
}
