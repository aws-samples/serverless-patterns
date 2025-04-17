// lib/secrets-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';
import { Construct } from 'constructs';

export class SecretsStack extends cdk.NestedStack {
  public readonly apiKey: secretsmanager.Secret;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create the secret
    this.apiKey = new secretsmanager.Secret(this, 'ExternalServiceApiKey', {
      secretName: 'orders/api-key',
      description: 'API Key for External Payment Service',
      removalPolicy: cdk.RemovalPolicy.RETAIN,
    });

    // Output the secret ARN
    new cdk.CfnOutput(this, 'ExtenralServiceApiKeySecretArn', {
      value: this.apiKey.secretArn,
      description: 'ARN of the API Key secret'
    });
  }
}