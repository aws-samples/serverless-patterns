import { Handler } from 'aws-lambda';
import {
  EC2Client,
  AssociateAddressCommand,
  DescribeAddressesCommand,
  DescribeNetworkInterfacesCommand,
} from '@aws-sdk/client-ec2'; // ES Modules import
import { AssociateLambdaElasticIpEvent } from '../types/associate-lambda-elastic-ip-event';
const client = new EC2Client();

export const handler: Handler = async (event: AssociateLambdaElasticIpEvent) => {
  // Call the async function

  console.log('Associating Lambda to Elastic IP Custom Resource');
  console.log('environment', process.env);
  const allocationId = process.env.ELASTIC_IP_ALLOCATION_ID;
  if (!allocationId) {
    throw new Error(`Error allocation id cannot be null or empty. '${allocationId}'`);
  }
  console.log(`allocation id from env: ${allocationId}`);
  try {
    console.log('Fetching Lambda network interface ID associated with the elastic ip...');

    const input1 = {
      // DescribeAddressesRequest

      AllocationIds: [
        // AllocationIdList
        allocationId,
      ],
      DryRun: true || false,
    };
    const response = await client.send(new DescribeAddressesCommand(input1));
    console.log('response:', response);

    if (!response.Addresses || !response.Addresses?.length) {
      // throw new Error(`Error allocation id cannot be null or empty. '${allocationId}'`);

      console.error(`Error allocation id cannot be null or empty. '${allocationId}'`);
    }
    // const networkInterfaceId = response.Addresses![0].NetworkInterfaceId!;
    // console.log(`Lambda network interface id ${networkInterfaceId}`);

    const input = {
      // DescribeAddressesRequest
      Filters: [
        {
          Name: 'interface-type',
          Values: ['lambda'],
        },
        {
          Name: 'subnet-id',
          Values: [event.subnetId],
        },
        {
          Name: 'vpc-id',
          Values: [event.vpcId],
        },
        {
          Name: 'group-id',
          Values: [event.securityGroupId],
        },
        {
          Name: 'availability-zone',
          Values: [event.availabilityZone],
        },
      ],
      // PublicIps: [
      //     // PublicIpStringList
      //     'STRING_VALUE',
      // ],
      AllocationIds: [
        // AllocationIdList
        allocationId,
      ],
      NextToken: 'STRING_VALUE',
      MaxResults: Number('int'),
      DryRun: true || false,
    };

    const response1 = await client.send(new DescribeNetworkInterfacesCommand(input));
    console.log('response1:', response1);

    console.log('Associating Lambda to Elastic IP...');

    const input2 = {
      // AssociateAddressRequest
      AllocationId: allocationId,
      // InstanceId: "STRING_VALUE",
      // PublicIp: "STRING_VALUE",
      // AllowReassociation: true || false,
      DryRun: true || false,
      // NetworkInterfaceId: networkInterfaceId,
      NetworkInterfaceId: response1.NetworkInterfaces![0].NetworkInterfaceId,

      // PrivateIpAddress: "STRING_VALUE",
    };

    const response2 = await client.send(new AssociateAddressCommand(input2));
    console.log('response2:', response2);

    console.log('Association ID:', response2.AssociationId);
  } catch (error: any) {
    console.error(`Error Fetching VIN: ${error.message}`);
    throw error;
  }
};
