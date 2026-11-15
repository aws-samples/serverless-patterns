const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand, ScanCommand, BatchWriteCommand } = require('@aws-sdk/lib-dynamodb');

const dynamoClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(dynamoClient);
const TABLE_NAME = process.env.TABLE_NAME;

/**
 * Unified task management function
 * Handles: GET single task, GET all tasks, DELETE all tasks
 */
exports.handler = async (event) => {
  console.log('Task management event:', JSON.stringify(event));
  
  const httpMethod = event.httpMethod || event.requestContext?.http?.method;
  const taskId = event.pathParameters?.taskId || event.taskId;
  
  // Route based on HTTP method and path
  try {
    // DELETE /tasks - Delete all tasks
    if (httpMethod === 'DELETE' && !taskId) {
      return await deleteAllTasks();
    }
    
    // GET /tasks - List all tasks
    if (httpMethod === 'GET' && !taskId) {
      return await listAllTasks();
    }
    
    // GET /tasks/{taskId} - Get single task status
    if (httpMethod === 'GET' && taskId) {
      return await getTaskStatus(taskId);
    }
    
    // Invalid request
    return {
      statusCode: 400,
      headers: getCorsHeaders(),
      body: JSON.stringify({ error: 'Invalid request' })
    };
    
  } catch (error) {
    console.error('Error in task management:', error);
    return {
      statusCode: 500,
      headers: getCorsHeaders(),
      body: JSON.stringify({ error: 'Internal server error: ' + error.message })
    };
  }
};

function getCorsHeaders() {
  return {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
    'Access-Control-Allow-Methods': 'GET,DELETE,OPTIONS'
  };
}

async function getTaskStatus(taskId) {
  try {
    const result = await docClient.send(new GetCommand({
      TableName: TABLE_NAME,
      Key: { taskId }
    }));
    
    if (!result.Item) {
      return {
        statusCode: 404,
        headers: getCorsHeaders(),
        body: JSON.stringify({ error: 'Task not found' })
      };
    }
    
    const task = result.Item;
    const totalDays = 7;
    const currentDay = task.currentDay || 0;
    const progressPercentage = Math.round((currentDay / totalDays) * 100);
    
    return {
      statusCode: 200,
      headers: getCorsHeaders(),
      body: JSON.stringify({
        taskId: task.taskId,
        status: task.status,
        currentDay: task.currentDay,
        progress: {
          percentage: progressPercentage,
          completedDays: currentDay,
          totalDays: totalDays,
          steps: task.progress || []
        },
        config: task.config,
        startTime: task.startTime,
        completedAt: task.completedAt,
        finalReport: task.finalReport,
        error: task.error
      })
    };
  } catch (error) {
    console.error('Error fetching task status:', error);
    throw error;
  }
}

async function listAllTasks() {
  try {
    const result = await docClient.send(new ScanCommand({
      TableName: TABLE_NAME,
      Limit: 100
    }));
    
    const tasks = result.Items || [];
    
    // Transform tasks with progress percentage
    const transformedTasks = tasks.map(task => {
      const totalDays = 7;
      const currentDay = task.currentDay || 0;
      const progressPercentage = Math.round((currentDay / totalDays) * 100);
      
      return {
        taskId: task.taskId,
        status: task.status,
        currentDay: task.currentDay,
        progress: {
          percentage: progressPercentage,
          completedDays: currentDay,
          totalDays: totalDays,
          steps: task.progress || []
        },
        config: task.config,
        startTime: task.startTime,
        completedAt: task.completedAt,
        finalReport: task.finalReport
      };
    });
    
    // Sort by startTime descending (newest first)
    transformedTasks.sort((a, b) => {
      const timeA = new Date(a.startTime || 0).getTime();
      const timeB = new Date(b.startTime || 0).getTime();
      return timeB - timeA;
    });
    
    return {
      statusCode: 200,
      headers: getCorsHeaders(),
      body: JSON.stringify({
        tasks: transformedTasks,
        count: transformedTasks.length
      })
    };
  } catch (error) {
    console.error('Error listing tasks:', error);
    throw error;
  }
}

async function deleteAllTasks() {
  try {
    // Scan all items
    const scanResult = await docClient.send(new ScanCommand({
      TableName: TABLE_NAME
    }));
    
    const items = scanResult.Items || [];
    
    if (items.length === 0) {
      return {
        statusCode: 200,
        headers: getCorsHeaders(),
        body: JSON.stringify({
          message: 'No tasks to delete',
          deletedCount: 0
        })
      };
    }
    
    // DynamoDB BatchWrite can handle max 25 items at a time
    const batchSize = 25;
    let deletedCount = 0;
    
    for (let i = 0; i < items.length; i += batchSize) {
      const batch = items.slice(i, i + batchSize);
      
      const deleteRequests = batch.map(item => ({
        DeleteRequest: {
          Key: { taskId: item.taskId }
        }
      }));
      
      await docClient.send(new BatchWriteCommand({
        RequestItems: {
          [TABLE_NAME]: deleteRequests
        }
      }));
      
      deletedCount += batch.length;
      console.log(`Deleted ${deletedCount} of ${items.length} tasks`);
    }
    
    return {
      statusCode: 200,
      headers: getCorsHeaders(),
      body: JSON.stringify({
        message: 'All tasks deleted successfully',
        deletedCount
      })
    };
  } catch (error) {
    console.error('Error deleting tasks:', error);
    throw error;
  }
};
