
import { Construct } from 'constructs';
import { OAuthScope, UserPool, UserPoolResourceServer } from 'aws-cdk-lib/aws-cognito';
import { AwsCustomResource, AwsCustomResourcePolicy, PhysicalResourceId } from 'aws-cdk-lib/custom-resources';

export interface AuthProps {
  authDomainPrefix: string;
}

export class Auth extends Construct {
  public readonly userPoolId: string;
  public readonly authEndpoint: string;
  public readonly destinationClientId: string;
  public readonly destinationClientSecret: string;

  constructor(scope: Construct, id: string, props: AuthProps) {
    super(scope, id);
    
    const userPool = new UserPool(this, "AppUserPool")

    userPool.addDomain("UserPoolDomain", {
      cognitoDomain: {
        domainPrefix: props.authDomainPrefix
      }
    })

    // client_credentials scope requires resource server with a dummy scope
    const resourceServer = new UserPoolResourceServer(this, "UserPoolResourceServer", {
      identifier: props.authDomainPrefix,
      userPool: userPool,
      scopes: [
        {
          scopeName: "publish-update",
          scopeDescription: "Publish update to AppSync endpoint"
        }
      ]
    })

    const destinationClient = userPool.addClient("publishUpdateClient", {
      disableOAuth: false,
      generateSecret: true,
      preventUserExistenceErrors: true,
      oAuth: {
        flows: {
          clientCredentials: true
        },
        scopes: [
          OAuthScope.custom(`${props.authDomainPrefix}/publish-update`)
        ]
      }
    })

    // CDK will not infer dependency without it being explicit here
    destinationClient.node.addDependency(resourceServer)

    const describeUserPoolClient = new AwsCustomResource(this, "DescribeUserPoolClient", {
      resourceType: "Custom::DescribeUserPoolClient",
      onCreate: {
        region: process.env.CDK_DEPLOY_REGION || process.env.CDK_DEFAULT_REGION,
        service: "CognitoIdentityServiceProvider",
        action: "describeUserPoolClient",
        parameters: {
          UserPoolId: userPool.userPoolId,
          ClientId: destinationClient.userPoolClientId
        },
        physicalResourceId: PhysicalResourceId.of(destinationClient.userPoolClientId)
      },
      policy: AwsCustomResourcePolicy.fromSdkCalls({
        resources: AwsCustomResourcePolicy.ANY_RESOURCE
      })
    })

    const endpoint = `https://${props.authDomainPrefix}.auth.${process.env.CDK_DEPLOY_REGION || process.env.CDK_DEFAULT_REGION}.amazoncognito.com`

    this.userPoolId = userPool.userPoolId
    this.authEndpoint = endpoint
    this.destinationClientId = destinationClient.userPoolClientId
    this.destinationClientSecret = describeUserPoolClient.getResponseField("UserPoolClient.ClientSecret")
  }
}
