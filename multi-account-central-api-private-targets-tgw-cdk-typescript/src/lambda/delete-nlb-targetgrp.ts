import {
  ElasticLoadBalancingV2Client,
  DescribeTargetGroupsCommandInput,
  DescribeTargetGroupsCommand,
  DeleteTargetGroupCommandInput,
  DeleteTargetGroupCommand,
  DescribeListenersCommandInput,
  DescribeListenersCommand,
  DeleteListenerCommandInput,
  DeleteListenerCommand,
} from '@aws-sdk/client-elastic-load-balancing-v2';
import { Protocol, TargetType } from 'aws-cdk-lib/aws-elasticloadbalancingv2';

// Define clients
const elbV2Client = new ElasticLoadBalancingV2Client({
  region: process.env.AWS_REGION,
});

interface CustomResourceInvokeEvent {
  nlbARN: string;
}

export const handler = async (event: CustomResourceInvokeEvent) => {
  try {
    console.log('Event:', JSON.stringify(event, null, 2));

    const { nlbARN } = event;

    // Get the list of Listeners for the NLB
    const listenerARNs = await GetListenersForNLB(nlbARN, elbV2Client);

    // Get the list of Target Groups for the NLB
    const targetGroupARNs = await GetTargetGroupsForNLB(nlbARN, elbV2Client);

    // Delete the Listeners for the NLB
    await DeleteListeners(listenerARNs, elbV2Client);

    // Delete the target groups
    await DeleteTargetGroups(targetGroupARNs, elbV2Client);

    return {
      statusCode: 200,
      body: JSON.stringify({
        status: 'SUCCESS',
        reason: 'Target groups deleted successfully',
      }),
    };
  } catch (error) {
    console.error('Error:', error);

    return {
      statusCode: 500,
      body: JSON.stringify({
        status: 'FAILED',
        reason:
          error instanceof Error ? error.message : 'Unknown error occurred',
      }),
    };
  }
};

// Function to get list of Target Groups for the NLB
async function GetTargetGroupsForNLB(
  nlbARN: string,
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<string[]> {
  try {
    // Create the DescribeListenersCommandInput
    const describeTGCommandInput: DescribeTargetGroupsCommandInput = {
      LoadBalancerArn: nlbARN,
    };

    const describeTGCommand = new DescribeTargetGroupsCommand(
      describeTGCommandInput
    );
    const response = await elbV2Client.send(describeTGCommand);

    // Extract the TargetGroupARNs
    const targetGroupARNs: string[] =
      response.TargetGroups?.map(
        (targetGroup) => targetGroup.TargetGroupArn || ''
      ) ?? [];

    return targetGroupARNs;
  } catch (error) {
    console.error('Error getting target groups for NLB:', error);
    throw error;
  }
}

// Function to delete given list of target groups
async function DeleteTargetGroups(
  targetGroupARNs: string[],
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<void> {
  try {
    for (const targetGroupARN of targetGroupARNs) {
      // Create the DeleteTargetGroupCommandInput
      const deleteTargetGroupCommandInput: DeleteTargetGroupCommandInput = {
        TargetGroupArn: targetGroupARN,
      };

      const deleteTargetGroupCommand = new DeleteTargetGroupCommand(
        deleteTargetGroupCommandInput
      );
      await elbV2Client.send(deleteTargetGroupCommand);
    }
  } catch (error) {
    console.error('Error deleting target group:', error);
    throw error;
  }
}

// Function to get the list of listeners for the NLB
async function GetListenersForNLB(
  nlbARN: string,
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<string[]> {
  try {
    // Create the DescribeListenersCommandInput
    const describeListenersCommandInput: DescribeListenersCommandInput = {
      LoadBalancerArn: nlbARN,
    };

    const describeListenersCommand = new DescribeListenersCommand(
      describeListenersCommandInput
    );
    const response = await elbV2Client.send(describeListenersCommand);

    // Extract the ListenerARNs
    const listenerARNs: string[] =
      response.Listeners?.map(
        (listener) => listener.ListenerArn || ''
      ) ?? [];

    return listenerARNs;
  } catch (error) {
    console.error('Error getting listeners for NLB:', error);
    throw error;
  }
}

// Function to delete list of listeners for NLB
async function DeleteListeners(
  listenerARNs: string[],
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<void> {
  try {
    for (const listenerARN of listenerARNs) {
      // Create the DeleteListenerCommandInput
      const deleteListenerCommandInput: DeleteListenerCommandInput = {
        ListenerArn: listenerARN,
      };

      const deleteListenerCommand = new DeleteListenerCommand(
        deleteListenerCommandInput
      );
      await elbV2Client.send(deleteListenerCommand);
    }
  } catch (error) {
    console.error('Error deleting listener:', error);
    throw error;
  }
}
