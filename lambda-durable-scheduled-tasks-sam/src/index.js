const { withDurableExecution } = require('@aws/durable-execution-sdk-js');
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand, UpdateCommand } = require('@aws-sdk/lib-dynamodb');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const TABLE_NAME = process.env.TABLE_NAME;

/**
 * Multi-Day Scheduled Task Orchestration
 * 
 * This durable function demonstrates a multi-day workflow with scheduled waits
 * and automatic checkpointing using AWS Lambda durable functions.
 */
exports.handler = withDurableExecution(async (event, context) => {
  
  // Generate task ID from timestamp for deterministic IDs
  const taskId = event.taskId || `TASK-${Date.now()}`;
  const config = event.config || {};
  
  console.log(`Starting scheduled task orchestration: ${taskId}`);
  
  try {
    // Initialize task state
    await context.step('initialize-task', async () => {
      await docClient.send(new PutCommand({
        TableName: TABLE_NAME,
        Item: {
          taskId,
          status: 'INITIALIZED',
          config,
          startTime: new Date().toISOString(),
          currentDay: 0,
          progress: []
        }
      }));
      return { taskId, initialized: true };
    });
    
    // Step 1: Initial processing
    await context.step('step1-process', async () => {
      console.log('Step 1: Processing...');
      
      await docClient.send(new UpdateCommand({
        TableName: TABLE_NAME,
        Key: { taskId },
        UpdateExpression: 'SET #status = :status, currentDay = :day',
        ExpressionAttributeNames: {
          '#status': 'status'
        },
        ExpressionAttributeValues: {
          ':status': 'STEP_1_COMPLETE',
          ':day': 1
        }
      }));
      
      return { step: 1, completed: true };
    });
    
    // Wait 1 minute (change to { hours: 24 } for real 24-hour intervals)
    console.log('Waiting 1 minute until next step...');
    await context.wait({ minutes: 1 });
    
    // Steps 2-6: Intermediate processing with waits
    for (let step = 2; step <= 6; step++) {
      await context.step(`step${step}-process`, async () => {
        console.log(`Step ${step}: Processing...`);
        
        await docClient.send(new UpdateCommand({
          TableName: TABLE_NAME,
          Key: { taskId },
          UpdateExpression: 'SET #status = :status, currentDay = :day',
          ExpressionAttributeNames: {
            '#status': 'status'
          },
          ExpressionAttributeValues: {
            ':status': `STEP_${step}_COMPLETE`,
            ':day': step
          }
        }));
        
        return { step, completed: true };
      });
      
      // Wait between steps (except after last step)
      if (step < 6) {
        console.log(`Waiting 1 minute until step ${step + 1}...`);
        await context.wait({ minutes: 1 });
      }
    }
    
    // Wait before final step
    console.log('Waiting 1 minute until final step...');
    await context.wait({ minutes: 1 });
    
    // Final step: Complete workflow
    const finalResult = await context.step('final-step', async () => {
      console.log('Final step: Completing workflow...');
      
      await docClient.send(new UpdateCommand({
        TableName: TABLE_NAME,
        Key: { taskId },
        UpdateExpression: 'SET #status = :status, currentDay = :day',
        ExpressionAttributeNames: {
          '#status': 'status'
        },
        ExpressionAttributeValues: {
          ':status': 'FINAL_STEP_COMPLETE',
          ':day': 7
        }
      }));
      
      return { step: 7, completed: true };
    });
    
    // Complete task
    await context.step('complete-task', async () => {
      console.log('Completing task...');
      
      await docClient.send(new UpdateCommand({
        TableName: TABLE_NAME,
        Key: { taskId },
        UpdateExpression: 'SET #status = :status, completedAt = :completedAt',
        ExpressionAttributeNames: {
          '#status': 'status'
        },
        ExpressionAttributeValues: {
          ':status': 'COMPLETED',
          ':completedAt': new Date().toISOString()
        }
      }));
      
      return { completed: true };
    });
    
    console.log(`Task ${taskId} completed successfully`);
    
    return {
      statusCode: 200,
      body: JSON.stringify({
        taskId,
        status: 'COMPLETED',
        result: finalResult
      })
    };
    
  } catch (error) {
    console.error('Error in scheduled task orchestration:', error);
    
    // Update status to failed
    await docClient.send(new UpdateCommand({
      TableName: TABLE_NAME,
      Key: { taskId },
      UpdateExpression: 'SET #status = :status, error = :error',
      ExpressionAttributeNames: {
        '#status': 'status'
      },
      ExpressionAttributeValues: {
        ':status': 'FAILED',
        ':error': error.message
      }
    }));
    
    throw error;
  }
});
