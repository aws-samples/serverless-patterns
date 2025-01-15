import {
  EC2Client,
  DescribeNetworkInterfacesCommand,
  DescribeNetworkInterfacesCommandInput,
} from '@aws-sdk/client-ec2';

const ec2Client = new EC2Client({ region: process.env.AWS_REGION });

interface CustomResourceInvokeEvent {
  elbArn: string;
}

export const handler = async (event: CustomResourceInvokeEvent) => {
  try {
    console.log('Event:', JSON.stringify(event, null, 2));

    // Extract elbArn
    const { elbArn } = event;

    const response = await getENIattributes(elbArn, ec2Client);

    return response;
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

// Function to get the IP address and Availability zones of the provided loadbalancer
async function getENIattributes(
  elbArn: string,
  ec2Client: EC2Client
): Promise<string> {
  // Get the ELB name from the ELB ARN
  const elbName = getELBName(elbArn);

  // Describe the network interfaces of the ELB using the AWS SDK
  const input: DescribeNetworkInterfacesCommandInput = {
    Filters: [
      {
        Name: 'description',
        Values: [`ELB ${elbName}`],
      },
    ],
  };
  const command = new DescribeNetworkInterfacesCommand(input);
  const response = await ec2Client.send(command);

  // Extract the IP address and associated Availability zones and save it in a format that is easy
  // to parse using CloudFormation functions
  // e.g. 10.1.2.3/us-east-1d
  const elbPoints: string[] =
    response.NetworkInterfaces?.map(
      (eni) => `${eni.PrivateIpAddress!}/${eni.AvailabilityZone!}`
    ) ?? [];

  if (elbPoints.length === 0) {
    throw new Error('No IP address found for the provided load balancer');
  }

  return elbPoints.join(",");
}

// Function to get ELB name from the ELB ARN
// e.g. arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/Some-Name/abcdefghijkl1234
function getELBName(elbArn: string): string {
  const elbName = elbArn.split(':loadbalancer/')[1];
  return elbName;
}
