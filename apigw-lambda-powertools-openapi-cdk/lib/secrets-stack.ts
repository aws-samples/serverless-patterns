// lib/secrets-stack.ts
import * as cdk from "aws-cdk-lib";
import * as secretsmanager from "aws-cdk-lib/aws-secretsmanager";
import { Construct } from "constructs";

export interface SecretsStackProps extends cdk.NestedStackProps {
  stageName: string;
}

export class SecretsStack extends cdk.NestedStack {
  public readonly apiKey: secretsmanager.Secret;

  constructor(scope: Construct, id: string, props: SecretsStackProps) {
    super(scope, id, props);

    // Create the secret
    this.apiKey = new secretsmanager.Secret(this, "ExternalServiceApiKey", {
      secretName: "orders/payment-api-key",
      description: "API Key for External Payment Service",
      removalPolicy:
        props.stageName === "dev"
          ? cdk.RemovalPolicy.DESTROY
          : cdk.RemovalPolicy.RETAIN,
    });
  }
}
