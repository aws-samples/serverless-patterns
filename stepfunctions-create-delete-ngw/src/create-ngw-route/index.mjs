import { EC2Client, CreateRouteCommand } from "@aws-sdk/client-ec2"; // ES Modules import
const client = new EC2Client({});
export const handler = async (event) => {

const routeinput = {
  "DestinationCidrBlock": "0.0.0.0/0",
  "GatewayId": event.ngwid,
  "RouteTableId": event.rtbid
};
const routecommand = new CreateRouteCommand(routeinput);

try
{
  const routeresponse = await client.send(routecommand);
  return { process : "Create NGW", status : "Complete", "ngwid" : event.ngwid, rtbid : event.rtbid };
}
catch
{
  return { status : "Error", ngwid : event.ngwid, rtbid : event.rtbid } ;
}

};
