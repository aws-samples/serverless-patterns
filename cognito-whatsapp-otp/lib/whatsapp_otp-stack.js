"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WhatsappOtpStack = void 0;
const cdk = require("aws-cdk-lib");
const aws_cdk_lib_1 = require("aws-cdk-lib");
const kms = require("aws-cdk-lib/aws-kms");
const cognito = require("aws-cdk-lib/aws-cognito");
const lambda = require("aws-cdk-lib/aws-lambda");
const iam = require("aws-cdk-lib/aws-iam");
const aws_cognito_1 = require("aws-cdk-lib/aws-cognito");
const lambdapython = require("@aws-cdk/aws-lambda-python-alpha");
const constants_1 = require("./constants");
class WhatsappOtpStack extends cdk.Stack {
    constructor(scope, id, props) {
        super(scope, id, props);
        // Kms key for Cognito custom message sender Lambda
        const cognito_custom_sms_sender_kmskey = new kms.Key(this, 'cognito-customsmssender-kmskey', {
            removalPolicy: aws_cdk_lib_1.RemovalPolicy.DESTROY,
            pendingWindow: aws_cdk_lib_1.Duration.days(7),
            alias: 'alias/customsmssenderKey',
            description: 'KMS key for encrypting cognito code',
            enableKeyRotation: false,
        });
        // Permissions required by Cognito encrypt code using KMS key
        cognito_custom_sms_sender_kmskey.addToResourcePolicy(new iam.PolicyStatement({
            effect: iam.Effect.ALLOW,
            principals: [new iam.ServicePrincipal('cognito-idp.amazonaws.com')],
            actions: ['kms:CreateGrant', 'kms:Encrypt'],
            resources: ['*'],
        }));
        //Permissions required by AWS Lambda function decrypt code from cognito and get Whatsapp access token
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
                    resources: [constants_1.SECRET_ARN],
                }),
            ]
        });
        //Creating an IAM role for AWS Lambda function
        const lambda_role = new iam.Role(this, 'cognito-customsmssender-lambda-role', {
            assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
            description: 'Lambda Execution Role for Cognito Custom SMS Sender',
            roleName: 'cognito-custom-sms-sender-lambda-role-2',
            managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')]
        });
        //Creating an AWS Lambda Role Policy
        const lambda_policy = new iam.Policy(this, 'cognito-customsmssender-lambda-policy', {
            document: cognito_custom_sms_sender_lambda_permissions
        });
        lambda_policy.attachToRole(lambda_role);
        //Custom Lambda message sender function
        const cognito_custom_sms_sender_lambda_function = new lambdapython.PythonFunction(this, 'cognito-customsmssender-lambda-function', {
            functionName: 'cognito-whatsapp',
            entry: 'lambda/code',
            runtime: lambda.Runtime.PYTHON_3_11,
            index: 'lambda_function.py',
            handler: 'handler',
            description: 'Custom Whatsapp Message Sending Lambda function',
            role: lambda_role,
            timeout: aws_cdk_lib_1.Duration.minutes(3),
            environment: {
                'PHONE_NUMBER_ID': constants_1.PHONE_NUMBER_ID,
                'SECRET_NAME': constants_1.SECRET_NAME,
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
            removalPolicy: aws_cdk_lib_1.RemovalPolicy.DESTROY,
            accountRecovery: cognito.AccountRecovery.EMAIL_ONLY,
            customSenderKmsKey: cognito_custom_sms_sender_kmskey
        });
        //Enable CustomSMSSender Lambda trigger
        cognito_custom_sms_sender_userpool.addTrigger(aws_cognito_1.UserPoolOperation.CUSTOM_SMS_SENDER, cognito_custom_sms_sender_lambda_function);
        //Creating Cognito pool app client 
        const cognito_custom_sms_sender_client_app = cognito_custom_sms_sender_userpool.addClient("cognito-custom-sms-sender-app-client", {
            userPoolClientName: "cognito-custom-sms-sender-client-app-id"
        });
        new aws_cdk_lib_1.CfnOutput(this, "cognito-custom-sms-sender-client-app-id", {
            value: cognito_custom_sms_sender_client_app.userPoolClientId,
        });
    }
}
exports.WhatsappOtpStack = WhatsappOtpStack;
