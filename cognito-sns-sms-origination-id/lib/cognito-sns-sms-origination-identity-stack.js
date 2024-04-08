"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CognitoSnsSmsOriginationIdentityStack = void 0;
const cdk = require("aws-cdk-lib");
const aws_cdk_lib_1 = require("aws-cdk-lib");
const kms = require("aws-cdk-lib/aws-kms");
const cognito = require("aws-cdk-lib/aws-cognito");
const lambda = require("aws-cdk-lib/aws-lambda");
const iam = require("aws-cdk-lib/aws-iam");
const aws_cognito_1 = require("aws-cdk-lib/aws-cognito");
class CognitoSnsSmsOriginationIdentityStack extends cdk.Stack {
    constructor(scope, id, props) {
        super(scope, id, props);
        // Kms key for Cognito custom sms sender 
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
        //Permissions required by AWS Lambda function decrypt code from cognito
        const cognito_custom_sms_sender_lambda_permissions = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "sid": "cognito-customsmssender-sns-permission",
                    "Effect": "Allow",
                    "Action": [
                        "sns:publish"
                    ],
                    "Resource": "*"
                },
                {
                    "sid": "cognito-customsmssender-kms-permission",
                    "Effect": "Allow",
                    "Action": [
                        "kms:Decrypt"
                    ],
                    "Resource": "*"
                }
            ]
        };
        //Creating an IAM role for AWS Lambda function
        const lambda_role = new iam.Role(this, 'cognito-customsmssender-lambda-role', {
            assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
            description: 'Lambda Execution Role for Cognito Custom SMS Sender',
            roleName: 'cognito-custom-sms-sender-lambda-role',
            managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')]
        });
        //Creating an AWS Lambda Role Policy
        const lambda_policy = new iam.Policy(this, 'cognito-customsmssender-lambda-policy', {
            document: iam.PolicyDocument.fromJson(cognito_custom_sms_sender_lambda_permissions)
        });
        lambda_policy.attachToRole(lambda_role);
        //Creating an AWS Lambda layers
        const cognito_custom_sms_sender_lambda_layer = new lambda.LayerVersion(this, 'cognito-customsmssender-nodejs-lib', {
            code: new lambda.AssetCode('lambda/layer/'),
            compatibleRuntimes: [lambda.Runtime.NODEJS_18_X],
            compatibleArchitectures: [lambda.Architecture.X86_64, lambda.Architecture.ARM_64],
            removalPolicy: aws_cdk_lib_1.RemovalPolicy.DESTROY,
        });
        //Creating CustomSMSSender Lambda function
        const cognito_custom_sms_sender_lambda_function = new lambda.Function(this, 'cognito-customsmssender-lambda-function', {
            runtime: lambda.Runtime.NODEJS_18_X,
            code: lambda.Code.fromAsset('lambda/code'),
            description: 'Customer SMS Sender Lambda function',
            role: lambda_role,
            handler: 'index.handler',
            layers: [cognito_custom_sms_sender_lambda_layer],
            environment: {
                'KMS_KEY_ARN': cognito_custom_sms_sender_kmskey.keyArn
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
exports.CognitoSnsSmsOriginationIdentityStack = CognitoSnsSmsOriginationIdentityStack;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiY29nbml0by1zbnMtc21zLW9yaWdpbmF0aW9uLWlkZW50aXR5LXN0YWNrLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiY29nbml0by1zbnMtc21zLW9yaWdpbmF0aW9uLWlkZW50aXR5LXN0YWNrLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7OztBQUFBLG1DQUFtQztBQUNuQyw2Q0FBaUU7QUFDakUsMkNBQTJDO0FBQzNDLG1EQUFtRDtBQUNuRCxpREFBaUQ7QUFDakQsMkNBQTJDO0FBRzNDLHlEQUE0RDtBQUc1RCxNQUFhLHFDQUFzQyxTQUFRLEdBQUcsQ0FBQyxLQUFLO0lBQ2xFLFlBQVksS0FBZ0IsRUFBRSxFQUFVLEVBQUUsS0FBc0I7UUFDOUQsS0FBSyxDQUFDLEtBQUssRUFBRSxFQUFFLEVBQUUsS0FBSyxDQUFDLENBQUM7UUFFeEIseUNBQXlDO1FBQ3ZDLE1BQU0sZ0NBQWdDLEdBQUcsSUFBSSxHQUFHLENBQUMsR0FBRyxDQUFDLElBQUksRUFBRSxnQ0FBZ0MsRUFBQztZQUMxRixhQUFhLEVBQUUsMkJBQWEsQ0FBQyxPQUFPO1lBQ3BDLGFBQWEsRUFBRSxzQkFBUSxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUM7WUFDL0IsS0FBSyxFQUFFLDBCQUEwQjtZQUNqQyxXQUFXLEVBQUUscUNBQXFDO1lBQ2xELGlCQUFpQixFQUFFLEtBQUs7U0FDekIsQ0FBQyxDQUFDO1FBRUwsNkRBQTZEO1FBQzdELGdDQUFnQyxDQUFDLG1CQUFtQixDQUM5QyxJQUFJLEdBQUcsQ0FBQyxlQUFlLENBQUM7WUFDdEIsTUFBTSxFQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsS0FBSztZQUN2QixVQUFVLEVBQUUsQ0FBQyxJQUFJLEdBQUcsQ0FBQyxnQkFBZ0IsQ0FBQywyQkFBMkIsQ0FBQyxDQUFDO1lBQ25FLE9BQU8sRUFBRSxDQUFDLGlCQUFpQixFQUFFLGFBQWEsQ0FBQztZQUMzQyxTQUFTLEVBQUUsQ0FBQyxHQUFHLENBQUM7U0FDakIsQ0FBQyxDQUNILENB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ZDtnQkFDRCxLQUFLLEVBQUU7b0JBQ0wsUUFBUSxFQUFFLElBQUk7b0JBQ2QsT0FBTyxFQUFFLElBQUk7aUJBQ2Q7Z0JBQ0QsV0FBVyxFQUFFO29CQUNYLFFBQVEsRUFBRSxJQUFJO29CQUNkLE9BQU8sRUFBRSxJQUFJO2lCQUNkO2FBQ0Y7WUFDRCxHQUFHLEVBQUUsT0FBTyxDQUFDLEdBQUcsQ0FBQyxRQUFRO1lBQ3pCLGVBQWUsRUFBRTtnQkFDZixHQUFHLEVBQUUsSUFBSTtnQkFDVCxHQUFHLEVBQUUsS0FBSzthQUNYO1lBQ0QsY0FBYyxFQUFFO2dCQUNkLFNBQVMsRUFBRSxDQUFDO2dCQUNaLGdCQUFnQixFQUFFLElBQUk7Z0JBQ3RCLGFBQWEsRUFBRSxJQUFJO2dCQUNuQixjQUFjLEVBQUUsSUFBSTthQUNyQjtZQUNELGFBQWEsRUFBRSwyQkFBYSxDQUFDLE9BQU87WUFDcEMsZUFBZSxFQUFFLE9BQU8sQ0FBQyxlQUFlLENBQUMsVUFBVTtZQUNuRCxrQkFBa0IsRUFBRSxnQ0FBZ0M7U0FDckQsQ0FBQyxDQUFDO1FBRUgsdUNBQXVDO1FBQ3ZDLGtDQUFrQyxDQUFDLFVBQVUsQ0FBQywrQkFBaUIsQ0FBQyxpQkFBaUIsRUFBRSx5Q0FBeUMsQ0FBQyxDQUFDO1FBRTlILG1DQUFtQztRQUNuQyxNQUFNLG9DQUFvQyxHQUFHLGtDQUFrQyxDQUFDLFNBQVMsQ0FBQyxzQ0FBc0MsRUFBRTtZQUNoSSxrQkFBa0IsRUFBRSx5Q0FBeUM7U0FDOUQsQ0FBQyxDQUFDO1FBRUgsSUFBSSx1QkFBUyxDQUFDLElBQUksRUFBRSx5Q0FBeUMsRUFBRTtZQUM3RCxLQUFLLEVBQUUsb0NBQW9DLENBQUMsZ0JBQWdCO1NBQzdELENBQUMsQ0FBQztJQUVQLENBQUM7Q0FDRjtBQXpJRCxzRkF5SUMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgKiBhcyBjZGsgZnJvbSAnYXdzLWNkay1saWInO1xuaW1wb3J0IHsgQ2ZuT3V0cHV0LCBEdXJhdGlvbiwgUmVtb3ZhbFBvbGljeSB9IGZyb20gJ2F3cy1jZGstbGliJztcbmltcG9ydCAqIGFzIGttcyBmcm9tICdhd3MtY2RrLWxpYi9hd3Mta21zJztcbmltcG9ydCAqIGFzIGNvZ25pdG8gZnJvbSAnYXdzLWNkay1saWIvYXdzLWNvZ25pdG8nO1xuaW1wb3J0ICogYXMgbGFtYmRhIGZyb20gJ2F3cy1jZGstbGliL2F3cy1sYW1iZGEnO1xuaW1wb3J0ICogYXMgaWFtIGZyb20gJ2F3cy1jZGstbGliL2F3cy1pYW0nO1xuXG5pbXBvcnQgeyBDb25zdHJ1Y3QgfSBmcm9tICdjb25zdHJ1Y3RzJztcbmltcG9ydCB7IFVzZXJQb29sT3BlcmF0aW9uIH0gZnJvbSAnYXdzLWNkay1saWIvYXdzLWNvZ25pdG8nO1xuXG5cbmV4cG9ydCBjbGFzcyBDb2duaXRvU25zU21zT3JpZ2luYXRpb25JZGVudGl0eVN0YWNrIGV4dGVuZHMgY2RrLlN0YWNrIHtcbiAgY29uc3RydWN0b3Ioc2NvcGU6IENvbnN0cnVjdCwgaWQ6IHN0cmluZywgcHJvcHM/OiBjZGsuU3RhY2tQcm9wcykge1xuICAgIHN1cGVyKHNjb3BlLCBpZCwgcHJvcHMpO1xuXG4gICAgLy8gS21zIGtleSBmb3IgQ29nbml0byBjdXN0b20gc21zIHNlbmRlciBcbiAgICAgIGNvbnN0IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfa21za2V5ID0gbmV3IGttcy5LZXkodGhpcywgJ2NvZ25pdG8tY3VzdG9tc21zc2VuZGVyLWttc2tleScse1xuICAgICAgICByZW1vdmFsUG9saWN5OiBSZW1vdmFsUG9saWN5LkRFU1RST1ksXG4gICAgICAgIHBlbmRpbmdXaW5kb3c6IER1cmF0aW9uLmRheXMoNyksXG4gICAgICAgIGFsaWFzOiAnYWxpYXMvY3VzdG9tc21zc2VuZGVyS2V5JyxcbiAgICAgICAgZGVzY3JpcHRpb246ICdLTVMga2V5IGZvciBlbmNyeXB0aW5nIGNvZ25pdG8gY29kZScsXG4gICAgICAgIGVuYWJsZUtleVJvdGF0aW9uOiBmYWxzZSxcbiAgICAgIH0pO1xuXG4gICAgLy8gUGVybWlzc2lvbnMgcmVxdWlyZWQgYnkgQ29nbml0byBlbmNyeXB0IGNvZGUgdXNpbmcgS01TIGtleVxuICAgIGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfa21za2V5LmFkZFRvUmVzb3VyY2VQb2xpY3koXG4gICAgICAgICAgbmV3IGlhbS5Qb2xpY3lTdGF0ZW1lbnQoe1xuICAgICAgICAgICAgZWZmZWN0OmlhbS5FZmZlY3QuQUxMT1csXG4gICAgICAgICAgICBwcmluY2lwYWxzOiBbbmV3IGlhbS5TZXJ2aWNlUHJpbmNpcGFsKCdjb2duaXRvLWlkcC5hbWF6b25hd3MuY29tJyldLFxuICAgICAgICAgICAgYWN0aW9uczogWydrbXM6Q3JlYXRlR3JhbnQnLCAna21zOkVuY3J5cHQnXSxcbiAgICAgICAgICAgIHJlc291cmNlczogWycqJ10sXG4gICAgICAgICAgfSlcbiAgICAgICAgKTtcblxuICAgIC8vUGVybWlzc2lvbnMgcmVxdWlyZWQgYnkgQVdTIExhbWJkYSBmdW5jdGlvbiBkZWNyeXB0IGNvZGUgZnJvbSBjb2duaXRvXG4gICAgICBjb25zdCBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2xhbWJkYV9wZXJtaXNzaW9ucyA9IHtcbiAgICAgICAgICAgIFwiVmVyc2lvblwiOiBcIjIwMTItMTAtMTdcIixcbiAgICAgICAgICAgIFwiU3RhdGVtZW50XCI6IFtcbiAgICAgICAgICAgICAgICB7XG4gICAgICAgICAgICAgICAgICAgIFwic2lkXCI6XCJjb2duaXRvLWN1c3RvbXNtc3NlbmRlci1zbnMtcGVybWlzc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsXG4gICAgICAgICAgICAgICAgICAgIFwiQWN0aW9uXCI6IFtcbiAgICAgICAgICAgICAgICAgICAgICAgIFwic25zOnB1Ymxpc2hcIlxuICAgICAgICAgICAgICAgICAgICBdLFxuICAgICAgICAgICAgICAgICAgICBcIlJlc291cmNlXCI6IFwiKlwiXG4gICAgICAgICAgICAgICAgfSxcbiAgICAgICAgICAgICAgICB7XG4gICAgICAgICAgICAgICAgICAgIFwic2lkXCI6XCJjb2duaXRvLWN1c3RvbXNtc3NlbmRlci1rbXMtcGVybWlzc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsXG4gICAgICAgICAgICAgICAgICAgIFwiQWN0aW9uXCI6IFtcbiAgICAgICAgICAgICAgICAgICAgICAgIFwia21zOkRlY3J5cHRcIlxuICAgICAgICAgICAgICAgICAgICBdLFxuICAgICAgICAgICAgICAgICAgICBcIlJlc291cmNlXCI6IFwiKlwiXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgXVxuICAgICAgICB9XG5cbiAgICAgICAvL0NyZWF0aW5nIGFuIElBTSByb2xlIGZvciBBV1MgTGFtYmRhIGZ1bmN0aW9uXG4gICAgICAgIGNvbnN0IGxhbWJkYV9yb2xlID0gbmV3IGlhbS5Sb2xlICh0aGlzLCAnY29nbml0by1jdXN0b21zbXNzZW5kZXItbGFtYmRhLXJvbGUnLHtcbiAgICAgICAgICBhc3N1bWVkQnk6IG5ldyBpYW0uU2VydmljZVByaW5jaXBhbCgnbGFtYmRhLmFtYXpvbmF3cy5jb20nKSxcbiAgICAgICAgICBkZXNjcmlwdGlvbjonTGFtYmRhIEV4ZWN1dGlvbiBSb2xlIGZvciBDb2duaXRvIEN1c3RvbSBTTVMgU2VuZGVyJyxcbiAgICAgICAgICByb2xlTmFtZTonY29nbml0by1jdXN0b20tc21zLXNlbmRlci1sYW1iZGEtcm9sZScsXG4gICAgICAgICAgbWFuYWdlZFBvbGljaWVzOltpYW0uTWFuYWdlZFBvbGljeS5mcm9tQXdzTWFuYWdlZFBvbGljeU5hbWUoJ3NlcnZpY2Utcm9sZS9BV1NMYW1iZGFCYXNpY0V4ZWN1dGlvblJvbGUnKV1cbiAgICAgICAgfSk7XG4gIFxuICAgICAgLy9DcmVhdGluZyBhbiBBV1MgTGFtYmRhIFJvbGUgUG9saWN5XG4gICAgICAgIGNvbnN0IGxhbWJkYV9wb2xpY3kgPSBuZXcgaWFtLlBvbGljeSh0aGlzLCdjb2duaXRvLWN1c3RvbXNtc3NlbmRlci1sYW1iZGEtcG9saWN5Jyx7XG4gICAgICAgICAgZG9jdW1lbnQ6IGlhbS5Qb2xpY3lEb2N1bWVudC5mcm9tSnNvbihjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2xhbWJkYV9wZXJtaXNzaW9ucylcbiAgICAgICAgfSk7XG4gICAgICAgIGxhbWJkYV9wb2xpY3kuYXR0YWNoVG9Sb2xlKGxhbWJkYV9yb2xlKVxuXG4gICAgICAvL0NyZWF0aW5nIGFuIEFXUyBMYW1iZGEgbGF5ZXJzXG4gICAgICAgIGNvbnN0IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfbGFtYmRhX2xheWVyID0gbmV3IGxhbWJkYS5MYXllclZlcnNpb24odGhpcywgJ2NvZ25pdG8tY3VzdG9tc21zc2VuZGVyLW5vZGVqcy1saWInLHtcbiAgICAgICAgICBjb2RlOiBuZXcgbGFtYmRhLkFzc2V0Q29kZSgnbGFtYmRhL2xheWVyLycpLFxuICAgICAgICAgIGNvbXBhdGlibGVSdW50aW1lczpbbGFtYmRhLlJ1bnRpbWUuTk9ERUpTXzE4X1hdLFxuICAgICAgICAgIGNvbXBhdGlibGVBcmNoaXRlY3R1cmVzOiBbbGFtYmRhLkFyY2hpdGVjdHVyZS5YODZfNjQsIGxhbWJkYS5BcmNoaXRlY3R1cmUuQVJNXzY0XSxcbiAgICAgICAgICByZW1vdmFsUG9saWN5OiBSZW1vdmFsUG9saWN5LkRFU1RST1ksXG4gICAgICAgIH0pO1xuICAgICAgXG4gICAgICAvL0NyZWF0aW5nIEN1c3RvbVNNU1NlbmRlciBMYW1iZGEgZnVuY3Rpb25cbiAgICAgICAgY29uc3QgY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9sYW1iZGFfZnVuY3Rpb24gPSBuZXcgbGFtYmRhLkZ1bmN0aW9uKHRoaXMsICdjb2duaXRvLWN1c3RvbXNtc3NlbmRlci1sYW1iZGEtZnVuY3Rpb24nLCB7XG4gICAgICAgICAgcnVudGltZTogbGFtYmRhLlJ1bnRpbWUuTk9ERUpTXzE4X1ggLFxuICAgICAgICAgIGNvZGU6IGxhbWJkYS5Db2RlLmZyb21Bc3NldCgnbGFtYmRhL2NvZGUnKSxcbiAgICAgICAgICBkZXNjcmlwdGlvbjonQ3VzdG9tZXIgU01TIFNlbmRlciBMYW1iZGEgZnVuY3Rpb24nLFxuICAgICAgICAgIHJvbGU6bGFtYmRhX3JvbGUsXG4gICAgICAgICAgaGFuZGxlcjogJ2luZGV4LmhhbmRsZXInLFxuICAgICAgICAgIGxheWVyczpbY29nbml0b19jdXN0b21fc21zX3NlbmRlcl9sYW1iZGFfbGF5ZXJdLFxuICAgICAgICAgIGVudmlyb25tZW50OiB7XG4gICAgICAgICAgICAnS01TX0tFWV9BUk4nOiBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2ttc2tleS5rZXlBcm5cbiAgICAgICAgICB9ICAgICAgICAgICAgICAgIFxuICAgICAgICB9KTtcblxuICAgICAgLy8gQ3JlYXRpbmcgY29nbml0byB1c2VyIHBvb2xcbiAgICAgIGNvbnN0IGNvZ25pdG9fY3VzdG9tX3Ntc19zZW5kZXJfdXNlcnBvb2wgPSBuZXcgY29nbml0by5Vc2VyUG9vbCh0aGlzLCAnY3VzdG9tLXNtcy1zZW5kZXItdXNlcnBvb2wnLCB7XG4gICAgICAgIHVzZXJQb29sTmFtZTogJ2N1c3RvbS1zbXMtc2VuZGVyLXVzZXJwb29sJyxcbiAgICAgICAgc2VsZlNpZ25VcEVuYWJsZWQ6IHRydWUsXG4gICAgICAgIHNpZ25JbkNhc2VTZW5zaXRpdmU6IGZhbHNlLFxuICAgICAgICBzaWduSW5BbGlhc2VzOiB7XG4gICAgICAgICAgZW1haWw6IHRydWUsXG4gICAgICAgICAgcGhvbmU6IHRydWUsXG4gICAgICAgIH0sXG4gICAgICAgIGF1dG9WZXJpZnk6IHtcbiAgICAgICAgICBlbWFpbDogdHJ1ZSxcbiAgICAgICAgICBwaG9uZTogdHJ1ZVxuICAgICAgICB9LFxuICAgICAgICBzdGFuZGFyZEF0dHJpYnV0ZXM6IHtcbiAgICAgICAgICBmdWxsbmFtZToge1xuICAgICAgICAgICAgcmVxdWlyZWQ6IHRydWUsXG4gICAgICAgICAgICBtdXRhYmxlOiB0cnVlLFxuICAgICAgICAgIH0sXG4gICAgICAgICAgZW1haWw6IHtcbiAgICAgICAgICAgIHJlcXVpcmVkOiB0cnVlLFxuICAgICAgICAgICAgbXV0YWJsZTogdHJ1ZSxcbiAgICAgICAgICB9LFxuICAgICAgICAgIHBob25lTnVtYmVyOiB7XG4gICAgICAgICAgICByZXF1aXJlZDogdHJ1ZSxcbiAgICAgICAgICAgIG11dGFibGU6IHRydWUsXG4gICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICBtZmE6IGNvZ25pdG8uTWZhLlJFUVVJUkVELFxuICAgICAgICBtZmFTZWNvbmRGYWN0b3I6IHtcbiAgICAgICAgICBzbXM6IHRydWUsXG4gICAgICAgICAgb3RwOiBmYWxzZSxcbiAgICAgICAgfSxcbiAgICAgICAgcGFzc3dvcmRQb2xpY3k6IHtcbiAgICAgICAgICBtaW5MZW5ndGg6IDgsXG4gICAgICAgICAgcmVxdWlyZUxvd2VyY2FzZTogdHJ1ZSxcbiAgICAgICAgICByZXF1aXJlRGlnaXRzOiB0cnVlLFxuICAgICAgICAgIHJlcXVpcmVTeW1ib2xzOiB0cnVlLFxuICAgICAgICB9LFxuICAgICAgICByZW1vdmFsUG9saWN5OiBSZW1vdmFsUG9saWN5LkRFU1RST1ksXG4gICAgICAgIGFjY291bnRSZWNvdmVyeTogY29nbml0by5BY2NvdW50UmVjb3ZlcnkuRU1BSUxfT05MWSxcbiAgICAgICAgY3VzdG9tU2VuZGVyS21zS2V5OiBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2ttc2tleVxuICAgICAgfSk7XG5cbiAgICAgIC8vRW5hYmxlIEN1c3RvbVNNU1NlbmRlciBMYW1iZGEgdHJpZ2dlclxuICAgICAgY29nbml0b19jdXN0b21fc21zX3NlbmRlcl91c2VycG9vbC5hZGRUcmlnZ2VyKFVzZXJQb29sT3BlcmF0aW9uLkNVU1RPTV9TTVNfU0VOREVSLCBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2xhbWJkYV9mdW5jdGlvbik7XG5cbiAgICAgIC8vQ3JlYXRpbmcgQ29nbml0byBwb29sIGFwcCBjbGllbnQgXG4gICAgICBjb25zdCBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2NsaWVudF9hcHAgPSBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX3VzZXJwb29sLmFkZENsaWVudChcImNvZ25pdG8tY3VzdG9tLXNtcy1zZW5kZXItYXBwLWNsaWVudFwiLCB7XG4gICAgICAgIHVzZXJQb29sQ2xpZW50TmFtZTogXCJjb2duaXRvLWN1c3RvbS1zbXMtc2VuZGVyLWNsaWVudC1hcHAtaWRcIlxuICAgICAgfSk7XG4gIFxuICAgICAgbmV3IENmbk91dHB1dCh0aGlzLCBcImNvZ25pdG8tY3VzdG9tLXNtcy1zZW5kZXItY2xpZW50LWFwcC1pZFwiLCB7XG4gICAgICAgIHZhbHVlOiBjb2duaXRvX2N1c3RvbV9zbXNfc2VuZGVyX2NsaWVudF9hcHAudXNlclBvb2xDbGllbnRJZCxcbiAgICAgIH0pO1xuICAgICBcbiAgfSAgICAgIFxufVxuIl19