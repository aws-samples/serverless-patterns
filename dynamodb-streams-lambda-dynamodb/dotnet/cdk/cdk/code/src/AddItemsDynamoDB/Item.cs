using Amazon.DynamoDBv2.DataModel;

namespace AddItemsDynamoDB
{
    [DynamoDBTable("TargetDynamoDB")]
    public class Item
    {
        [DynamoDBHashKey]
        public string Id { get; set; } = string.Empty;
    }
}
