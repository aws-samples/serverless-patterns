import { SFNClient, StartExecutionCommand } from '@aws-sdk/client-sfn';

const sfnClient = new SFNClient();
const STATE_MACHINE_ARN = process.env.STATE_MACHINE_ARN;

export const handler = async (event) => {
  const { prompt, agentRuntimeArns } = event;

  const result = await sfnClient.send(new StartExecutionCommand({
    stateMachineArn: STATE_MACHINE_ARN,
    input: JSON.stringify({ prompt, agentRuntimeArns }),
  }));

  return {
    statusCode: 200,
    body: JSON.stringify({ executionArn: result.executionArn }),
  };
};
