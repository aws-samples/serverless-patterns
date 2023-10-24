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
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoid2hhdHNhcHBfb3RwLXN0YWNrLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsid2hhdHNhcHBfb3RwLXN0YWNrLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7OztBQUFBLG1DQUFtQztBQUNuQyw2Q0FBNEY7QUFDNUYsMkNBQTJDO0FBQzNDLG1EQUFtRDtBQUNuRCxpREFBaUQ7QUFDakQsMkNBQTJDO0FBRTNDLHlEQUE0RDtBQUM1RCxpRUFBaUU7QUFFakUsMkNBQXdFO0FBR3hFLE1BQWEsZ0JBQWlCLFNBQVEsR0FBRyxDQUFDLEtBQUs7SUFDN0MsWUFBWSxLQUFnQixFQUFFLEVBQVUsRUFBRSxLQUFzQjtRQUM5RCxLQUFLLENBQUMsS0FBSyxFQUFFLEVBQUUsRUFBRSxLQUFLLENBQUMsQ0FBQztRQUd4QixtREFBbUQ7UUFDbkQsTUFBTSxnQ0FBZ0MsR0FBRyxJQUFJLEdBQUcsQ0FBQyxHQUFHLENBQUMsSUFBSSxFQUFFLGdDQUFnQyxFQUFDO1lBQzFGLGFBQWEsRUFBRSwyQkFBYSxDQUFDLE9BQU87WUFDcEMsYUFBYSxFQUFFLHNCQUFRLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQztZQUMvQixLQUFLLEVBQUUsMEJBQTBCO1lBQ2pDLFdBQVcsRUFBRSxxQ0FBcUM7WUFDbEQsaUJBQWlCLEVBQUUsS0FBSztTQUN6QixDQUFDLENBQUM7UUFFTCw2REFBNkQ7UUFDN0QsZ0NBQWdDLENBQUMsbUJBQW1CLENBQzlDLElBQUksR0FBRyxDQUFDLGVBQWUsQ0FBQztZQUN0QixNQUFNLEVBQUMsR0FBRyxDQUFDLE1BQU0sQ0FBQyxLQUFLO1lBQ3ZCLFVBQVUsRUFBRSxDQUFDLElBQUksR0FBRyxDQUFDLGdCQUFnQixDQUFDLDJCQUEyQixDQUFDLENBQUM7WUFDbkUsT0FBTyxFQUFFLENBQUMsaUJBQWlCLEVBQUUsYUFBYSxDQUFDO1lBQzNDLFNBQVMsRUFBRSxDQUFDLEdBQUcsQ0FBQztTQUNqQixDQUFDLENBQ0gsQ0FBQztRQUVOLHFHQUFxRztRQUNyRyxN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SUFBSTtnQkFDVCxHQUFHLEVBQUUsS0FBSzthQUNYO1lBQ0QsY0FBYyxFQUFFO2dCQUNkLFNBQVMsRUFBRSxDQUFDO2dCQUNaLGdCQUFnQixFQUFFLElBQUk7Z0JBQ3RCLGFBQWEsRUFBRSxJQUFJO2dCQUNuQixjQUFjLEVBQUUsSUFBSTthQUNyQjtZQUNELGFBQWEsRUFBRSwyQkFBYSxDQUFDLE9BQU87WUFDcEMsZUFBZSxFQUFFLE9BQU8sQ0FBQyxlQUFlLENBQUMsVUFBVTtZQUNuRCxrQkFBa0IsRUFBRSxnQ0FBZ0M7U0FDckQsQ0FBQyxDQUFDO1FBRUgsdUNBQXVDO1FBQ3ZDLGtDQUFrQyxDQUFDLFVBQVUsQ0FBQywrQkFBaUIsQ0FBQyxpQkFBaUIsRUFBRSx5Q0FBeUMsQ0FBQyxDQUFDO1FBRTlILG1DQUFtQztRQUNuQyxNQUFNLG9DQUFvQyxHQUFHLGtDQUFrQyxDQUFDLFNBQVMsQ0FBQyxzQ0FBc0MsRUFBRTtZQUNoSSxrQkFBa0IsRUFBRSx5Q0FBeUM7U0FDOUQsQ0FBQyxDQUFDO1FBRUgsSUFBSSx1QkFBUyxDQUFDLElBQUksRUFBRSx5Q0FBeUMsRUFBRTtZQUM3RCxLQUFLLEVBQUUsb0NBQW9DLENBQUMsZ0JBQWdCO1NBQzdELENBQUMsQ0FBQztJQUNMLENBQUM7Q0FDRjtBQS9IRCw0Q0ErSEMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgKiBhcyBjZGsgZnJvbSAnYXdzLWNkay1saWInO1xuaW1wb3J0IHsgQ2ZuT3V0cHV0LCBEdXJhdGlvbiwgUmVtb3ZhbFBvbGljeSwgQ2ZuUGFyYW1ldGVyLCBTZWNyZXRWYWx1ZSB9IGZyb20gJ2F3cy1jZGstbGliJztcbmltcG9ydCAqIGFzIGttcyBmcm9tICdhd3MtY2RrLWxpYi9hd3Mta21zJztcbmltcG9ydCAqIGFzIGNvZ25pdG8gZnJvbSAnYXdzLWNkay1saWIvYXdzLWNvZ25pdG8nO1xuaW1wb3J0ICogYXMgbGFtYmRhIGZyb20gJ2F3cy1jZGstbGliL2F3cy1sYW1iZGEnO1xuaW1wb3J0ICogYXMgaWFtIGZyb20gJ2F3cy1jZGstbGliL2F3cy1pYW0nO1xuaW1wb3J0ICogYXMgc2VjcmV0c21hbmFnZXIgZnJvbSAnYXdzLWNkay1saWIvYXdzLXNlY3JldHNtYW5hZ2VyJztcbmltcG9ydCB7IFVzZXJQb29sT3BlcmF0aW9uIH0gZnJvbSAnYXdzLWNkay1saWIvYXdzLWNvZ25pdG8nO1xuaW1wb3J0ICogYXMgbGFtYmRhcHl0aG9uIGZyb20gJ0Bhd3MtY2RrL2F3cy1sYW1iZGEtcHl0aG9uLWFscGhhJztcbmltcG9ydCB7IENvbnN0cnVjdCB9IGZyb20gJ2NvbnN0cnVjdHMnO1xuaW1wb3J0IHsgUEhPTkVfTlVNQkVSX0lELCBTRUNSRVRfTkFNRSwgU0VDUkVUX0FSTiAgfSBmcm9tICcuL2NvbnN0YW50cyc7XG5cblxuZXhwb3J0IGNsYXNzIFdoYXRzYXBwT3RwU3RhY2sgZXh0ZW5kcyBjZGsuU3RhY2sge1xuICBjb25zdHJ1Y3RvcihzY29wZTogQ29uc3RydWN0LCBpZDogc3RyaW5nLCBwcm9wcz86IGNkay5TdGFja1Byb3BzKSB7XG4gICAgc3VwZXIoc2NvcGUsIGlkLCBwcm9wcyk7XG5cbiAgXG4gICAgLy8gS21zIGtleSBmb3IgQ29nbml0byBjdXN0b20gbWVzc2FnZSBzZW5kZXIgTGFtYmRhXG4gICAgY29uc3QgY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9rbXNrZXkgPSBuZXcga21zLktleSh0aGlzLCAnY29nbml0by1jdXN0b21zbXNzZW5kZXIta21za2V5Jyx7XG4gICAgICByZW1vdmFsUG9saWN5OiBSZW1vdmFsUG9saWN5LkRFU1RST1ksXG4gICAgICBwZW5kaW5nV2luZG93OiBEdXJhdGlvbi5kYXlzKDcpLFxuICAgICAgYWxpYXM6ICdhbGlhcy9jdXN0b21zbXNzZW5kZXJLZXknLFxuICAgICAgZGVzY3JpcHRpb246ICdLTVMga2V5IGZvciBlbmNyeXB0aW5nIGNvZ25pdG8gY29kZScsXG4gICAgICBlbmFibGVLZXlSb3RhdGlvbjogZmFsc2UsXG4gICAgfSk7XG5cbiAgLy8gUGVybWlzc2lvbnMgcmVxdWlyZWQgYnkgQ29nbml0byBlbmNyeXB0IGNvZGUgdXNpbmcgS01TIGtleVxuICBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2ttc2tleS5hZGRUb1Jlc291cmNlUG9saWN5KFxuICAgICAgICBuZXcgaWFtLlBvbGljeVN0YXRlbWVudCh7XG4gICAgICAgICAgZWZmZWN0OmlhbS5FZmZlY3QuQUxMT1csXG4gICAgICAgICAgcHJpbmNpcGFsczogW25ldyBpYW0uU2VydmljZVByaW5jaXBhbCgnY29nbml0by1pZHAuYW1hem9uYXdzLmNvbScpXSxcbiAgICAgICAgICBhY3Rpb25zOiBbJ2ttczpDcmVhdGVHcmFudCcsICdrbXM6RW5jcnlwdCddLFxuICAgICAgICAgIHJlc291cmNlczogWycqJ10sXG4gICAgICAgIH0pXG4gICAgICApO1xuXG4gIC8vUGVybWlzc2lvbnMgcmVxdWlyZWQgYnkgQVdTIExhbWJkYSBmdW5jdGlvbiBkZWNyeXB0IGNvZGUgZnJvbSBjb2duaXRvIGFuZCBnZXQgV2hhdHNhcHAgYWNjZXNzIHRva2VuXG4gIGNvbnN0IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfbGFtYmRhX3Blcm1pc3Npb25zID0gbmV3IGlhbS5Qb2xpY3lEb2N1bWVudCh7XG4gICAgc3RhdGVtZW50czogW1xuICAgICAgbmV3IGlhbS5Qb2xpY3lTdGF0ZW1lbnQoe1xuICAgICAgICBlZmZlY3Q6IGlhbS5FZmZlY3QuQUxMT1csXG4gICAgICAgIGFjdGlvbnM6IFsna21zOkRlY3J5cHQnXSwgXG4gICAgICAgIHJlc291cmNlczogW2NvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfa21za2V5LmtleUFybl0sXG4gICAgICB9KSxcbiAgICAgIG5ldyBpYW0uUG9saWN5U3RhdGVtZW50KHtcbiAgICAgICAgZWZmZWN0OiBpYW0uRWZmZWN0LkFMTE9XLFxuICAgICAgICBhY3Rpb25zOiBbJ3NlY3JldHNtYW5hZ2VyOkdldFNlY3JldFZhbHVlJ10sIFxuICAgICAgICByZXNvdXJjZXM6IFtTRUNSRVRfQVJOXSxcbiAgICAgIH0pLFxuICAgIF1cbiAgfSlcblxuICAgICAvL0NyZWF0aW5nIGFuIElBTSByb2xlIGZvciBBV1MgTGFtYmRhIGZ1bmN0aW9uXG4gICAgICBjb25zdCBsYW1iZGFfcm9sZSA9IG5ldyBpYW0uUm9sZSAodGhpcywgJ2NvZ25pdG8tY3VzdG9tc21zc2VuZGVyLWxhbWJkYS1yb2xlJyx7XG4gICAgICAgIGFzc3VtZWRCeTogbmV3IGlhbS5TZXJ2aWNlUHJpbmNpcGFsKCdsYW1iZGEuYW1hem9uYXdzLmNvbScpLFxuICAgICAgICBkZXNjcmlwdGlvbjonTGFtYmRhIEV4ZWN1dGlvbiBSb2xlIGZvciBDb2duaXRvIEN1c3RvbSBTTVMgU2VuZGVyJyxcbiAgICAgICAgcm9sZU5hbWU6J2NvZ25pdG8tY3VzdG9tLXNtcy1zZW5kZXItbGFtYmRhLXJvbGUtMicsXG4gICAgICAgIG1hbmFnZWRQb2xpY2llczpbaWFtLk1hbmFnZWRQb2xpY3kuZnJvbUF3c01hbmFnZWRQb2xpY3lOYW1lKCdzZXJ2aWNlLXJvbGUvQVdTTGFtYmRhQmFzaWNFeGVjdXRpb25Sb2xlJyldXG4gICAgICB9KTtcblxuICAgIC8vQ3JlYXRpbmcgYW4gQVdTIExhbWJkYSBSb2xlIFBvbGljeVxuICAgICAgY29uc3QgbGFtYmRhX3BvbGljeSA9IG5ldyBpYW0uUG9saWN5KHRoaXMsJ2NvZ25pdG8tY3VzdG9tc21zc2VuZGVyLWxhbWJkYS1wb2xpY3knLHtcbiAgICAgICAgZG9jdW1lbnQ6IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfbGFtYmRhX3Blcm1pc3Npb25zXG4gICAgICB9KTtcbiAgICAgIGxhbWJkYV9wb2xpY3kuYXR0YWNoVG9Sb2xlKGxhbWJkYV9yb2xlKVxuXG4gICAgLy9DdXN0b20gTGFtYmRhIG1lc3NhZ2Ugc2VuZGVyIGZ1bmN0aW9uXG4gICAgY29uc3QgY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9sYW1iZGFfZnVuY3Rpb24gPW5ldyBsYW1iZGFweXRob24uUHl0aG9uRnVuY3Rpb24odGhpcywgJ2NvZ25pdG8tY3VzdG9tc21zc2VuZGVyLWxhbWJkYS1mdW5jdGlvbicsIHtcbiAgICAgIGZ1bmN0aW9uTmFtZTonY29nbml0by13aGF0c2FwcCcsXG4gICAgICBlbnRyeTogJ2xhbWJkYS9jb2RlJywgLy8gcmVxdWlyZWRcbiAgICAgIHJ1bnRpbWU6IGxhbWJkYS5SdW50aW1lLlBZVEhPTl8zXzExLCAvLyByZXF1aXJlZFxuICAgICAgaW5kZXg6ICdsYW1iZGFfZnVuY3Rpb24ucHknLCAvLyBvcHRpb25hbCwgZGVmYXVsdHMgdG8gJ2luZGV4LnB5J1xuICAgICAgaGFuZGxlcjogJ2hhbmRsZXInLCAvLyBvcHRpb25hbCwgZGVmYXVsdHMgdG8gJ2hhbmRsZXInLFxuICAgICAgZGVzY3JpcHRpb246J0N1c3RvbSBXaGF0c2FwcCBNZXNzYWdlIFNlbmRpbmcgTGFtYmRhIGZ1bmN0aW9uJyxcbiAgICAgIHJvbGU6bGFtYmRhX3JvbGUsXG4gICAgICB0aW1lb3V0OiBEdXJhdGlvbi5taW51dGVzKDMpLFxuICAgICAgZW52aXJvbm1lbnQ6IHtcbiAgICAgICAgJ1BIT05FX05VTUJFUl9JRCc6IFBIT05FX05VTUJFUl9JRCxcbiAgICAgICAgJ1NFQ1JFVF9OQU1FJzogU0VDUkVUX05BTUUsXG4gICAgICAgICdLRVlfQVJOJzogY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9rbXNrZXkua2V5QXJuXG4gICAgICB9ICBcbiAgICAgIH0pO1xuICAgIFxuXG4gICAgLy8gQ3JlYXRpbmcgY29nbml0byB1c2VyIHBvb2xcbiAgICBjb25zdCBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX3VzZXJwb29sID0gbmV3IGNvZ25pdG8uVXNlclBvb2wodGhpcywgJ2N1c3RvbS1zbXMtc2VuZGVyLXVzZXJwb29sJywge1xuICAgICAgdXNlclBvb2xOYW1lOiAnY3VzdG9tLXNtcy1zZW5kZXItdXNlcnBvb2wnLFxuICAgICAgc2VsZlNpZ25VcEVuYWJsZWQ6IHRydWUsXG4gICAgICBzaWduSW5DYXNlU2Vuc2l0aXZlOiBmYWxzZSxcbiAgICAgIHNpZ25JbkFsaWFzZXM6IHtcbiAgICAgICAgZW1haWw6IHRydWUsXG4gICAgICAgIHBob25lOiB0cnVlLFxuICAgICAgfSxcbiAgICAgIGF1dG9WZXJpZnk6IHtcbiAgICAgICAgZW1haWw6IHRydWUsXG4gICAgICAgIHBob25lOiB0cnVlXG4gICAgICB9LFxuICAgICAgc3RhbmRhcmRBdHRyaWJ1dGVzOiB7XG4gICAgICAgIGZ1bGxuYW1lOiB7XG4gICAgICAgICAgcmVxdWlyZWQ6IHRydWUsXG4gICAgICAgICAgbXV0YWJsZTogdHJ1ZSxcbiAgICAgICAgfSxcbiAgICAgICAgZW1haWw6IHtcbiAgICAgICAgICByZXF1aXJlZDogdHJ1ZSxcbiAgICAgICAgICBtdXRhYmxlOiB0cnVlLFxuICAgICAgICB9LFxuICAgICAgICBwaG9uZU51bWJlcjoge1xuICAgICAgICAgIHJlcXVpcmVkOiB0cnVlLFxuICAgICAgICAgIG11dGFibGU6IHRydWUsXG4gICAgICAgIH1cbiAgICAgIH0sXG4gICAgICBtZmE6IGNvZ25pdG8uTWZhLlJFUVVJUkVELFxuICAgICAgbWZhU2Vjb25kRmFjdG9yOiB7XG4gICAgICAgIHNtczogdHJ1ZSxcbiAgICAgICAgb3RwOiBmYWxzZSxcbiAgICAgIH0sXG4gICAgICBwYXNzd29yZFBvbGljeToge1xuICAgICAgICBtaW5MZW5ndGg6IDgsXG4gICAgICAgIHJlcXVpcmVMb3dlcmNhc2U6IHRydWUsXG4gICAgICAgIHJlcXVpcmVEaWdpdHM6IHRydWUsXG4gICAgICAgIHJlcXVpcmVTeW1ib2xzOiB0cnVlLFxuICAgICAgfSxcbiAgICAgIHJlbW92YWxQb2xpY3k6IFJlbW92YWxQb2xpY3kuREVTVFJPWSxcbiAgICAgIGFjY291bnRSZWNvdmVyeTogY29nbml0by5BY2NvdW50UmVjb3ZlcnkuRU1BSUxfT05MWSxcbiAgICAgIGN1c3RvbVNlbmRlckttc0tleTogY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9rbXNrZXlcbiAgICB9KTtcblxuICAgIC8vRW5hYmxlIEN1c3RvbVNNU1NlbmRlciBMYW1iZGEgdHJpZ2dlclxuICAgIGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfdXNlcnBvb2wuYWRkVHJpZ2dlcihVc2VyUG9vbE9wZXJhdGlvbi5DVVNUT01fU01TX1NFTkRFUiwgY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9sYW1iZGFfZnVuY3Rpb24pO1xuXG4gICAgLy9DcmVhdGluZyBDb2duaXRvIHBvb2wgYXBwIGNsaWVudCBcbiAgICBjb25zdCBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2NsaWVudF9hcHAgPSBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX3VzZXJwb29sLmFkZENsaWVudChcImNvZ25pdG8tY3VzdG9tLXNtcy1zZW5kZXItYXBwLWNsaWVudFwiLCB7XG4gICAgICB1c2VyUG9vbENsaWVudE5hbWU6IFwiY29nbml0by1jdXN0b20tc21zLXNlbmRlci1jbGllbnQtYXBwLWlkXCJcbiAgICB9KTtcblxuICAgIG5ldyBDZm5PdXRwdXQodGhpcywgXCJjb2duaXRvLWN1c3RvbS1zbXMtc2VuZGVyLWNsaWVudC1hcHAtaWRcIiwge1xuICAgICAgdmFsdWU6IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfY2xpZW50X2FwcC51c2VyUG9vbENsaWVudElkLFxuICAgIH0pO1xuICB9XG59XG5cbiJdfQ==