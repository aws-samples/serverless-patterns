using System;
using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Pipes;
using Amazon.CDK.AWS.SQS;
using Constructs;

namespace DynamoPipeSqs;

public class DynamoToSqsPipeProps
{
    public string Name { get; set; }
    public string DestinationQueueArn { get; set; }
    public string SourceTableStreamArn { get; set; }
}

public class DynamoToSqsPipeConstruct : Construct
{
    public DynamoToSqsPipeConstruct(Construct scope, string id, DynamoToSqsPipeProps props) : base(scope, id)
    {
        if (props.SourceTableStreamArn == null) throw new ArgumentException("DynamoToSqsPipeConstruct SourceTable.TableStreamArn is null");

        var role = new Role(this, "DynamoDbHandlerRole", new RoleProps()
        {
            Description = "Role assumed by the Pipes to transfer data from DynamoDB streams to SQS",
            AssumedBy = new ServicePrincipal("pipes.amazonaws.com"),
        });

        role.AddToPolicy(new PolicyStatement(new PolicyStatementProps
        {
            Effect = Effect.ALLOW,
            Actions = new[] { "sqs:SendMessage" },
            Resources = new[] { props.DestinationQueueArn }
        }));

        role.AddToPolicy(new PolicyStatement(new PolicyStatementProps
        {
            Effect = Effect.ALLOW,
            Actions = new[]
            {
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams"
            },
            Resources = new[] { props.SourceTableStreamArn }
        }));

        var dlq = new Queue(this, "PipeDlq", new QueueProps
        {
            RetentionPeriod = Duration.Days(14)
        });

        new CfnPipe(this, "Pipe", new CfnPipeProps
        {
            RoleArn = role.RoleArn,
            Source = props.SourceTableStreamArn,
            Target = props.DestinationQueueArn,

            // the properties below are optional
            Name = props.Name,
            SourceParameters = new CfnPipe.PipeSourceParametersProperty
            {
                DynamoDbStreamParameters = new CfnPipe.PipeSourceDynamoDBStreamParametersProperty
                {
                    StartingPosition = "LATEST",
                    BatchSize = 10,
                    OnPartialBatchItemFailure = "AUTOMATIC_BISECT",
                    DeadLetterConfig = new CfnPipe.DeadLetterConfigProperty {
                        Arn = dlq.QueueArn
                    },
                    MaximumRetryAttempts = 185
                },
            },
        });
    }
}