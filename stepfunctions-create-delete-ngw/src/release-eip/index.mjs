import { EC2Client, ReleaseAddressCommand } from "@aws-sdk/client-ec2"; // ES Modules import

const client = new EC2Client({});

export const handler = async (event) => {

const input = { // ReleaseAddressRequest
  AllocationId: event.eip,
  DryRun: false,
};
const command = new ReleaseAddressCommand(input);

  try
  {
    const response = await client.send(command);
    return  { status : "Success", eip : event.eip, "ngwid": event.ngwid } ;
  }
  catch(e)
  {
    if (e.name == "InvalidAllocationID.NotFound")
    {
      return { process : "Delete NGW", status : "Complete", eip : event.eip, "ngwid": event.ngwid };
    }
    else
    {
    return { status : "Error", eip : event.eip, "ngwid": event.ngwid } ; 
    }
  }
};
