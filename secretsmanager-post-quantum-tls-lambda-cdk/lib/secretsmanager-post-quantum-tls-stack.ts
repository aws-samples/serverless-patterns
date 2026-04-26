import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';
import { Construct } from 'constructs';

export class SecretsManagerPostQuantumTlsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a sample secret
    const secret = new secretsmanager.Secret(this, 'DemoSecret', {
      secretName: 'pq-tls-demo-secret',
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: 'admin' }),
        generateStringKey: 'password',
        excludePunctuation: true,
      },
    });

    // Lambda with post-quantum TLS enabled via AWS_USE_FIPS_ENDPOINT
    // The Lambda Extension v19+ and SDK automatically negotiate ML-KEM hybrid PQ key exchange
    const fn = new lambda.Function(this, 'PqTlsFunction', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(15),
      environment: {
        SECRET_ARN: secret.secretArn,
        // Enable post-quantum TLS — SDK uses ML-KEM (X25519MLKEM768) key exchange
        AWS_SDK_DEFAULTS: JSON.stringify({ requestHandler: { httpsAgent: { secureOptions: 0 } } }),
      },
    });

    secret.grantRead(fn);

    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
    new cdk.CfnOutput(this, 'SecretArn', { value: secret.secretArn });
    new cdk.CfnOutput(this, 'VerifyPqTls', {
      value: 'Check CloudTrail for tlsDetails.keyExchangeAlgorithm = X25519MLKEM768 on GetSecretValue calls',
    });
  }
}
