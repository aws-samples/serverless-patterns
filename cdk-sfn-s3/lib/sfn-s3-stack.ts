import {
  Stack,
  StackProps,
  RemovalPolicy,
  Duration,
  CfnOutput,
} from "aws-cdk-lib";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { StateMachine, DefinitionBody } from "aws-cdk-lib/aws-stepfunctions";
import { CallAwsService } from "aws-cdk-lib/aws-stepfunctions-tasks";
import { Construct } from "constructs";

export class SfnS3Stack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Generate a unique ID for resource naming
    const uniqueId = this.node.addr.substring(0, 8);

    // Create S3 Bucket
    const sfnDestinationBucket = new Bucket(this, "SfnDestinationBucket", {
      bucketName: `sfn-destination-bucket-${uniqueId}`,
      versioned: true,
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    const sfnCallS3PutObject = new CallAwsService(this, "SfnCallS3PutObject", {
      service: "s3",
      action: "putObject",
      parameters: {
        Bucket: sfnDestinationBucket.bucketName,
        Key: "filename.txt",
        Body: "Hello World",
      },
      iamResources: [sfnDestinationBucket.arnForObjects("*")],
    });

    // Create StateMachine
    const sfnStateMachine = new StateMachine(this, "SfnStateMachine", {
      stateMachineName: `sfn-state-machine-${uniqueId}`,
      definitionBody: DefinitionBody.fromChainable(sfnCallS3PutObject),
      timeout: Duration.seconds(30),
    });

    new CfnOutput(this, "StateMachineARN", {
      value: sfnStateMachine.stateMachineArn,
    });
  }
}
