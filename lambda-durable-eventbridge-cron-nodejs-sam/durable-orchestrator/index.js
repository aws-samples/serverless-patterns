// Main durable function that orchestrates two Lambda functions in sequence

import { withDurableExecution } from "@aws/durable-execution-sdk-js";

export const handler = withDurableExecution(
  async (event, context) => {
    
    const executionId = event.id || 'unknown';
    const triggerTime = event.time || new Date().toISOString();
    
    // Step 1: Invoke first Lambda function (data processing)
    const step1Result = await context.invoke("DataProcessorFunction", {
      executionId,
      triggerTime,
      task: "process_data_5minutes"
    });
    console.log(`[${executionId}] DataProcessorStep completed`);

    //Lambda will stop executing here and restart in 10 seconds
    await context.wait({seconds: 10});
    
    // Step 2: Invoke second Lambda function (notification service)
    const step2Result = await context.invoke("NotificationServiceFunction", {
      executionId,
      triggerTime,
      previousStepResult: step1Result,
      task: "send_completion_notification",
    });
    console.log(`[${executionId}] NotificationServiceStep completed`);
    
    console.log(`[${executionId}] DurableFunctionExecutionCompleted`);

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
