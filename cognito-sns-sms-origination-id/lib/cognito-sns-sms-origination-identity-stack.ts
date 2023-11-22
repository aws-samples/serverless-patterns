import * as cdk from 'aws-cdk-lib';
import { CfnOutput, Duration, RemovalPolicy } from 'aws-cdk-lib';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as cognito from 'aws-cdk-lib/aws-cognito';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';

import { Construct } from 'constructs';
import { UserPoolOperation } from 'aws-cdk-lib/aws-cognito';


export class CognitoSnsSmsOriginationIdentityStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Kms key for Cognito custom sms sender 
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

    //Permissions required by AWS Lambda function decrypt code from cognito
      const cognito_custom_sms_sender_lambda_permissions = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "sid":"cognito-customsmssender-sns-permission",
                    "Effect": "Allow",
                    "Action": [
                        "sns:publish"
                    ],
                    "Resource": "*"
                },
                {
                    "sid":"cognito-customsmssender-kms-permission",
                    "Effect": "Allow",
                    "Action": [
                        "kms:Decrypt"
                    ],
                    "Resource": "*"
                }
            ]
        }

       //Creating an IAM role for AWS Lambda function
        const lambda_role = new iam.Role (this, 'cognito-customsmssender-lambda-role',{
          assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
          description:'Lambda Execution Role for Cognito Custom SMS Sender',
          roleName:'cognito-custom-sms-sender-lambda-role',
          managedPolicies:[iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')]
        });
  
      //Creating an AWS Lambda Role Policy
        const lambda_policy = new iam.Policy(this,'cognito-customsmssender-lambda-policy',{
          document: iam.PolicyDocument.fromJson(cognito_custom_sms_sender_lambda_permissions)
        });
        lambda_policy.attachToRole(lambda_role)

      //Creating an AWS Lambda layers
        const cognito_custom_sms_sender_lambda_layer = new lambda.LayerVersion(this, 'cognito-customsmssender-nodejs-lib',{
          code: new lambda.AssetCode('lambda/layer/'),
          layerVersionName:'cognito-customsmssender-nodejs-lib',
          compatibleRuntimes:[lambda.Runtime.NODEJS_18_X],
          compatibleArchitectures: [lambda.Architecture.X86_64, lambda.Architecture.ARM_64],
          removalPolicy: RemovalPolicy.DESTROY,
        });
      
      //Creating CustomSMSSender Lambda function
        const cognito_custom_sms_sender_lambda_function = new lambda.Function(this, 'cognito-customsmssender-lambda-function', {
          runtime: lambda.Runtime.NODEJS_18_X ,
          functionName:'cognito-customsmssender',
          code: lambda.Code.fromAsset('lambda/code'),
          description:'Customer SMS Sender Lambda function',
          role:lambda_role,
          handler: 'index.handler',
          layers:[cognito_custom_sms_sender_lambda_layer],
          environment: {
            'KEY_ALIAS': 'customsmssenderKey',
            'KEY_ARN': cognito_custom_sms_sender_kmskey.keyArn
          }                
        });

      // Creating cognito user pool
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
