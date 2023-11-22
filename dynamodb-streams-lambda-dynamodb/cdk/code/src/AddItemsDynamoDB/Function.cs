using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Amazon.Lambda.Core;
using Amazon.Lambda.DynamoDBEvents;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace AddItemsDynamoDB
{
    public class Function
    {
        public void FunctionHandler(DynamoDBEvent dynamoEvent, ILambdaContext context)
        {
            try
            {
                AmazonDynamoDBClient client = new AmazonDynamoDBClient();
                DynamoDBContext dynamoDBContext = new DynamoDBContext(client);
                List<Item> items = new List<Item>();

                context.Logger.LogLine($"Beginning to process {dynamoEvent.Records.Count} records...");

                foreach (var record in dynamoEvent.Records)
                {
                    record.Dynamodb.NewImage.TryGetValue("Id", out var attribute);
                    Item newItem = new Item
                    {
                        Id = attribute!.S
                    };
                    items.Add(newItem);
                }

                // Create items in Target Dynamo DB Table            
                CreateNewItem(dynamoDBContext, items);
                context.Logger.LogLine("Stream processing complete.");
            }
            catch (Exception ex)
            {
                context.Logger.LogLine(ex.Message);
            }
        }

        private void CreateNewItem(DynamoDBContext dynamoDBContext, List<Item> items)
        {
            var itemBatch = dynamoDBContext.CreateBatchWrite<Item>();
            itemBatch.AddPutItems(items);
            itemBatch.ExecuteAsync();
        }
    }
}