using System.Diagnostics;
using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace Infra;

internal sealed class InfraStack : Stack
{
    internal InfraStack(Construct scope, string id, IStackProps? props = null)
        : base(scope, id, props)
    {
        // ──────────────────────────────────────────────────────────────────
        // DynamoDB Table — stores callback IDs (for testing) and results
        // ──────────────────────────────────────────────────────────────────
        var bookingsTable = new Table(this, "BookingsTable", new TableProps
        {
            PartitionKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "BookingId",
                Type = AttributeType.STRING
            },
            SortKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "SK",
                Type = AttributeType.STRING
            },
            BillingMode = BillingMode.PAY_PER_REQUEST,
            RemovalPolicy = RemovalPolicy.DESTROY
        });

        // ──────────────────────────────────────────────────────────────────
        // Lambda Function — Durable flight booking workflow
        // ──────────────────────────────────────────────────────────────────
        var publishOutputPath = PublishLambdaProject("src/TravelBooking/TravelBooking.csproj");

        var bookingFunction = new Function(this, "BookingFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "TravelBooking::TravelBooking.FlightBookingHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 512,
            Timeout = Duration.Seconds(900),
            DurableConfig = new DurableConfig
            {
                ExecutionTimeout = Duration.Minutes(15),
                RetentionPeriod = Duration.Days(7)
            },
            Environment = new Dictionary<string, string>
            {
                ["BOOKINGS_TABLE_NAME"] = bookingsTable.TableName
            },
            Description = "Durable Function: Flight booking with payment callback and saga compensation (15-min execution timeout)"
        });

        bookingsTable.GrantReadWriteData(bookingFunction);

        // ──────────────────────────────────────────────────────────────────
        // Lambda Function — Booking starter (thin proxy for API Gateway)
        // Receives the HTTP request, invokes the durable function async,
        // and returns 202 immediately.
        // ──────────────────────────────────────────────────────────────────
        var bookingStarterFunction = new Function(this, "BookingStarterFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "TravelBooking::TravelBooking.BookingStarterHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 256,
            Timeout = Duration.Seconds(30),
            Environment = new Dictionary<string, string>
            {
                ["BOOKING_FUNCTION_ARN"] = bookingFunction.CurrentVersion.FunctionArn
            },
            Description = "Booking starter — invokes durable workflow async and returns 202"
        });

        bookingFunction.CurrentVersion.GrantInvoke(bookingStarterFunction);

        // ──────────────────────────────────────────────────────────────────
        // Lambda Function — Payment callback handler
        // Payment gateway calls this after user completes OTP verification.
        // It simply forwards the confirmation to resume the durable function.
        // ──────────────────────────────────────────────────────────────────
        var paymentCallbackFunction = new Function(this, "PaymentCallbackFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "TravelBooking::TravelBooking.PaymentCallbackHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 256,
            Timeout = Duration.Seconds(30),
            Description = "Payment callback — resumes the durable booking workflow when payment gateway confirms"
        });

        // Allow the callback function to resume the durable workflow
        paymentCallbackFunction.AddToRolePolicy(new Amazon.CDK.AWS.IAM.PolicyStatement(
            new Amazon.CDK.AWS.IAM.PolicyStatementProps
            {
                Actions =
                [
                    "lambda:SendDurableExecutionCallbackSuccess",
                    "lambda:SendDurableExecutionCallbackFailure"
                ],
                Resources = [$"{bookingFunction.CurrentVersion.FunctionArn}/durable-execution/*"]
            }));

        // ──────────────────────────────────────────────────────────────────
        // REST API
        //   POST /bookings                          → start booking
        //   POST /bookings/payment-confirmation     → payment gateway confirms
        // ──────────────────────────────────────────────────────────────────
        var api = new RestApi(this, "BookingApi", new RestApiProps
        {
            RestApiName = "FlightBookingApi",
            Description = "Flight booking API"
        });

        var bookingsResource = api.Root.AddResource("bookings");
        bookingsResource.AddMethod("POST", new LambdaIntegration(bookingStarterFunction));

        var paymentConfirmResource = bookingsResource.AddResource("payment-confirmation");
        paymentConfirmResource.AddMethod("POST", new LambdaIntegration(paymentCallbackFunction));

        // ──────────────────────────────────────────────────────────────────
        // Outputs
        // ──────────────────────────────────────────────────────────────────
        _ = new CfnOutput(this, "ApiUrl", new CfnOutputProps
        {
            Value = api.Url!,
            Description = "API base URL"
        });

        _ = new CfnOutput(this, "BookingsEndpoint", new CfnOutputProps
        {
            Value = $"{api.Url}bookings",
            Description = "POST to start a booking"
        });

        _ = new CfnOutput(this, "PaymentCallbackEndpoint", new CfnOutputProps
        {
            Value = $"{api.Url}bookings/payment-confirmation",
            Description = "POST to confirm payment (callback token in request body)"
        });

        _ = new CfnOutput(this, "BookingsTableName", new CfnOutputProps
        {
            Value = bookingsTable.TableName,
            Description = "DynamoDB table — query for callback ID and results"
        });

        _ = new CfnOutput(this, "BookingFunctionArn", new CfnOutputProps
        {
            Value = bookingFunction.FunctionArn,
            Description = "ARN of the durable booking function"
        });
    }

    private static string PublishLambdaProject(string projectPath)
    {
        var publishDir = Path.Combine(
            Path.GetDirectoryName(projectPath)!,
            "bin", "Release", "net10.0", "publish");

        var process = Process.Start(new ProcessStartInfo
        {
            FileName = "dotnet",
            Arguments = $"publish \"{projectPath}\" -c Release -r linux-x64 --self-contained false -o \"{publishDir}\"",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        }) ?? throw new InvalidOperationException("Failed to start dotnet publish process.");

        var stdout = process.StandardOutput.ReadToEnd();
        var stderr = process.StandardError.ReadToEnd();
        process.WaitForExit();

        if (process.ExitCode != 0)
        {
            throw new InvalidOperationException(
                $"dotnet publish failed for '{projectPath}' (exit code {process.ExitCode}):\n{stderr}\n{stdout}");
        }

        return publishDir;
    }
}
