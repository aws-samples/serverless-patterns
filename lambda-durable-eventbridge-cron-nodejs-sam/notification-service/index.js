
// Second Lambda function in the sequence
export const handler = async (event) => {
  console.log('Notification Service invoked with:', JSON.stringify(event, null, 2));
  
  const { executionId, triggerTime, previousStepResult, task } = event;
  
  // Simulate sending notifications
  const notificationsSent = Math.floor(Math.random() * 10) + 1;
  
  await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate notification time
  
  const result = {
    functionName: 'NotificationServiceFunction',
    executionId,
    triggerTime,
    task,
    notificationsSent,
    recipientCount: notificationsSent,
    previousStepSummary: {
      recordsProcessed: previousStepResult.recordsProcessed
    },
    status: 'success',
    notifiedAt: new Date().toISOString()
  };
  
  console.log('Notifications sent:', result);
  return result;
};

