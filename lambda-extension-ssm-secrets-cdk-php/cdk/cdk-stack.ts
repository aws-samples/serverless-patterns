import { CfnOutput, CfnParameter, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { join } from "path";
import { packagePhpCode, PhpFunction } from "@bref.sh/constructs";
import { FunctionUrlAuthType, LayerVersion, Runtime } from "aws-cdk-lib/aws-lambda";
import { StringParameter } from "aws-cdk-lib/aws-ssm";
import { Policy, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Secret } from 'aws-cdk-lib/aws-secretsmanager';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stackPrefix = id;

    // May be set as parameter new CfnParameter(this, 'parameterStoreExtensionArn', { type: 'String' });
    const parameterStoreExtensionArn = 'arn:aws:lambda:us-east-1:177933569100:layer:AWS-Parameters-and-Secrets-Lambda-Extension:11';
    const parameterStoreExtension = new CfnParameter(this, 'parameterStoreExtensionArn', { type: 'String', default: parameterStoreExtensionArn });

    const paramTheSsmParam = new StringParameter(this, `${stackPrefix}-TheSsmParam`, {
      parameterName: `/${stackPrefix.toLowerCase()}/ssm/param`,
      stringValue: 'the-value-here',
    });

    // CDK cannot create SecureString
    // You would create the SecureString out of CDK and use the param name here
    // const paramAnSsmSecureStringParam = StringParameter.fromSecureStringParameterAttributes(this, `${stackPrefix}-AnSsmSecureStringParam`, {
    //   parameterName: `/${stackPrefix.toLowerCase()}/ssm/secure-string/params`,
    // });

    const templatedSecret = new Secret(this, 'TemplatedSecret', {
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ username: 'postgres' }),
        generateStringKey: 'password',
        excludeCharacters: '/@"',
      },
    });

    // The param path that will be used to retrieve value by the lambda
    const lambdaEnvironment = {
      THE_SSM_PARAM_PATH: paramTheSsmParam.parameterName,
      THE_SECRET_NAME: templatedSecret.secretName,
      // If you create the SecureString
      // THE_SECURE_SSMPARAM_PATH: paramAnSsmSecureStringParam.parameterName,
    };

    const functionName = `${id}-lambda`;
    const theLambda = new PhpFunction(this, `${stackPrefix}${functionName}`, {
      handler: 'lambda.php',
      phpVersion: '8.3',
      runtime: Runtime.PROVIDED_AL2,
      code: packagePhpCode(join(__dirname, `../assets/lambda`)),
      functionName,
      environment: lambdaEnvironment,
    });

    // Add extension layer
    theLambda.addLayers(
      LayerVersion.fromLayerVersionArn(this, 'ParameterStoreExtension', parameterStoreExtension.valueAsString)
    );

    // Set additional permissions for parameter store
    theLambda.role?.attachInlinePolicy(
      new Policy(this, 'additionalPermissionsForParameterStore', {
        statements: [
          new PolicyStatement({
            actions: ['ssm:GetParameter'],
            resources: [
              paramTheSsmParam.parameterArn,
              // If you create the SecureString
              // paramAnSsmSecureStringParam.parameterArn,
            ],
          }),
        ],
      }),
    )

    templatedSecret.grantRead(theLambda);

    const fnUrl = theLambda.addFunctionUrl({ authType: FunctionUrlAuthType.NONE });

    new CfnOutput(this, 'LambdaUrl', { value: fnUrl.url });
  }
}
