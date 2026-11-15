import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { AttributeType, BillingMode, Table } from "aws-cdk-lib/aws-dynamodb";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import * as iam from "aws-cdk-lib/aws-iam";
import * as path from "path";
import { aws_cognito as Cognito } from "aws-cdk-lib";

export class CdkStack extends cdk.Stack {
  public readonly usersTable: Table;
  public readonly addUserToTableFunc: NodejsFunction;
  public readonly userPool: Cognito.UserPool;
  public readonly userPoolClient: Cognito.UserPoolClient;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // 1. Create the DynamoDB Table
    this.usersTable = new Table(this, "UsersTable", {
      partitionKey: {
        name: "UserID",
        type: AttributeType.STRING,
      },
      tableName: "Users", // optional: specify the table name
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    //    This function will be used as the Cognito PostConfirmation trigger
    this.addUserToTableFunc = new NodejsFunction(
      this,
      "AddUserPostConfirmationFunc",
      {
        functionName: "addUserFunc", // optional
        runtime: Runtime.NODEJS_24_X,
        handler: "handler",
        entry: path.join(
          __dirname,
          "./functions/AddUserPostConfirmation/handler.ts"
        ),
        environment: {
          REGION: cdk.Stack.of(this).region,
          TABLE_NAME: this.usersTable.tableName,
        },
      }
    );

    // 3. Grant the Lambda permission to write to the "Users" table
    this.addUserToTableFunc.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["dynamodb:PutItem"],
        resources: [this.usersTable.tableArn],
      })
    );

    // 4. Create the Cognito User Pool and configure it
    this.userPool = new Cognito.UserPool(this, "UserPool", {
      userPoolName: "USER-POOL",
      selfSignUpEnabled: true,
      deletionProtection: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoVerify: {
        email: true,
      },
      passwordPolicy: {
        minLength: 8,
        requireLowercase: false,
        requireUppercase: false,
        requireDigits: false,
        requireSymbols: false,
      },
      signInAliases: {
        email: true,
      },
      standardAttributes: {
        email: {
          required: true,
          mutable: true,
        },
      },
      customAttributes: {
        firstName: new Cognito.StringAttribute({ minLen: 1, maxLen: 50 }),
        lastName: new Cognito.StringAttribute({ minLen: 1, maxLen: 50 }),
      },

      // 5. Attach our post-confirmation trigger to the Lambda
      lambdaTriggers: {
        postConfirmation: this.addUserToTableFunc,
      },
    });

    // 6. Create a User Pool Client
    this.userPoolClient = new Cognito.UserPoolClient(this, "UserPoolClient", {
      userPool: this.userPool,
      authFlows: {
        userPassword: true,
        userSrp: true,
      },
    });

    // 7. (Optional) Output values for later reference
    new cdk.CfnOutput(this, "UserPoolId", {
      value: this.userPool.userPoolId,
    });

    new cdk.CfnOutput(this, "UserPoolClientId", {
      value: this.userPoolClient.userPoolClientId,
    });
  }
}
