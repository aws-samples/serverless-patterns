import * as cdk from 'aws-cdk-lib';
import { GraphqlApi, SchemaFile, AuthorizationType, FieldLogLevel, MappingTemplate, FunctionRuntime, Code } from 'aws-cdk-lib/aws-appsync';
import { PolicyDocument, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';


export class BackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Appsync API
    const api = new GraphqlApi(this, 'Api', {
      name: 'Api',
      schema: SchemaFile.fromAsset("src/schema.gql"),
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

    // Lambda Function
    const lambdaFunction = new NodejsFunction(this, "chat", {
      entry: "src/ask.ts",
      timeout: cdk.Duration.seconds(15),
      runtime: cdk.aws_lambda.Runtime.NODEJS_18_X,
      memorySize: 2048,
      bundling: {
        nodeModules: ["langchain"],
      },
      environment: {
        GRAPHQL_URL: api.graphqlUrl,
        REGION: this.region,
      },
      role: new Role(this, "LambdaRole", {
        roleName: "langchain-lambda",
        assumedBy: new ServicePrincipal("lambda.amazonaws.com"),
        inlinePolicies: {
          "LambdaPolicy": new PolicyDocument({
            statements: [
              // Grant Lambda permissions to call Bedrock API
              new PolicyStatement({
                resources: [
                  `arn:aws:bedrock:${this.region}::foundation-model/anthropic.claude-v2`,
                ],
                actions: ["bedrock:*"],
              }),
              // Grant Lambda permissions to call AppSync API
              new PolicyStatement({
                resources: [`${api.arn}/*`],
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
