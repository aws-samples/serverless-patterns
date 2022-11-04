import { Stack, StackProps } from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import { Construct } from 'constructs';
import * as cognito from 'aws-cdk-lib/aws-cognito';
import * as cdk from 'aws-cdk-lib';

export class CdkCognitoApigatewayLambdaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    //AWS Lambda resource

    const userLambda = new lambda.Function(this, 'UserHanlder', {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromAsset('lambda'),
      handler: 'user.handler'
    })

    const pool = new cognito.UserPool(this, 'Pool', {
      userPoolName: 'user-pool',
      selfSignUpEnabled: true,
      signInAliases: {
        email: true,
      },
      autoVerify: {
        email: true,
      },
      passwordPolicy: {
        minLength: 8,
        requireLowercase: true,
        requireDigits: true,
        requireUppercase: false,
        requireSymbols: false,
      },
      accountRecovery: cognito.AccountRecovery.EMAIL_ONLY,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const readOnlyScope = new cognito.ResourceServerScope({ scopeName: 'read', scopeDescription: 'Read-only access' });
    const userServer = pool.addResourceServer('ResourceServer', {
      identifier: 'users',
      scopes: [readOnlyScope],
    });

    pool.addClient('s2s-client', {
      oAuth: {
        flows: {
          clientCredentials: true
        },
        scopes: [cognito.OAuthScope.resourceServer(userServer, readOnlyScope)]
      },
      generateSecret: true
    });

    pool.addDomain('Domain', {
      cognitoDomain: {
        domainPrefix: 'apg-user-pool'
      }
    });

    const auth = new apigateway.CognitoUserPoolsAuthorizer(this, 'userAuthorizer', {
      cognitoUserPools: [pool]
    });

    const api = new apigateway.LambdaRestApi(this, 'userApi', {
      handler: userLambda,
      defaultMethodOptions: {
        authorizationType: apigateway.AuthorizationType.COGNITO,
        authorizer: auth,
        authorizationScopes: [cognito.OAuthScope.resourceServer(userServer, readOnlyScope).scopeName]
      }
    })
  }
}
