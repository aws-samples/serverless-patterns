const { withDurableExecution } = require('@aws/durable-execution-sdk-js');
const { ECSClient, RunTaskCommand, DescribeTasksCommand } = require('@aws-sdk/client-ecs');

const ecs = new ECSClient({});

exports.handler = withDurableExecution(async (event, context) => {
  console.log('Starting Lambda Durable Function - Polling Pattern');
  console.log('Event:', JSON.stringify(event));

  const { message = 'Default message', processingTime = 10 } = event;

  // Step 1: Start ECS task (checkpointed)
  const taskInfo = await context.step('start-ecs-task', async () => {
    const params = {
      cluster: process.env.ECS_CLUSTER,
      taskDefinition: process.env.ECS_TASK_DEFINITION,
      launchType: 'FARGATE',
      networkConfiguration: {
        awsvpcConfiguration: {
          subnets: [process.env.ECS_SUBNET_1, process.env.ECS_SUBNET_2],
          assignPublicIp: 'ENABLED'
        }
      },
      overrides: {
        containerOverrides: [{
          name: 'worker',
          environment: [
            { name: 'MESSAGE', value: message },
            { name: 'PROCESSING_TIME', value: String(processingTime) }
          ]
        }]
      }
    };

    console.log('Starting ECS task...');
    const response = await ecs.send(new RunTaskCommand(params));
    const taskArn = response.tasks[0].taskArn;
    console.log('ECS task started:', taskArn);
    return { taskArn, cluster: process.env.ECS_CLUSTER };
  });

  console.log('Task started:', taskInfo.taskArn);

  // Step 2: Poll until complete (checkpointed)
  const result = await context.step('poll-until-complete', async () => {
    let attempts = 0;
    const maxAttempts = 60;
    
    while (attempts < maxAttempts) {
      await new Promise(r => setTimeout(r, 5000));
      
      const response = await ecs.send(new DescribeTasksCommand({
        cluster: taskInfo.cluster,
        tasks: [taskInfo.taskArn]
      }));
      
      const task = response.tasks[0];
      console.log(`Poll attempt ${attempts + 1}: Status = ${task.lastStatus}`);
      
      if (task.lastStatus === 'STOPPED') {
        const exitCode = task.containers[0].exitCode;
        console.log(`Task stopped with exit code: ${exitCode}`);
        
        if (exitCode === 0) {
          return { success: true, message: 'Task completed successfully', taskArn: taskInfo.taskArn };
        } else {
          throw new Error(`Task failed with exit code: ${exitCode}`);
        }
      }
      
      attempts++;
    }
    
    throw new Error('Polling timeout - task did not complete');
  });

  console.log('Workflow completed:', JSON.stringify(result));
  return result;
});
