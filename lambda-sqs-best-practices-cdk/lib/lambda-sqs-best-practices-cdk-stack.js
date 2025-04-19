const { Stack, Duration, CfnOutput } = require('aws-cdk-lib');
const lambda = require('aws-cdk-lib/aws-lambda');
const sqs = require('aws-cdk-lib/aws-sqs');
const lambdaEventSources = require('aws-cdk-lib/aws-lambda-event-sources');
const cloudwatch = require('aws-cdk-lib/aws-cloudwatch');
const iam = require('aws-cdk-lib/aws-iam');
const path = require('path');

class LambdaSqsBestPracticesCdkStack extends Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    // Create DLQ
    const dlq = new sqs.Queue(this, 'MyDeadLetterQueue', {
      queueName: 'my-dead-letter-queue',
      retentionPeriod: Duration.days(14),
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true
    });

    // Create main queue
    const queue = new sqs.Queue(this, 'MyQueue', {
      queueName: 'my-sample-queue',
      visibilityTimeout: Duration.seconds(30),
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      deadLetterQueue: {
        queue: dlq,
        maxReceiveCount: 3
      }
    });

    // Create Lambda function
    const mainLambdaFunction = new lambda.Function(this, 'MyLambdaFunction', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda')),
      environment: {
        POWERTOOLS_SERVICE_NAME: 'sqs-processor',
        POWERTOOLS_METRICS_NAMESPACE: 'SQSProcessor',
        LOG_LEVEL: 'INFO',
        ENVIRONMENT: props?.environment || 'development',
        POWERTOOLS_TRACER_CAPTURE_RESPONSE: 'true',
        POWERTOOLS_TRACER_CAPTURE_ERROR: 'true',
        AWS_NODEJS_CONNECTION_REUSE_ENABLED: '1'
      },
      timeout: Duration.seconds(30),
      memorySize: 256,
      tracing: lambda.Tracing.ACTIVE
    });

    // Add X-Ray permissions
    mainLambdaFunction.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'xray:PutTraceSegments',
        'xray:PutTelemetryRecords'
      ],
      resources: ['*']
    }));

    // Add CloudWatch Metrics permissions
    mainLambdaFunction.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'cloudwatch:PutMetricData'
      ],
      resources: ['*']
    }));

    // Add SQS trigger
    mainLambdaFunction.addEventSource(
      new lambdaEventSources.SqsEventSource(queue, {
        batchSize: 10,
        reportBatchItemFailures: true
      })
    );

    // Grant permissions
    queue.grantConsumeMessages(mainLambdaFunction);
    dlq.grantConsumeMessages(mainLambdaFunction);

    // Create CloudWatch Dashboard
    const dashboard = new cloudwatch.Dashboard(this, 'ProcessingDashboard', {
      dashboardName: 'SQS-Processing-Dashboard'
    });

    // Message Success/Failure Widget
    const messageProcessingWidget = new cloudwatch.GraphWidget({
      title: 'Message Processing Success/Failure',
      left: [
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'SuccessfulMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        }),
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'FailedMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        })
      ],
      width: 12
    });

    // Message Types Success Widget
    const messageTypesSuccessWidget = new cloudwatch.GraphWidget({
      title: 'Message Types - Success',
      left: [
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'SuccessfulJSONMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        }),
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'SuccessfulTEXTMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        })
      ],
      width: 12
    });

    // Message Types Failure Widget
    const messageTypesFailureWidget = new cloudwatch.GraphWidget({
      title: 'Message Types - Failure',
      left: [
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'FailedJSONMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        }),
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'FailedTEXTMessages',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        })
      ],
      width: 12
    });

    // Batch Processing Widget
    const batchProcessingWidget = new cloudwatch.GraphWidget({
      title: 'Batch Processing',
      left: [
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'BatchSize',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'sum',
          period: Duration.minutes(1)
        }),
        new cloudwatch.Metric({
          namespace: 'SQSProcessor',
          metricName: 'BatchProcessingTime',
          dimensionsMap: {
            service: 'sqs-processor'
          },
          statistic: 'average',
          period: Duration.minutes(1)
        })
      ],
      width: 12
    });

    // Queue Metrics Widget
    const queueMetricsWidget = new cloudwatch.GraphWidget({
      title: 'Queue Metrics',
      left: [
        queue.metricApproximateNumberOfMessagesVisible({
          period: Duration.minutes(1),
          statistic: 'sum'
        }),
        queue.metricApproximateAgeOfOldestMessage({
          period: Duration.minutes(1),
          statistic: 'maximum'
        }),
        dlq.metricApproximateNumberOfMessagesVisible({
          period: Duration.minutes(1),
          statistic: 'sum'
        })
      ],
      width: 12
    });

    // Lambda Performance Widget
    const lambdaPerformanceWidget = new cloudwatch.GraphWidget({
      title: 'Lambda Performance',
      left: [
        mainLambdaFunction.metricInvocations({
          period: Duration.minutes(1),
          statistic: 'sum'
        }),
        mainLambdaFunction.metricDuration({
          period: Duration.minutes(1),
          statistic: 'average'
        }),
        mainLambdaFunction.metricErrors({
          period: Duration.minutes(1),
          statistic: 'sum'
        })
      ],
      width: 12
    });

    // Add all widgets to dashboard
    dashboard.addWidgets(
      messageProcessingWidget,
      messageTypesSuccessWidget,
      messageTypesFailureWidget,
      batchProcessingWidget,
      queueMetricsWidget,
      lambdaPerformanceWidget
    );

    // Create CloudWatch Alarms
    
    // High Error Rate Alarm
    new cloudwatch.Alarm(this, 'HighErrorRate', {
      metric: new cloudwatch.Metric({
        namespace: 'SQSProcessor',
        metricName: 'FailedMessages',
        dimensionsMap: {
          service: 'sqs-processor'
        },
        statistic: 'sum',
        period: Duration.minutes(5)
      }),
      threshold: 1,
      evaluationPeriods: 1,
      alarmDescription: 'High message processing error rate'
    });

    // DLQ Messages Alarm
    new cloudwatch.Alarm(this, 'DLQMessagesPresent', {
      metric: dlq.metricApproximateNumberOfMessagesVisible(),
      threshold: 1,
      evaluationPeriods: 1,
      alarmDescription: 'Messages present in DLQ'
    });

    // Stack Outputs
    new CfnOutput(this, 'QueueUrl', {
      value: queue.queueUrl,
      description: 'Main SQS Queue URL',
      exportName: 'MainQueueUrl'
    });

    new CfnOutput(this, 'DlqUrl', {
      value: dlq.queueUrl,
      description: 'Dead Letter Queue URL',
      exportName: 'DlqUrl'
    });

    new CfnOutput(this, 'LambdaFunction', {
      value: mainLambdaFunction.functionName,
      description: 'Lambda Function Name',
      exportName: 'LambdaFunctionName'
    });

    new CfnOutput(this, 'DashboardUrl', {
      value: `https://${this.region}.console.aws.amazon.com/cloudwatch/home?region=${this.region}#dashboards:name=${dashboard.dashboardName}`,
      description: 'CloudWatch Dashboard URL',
      exportName: 'DashboardUrl'
    });
  }
}

module.exports = { LambdaSqsBestPracticesCdkStack }