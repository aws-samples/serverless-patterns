import json
import boto3
import os
import ipaddress

ec2 = boto3.client('ec2')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DynamoDBTable"])
sns = boto3.client('sns')

def lambda_handler(event, context):
    print(json.dumps(event))
    print(event['detail']['eventName'], " requested for ", event['detail']['requestParameters']['AdvertiseByoipCidrRequest']['Cidr'])
    cidr = event['detail']['requestParameters']['AdvertiseByoipCidrRequest']['Cidr']
    allowed = False
    if (event['detail']['eventName'] == 'AdvertiseByoipCidr'):
        allowed_cidrs = table.get_item(
            Key={
                'id': 'Allowed_CIDRs'
            }
        )
        print (allowed_cidrs)
        try:
            for allowed_cidr in allowed_cidrs['Item']['CIDRs']:
                if (ipaddress.IPv6Network(cidr).overlaps(ipaddress.IPv6Network(allowed_cidr))):
                    allowed = True
                    print("CIDR is in allowed list, ignoring.")
        except: 
            print("No allowed list exists.")
        if not allowed:
            print("CIDR is not in allowed list, removing advertisement.")
            response = ec2.withdraw_byoip_cidr(
                Cidr=cidr, 
                DryRun=False
            )
            
            message="Attempt to advertise BYOIP CIDR {} blocked via automation.".format(cidr)
            subject="BYOIP CIDR Advertisement Withdrawn"
            
            sns.publish(
                TopicArn=os.environ["SNSTopic"],
                Message=message,
                Subject=subject
            )
            print(json.dumps(response))