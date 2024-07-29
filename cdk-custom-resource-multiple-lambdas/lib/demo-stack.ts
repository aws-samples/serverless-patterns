import { CfnOutput, CustomResource, Fn, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Architecture, LoggingFormat, Runtime } from 'aws-cdk-lib/aws-lambda';
import { SqsEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { NodejsFunction, NodejsFunctionProps } from 'aws-cdk-lib/aws-lambda-nodejs';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

export class DemoStack extends Stack {
    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props);

        const logGroup = new LogGroup(this, 'CustomResourceLogGroup', {
            logGroupName: `/demo/CustomResourceMultipleLambdas`,
            retention: RetentionDays.ONE_DAY,
            removalPolicy: RemovalPolicy.DESTROY,
        });

        const commonLambdaProps: NodejsFunctionProps = {
            architecture: Architecture.ARM_64,
            logGroup,
            loggingFormat: LoggingFormat.JSON,
            runtime: Runtime.NODEJS_20_X,
        };

        const customResourceStartLambda = new NodejsFunction(this, 'start', commonLambdaProps);

        const customResourceQueue = new Queue(this, 'CustomResourceQueue', {});
        customResourceQueue.grantSendMessages(customResourceStartLambda);

        const customResource = new CustomResource(this, 'CustomResource', {
            serviceToken: customResourceStartLambda.functionArn,
            properties: {
                CustomResourceQueueUrl: customResourceQueue.queueUrl,
            },
        });

        const customResourceStopLambda = new NodejsFunction(this, 'stop', {
            ...commonLambdaProps,
            events: [new SqsEventSource(customResourceQueue),],
        });

        customResource.node.addDependency(customResourceStopLambda);
    }
}
