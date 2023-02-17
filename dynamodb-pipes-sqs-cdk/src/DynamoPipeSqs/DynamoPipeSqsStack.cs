using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.SQS;
using Constructs;

namespace DynamoPipeSqs;

public class DynamoPipeSqsStack : Stack
{
    public DynamoPipeSqsStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
    {
        var dynamoDbTable = new Table(this, "MyCdkTable", new TableProps()
        {
            BillingMode = BillingMode.PAY_PER_REQUEST,
            TableName = "dynamo-pipes-to-sqs",
            PartitionKey = new Attribute()
            {
                Name = "PK",
                Type = AttributeType.STRING
            },
            Stream = StreamViewType.NEW_IMAGE
        });

        // The CDK includes built-in constructs for most resource types, such as Queues and Topics.
        var queue = new Queue(this, "DynamoPipeSqsQueue", new QueueProps
        {
            QueueName = "dynamo-pipes-to-sqs",
            VisibilityTimeout = Duration.Seconds(300)
        });

        new DynamoToSqsPipeConstruct(this, "Pipe", new DynamoToSqsPipeProps
        {
            Name = "DynamoPipeSQSApp",
            SourceTableStreamArn = dynamoDbTable.TableStreamArn,
            DestinationQueueArn = queue.QueueArn
        });
    }
}
