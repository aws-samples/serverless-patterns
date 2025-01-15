import {
  ElasticLoadBalancingV2Client,
  CreateTargetGroupCommand,
  CreateTargetGroupCommandInput,
  RegisterTargetsCommand,
  RegisterTargetsCommandInput,
  TargetDescription,
  CreateListenerCommandInput,
  CreateListenerCommand,
} from '@aws-sdk/client-elastic-load-balancing-v2';
import {
  GetParameterCommand,
  GetParameterCommandInput,
  SSMClient,
} from '@aws-sdk/client-ssm';
import { TagResourcesCommand, ResourceGroupsTaggingAPIClient } from '@aws-sdk/client-resource-groups-tagging-api';
import { Protocol, TargetType } from 'aws-cdk-lib/aws-elasticloadbalancingv2';

// Define clients
const elbV2Client = new ElasticLoadBalancingV2Client({
  region: process.env.AWS_REGION,
});
const ssmClient = new SSMClient({ region: process.env.AWS_REGION });
const taggingClient = new ResourceGroupsTaggingAPIClient({
  region: process.env.AWS_REGION,
});

interface CustomResourceInvokeEvent {
  tgName: string;
  listenerPort: number;
  targetPort: number;
  protocol: Protocol;
  targetType: TargetType;
  vpcId: string;
  ssmARN: string;
  nlbARN: string;
  tags: { [key: string]: string };
}

export const handler = async (event: CustomResourceInvokeEvent) => {
  try {
    console.log('Event:', JSON.stringify(event, null, 2));

    const {
      tgName,
      listenerPort,
      targetPort,
      protocol,
      targetType,
      vpcId,
      ssmARN,
      nlbARN,
      tags
    } = event;

    // Get the NLB ENI IP/AZ pairs from SSM
    const nlbENIsString: string = await GetParameterFromSSM(ssmARN, ssmClient);
    console.log('nlbENIsString:', nlbENIsString);

    if (!nlbENIsString) {
      throw new Error(
        'No ENI IP/AZ pairs found for the provided load balancer'
      );
    }

    // Create the targets
    const targets = CreateTargets(nlbENIsString, targetPort);

    // Create the Target Group
    const targetGroupARN = await CreateTargetGroup(
      tgName,
      targetPort,
      protocol,
      targetType,
      vpcId,
      elbV2Client
    );

    if (!targetGroupARN) {
      throw new Error('Target group ARN is undefined');
    }

    // Register the targets to the Target Group
    await RegisterTargets(targetGroupARN, targets, elbV2Client);

    // Create the listener with the target group
    await CreateListener(
      nlbARN,
      targetGroupARN,
      listenerPort,
      protocol,
      elbV2Client
    );

    // Tag the target group
    await TagTargetGroup(targetGroupARN, tags, taggingClient);

    return {
      statusCode: 200,
      body: JSON.stringify({
        status: 'SUCCESS',
        reason: 'Listener and Target group created successfully',
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

// Function to create the target group
async function CreateTargetGroup(
  tgName: string,
  port: number,
  protocol: Protocol,
  targetType: TargetType,
  vpcId: string,
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<string> {
  try {
    // Create the TargetGroupInput
    const createTargetGroupCommandInput: CreateTargetGroupCommandInput = {
      Name: `${tgName}-${Date.now()}`,
      Port: port,
      Protocol: protocol,
      VpcId: vpcId,
      TargetType: targetType,
    };

    const targetGroupCommand = new CreateTargetGroupCommand(
      createTargetGroupCommandInput
    );
    const response = await elbV2Client.send(targetGroupCommand);

    return response.TargetGroups
      ? response.TargetGroups[0].TargetGroupArn || ''
      : '';
  } catch (error) {
    console.error('Error creating target group:', error);
    throw error;
  }
}

async function RegisterTargets(
  targetGroupARN: string,
  targets: TargetDescription[],
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<void> {
  try {
    // Create the RegisterTargetsCommandInput
    const createRegisterTargetsCommandInput: RegisterTargetsCommandInput = {
      TargetGroupArn: targetGroupARN,
      Targets: targets,
    };

    const registerTargetsCommand = new RegisterTargetsCommand(
      createRegisterTargetsCommandInput
    );

    await elbV2Client.send(registerTargetsCommand);
  } catch (error) {
    console.error('Error registering targets:', error);
    throw error;
  }
}

function CreateTargets(
  nlbEnisString: string,
  port: number
): TargetDescription[] {
  const targets: TargetDescription[] = [];
  const quotesStrippedInput = nlbEnisString.replace(/"/g, ''); // Remove quotes from nlbEnisString
  const nlbEnis = quotesStrippedInput.split(',');
  for (const eni of nlbEnis) {
    const [ip, az] = eni.split('/');
    targets.push({
      Id: ip,
      Port: port,
      AvailabilityZone: az,
    });
  }
  return targets;
}

async function GetParameterFromSSM(
  ssmARN: string,
  ssmClient: SSMClient
): Promise<string> {
  const input: GetParameterCommandInput = {
    Name: ssmARN,
  };
  const command = new GetParameterCommand(input);
  const response = await ssmClient.send(command);
  return response.Parameter?.Value || '';
}

async function CreateListener(
  nlbARN: string,
  targetGroupARN: string,
  port: number,
  protocol: Protocol,
  elbV2Client: ElasticLoadBalancingV2Client
): Promise<void> {
  try {
    // Create the ListenerInput
    const createListenerCommandInput: CreateListenerCommandInput = {
      DefaultActions: [
        {
          Type: 'forward',
          TargetGroupArn: targetGroupARN,
        },
      ],
      LoadBalancerArn: nlbARN,
      Port: port,
      Protocol: protocol,
    };

    const listenerCommand = new CreateListenerCommand(
      createListenerCommandInput
    );
    await elbV2Client.send(listenerCommand);
  } catch (error) {
    console.error('Error creating listener:', error);
    throw error;
  }
}

// Function to tag the newly created target group
async function TagTargetGroup(
  targetGroupARN: string,
  tags: {[key: string]: string},
  taggingClient: ResourceGroupsTaggingAPIClient
): Promise<void> {
  try {
    const tagResourcesCommand = new TagResourcesCommand({
      ResourceARNList: [targetGroupARN],
      Tags: tags,
    });

    await taggingClient.send(tagResourcesCommand);
  } catch (error) {
    console.error('Error tagging target group:', error);
    throw error;
  }
}