import { Handler } from 'aws-lambda';
import { EC2Client, AssociateAddressCommand, DescribeNetworkInterfacesCommand } from '@aws-sdk/client-ec2'; // ES Modules import
import { AssociateLambdaElasticIpEvent } from '../types/associate-lambda-elastic-ip-event';
const client = new EC2Client();

export const handler: Handler = async (event: AssociateLambdaElasticIpEvent) => {
    console.log('Associating Lambda to Elastic IP Custom Resource Event:', event);
    console.log('Environment', process.env);
    const allocationId = process.env.ELASTIC_IP_ALLOCATION_ID;
    if (!allocationId) {
        throw new Error(`Error allocation id cannot be null or empty. '${allocationId}'`);
    }
    console.log(`Allocation id from env: ${allocationId}`);
    try {
        console.log('Fetching lambda network interface ID associated with the elastic ip...');

        const DescribeNetworkInterfacesCommandRequest = {
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
                {
                    Name: 'status',
                    Values: ['in-use'],
                },
                {
                    Name: 'description',
                    Values: [`AWS Lambda VPC ENI-${event.functionName}*`],
                },
            ],
            AllocationIds: [allocationId],
            MaxResults: 10,
            DryRun: false,
        };

        console.log('DescribeNetworkInterfacesCommandRequest:', JSON.stringify(DescribeNetworkInterfacesCommandRequest, null, 2));

        const DescribeNetworkInterfacesCommandResponse = await client.send(
            new DescribeNetworkInterfacesCommand(DescribeNetworkInterfacesCommandRequest),
        );
        console.log('DescribeNetworkInterfacesCommandResponse:', JSON.stringify(DescribeNetworkInterfacesCommandResponse, null, 2));
        const returnedNetworkInterfaces = DescribeNetworkInterfacesCommandResponse.NetworkInterfaces;
        if (!returnedNetworkInterfaces?.length) {
            throw new Error(`No network interface is associated with this lambda function ${event.functionName}`);
        }

        console.log('Associating Lambda to Elastic IP...');

        const AssociateAddressRequest = {
            AllocationId: allocationId,
            DryRun: false,
            NetworkInterfaceId: returnedNetworkInterfaces[0].NetworkInterfaceId,
        };

        console.log('AssociateAddressRequest:', AssociateAddressRequest);
        const AssociateAddressCommandResponse = await client.send(new AssociateAddressCommand(AssociateAddressRequest));
        console.log('AssociateAddressCommandResponse:', AssociateAddressCommandResponse);

        console.log('Association ID:', AssociateAddressCommandResponse.AssociationId);
    } catch (error: any) {
        console.error(`Error Associating ElasticIP with Lambda: ${error.message}`);
        throw error;
    }
};
