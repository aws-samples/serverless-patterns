// lib/cognito-stack.ts
import * as cdk from "aws-cdk-lib";
import * as cognito from "aws-cdk-lib/aws-cognito";
import { Construct } from "constructs";

export interface CognitoStackProps extends cdk.NestedStackProps {
  stageName: string;
}

export class CognitoStack extends cdk.NestedStack {
  public readonly userPool: cognito.UserPool;
  public readonly userPoolClient: cognito.UserPoolClient;

  constructor(scope: Construct, id: string, props: CognitoStackProps) {
    super(scope, id, props);

    this.userPool = new cognito.UserPool(this, "UserPool", {
      removalPolicy:
        props.stageName === "dev"
          ? cdk.RemovalPolicy.DESTROY
          : cdk.RemovalPolicy.RETAIN,
    });

    this.userPoolClient = new cognito.UserPoolClient(this, "UserPoolClient", {
      userPool: this.userPool,
      authFlows: {
        userPassword: true,
        adminUserPassword: true,
      },
    });
  }
}
