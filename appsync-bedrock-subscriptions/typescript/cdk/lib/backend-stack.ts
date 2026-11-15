import * as cdk from 'aws-cdk-lib';
import { GraphqlApi, Definition, AuthorizationType, FieldLogLevel, MappingTemplate, FunctionRuntime, Code } from 'aws-cdk-lib/aws-appsync';
import { PolicyDocument, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';


export class BackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Appsync API
    const api = new GraphqlApi(this, 'Api', {
      name: 'Api',
      definition: Definition.fromFile("src/schema.gql"),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.IAM
        },
        additionalAuthorizationModes: [{
          authorizationType: AuthorizationType.API_KEY,
        }]
      },
      xrayEnabled: true,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL
      },
    })

    // Claude Haiku 5.5 through the global cross-Region inference profile.
    // Bedrock serves this model on demand only through an inference profile.
    const modelName = "anthropic.claude-haiku-5-5";
    const inferenceProfileArn = `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/global.${modelName}`;

    // Lambda Function
    const lambdaFunction = new NodejsFunction(this, "chat", {
      entry: "src/ask.ts",
      timeout: cdk.Duration.seconds(60),
      runtime: cdk.aws_lambda.Runtime.NODEJS_24_X,
      memorySize: 512,
      environment: {
        GRAPHQL_URL: api.graphqlUrl,
        REGION: this.region,
        MODEL_ID: `global.${modelName}`,
      },
      role: new Role(this, "LambdaRole", {
        assumedBy: new ServicePrincipal("lambda.amazonaws.com"),
        inlinePolicies: {
          "LambdaPolicy": new PolicyDocument({
            statements: [
              // Grant Lambda permissions to stream from the inference profile
              new PolicyStatement({
                resources: [inferenceProfileArn],
                actions: ["bedrock:InvokeModelWithResponseStream"],
              }),
              // ...and from the model it routes to, only through that profile
              new PolicyStatement({
                resources: [
                  `arn:aws:bedrock:${this.region}::foundation-model/${modelName}`,
                  `arn:aws:bedrock:::foundation-model/${modelName}`,
                ],
                actions: ["bedrock:InvokeModelWithResponseStream"],
                conditions: {
                  StringEquals: { "bedrock:InferenceProfileArn": inferenceProfileArn },
                },
              }),
              // Grant Lambda permissions to call AppSync API
              new PolicyStatement({
                resources: [`${api.arn}/types/Mutation/fields/send`],
                actions: ["appsync:GraphQL"],
              }),
              // Grant Lambda permissions to write to CloudWatch Logs
              new PolicyStatement({
                resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:*`],
                actions: [
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream",
                  "logs:PutLogEvents",
                ],
              }),
            ]
          })
        }
      })
    })


    // AppSync to Lambda DataSource
    const lambdaDataSource = api.addLambdaDataSource("LambdaDataSource", lambdaFunction)

    // Appsync to Lambda Resolver
    lambdaDataSource.createResolver("lambdaResolver", {
      typeName: "Mutation",
      fieldName: "ask",
    })

    // AppSync to None DataSource
    const noneDataSource = api.addNoneDataSource("NoneDataSource")

    // AppSync to Local Resolver
    const localResolver = noneDataSource.createResolver("localResolver", {
      typeName: "Mutation",
      fieldName: "send",
      runtime: FunctionRuntime.JS_1_0_0,
      code: Code.fromAsset("src/send.js")
    })

    // Outputs
    new cdk.CfnOutput(this, "GraphQLApiURL", {
      value: api.graphqlUrl
    })
    new cdk.CfnOutput(this, "GraphQLApiKey", {
      value: api.apiKey || ""
    })
    new cdk.CfnOutput(this, "GraphQLApiID", {
      value: api.apiId
    })
    new cdk.CfnOutput(this, "Region", {
      value: this.region
    })
  }
}
