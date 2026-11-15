using Amazon.CDK;
using Amazon.CDK.AWS.SNS;
using Amazon.CDK.AWS.SNS.Subscriptions;
using Amazon.CDK.AWS.SQS;
using Constructs;

namespace Cdk
{
    using System;
    using System.Collections.Generic;

    using Cdk.Models;

    using Microsoft.Extensions.Configuration;

    using Queue = Amazon.CDK.AWS.SQS.Queue;
    using Topic = Amazon.CDK.AWS.SNS.Topic;

    /// <summary>
    /// Implementation of CDK stack
    /// </summary>
    public class CdkStack : Stack
    {
        /// <summary>
        /// Create CDK stack in the constructor
        /// </summary>
        /// <param name="scope">Scope of the construct</param>
        /// <param name="id">Id of the stack to create</param>
        /// <param name="props">Stack properties</param>
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Read settings from appSettings.json file
            IConfigurationRoot configuration = new ConfigurationBuilder().SetBasePath(AppDomain.CurrentDomain.BaseDirectory).AddJsonFile("appSettings.json").Build();
            Settings settings = configuration.Get<Settings>();
            if (settings is null)
                return;
            // Create SNS topic
            var topic = new Topic(this, $"{id}-{settings.SnsTopic.Name}", new TopicProps
            {
                TopicName = $"{id}-{settings.SnsTopic.Name}"
            });
            
            // Create Sqs queues based on the settings file 
            foreach (var sqsQueue in settings.SqsQueues)
            {
                this.GenerateQueue(
                    this,
                    sqsQueue,
                    topic,
                    id);
            }
        }
        
        /// <summary>
        /// Populate Queue object within the stack scope
        /// </summary>
        /// <param name="scope">Scope of the construct</param>
        /// <param name="sqsQueue">Queues settings provided in the appSettings.json</param>
        /// <param name="topicToSubscribe">SNS topic created in this stack</param>
        /// <param name="stackName">Name of the stack</param>
        private void GenerateQueue(Construct scope, SqsQueue sqsQueue, Topic topicToSubscribe, string stackName)
        {
            var queue = new Queue(
                scope,
                $"{stackName}-{sqsQueue.Name}",
                new QueueProps { QueueName = $"{stackName}-{sqsQueue.Name}" });
            
            // Subscribe to the Sns topic
            topicToSubscribe.AddSubscription(
                this.GenerateSubscription(
                    queue,
                    sqsQueue));
        }
        
        /// <summary>
        /// Populate Sqs subscription
        /// </summary>
        /// <param name="queue">Queue construct in scope</param>
        /// <param name="sqsQueue">Queue settings from appSettings.json</param>
        /// <returns>Created Subscription object</returns>
        private SqsSubscription GenerateSubscription(Queue queue, SqsQueue sqsQueue)
        {
            SqsSubscriptionProps props = null;
            if (sqsQueue.FilterByAttribute)
            {
                props = new SqsSubscriptionProps
                {
                    FilterPolicy = this.GenerateAttributedBasedFilterPolicy(sqsQueue.Filters)
                };
            }
            else
            {
                props = new SqsSubscriptionProps
                {
                    FilterPolicyWithMessageBody = this.GenerateMessageBasedFilterPolicy(sqsQueue.Filters)
                };
            }
            return new SqsSubscription(
                queue,
                props);
        }
        
        /// <summary>
        /// Populate Filter policy by message attribute
        /// </summary>
        /// <param name="filters">Filters provided in appSettings.json</param>
        /// <returns>Attribute based filter policy</returns>
        private IDictionary<string, SubscriptionFilter> GenerateAttributedBasedFilterPolicy(IList<Filter> filters)
        {
            var filterPolicy = new Dictionary<string, SubscriptionFilter>();
            foreach (var filter in filters)
            {
                filterPolicy.Add(
                    filter.Name,
                    SubscriptionFilter.StringFilter(
                        new StringConditions
                            { Allowlist = filter.Values }));
            }

            return filterPolicy;
        }
        
        /// <summary>
        /// Populate Filter policy by message body
        /// </summary>
        /// <param name="filters">Filters provided in appSettings.json</param>
        /// <returns>Message based filter policy</returns>
        private IDictionary<string, FilterOrPolicy> GenerateMessageBasedFilterPolicy(IList<Filter> filters)
        {
            var filterPolicy = new Dictionary<string, FilterOrPolicy>();
            foreach (var filter in filters)
            {
                filterPolicy.Add(filter.Name,
                    FilterOrPolicy.Filter(
                        SubscriptionFilter.StringFilter(
                            new StringConditions
                                { Allowlist = filter.Values })));
            }
            return filterPolicy;
        }
    }
}
