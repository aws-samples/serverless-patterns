import cfnresponse
import json
import boto3

def lambda_handler(event, context):
    print('REQUEST RECEIVED:\n' + json.dumps(event))
    responseData = {}

    # Handle Delete requests
    if event['RequestType'] == 'Delete':
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
        return

    # Handle Create or Update requests
    if event['RequestType'] == 'Create' or event['RequestType'] == 'Update':
        try:
            ec2 = boto3.resource('ec2')
            enis = event['ResourceProperties']['NetworkInterfaceIds']

            # Fetch private IPs of the network interfaces
            for index, eni in enumerate(enis):
                network_interface = ec2.NetworkInterface(eni)
                responseData[f'IP{index}'] = network_interface.private_ip_address
                print(responseData)

            # Send success response back to CloudFormation
            cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)

        except Exception as e:
            # Send failure response to CloudFormation with the error message
            responseData = {'error': str(e)}
            cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
            return
