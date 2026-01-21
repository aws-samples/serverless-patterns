import * as cdk from "aws-cdk-lib";
import {
  GraphqlApi,
  SchemaFile,
  AuthorizationType,
  FieldLogLevel,
  UserPoolDefaultAction,
} from "aws-cdk-lib/aws-appsync";
import * as cognito from "aws-cdk-lib/aws-cognito";
import { PolicyStatement, Effect } from "aws-cdk-lib/aws-iam"; // Removed Role, ServicePrincipal if not used elsewhere
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import * as path from "path";
// import { MappingTemplate } from "aws-cdk-lib/aws-appsync"; // Not strictly needed for default Lambda resolver

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // --- Cognito User Pool and Client ---
    // (This section remains the same as your previous version)
    const userPool = new cognito.UserPool(this, "AppsyncBedrockUserPool", {
      userPoolName: "AppsyncBedrockUserPool",
      selfSignUpEnabled: true,
      signInAliases: { email: true, username: false },
      autoVerify: { email: true },
      passwordPolicy: {
        minLength: 8,
        requireLowercase: true,
        requireUppercase: true,
        requireDigits: true,
        requireSymbols: false,
      },
      standardAttributes: {
        email: { required: true, mutable: true },
      },
      deletionProtection: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const userPoolClient = new cognito.UserPoolClient(
      this,
      "AppsyncBedrockUserPoolClient",
      {
        userPool: userPool,
        userPoolClientName: "AppsyncBedrockClient",
        authFlows: {
          userSrp: true,
          userPassword: true,
          adminUserPassword: true,
        },
      }
    );

    // --- AppSync GraphQL API ---
    // (This section remains the same)
    const api = new GraphqlApi(this, "AppsyncBedrockApi", {
      name: "AppsyncBedrockApi",
      definition: {
        schema: SchemaFile.fromAsset("src/schema.gql"),
      },
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.USER_POOL,
          userPoolConfig: {
            userPool: userPool,
            defaultAction: UserPoolDefaultAction.ALLOW,
          },
        },
      },
      xrayEnabled: true,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL,
      },
    });

    // --- AWS Lambda Function for Bedrock Invocation ---
    // IMPORTANT: Update MODEL_ID to your specific Claude 3 model if different.
    const modelIdForLambda = "anthropic.claude-3-sonnet-20240229-v1:0"; // Or your specific ID: "anthropic.claude-3-7-sonnet-20250219-v1:0"
    // if you've confirmed it's correct and accessible.

    const bedrockInvokeLambda = new NodejsFunction(
      this,
      "BedrockInvokeLambdaHandler",
      {
        runtime: lambda.Runtime.NODEJS_20_X,
        handler: "handler",
        entry: path.join(__dirname, "../src/lambda/invokeBedrock/index.ts"),
        memorySize: 512, // Increased memory for potentially larger SDK and payloads
        timeout: cdk.Duration.seconds(30), // Increased timeout
        bundling: {
          minify: false,
          sourceMap: true,
        },
        environment: {
          MODEL_ID: modelIdForLambda,
          ANTHROPIC_VERSION: "bedrock-2023-05-31", // Required for Claude 3 Messages API
          // You can add more env vars here to configure temperature, max_tokens etc.
          // MAX_TOKENS: "1024",
          // TEMPERATURE: "0.7",
        },
      }
    );

    // Grant Lambda permission to invoke the specific Bedrock model
    bedrockInvokeLambda.addToRolePolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        resources: [
          // IMPORTANT: Ensure this ARN matches the modelIdForLambda
          `arn:aws:bedrock:${this.region}::foundation-model/${modelIdForLambda}`,
        ],
        actions: ["bedrock:InvokeModel"],
      })
    );

    // --- AppSync Lambda Data Source ---
    // (This section remains the same)
    const lambdaDataSource = api.addLambdaDataSource(
      "BedrockLambdaDSSource",
      bedrockInvokeLambda,
      {
        name: "BedrockLambdaDataSource",
        description: "Lambda function to invoke Bedrock models (Claude 3)",
      }
    );

    // --- AppSync Resolver for Mutation.invoke using Lambda Data Source ---
    // (This section remains the same as Lambda still returns a string)
    lambdaDataSource.createResolver("InvokeMutationLambdaResolver", {
      typeName: "Mutation",
      fieldName: "invoke",
    });

    // --- CloudFormation Outputs ---
    // (This section remains largely the same, added Lambda name)
    new cdk.CfnOutput(this, "GraphQLApiUrl", { value: api.graphqlUrl });
    new cdk.CfnOutput(this, "GraphQLApiId", { value: api.apiId });
    new cdk.CfnOutput(this, "AWSRegion", { value: this.region });
    new cdk.CfnOutput(this, "CognitoUserPoolId", {
      value: userPool.userPoolId,
    });
    new cdk.CfnOutput(this, "CognitoUserPoolClientId", {
      value: userPoolClient.userPoolClientId,
    });
    new cdk.CfnOutput(this, "BedrockInvokeLambdaName", {
      value: bedrockInvokeLambda.functionName,
    });
    new cdk.CfnOutput(this, "BedrockModelIdUsed", { value: modelIdForLambda });
  }
}
