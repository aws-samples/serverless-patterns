const { ECSClient, RunTaskCommand } = require('@aws-sdk/client-ecs');
const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

const ecs = new ECSClient({ region: process.env.AWS_REGION });

/**
 * Lambda durable function - Callback Pattern
 * 
 * This function demonstrates the callback pattern where:
 * 1. Lambda creates a callback and gets a callback ID
 * 2. Lambda starts an ECS task and passes the callback ID
 * 3. Lambda waits for the callback (suspends without charges)
 * 4. ECS task calls Lambda APIs directly to send success/failure
 * 5. Lambda resumes and returns the result
 */
exports.handler = withDurableExecution(async (event, context) => {
  context.logger.info('Starting Lambda durable function - Callback Pattern');
  context.logger.info('Event:', JSON.stringify(event));

  const message = event.message || 'Hello from Lambda durable function';
  const processingTime = event.processingTime || 10;

  try {
    // Use waitForCallback to create callback and start ECS task
    const result = await context.waitForCallback(
      'ecs-task-callback',
      async (callbackId) => {
        context.logger.info('Callback ID created:', callbackId);
        context.logger.info('Starting ECS task with callback ID...');
        
        // Start ECS task with callback ID as environment variable
        const runTaskParams = {
          cluster: process.env.ECS_CLUSTER,
          taskDefinition: process.env.ECS_TASK_DEFINITION,
          launchType: 'FARGATE',
          networkConfiguration: {
            awsvpcConfiguration: {
              subnets: process.env.ECS_SUBNETS.split(','),
              securityGroups: [process.env.ECS_SECURITY_GROUP],
              assignPublicIp: 'ENABLED'
            }
          },
          overrides: {
            containerOverrides: [
              {
                name: 'worker',
                environment: [
                  { name: 'CALLBACK_ID', value: callbackId },
                  { name: 'MESSAGE', value: message },
                  { name: 'PROCESSING_TIME', value: processingTime.toString() }
                ]
              }
            ]
          }
        };

        const response = await ecs.send(new RunTaskCommand(runTaskParams));
        
        if (!response.tasks || response.tasks.length === 0) {
          throw new Error('Failed to start ECS task');
        }

        const taskArn = response.tasks[0].taskArn;
        context.logger.info('ECS task started:', taskArn);
      },
      {
        timeout: { hours: 1 },  // Wait up to 1 hour for callback
        heartbeatTimeout: { minutes: 5 }  // Expect heartbeat every 5 minutes
      }
    );

    context.logger.info('Callback received with result:', result);

    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'ECS task completed successfully',
        result: result,
        pattern: 'callback'
      })
    };

  } catch (error) {
    context.logger.error('Error in durable function:', error);
    
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'ECS task failed',
        error: error.message,
        pattern: 'callback'
      })
    };
  }
});
