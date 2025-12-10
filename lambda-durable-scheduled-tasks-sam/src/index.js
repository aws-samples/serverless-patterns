const { withDurableExecution } = require('@aws/durable-execution-sdk-js');
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand, UpdateCommand } = require('@aws-sdk/lib-dynamodb');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const TABLE_NAME = process.env.TABLE_NAME;

/**
 * Multi-Day Scheduled Task Orchestration
 * 
 * This durable function demonstrates a 7-day workflow with scheduled checkpoints.
 * Use case: Daily data processing and report generation
 * 
 * Workflow:
 * - Day 1: Initialize and collect data
 * - Day 2-6: Process daily batches
 * - Day 7: Generate final report
 */
exports.handler = withDurableExecution(async (event, context) => {
  
  // Generate task ID from timestamp for deterministic IDs
  const taskId = event.taskId || `TASK-${Date.now()}`;
  const config = event.config || {
    reportType: 'weekly',
    dataSource: 'analytics'
  };
  
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
    
    // Day 1: Data Collection
    const day1Result = await context.step('day1-collect-data', async () => {
      console.log('Day 1: Collecting initial data...');
      
      // Simulate data collection
      const dataCollected = {
        records: Math.floor(Math.random() * 10000) + 5000,
        timestamp: new Date().toISOString()
      };
      
      await docClient.send(new UpdateCommand({
        TableName: TABLE_NAME,
        Key: { taskId },
        UpdateExpression: 'SET #status = :status, currentDay = :day, #progress = list_append(if_not_exists(#progress, :empty), :item)',
        ExpressionAttributeNames: {
          '#status': 'status',
          '#progress': 'progress'
        },
        ExpressionAttributeValues: {
          ':status': 'DAY_1_COMPLETE',
          ':day': 1,
          ':empty': [],
          ':item': [{
            day: 1,
            action: 'Data Collection',
            result: dataCollected,
            completedAt: new Date().toISOString()
          }]
        }
      }));
      
      return dataCollected;
    });
    
    // Wait 1 minute (Day 1 -> Day 2)
    // Change to { hours: 24 } for real 24-hour intervals
    console.log('Waiting 1 minute until Day 2...');
    await context.wait({ minutes: 1 });
    
    // Days 2-6: Daily Processing
    const dailyResults = [];
    for (let day = 2; day <= 6; day++) {
      const dayResult = await context.step(`day${day}-process-batch`, async () => {
        console.log(`Day ${day}: Processing daily batch...`);
        
        const batchResult = {
          day,
          recordsProcessed: Math.floor(Math.random() * 1000) + 500,
          timestamp: new Date().toISOString()
        };
        
        await docClient.send(new UpdateCommand({
          TableName: TABLE_NAME,
          Key: { taskId },
          UpdateExpression: 'SET #status = :status, currentDay = :day, #progress = list_append(#progress, :item)',
          ExpressionAttributeNames: {
            '#status': 'status',
            '#progress': 'progress'
          },
          ExpressionAttributeValues: {
            ':status': `DAY_${day}_COMPLETE`,
            ':day': day,
            ':item': [{
              day,
              action: 'Batch Processing',
              result: batchResult,
              completedAt: new Date().toISOString()
            }]
          }
        }));
        
        return batchResult;
      });
      
      dailyResults.push(dayResult);
      
      // Wait 1 minute before next day (except after Day 6)
      // Change to { hours: 24 } for real 24-hour intervals
      if (day < 6) {
        console.log(`Waiting 1 minute until Day ${day + 1}...`);
        await context.wait({ minutes: 1 });
      }
    }
    
    // Wait 1 minute (Day 6 -> Day 7)
    // Change to { hours: 24 } for real 24-hour intervals
    console.log('Waiting 1 minute until Day 7...');
    await context.wait({ minutes: 1 });
    
    // Day 7: Generate Final Report
    const finalReport = await context.step('day7-generate-report', async () => {
      console.log('Day 7: Generating final report...');
      
      const report = {
        taskId,
        status: 'Report completed',
        completedDays: 7,
        generatedAt: new Date().toISOString()
      };
      
      await docClient.send(new UpdateCommand({
        TableName: TABLE_NAME,
        Key: { taskId },
        UpdateExpression: 'SET #status = :status, currentDay = :day, finalReport = :report',
        ExpressionAttributeNames: {
          '#status': 'status'
        },
        ExpressionAttributeValues: {
          ':status': 'REPORT_GENERATED',
          ':day': 7,
          ':report': report
        }
      }));
      
      return report;
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
        report: finalReport
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
