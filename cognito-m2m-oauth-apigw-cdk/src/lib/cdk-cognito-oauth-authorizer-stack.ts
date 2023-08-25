import {
  Duration,
  RemovalPolicy,
  Stack,
  StackProps,
  aws_cognito,
  aws_lambda,
  aws_apigateway,
  CfnOutput,
  aws_lambda_nodejs,
} from "aws-cdk-lib";
import { Construct } from "constructs";
import * as path from "path";

export class CdkCognitoOauthAuthorizerStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // user pool
    const oauthUserPool = new aws_cognito.UserPool(this, `OauthUserPool`, {
      accountRecovery: aws_cognito.AccountRecovery.EMAIL_ONLY,
      removalPolicy: RemovalPolicy.DESTROY,
      userPoolName: `OauthUserPool`,
    });

    // Scopes
    const userReadScope = new aws_cognito.ResourceServerScope({
      scopeName: "user.read",
      scopeDescription: "user read scope",
    });

    const userWriteScope = new aws_cognito.ResourceServerScope({
      scopeName: "user.write",
      scopeDescription: "user read scope",
    });

    // attach scope to user pool
    const oauthResourceServer = new aws_cognito.UserPoolResourceServer(
      this,
      `OauthResourceServer`,
      {
        identifier: `OauthResourceServer`,
        userPool: oauthUserPool,
        scopes: [userReadScope, userWriteScope],
      }
    );

    // client which accesses application scope limited to read
    new aws_cognito.UserPoolClient(this, `OauthAppClient`, {
      userPool: oauthUserPool,
      accessTokenValidity: Duration.minutes(60),
      generateSecret: true,
      refreshTokenValidity: Duration.days(1),
      enableTokenRevocation: true,
      oAuth: {
        flows: {
          clientCredentials: true,
        },
        scopes: [
          aws_cognito.OAuthScope.resourceServer(
            oauthResourceServer,
            userReadScope
          ),
          aws_cognito.OAuthScope.resourceServer(
            oauthResourceServer,
            userWriteScope
          ),
        ],
      },
    });

    oauthUserPool.addDomain(`OauthUserPoolDomain`, {
      cognitoDomain: {
        domainPrefix: `sample-oauth`,
      },
    });

    // User Lambda

    const apiLambda = new aws_lambda_nodejs.NodejsFunction(this, "UserLambda", {
      runtime: aws_lambda.Runtime.NODEJS_16_X,
      handler: "handler",
      entry: path.join(__dirname, "../src/lambda/user/index.ts"),
      bundling: {
        externalModules: ["aws-sdk"],
        forceDockerBundling: false,
      },
    });

    // API Gateway
    const api = new aws_apigateway.RestApi(this, "usereapi", {
      restApiName: "UserAPI",
      description: "This is the User API",
    });

    // Authorizer for API Gateway
    const auth = new aws_apigateway.CognitoUserPoolsAuthorizer(
      this,
      "userAuthorizer",
      {
        cognitoUserPools: [oauthUserPool],
      }
    );

    // API Gateway Resource
    const user = api.root.addResource("user");

    // API Gateway Method for user and attach authorizer to it
    user.addMethod("GET", new aws_apigateway.LambdaIntegration(apiLambda), {
      authorizer: auth,
      authorizationType: aws_apigateway.AuthorizationType.COGNITO,
      authorizationScopes: [`OauthResourceServer/${userReadScope.scopeName}`],
    });

    new CfnOutput(this, "ApiEndpoint", {
      value: api.url,
    });
  }
}
