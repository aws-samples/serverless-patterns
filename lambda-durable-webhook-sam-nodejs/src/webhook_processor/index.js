import { withDurableExecution } from "@aws/durable-execution-sdk-js";
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import { randomUUID } from 'crypto';

// Initialize AWS clients
const dynamodbClient = new DynamoDBClient({});
const dynamodb = DynamoDBDocumentClient.from(dynamodbClient);

export const handler = withDurableExecution(
    async (event, context) => {
        /**
         * Webhook processor durable function with 3 checkpointed steps:
         * 1. Validate webhook
         * 2. Process business logic  
         * 3. Finalize processing
         */
        
        // Extract configuration from environment
        const eventsTableName = process.env.EVENTS_TABLE_NAME;
        const environment = process.env.ENVIRONMENT || 'dev';
        
        // Parse the incoming webhook event
        const webhookPayload = JSON.parse(event.body || '{}');
        
        // Use executionToken from API Gateway or generate new one
        const executionToken = event.executionToken || randomUUID();
        
        console.log(`Processing webhook with execution token: ${executionToken}`);
        console.log(`Webhook payload:`, JSON.stringify(webhookPayload, null, 2));
        
        try {
            // Store initial execution state
            await dynamodb.send(new PutCommand({
                TableName: eventsTableName,
                Item: {
                    executionToken: executionToken,
                    status: 'STARTED',
                    timestamp: Date.now(),
                    payload: webhookPayload,
                    ttl: Math.floor(Date.now() / 1000) + (7 * 24 * 60 * 60) // 7 days TTL
                }
            }));

            // Step 1: Validate webhook (checkpointed)
            const validationResult = await context.step(async (stepContext) => {
                stepContext.logger.info(`Validating webhook ${executionToken}`);
                
                // Update status to VALIDATING
                await dynamodb.send(new UpdateCommand({
                    TableName: eventsTableName,
                    Key: { executionToken },
                    UpdateExpression: 'SET #status = :status, #step = :step',
                    ExpressionAttributeNames: {
                        '#status': 'status',
                        '#step': 'currentStep'
                    },
                    ExpressionAttributeValues: {
                        ':status': 'VALIDATING',
                        ':step': 'validate'
                    }
                }));

                // Call the separate webhook validator function
                const { LambdaClient, InvokeCommand } = await import('@aws-sdk/client-lambda');
                const lambdaClient = new LambdaClient({});
                
                const validatorFunctionArn = process.env.WEBHOOK_VALIDATOR_FUNCTION_ARN;
                const invokeResponse = await lambdaClient.send(new InvokeCommand({
                    FunctionName: validatorFunctionArn,
                    Payload: JSON.stringify({
                        payload: webhookPayload,
                        executionToken: executionToken
                    })
                }));
                
                const validatorResult = JSON.parse(new TextDecoder().decode(invokeResponse.Payload));
                
                if (!validatorResult.isValid) {
                    await dynamodb.send(new UpdateCommand({
                        TableName: eventsTableName,
                        Key: { executionToken },
                        UpdateExpression: 'SET #status = :status, #error = :error',
                        ExpressionAttributeNames: {
                            '#status': 'status',
                            '#error': 'error'
                        },
                        ExpressionAttributeValues: {
                            ':status': 'FAILED',
                            ':error': 'Validation failed: ' + validatorResult.errors.join(', ')
                        }
                    }));
                    
                    return {
                        executionToken: executionToken,
                        status: "failed",
                        error: `Validation failed: ${validatorResult.errors.join(', ')}`
                    };
                }
                
                return {
                    executionToken: executionToken,
                    status: "validated",
                    payloadType: validatorResult.payloadType,
                    validatedAt: validatorResult.validatedAt
                };
            });

            // Check if validation failed
            if (validationResult.status === "failed") {
                return {
                    statusCode: 400,
                    body: JSON.stringify({
                        executionToken: executionToken,
                        status: 'FAILED',
                        error: validationResult.error
                    })
                };
            }

            // Step 2: Process business logic (checkpointed)
            const processingResult = await context.step(async (stepContext) => {
                stepContext.logger.info(`Processing webhook ${executionToken}`);
                
                // Update status to PROCESSING
                await dynamodb.send(new UpdateCommand({
                    TableName: eventsTableName,
                    Key: { executionToken },
                    UpdateExpression: 'SET #status = :status, #step = :step',
                    ExpressionAttributeNames: {
                        '#status': 'status',
                        '#step': 'currentStep'
                    },
                    ExpressionAttributeValues: {
                        ':status': 'PROCESSING',
                        ':step': 'process'
                    }
                }));

                // Simulate business processing logic - customize this based on your needs
                return {
                    executionToken: executionToken,
                    status: "processed",
                    originalPayload: webhookPayload,
                    businessResult: `Processed webhook of type: ${webhookPayload.type || 'unknown'}`,
                    dataTransformed: webhookPayload.data ? JSON.stringify(webhookPayload.data).toUpperCase() : null,
                    processedAt: new Date().toISOString(),
                    metadata: {
                        processedBy: 'webhook-processor-nodejs',
                        version: '1.0.0'
                    }
                };
            });

            // Step 3: Finalize processing (checkpointed)
            const finalResult = await context.step(async (stepContext) => {
                stepContext.logger.info(`Finalizing webhook ${executionToken}`);
                
                // Update final status to COMPLETED
                await dynamodb.send(new UpdateCommand({
                    TableName: eventsTableName,
                    Key: { executionToken },
                    UpdateExpression: 'SET #status = :status, #step = :step, #result = :result, #completedAt = :completedAt',
                    ExpressionAttributeNames: {
                        '#status': 'status',
                        '#step': 'currentStep',
                        '#result': 'result',
                        '#completedAt': 'completedAt'
                    },
                    ExpressionAttributeValues: {
                        ':status': 'COMPLETED',
                        ':step': 'finalize',
                        ':result': processingResult,
                        ':completedAt': new Date().toISOString()
                    }
                }));

                return {
                    executionToken: executionToken,
                    status: "completed",
                    finalResult: processingResult
                };
            });

            // Return final response
            return {
                statusCode: 202,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: 'Webhook processing completed successfully',
                    executionToken: executionToken,
                    status: 'COMPLETED',
                    result: finalResult
                })
            };

        } catch (error) {
            console.error(`Error processing webhook ${executionToken}:`, error.message);
            
            // Update error state
            await dynamodb.send(new UpdateCommand({
                TableName: eventsTableName,
                Key: { executionToken },
                UpdateExpression: 'SET #status = :status, #error = :error',
                ExpressionAttributeNames: {
                    '#status': 'status',
                    '#error': 'error'
                },
                ExpressionAttributeValues: {
                    ':status': 'FAILED',
                    ':error': error.message
                }
            }));

            return {
                statusCode: 500,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: 'Webhook processing failed',
                    executionToken: executionToken,
                    error: error.message
                })
            };
        }
    }
);
