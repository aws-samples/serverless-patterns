import { withDurableExecution } from "@aws/durable-execution-sdk-js";
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';
import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';
import { randomUUID } from 'crypto';

// Initialize AWS clients at module scope for connection reuse
const dynamodbClient = new DynamoDBClient({});
const dynamodb = DynamoDBDocumentClient.from(dynamodbClient);
const lambdaClient = new LambdaClient({});

export const handler = withDurableExecution(
    async (event, context) => {
        /**
         * Webhook processor durable function with 3 checkpointed steps:
         * 1. Validate webhook
         * 2. Process business logic  
         * 3. Finalize processing
         * 
         * Design Note: Each step writes a status update to DynamoDB before doing its main work.
         * DynamoDB UpdateCommand is naturally idempotent for these status writes.
         * The DynamoDB status reflects the last successfully written status, not necessarily
         * the current replay position.
         */
        
        // Extract configuration from environment
        const eventsTableName = process.env.EVENTS_TABLE_NAME;
        const environment = process.env.ENVIRONMENT || 'dev';
        
        // Parse the incoming webhook event
        const webhookPayload = JSON.parse(event.body || '{}');
        
        // Step 0: Initialize execution (checkpointed) - handles non-deterministic operations
        const initResult = await context.step('initialize-execution', async (stepContext) => {
            // Generate executionToken inside step to ensure determinism on replay
            const token = event.executionToken || randomUUID();
            const startTimestamp = Date.now();
            
            stepContext.logger.info(`Initializing webhook processing with token: ${token}`);
            stepContext.logger.info(`Webhook payload: ${JSON.stringify(webhookPayload)}`);
            
            // Store initial execution state
            await dynamodb.send(new PutCommand({
                TableName: eventsTableName,
                Item: {
                    executionToken: token,
                    status: 'STARTED',
                    timestamp: startTimestamp,
                    payload: webhookPayload,
                    ttl: Math.floor(startTimestamp / 1000) + (7 * 24 * 60 * 60) // 7 days TTL
                }
            }));
            
            return {
                executionToken: token,
                startTimestamp: startTimestamp
            };
        });
        
        const executionToken = initResult.executionToken;

        try {
            // Step 1: Validate webhook (checkpointed)
            const validationResult = await context.step('validate-webhook', async (stepContext) => {
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
                const validatorFunctionArn = process.env.WEBHOOK_VALIDATOR_FUNCTION_ARN;
                const invokeResponse = await lambdaClient.send(new InvokeCommand({
                    FunctionName: validatorFunctionArn,
                    InvocationType: 'RequestResponse',
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
            const processingResult = await context.step('process-webhook', async (stepContext) => {
                stepContext.logger.info(`Processing webhook ${executionToken}`);
                
                // Generate timestamp once at start of step for consistency
                const processedAt = new Date().toISOString();
                
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
                // Keep state minimal - store IDs and references, not full objects
                return {
                    executionToken,
                    status: "processed",
                    payloadType: webhookPayload.type || 'unknown',
                    processedAt: processedAt
                };
            });

            // Step 3: Finalize processing (checkpointed)
            const finalResult = await context.step('finalize-webhook', async (stepContext) => {
                stepContext.logger.info(`Finalizing webhook ${executionToken}`);
                
                // Generate timestamp once at start of step for consistency
                const completedAt = new Date().toISOString();
                
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
                        ':completedAt': completedAt
                    }
                }));

                return {
                    executionToken: executionToken,
                    status: "completed",
                    completedAt: completedAt
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
            // Wrap error handling in a step to ensure proper checkpoint behavior
            const errorResult = await context.step('handle-error', async (stepContext) => {
                stepContext.logger.error(`Error processing webhook ${executionToken}: ${error.message}`);
                
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
                    status: 'FAILED',
                    error: error.message
                };
            });

            return {
                statusCode: 500,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: 'Webhook processing failed',
                    executionToken: executionToken,
                    ...errorResult
                })
            };
        }
    }
);