using Amazon.CDK;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.SQS;
using Amazon.CDK.AWS.S3.Notifications; 
using Constructs;

namespace S3SqsDotnetCdk
{
    public class S3SqsDotnetCdkStack : Stack
    {
        internal S3SqsDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var queue = new Queue(this, "s3-to-sqs");
            var bucket = new Bucket(this, "MyBucket");
            bucket.AddEventNotification(EventType.OBJECT_CREATED, new SqsDestination(queue));

            // Output information about the created resources
            new CfnOutput(this, "sqs-queue-name", new CfnOutputProps { Value = queue.QueueName, Description = "Name of the SQS queue" });
            new CfnOutput(this, "sqs-queue-url", new CfnOutputProps { Value = queue.QueueUrl, Description = "URL of the SQS queue" });
            new CfnOutput(this, "s3-bucket-name", new CfnOutputProps { Value = bucket.BucketName, Description = "S3 bucket name" });
            new CfnOutput(this, "s3-bucket-url", new CfnOutputProps { Value = bucket.BucketWebsiteUrl, Description = "S3 bucket url" });
        }
    }
}
