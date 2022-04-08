package main

import (
	"github.com/aws/aws-cdk-go/awscdk/v2"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsapigateway"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsdynamodb"
	"github.com/aws/aws-cdk-go/awscdk/v2/awsiam"
	"github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
	"github.com/aws/constructs-go/constructs/v10"
	"github.com/aws/jsii-runtime-go"
)

type ApigwLambdaDynamodbCdkGolangStackProps struct {
	awscdk.StackProps
}

// DynamoDB related constants
const (
	tableName               = "users-table"
	partitionKeyName        = "email"
	dynamoDBTableNameEnvVar = "DYNAMODB_TABLE_NAME"
)

// Lambda function related constants
const (
	lambdaHandlerName   = "my-func" //same as Go binary name
	functionZipFilePath = "../function/function.zip"
)

// API Gateway related constants
const (
	apigwResourceName = "users"
	httpMethod        = "POST"
)

func NewApigwLambdaDynamodbCdkGolangStack(scope constructs.Construct, id string, props *ApigwLambdaDynamodbCdkGolangStackProps) awscdk.Stack {
	var sprops awscdk.StackProps
	if props != nil {
		sprops = props.StackProps
	}
	stack := awscdk.NewStack(scope, &id, &sprops)

	// DynamoDB partition key
	partitionKey := &awsdynamodb.Attribute{Name: jsii.String(partitionKeyName), Type: awsdynamodb.AttributeType_STRING}

	// DynamoDB table
	dynamoDBTable := awsdynamodb.NewTable(stack, jsii.String("dynamodb-table"), &awsdynamodb.TableProps{TableName: jsii.String(tableName), BillingMode: awsdynamodb.BillingMode_PAY_PER_REQUEST, PartitionKey: partitionKey, RemovalPolicy: awscdk.RemovalPolicy_DESTROY})

	// environment variable for Lambda function
	lambdaEnvVar := &map[string]*string{dynamoDBTableNameEnvVar: dynamoDBTable.TableName()}

	// lambda function packaged as zip file
	function := awslambda.NewFunction(stack, jsii.String("lambda-function"), &awslambda.FunctionProps{Runtime: awslambda.Runtime_GO_1_X(), Handler: jsii.String(lambdaHandlerName), Code: awslambda.AssetCode_FromAsset(jsii.String(functionZipFilePath), nil), Environment: lambdaEnvVar})

	// policy to allow DynamoDB PutItem calls
	dynamoDBPutItemPolicy := awsiam.NewPolicy(stack, jsii.String("policy"), &awsiam.PolicyProps{PolicyName: jsii.String("LambdaDynamoDBPutItemPolicy"), Statements: &[]awsiam.PolicyStatement{awsiam.NewPolicyStatement(&awsiam.PolicyStatementProps{Effect: awsiam.Effect_ALLOW, Actions: jsii.Strings("dynamodb:PutItem"), Resources: jsii.Strings(*dynamoDBTable.TableArn())})}})

	// attach the policy to an IAM role which is created during Lambda creation
	function.Role().AttachInlinePolicy(dynamoDBPutItemPolicy)

	// API Gateway REST API
	restapi := awsapigateway.NewRestApi(stack, jsii.String("rest-apigw"), &awsapigateway.RestApiProps{EndpointTypes: &[]awsapigateway.EndpointType{awsapigateway.EndpointType_REGIONAL}, RestApiName: jsii.String("apigw-users")})

	// explict method definition (instead of proxy)
	restapi.Root().AddMethod(jsii.String(httpMethod), awsapigateway.NewLambdaIntegration(function, &awsapigateway.LambdaIntegrationOptions{AllowTestInvoke: jsii.Bool(false)}), restapi.Root().DefaultMethodOptions())

	return stack
}

func main() {
	app := awscdk.NewApp(nil)

	NewApigwLambdaDynamodbCdkGolangStack(app, "ServerlessCDKGoStack", &ApigwLambdaDynamodbCdkGolangStackProps{
		awscdk.StackProps{
			Env: env(),
		},
	})

	app.Synth(nil)
}

// env determines the AWS environment (account+region) in which our stack is to
// be deployed. For more information see: https://docs.aws.amazon.com/cdk/latest/guide/environments.html
func env() *awscdk.Environment {
	return nil
}
