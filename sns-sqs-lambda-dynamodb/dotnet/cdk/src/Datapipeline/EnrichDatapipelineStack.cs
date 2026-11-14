using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.SNS.Subscriptions;
using Amazon.CDK.AWS.SQS;
using Constructs;
using System;
using System.Collections.Generic;
using System.Text;

namespace Datapipeline
{

    public class EnrichDatapipelineStack : Stack
    {
        internal EnrichDatapipelineStack(Construct scope, string id, CrossStackProp props = null) : base(scope, id, props)
        {
            var CrossStackTopic = props.CrossStackTopic;
            var CrossStackTable = props.CrossStackTable;

            var enrichQueue = new Queue(this, "Enrich Queue", new QueueProps
            {
                VisibilityTimeout = Duration.Minutes(1)
            });

            CrossStackTopic.AddSubscription(new SqsSubscription(enrichQueue));

            var enrichQueueOutput = new Queue(this, "Enrich Queue Output", new QueueProps
            {
                VisibilityTimeout = Duration.Minutes(1)
            });

            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("./src/enrichLambda");

            DockerImageFunction dockerImageFunction = new DockerImageFunction(this,
                "container-image-enrichlambda-function",
                new DockerImageFunctionProps()
                {
                    Code = dockerImageCode,
                    Description = ".NET 6 Docker rawLambda function",
                    Environment = new Dictionary<string, string>
                    {
                        { "ENRICH_QUEUE", enrichQueueOutput.QueueUrl},
                        { "TABLE_NAME", CrossStackTable.TableName}
                    },
                    Timeout = Duration.Minutes(1)
                });

            enrichQueueOutput.GrantSendMessages(dockerImageFunction);
            CrossStackTable.GrantReadWriteData(dockerImageFunction);
            dockerImageFunction.AddEventSource(new SqsEventSource(enrichQueue));

        }
    }
}
