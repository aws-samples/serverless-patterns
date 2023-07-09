import { S3EventbridgeStepFunctions } from "./s3-eventbridge-sfn";
import { Stack, StackProps, CfnOutput } from "aws-cdk-lib";
import {
  Bucket,
  BlockPublicAccess,
  BucketEncryption,
} from "aws-cdk-lib/aws-s3";
import { Construct } from "constructs";
import { Pass, StateMachine } from "aws-cdk-lib/aws-stepfunctions";
import { EventField, RuleTargetInput } from "aws-cdk-lib/aws-events";

export class S3EventBridgeStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bucket = new Bucket(this, "bucket", {
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      encryption: BucketEncryption.S3_MANAGED,
      enforceSSL: true,
    });

    const stepfunction = new StateMachine(this, "statemachine", {
      definition: new Pass(this, "state"),
    });

    const pattern = new S3EventbridgeStepFunctions(this, "pattern", {
      sourceBucket: bucket,
      stateMachine: stepfunction,
      stateMachineInput: RuleTargetInput.fromObject({
        detail: EventField.fromPath("$.detail"),
      }),
    });

    new CfnOutput(this, "S3BucketName", { value: bucket.bucketName });
    new CfnOutput(this, "LambdaFunctionARN", {
      value: stepfunction.stateMachineName,
    });
    new CfnOutput(this, "EventBridgeRuleARN", {
      value: pattern.eventRule.ruleArn,
    });
  }
}
