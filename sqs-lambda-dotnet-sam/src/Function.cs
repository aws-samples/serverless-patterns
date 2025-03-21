// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using static Amazon.Lambda.SQSEvents.SQSBatchResponse;


// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace SqsIntegration;

public class Function
{
    public async Task<SQSBatchResponse> FunctionHandler(SQSEvent evnt, ILambdaContext context)
    {
        List<BatchItemFailure> _batchItemFailures = new();

        if (evnt.Records.Count == 0)
        {
            context.Logger.LogLine("Empty SQS Event received");
            return new SQSBatchResponse();
        }

        foreach (var message in evnt.Records)
        {
            BatchItemFailure? result = await ProcessMessageAsync(message, context);
            if (result != null)
            {
                _batchItemFailures.Add(result);
            }
        }

        return new SQSBatchResponse(_batchItemFailures);
    }

    private async Task<BatchItemFailure?> ProcessMessageAsync(SQSEvent.SQSMessage message, ILambdaContext context)
    {
        try
        {
            context.Logger.LogInformation($"Processed message {message.Body}");
            // TODO: Do interesting work based on the new message
            await Task.CompletedTask; // Placeholder for actual async work
            return null;

        }
        catch (Exception e)
        {
            context.Logger.LogError($"An error occurred - {e.Message}");
            return new BatchItemFailure { ItemIdentifier = message.MessageId };
        }
    }
}