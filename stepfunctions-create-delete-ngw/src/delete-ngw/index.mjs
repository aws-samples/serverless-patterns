import { EC2Client, DescribeNatGatewaysCommand, DeleteNatGatewayCommand, DeleteRouteCommand } from "@aws-sdk/client-ec2"; // ES Modules import
const client = new EC2Client({});

export const handler = async (event) => {

const input = { // DescribeNatGatewaysRequest
  DryRun: false
};
const command = new DescribeNatGatewaysCommand(input);
const response = await client.send(command);
var rtbid = event.rtbid;


var ngwid = "";
var eip = "eipalloc-00000000000000000";
for (let i = 0; i < response.NatGateways.length; i++)
{
    if (response.NatGateways[i].State.toString() == 'available')
    {
      ngwid = response.NatGateways[i].NatGatewayId;
      eip = response.NatGateways[i].NatGatewayAddresses[0].AllocationId;

      const inputDel = { // DeleteNatGatewayRequest
        DryRun: false,
        NatGatewayId: ngwid, // required
      };
      const commandDel = new DeleteNatGatewayCommand(inputDel);
      const responseDel = await client.send(commandDel);
      
      try
      {
        //Delete route from route table
        const route = {
          "DestinationCidrBlock": "0.0.0.0/0",
          "RouteTableId": rtbid
        };
        const routecommand = new DeleteRouteCommand(route);
        await client.send(routecommand);
      }
      catch(e){}
    }
}

return { status : 'InProgress', 'eip' : eip, 'ngwid' : ngwid } ;

};
