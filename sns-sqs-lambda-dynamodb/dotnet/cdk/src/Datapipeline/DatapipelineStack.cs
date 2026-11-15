using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.SNS;
using Amazon.CDK.AWS.SNS.Subscriptions;
using Amazon.CDK.AWS.SQS;
using Constructs;
using System.Collections.Generic;

namespace Datapipeline
{
    public class DatapipelineStack : Stack
    {
        public Topic CrossStackTopic { get; set; }
        public Table CrossStackTable { get; set; }


        internal DatapipelineStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var tableName = "gitusers";

            CrossStackTopic = new Topic(this, "Topic", new TopicProps
            {
                DisplayName = "git user topic"
            });

            var rawQueue = new Queue(this, "Raw Queue", new QueueProps
            {
                VisibilityTimeout = Duration.Minutes(1)
            });

            CrossStackTopic.AddSubscription(new SqsSubscription(rawQueue));


            CrossStackTable = new Table(this, "MyCdkTable", new TableProps()
            {
                BillingMode = BillingMode.PAY_PER_REQUEST,
                TableName = tableName,
                PartitionKey = new Attribute()
                {
                    Name = "login",
                    Type = AttributeType.STRING
                },
                SortKey = new Attribute()
                {
                    Name = "datatype",
                    Type = AttributeType.STRING
                }
            });

            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("./src/rawlambda");

            DockerImageFunction dockerImageFunction = new DockerImageFunction(this,
                "container-image-rawlambda-function",
                new DockerImageFunctionProps()
                {
                    Code = dockerImageCode,
                    Description = ".NET 6 Docker rawLambda function",
                    Environment = new Dictionary<string, string>
                    {
                        { "TABLE_NAME", CrossStackTable.TableName}
                    },
                    Timeout = Duration.Minutes(1)
                });

            CrossStackTable.GrantReadWriteData(dockerImageFunction);
            dockerImageFunction.AddEventSource(new SqsEventSource(rawQueue));
        }
    }
}
