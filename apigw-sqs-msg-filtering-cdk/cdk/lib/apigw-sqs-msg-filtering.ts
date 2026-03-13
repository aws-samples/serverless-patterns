
import {
    aws_apigateway as apigw,
    aws_sqs as sqs,
    aws_iam as iam,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface ApiGwSqsProps {
    /**
     * API Gateway object
     */
    readonly apiGateway: apigw.IRestApi;

    /**
     * SQS Queue object
     */
    readonly sqsQueue: sqs.IQueue;

    /**
     * VTL Mapping  
     */
    readonly vtlMappingTemplate: string;
}

export class ApiGwSqsConstruct extends Construct {
    public customApiGateway: apigw.IRestApi;
    public customQueue: sqs.IQueue;

    constructor(scope: Construct, id: string, props: ApiGwSqsProps) {
        super(scope, id);

        this.customQueue = props.sqsQueue;
        this.customApiGateway = props.apiGateway;

        // Create IAM Role for API Gateway
        const sqsIntegrationRole = new iam.Role(this, 'apigwSqs-integration-role', {
            assumedBy: new iam.ServicePrincipal('apigateway.amazonaws.com'),
        });

        // Grant sqs:SendMessage* to Api Gateway Role
        this.customQueue.grantSendMessages(sqsIntegrationRole);

        // ApiGw-SQS Integration
        const apiGwSqsIntegration = new apigw.AwsIntegration({
            service: 'sqs',
            path: `${process.env.CDK_DEFAULT_ACCOUNT}/${this.customQueue.queueName}`,
            integrationHttpMethod: 'POST',
            options: {
                credentialsRole: sqsIntegrationRole,
                requestParameters: {
                    // https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests-json.html
                    'integration.request.header.Content-Type': `'application/x-amz-json-1.0'`,
                    'integration.request.header.X-Amz-Target': `'AmazonSQS.SendMessage'`
                },
                passthroughBehavior: apigw.PassthroughBehavior.NEVER,
                requestTemplates: {
                    'application/json': props.vtlMappingTemplate,
                },
                integrationResponses: [
                    {
                        statusCode: '200',
                    },
                    {
                        statusCode: '400',
                    },
                    {
                        statusCode: '500',
                    }
                ]
            },
        });


        const sqs_resource = this.customApiGateway.root.addResource('sqs');
        sqs_resource.addMethod('POST', apiGwSqsIntegration, {
            methodResponses: [
                {
                    statusCode: '400',
                },
                {
                    statusCode: '200',
                    'responseModels': {
                        'application/json': apigw.Model.EMPTY_MODEL
                    }
                },
                {
                    statusCode: '500',
                }
            ]
        });
    }
}