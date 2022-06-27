import * as cdk from "@aws-cdk/core";
import * as s3 from "@aws-cdk/aws-s3";
import * as sfn from "@aws-cdk/aws-stepfunctions";
import * as sfn_task from "@aws-cdk/aws-stepfunctions-tasks";

export class CdkSfnS3Stack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

      //S3 Bucket Creation
      const destinationBucket= new s3.Bucket(this, "DestinationBucket", {
      bucketName: "my-sfn-bucket-target",
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      versioned: true
   })

   const invokeS3PutObject = new sfn_task.CallAwsService(this, 'SendCustomEvent', {
     service: 's3',
     action: 'putObject',
     parameters: {
       Body:'Hello World',
       Bucket: destinationBucket.bucketName,
       Key: 'filename.txt'
     },
     iamResources: [destinationBucket.arnForObjects('*')],
   });

      //STATEMACHINE Creation
      
      const myStateMachine= new sfn.StateMachine(this, "MyS3StateMachine", {
        definition:invokeS3PutObject,
        timeout: cdk.Duration.minutes(5)
      });

      new cdk.CfnOutput(this, 'StateMachineARN', {value: myStateMachine.stateMachineArn})
  }
}
