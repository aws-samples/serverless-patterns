import { EC2Client, AllocateAddressCommand, CreateNatGatewayCommand } from "@aws-sdk/client-ec2"; // ES Modules import
const client = new EC2Client({});

export const handler = async (event) => {

//Allocate EIP
const alloc = {};
const alloccommand = new AllocateAddressCommand(alloc);
const allocresponse = await client.send(alloccommand);
var subnetid = event.subnetid;
var rtbid = event.rtbid;

//Create Nat Gateway
const input = { // CreateNatGatewayRequest
  DryRun: false,
  SubnetId: subnetid, // required
  AllocationId: allocresponse.AllocationId,
  TagSpecifications: [ // TagSpecificationList
    { // TagSpecification
      ResourceType: "natgateway",
      Tags: [ // TagList
        { // Tag
          Key: "Project",
          Value: "NGW-Sample",
        },
      ],
    },
  ],
  ConnectivityType: "public"
};
const command = new CreateNatGatewayCommand(input);
const response = await client.send(command);

return { status : "InProgress", "ngwid" : response.NatGateway.NatGatewayId, "rtbid": rtbid } ;

};
