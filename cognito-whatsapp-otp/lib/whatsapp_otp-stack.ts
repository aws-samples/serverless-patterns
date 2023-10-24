import * as cdk from 'aws-cdk-lib';
import { CfnOutput, Duration, RemovalPolicy, CfnParameter, SecretValue } from 'aws-cdk-lib';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as cognito from 'aws-cdk-lib/aws-cognito';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';
import { UserPoolOperation } from 'aws-cdk-lib/aws-cognito';
import * as lambdapython from '@aws-cdk/aws-lambda-python-alpha';
import { Construct } from 'constructs';
import { PHONE_NUMBER_ID, SECRET_NAME, SECRET_ARN  } from './constants';


export class WhatsappOtpStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

  
    // Kms key for Cognito custom message sender Lambda
    const cognito_custom_sms_sender_kmskey = new kms.Key(this, 'cognito-customsmssender-kmskey',{
      removalPolicy: RemovalPolicy.DESTROY,
      pendingWindow: Duration.days(7),
      alias: 'alias/customsmssenderKey',
      description: 'KMS key for encrypting cognito code',
      enableKeyRotation: false,
    });

  // Permissions required by Cognito encrypt code using KMS key
  cognito_custom_sms_sender_kmskey.addToResourcePolicy(
        new iam.PolicyStatement({
          effect:iam.Effect.ALLOW,
          principals: [new iam.ServicePrincipal('cognito-idp.amazonaws.com')],
          actions: ['kms:CreateGrant', 'kms:Encrypt'],
          resources: ['*'],
        })
      );

  //Permissions required by AWS Lambda function to decrypt code from Cognito and get WhatsApp access token stored in Secret Manager
  const cognito_custom_sms_sender_lambda_permissions = new iam.PolicyDocument({
    statements: [
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ['kms:Decrypt'], 
        resources: [cognito_custom_sms_sender_kmskey.keyArn],
      }),
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ['secretsmanager:GetSecretValue'], 
        resources: [SECRET_ARN],
      }),
    ]
  })

     //Creating an IAM role for AWS Lambda function
      const lambda_role = new iam.Role (this, 'cognito-customsmssender-lambda-role',{
        assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
        description:'Lambda Execution Role for Cognito Custom SMS Sender',
        roleName:'cognito-custom-sms-sender-lambda-role',
        managedPolicies:[iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')]
      });

    //Creating an AWS Lambda Role Policy
      const lambda_policy = new iam.Policy(this,'cognito-customsmssender-lambda-policy',{
        document: cognito_custom_sms_sender_lambda_permissions
      });
      lambda_policy.attachToRole(lambda_role)

    //Custom Lambda message sender function
    const cognito_custom_sms_sender_lambda_function =new lambdapython.PythonFunction(this, 'cognito-customsmssender-lambda-function', {
      functionName:'cognito-whatsapp',
      entry: 'lambda/code', // required
      runtime: lambda.Runtime.PYTHON_3_11, // required
      index: 'lambda_function.py', // optional, defaults to 'index.py'
      handler: 'handler', // optional, defaults to 'handler',
      description:'Custom Whatsapp Message Sending Lambda function',
      role:lambda_role,
      timeout: Duration.minutes(3),
      environment: {
        'PHONE_NUMBER_ID': PHONE_NUMBER_ID,
        'SECRET_NAME': SECRET_NAME,
        'KEY_ARN': cognito_custom_sms_sender_kmskey.keyArn
      }  
      });
    

    // Creating Cognito user pool
    const cognito_custom_sms_sender_userpool = new cognito.UserPool(this, 'custom-sms-sender-userpool', {
      userPoolName: 'custom-sms-sender-userpool',
      selfSignUpEnabled: true,
      signInCaseSensitive: false,
      signInAliases: {
        email: true,
        phone: true,
      },
      autoVerify: {
        email: true,
        phone: true
      },
      standardAttributes: {
        fullname: {
          required: true,
          mutable: true,
        },
        email: {
          required: true,
          mutable: true,
        },
        phoneNumber: {
          required: true,
          mutable: true,
        }
      },
      mfa: cognito.Mfa.REQUIRED,
      mfaSecondFactor: {
        sms: true,
        otp: false,
      },
      passwordPolicy: {
        minLength: 8,
        requireLowercase: true,
        requireDigits: true,
        requireSymbols: true,
      },
      removalPolicy: RemovalPolicy.DESTROY,
      accountRecovery: cognito.AccountRecovery.EMAIL_ONLY,
      customSenderKmsKey: cognito_custom_sms_sender_kmskey
    });

    //Enable CustomSMSSender Lambda trigger
    cognito_custom_sms_sender_userpool.addTrigger(UserPoolOperation.CUSTOM_SMS_SENDER, cognito_custom_sms_sender_lambda_function);

    //Creating Cognito pool app client 
    const cognito_custom_sms_sender_client_app = cognito_custom_sms_sender_userpool.addClient("cognito-custom-sms-sender-app-client", {
      userPoolClientName: "cognito-custom-sms-sender-client-app-id"
    });

    new CfnOutput(this, "cognito-custom-sms-sender-client-app-id", {
      value: cognito_custom_sms_sender_client_app.userPoolClientId,
    });
  }
}

