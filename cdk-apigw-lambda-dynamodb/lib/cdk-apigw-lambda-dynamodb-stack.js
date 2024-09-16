const { Stack } = require("aws-cdk-lib");
const { Runtime, Code, Function } = require("aws-cdk-lib/aws-lambda");
const {
  RestApi,
  LambdaIntegration,
  Model,
  RequestValidator,
  JsonSchemaVersion,
  JsonSchemaType,
} = require("aws-cdk-lib/aws-apigateway");
const {
  Table,
  AttributeType,
  BillingMode,
} = require("aws-cdk-lib/aws-dynamodb");

class CdkApigwLambdaDynamodbStack extends Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    // Create a DynamoDB Table
    const table = new Table(this, "CdkSampleTable", {
      partitionKey: {
        name: "id",
        type: AttributeType.STRING,
      },
      billingMode: BillingMode.PAY_PER_REQUEST,
    });

    // Create a Lambda Function
    const lambda = new Function(this, "LambdaFunction", {
      runtime: Runtime.NODEJS_18_X,
      handler: "saveEmail.handler",
      code: Code.fromAsset("functions"),
      environment: {
        table_name: table.tableName,
      },
    });

    // Grant Lambda permission to wrtie to the DynamoDB Table
    table.grantWriteData(lambda);

    // API Gateway
    const newApi = new RestApi(this, "NewApi");

    // Model for Request Validation
    const emailValidatorModel = new Model(this, "EmailValidator", {
      restApi: newApi,
      contentType: "application/json",
      description: "Validate Eamil",
      modelName: "ValidateEmailModel",
      schema: {
        schema: JsonSchemaVersion.DRAFT4,
        title: "EmailValidatorSchema",
        type: JsonSchemaType.OBJECT,
        properties: {
          email: {
            type: JsonSchemaType.STRING,
            pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$",
          },
        },
        required: ["email"],
      },
    });

    // Request Validator
    const emailRequestValidator = new RequestValidator(
      this,
      "EmailRequestValidator",
      {
        restApi: newApi,
        requestValidatorName: "RequestValidator",
        validateRequestBody: true,
        validateRequestParameters: false,
      }
    );

    // Lambda Integration
    const lambdaIntegration = new LambdaIntegration(lambda);

    // API Method
    newApi.root.addMethod("POST", lambdaIntegration, {
      requestModels: {
        "application/json": emailValidatorModel,
      },
      requestValidator: emailRequestValidator,
    });
  }
}

module.exports = { CdkApigwLambdaDynamodbStack };
