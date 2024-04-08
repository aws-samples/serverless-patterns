using Amazon.DynamoDBv2.DataModel;

namespace AddItemsDynamoDB
{
    [DynamoDBTable("Users")]
    public class User
    {
        [DynamoDBHashKey]
        public string Id { get; set; }
        public string? Email { get; set; }
        public string? FirstName { get; set; }
        public string? LastName { get; set; }
        public string? Location { get; set; }
        public string? TTL { get; set; }
    }
}
