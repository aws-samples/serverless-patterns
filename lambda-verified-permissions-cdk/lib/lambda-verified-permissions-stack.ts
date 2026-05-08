import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as verifiedpermissions from 'aws-cdk-lib/aws-verifiedpermissions';
import { Construct } from 'constructs';

export class LambdaVerifiedPermissionsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create policy store with Cedar schema
    const policyStore = new verifiedpermissions.CfnPolicyStore(this, 'PolicyStore', {
      validationSettings: { mode: 'STRICT' },
      schema: {
        cedarJson: JSON.stringify({
          'MyApp': {
            entityTypes: {
              User: { shape: { type: 'Record', attributes: { role: { type: 'String' } } } },
              Document: { shape: { type: 'Record', attributes: { owner: { type: 'String' }, classification: { type: 'String' } } } }
            },
            actions: {
              Read: { appliesTo: { principalTypes: ['User'], resourceTypes: ['Document'] } },
              Write: { appliesTo: { principalTypes: ['User'], resourceTypes: ['Document'] } },
              Delete: { appliesTo: { principalTypes: ['User'], resourceTypes: ['Document'] } }
            }
          }
        })
      }
    });

    // Create policies
    new verifiedpermissions.CfnPolicy(this, 'AdminPolicy', {
      policyStoreId: policyStore.attrPolicyStoreId,
      definition: {
        static: {
          statement: 'permit(principal, action, resource) when { principal.role == "admin" };',
          description: 'Admins can perform any action'
        }
      }
    });

    new verifiedpermissions.CfnPolicy(this, 'ReaderPolicy', {
      policyStoreId: policyStore.attrPolicyStoreId,
      definition: {
        static: {
          statement: 'permit(principal, action == MyApp::Action::"Read", resource) when { principal.role == "reader" };',
          description: 'Readers can only read documents'
        }
      }
    });

    // Lambda authorizer function
    const authFn = new lambda.Function(this, 'AuthorizerFn', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      environment: { POLICY_STORE_ID: policyStore.attrPolicyStoreId },
      timeout: cdk.Duration.seconds(10)
    });

    authFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['verifiedpermissions:IsAuthorized'],
      resources: [`arn:aws:verifiedpermissions::${this.account}:policy-store/${policyStore.attrPolicyStoreId}`]
    }));

    const fnUrl = authFn.addFunctionUrl({ authType: lambda.FunctionUrlAuthType.AWS_IAM });

    new cdk.CfnOutput(this, 'FunctionUrl', { value: fnUrl.url });
    new cdk.CfnOutput(this, 'PolicyStoreId', { value: policyStore.attrPolicyStoreId });
  }
}
