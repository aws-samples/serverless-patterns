using Amazon.Lambda.Core;
using CallbackPatternSample.Models;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace completeOrderFunction;

public class Function
{

    /// <summary>
    /// A simple function that takes a string and does a ToUpper
    /// </summary>
    /// <param name="input"></param>
    /// <param name="context"></param>
    /// <returns></returns>
    public Order FunctionHandler(Order order, ILambdaContext context)
    {
        LambdaLogger.Log($"Order Completed => {order.OrderDetails}");
        return order;
    }
}
