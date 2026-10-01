import * as cdk from "aws-cdk-lib";
import { Match, Template } from "aws-cdk-lib/assertions";
import { CdkStack } from "../lib/cdk-stack";

describe("CdkStack Bedrock configuration", () => {
  test("uses the documented global Nova 2 Lite profile and matching IAM resources", () => {
    const app = new cdk.App();
    const stack = new CdkStack(app, "TestStack", {
      env: { account: "123456789012", region: "us-east-1" },
    });
    const template = Template.fromStack(stack);

    template.hasResourceProperties("AWS::Lambda::Function", {
      Environment: {
        Variables: Match.objectLike({
          BEDROCK_REGION: "us-east-1",
          MODEL_ID: "global.amazon.nova-2-lite-v1:0",
        }),
      },
    });

    template.hasResourceProperties("AWS::IAM::Policy", {
      PolicyDocument: {
        Statement: Match.arrayWith([
          Match.objectLike({
            Action: "bedrock:InvokeModel",
            Effect: "Allow",
            Resource: Match.arrayWith([
              "arn:aws:bedrock:us-east-1:123456789012:inference-profile/global.amazon.nova-2-lite-v1:0",
              "arn:aws:bedrock:*::foundation-model/amazon.nova-2-lite-v1:0",
            ]),
          }),
        ]),
      },
    });
  });
});
