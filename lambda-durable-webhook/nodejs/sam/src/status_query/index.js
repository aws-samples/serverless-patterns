const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

// Initialize AWS clients
const dynamodbClient = new DynamoDBClient({});
const dynamodb = DynamoDBDocumentClient.from(dynamodbClient);

/**
 * Status query function for webhook processing
 * Allows real-time status tracking via REST API
 */
exports.handler = async (event, context) => {
    const executionToken = event.pathParameters?.executionToken;
    const eventsTableName = process.env.EVENTS_TABLE_NAME;
    
    console.log(`Querying status for execution token: ${executionToken}`);
    
    if (!executionToken) {
        return {
            statusCode: 400,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                error: 'Missing executionToken parameter'
            })
        };
    }
    
    try {
        // Query execution state from DynamoDB
        const result = await dynamodb.send(new GetCommand({
            TableName: eventsTableName,
            Key: { executionToken }
        }));
        
        if (!result.Item) {
            return {
                statusCode: 404,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({
                    error: 'Execution token not found',
                    executionToken: executionToken
                })
            };
        }
        
        // Format response based on current status
        const execution = result.Item;
        const response = {
            executionToken: executionToken,
            status: execution.status,
            timestamp: execution.timestamp,
            currentStep: execution.currentStep || 'unknown'
        };
        
        // Add additional fields based on status
        if (execution.status === 'COMPLETED') {
            response.result = execution.result;
            response.completedAt = execution.completedAt;
        }
        
        if (execution.status === 'FAILED') {
            response.error = execution.error;
        }
        
        if (execution.payload) {
            response.originalPayload = execution.payload;
        }
        
        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(response)
        };
        
    } catch (error) {
        console.error(`Error querying status for ${executionToken}:`, error.message);
        
        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                error: 'Failed to query execution status',
                executionToken: executionToken,
                message: error.message
            })
        };
    }
};
