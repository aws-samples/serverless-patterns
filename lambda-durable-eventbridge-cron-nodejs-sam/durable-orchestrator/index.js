// Main durable function that orchestrates two Lambda functions in sequence

import * as durableSDK from "@aws/durable-execution-sdk-js";
const {withDurableExecution, Duration } = durableSDK;

import { LambdaClient, InvokeCommand } from "@aws-sdk/client-lambda";
const lambdaClient = new LambdaClient({});

export const handler = withDurableExecution(
  async (event, context) => {
    
    const executionId = event.id || 'unknown';
    const triggerTime = event.time || new Date().toISOString();
    
    // Step 1: Invoke first Lambda function (data processing)
    const step1Result = await context.step("invoke-data-processor", async () => {
      console.log('DataProcessorStep...');
      
      const command = new InvokeCommand({
        FunctionName: "DataProcessorFunction",
        InvocationType: "RequestResponse",
        Payload: JSON.stringify({
          executionId,
          triggerTime,
          task: "process_data_5minutes"
        })
      });
      
      const response = await lambdaClient.send(command);
      const payload = JSON.parse(new TextDecoder().decode(response.Payload));
      
      return payload;
    });

    //Lambda will stop executing here and restart in 10 seconds
    await context.wait({seconds: 10});
    
    // Step 2: Invoke second Lambda function (notification service)
    const step2Result = await context.step("invoke-notification-service", async () => {
      
      console.log('NotificationServiceStep...');
      
      const command = new InvokeCommand({
        FunctionName: "NotificationServiceFunction",
        InvocationType: "RequestResponse",
        Payload: JSON.stringify({
          executionId,
          triggerTime,
          previousStepResult: step1Result,
          task: "send_completion_notification",
        })
      });
      
      const response = await lambdaClient.send(command);
      const payload = JSON.parse(new TextDecoder().decode(response.Payload));
    
      return payload;
    });
    
    console.log('DurableFunctionExecutionCompleted...');

    // Return final result
    return {
      status: 'completed',
      executionId,
      triggerTime,
      steps: {
        dataProcessor: step1Result,
        notificationService: step2Result
      },
      completedAt: new Date().toISOString()
    };
  
  }
);