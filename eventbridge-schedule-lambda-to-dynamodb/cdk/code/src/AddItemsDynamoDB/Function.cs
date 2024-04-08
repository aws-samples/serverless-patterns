using Amazon.DynamoDBv2.DataModel;
using Amazon.DynamoDBv2;
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace AddItemsDynamoDB
{
    public class Function
    {
       public async Task<string> FunctionHandler(ILambdaContext context)
        {
            AmazonDynamoDBClient client = new AmazonDynamoDBClient();
            DynamoDBContext dynamoDBContext = new DynamoDBContext(client);
            await CreateNewUser(dynamoDBContext);
            return "A new user created - " + DateTime.Now;
        }

        private static async Task CreateNewUser(DynamoDBContext dynamoDBContext)
        {
            // Note: For demo pupose test data is created
            Guid guid = Guid.NewGuid();
            string userID = guid.ToString(); // Some unique value.
            User newUser = new User
            {
                Id = userID,
                Email = "FirstName.LastName@xxxx.com",
                FirstName = "FirstName",
                LastName = "LastName",
                TTL = DateTimeOffset.Now.AddMinutes(5).ToUnixTimeSeconds().ToString()
            };

            // Save the user.
            await dynamoDBContext.SaveAsync(newUser);
        }
    }
}