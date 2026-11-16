// First Lambda function in the sequence
export const handler = async (event) => {
  console.log('Data Processor invoked with:', JSON.stringify(event, null, 2));
  
  const { executionId, triggerTime, task } = event;
  
  // Simulate data processing
  const processedRecords = Math.floor(Math.random() * 1000) + 500;
  
  await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate processing time
  
  const result = {
    functionName: 'DataProcessorFunction',
    executionId,
    triggerTime,
    task,
    recordsProcessed: processedRecords,
    status: 'success',
    processedAt: new Date().toISOString()
  };
  
  console.log('Data processing completed:', result);
  return result;
};

