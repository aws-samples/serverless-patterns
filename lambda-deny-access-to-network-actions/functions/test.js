import { EC2Client, DeleteNetworkInterfaceCommand } from "@aws-sdk/client-ec2";

exports.handler = async(event, context) => {
  console.log('Before create client')

  const client = new EC2Client({ region: process.env.AWS_REGION });

  console.log('Attempt to delete...')

  try {
    
    const resp = await client.send(
      new DeleteNetworkInterfaceCommand({
        NetworkInterfaceId: process.env.NetworkInterfaceId
      })
    );

    console.warn('SHOULD NOT BE HERE!');
    console.log(resp);
    

  } catch (err) {
    console.log('SHOULD BE HERE -- IF ACCESS DENIED');
    console.log(err);
  }
};