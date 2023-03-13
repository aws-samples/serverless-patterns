using Amazon.Lambda.Core;
using CallbackPatternSample.Models;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace processOrderFunction;

public class Function
{    
    public Order FunctionHandler(Order order, ILambdaContext context)
    {
        LambdaLogger.Log($"Order received => {order.OrderDetails}");
        return order;
    }
}
