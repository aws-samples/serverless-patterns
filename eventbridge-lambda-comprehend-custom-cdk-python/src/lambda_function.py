import boto3
import os
import logging
import http
from datetime import datetime
from boto3.dynamodb.conditions import Key

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

region_name = os.getenv("region", "us-east-1")
inference_unit = os.getenv("inferenceunit", 2)
comprehend_obj = boto3.client("comprehend", region_name=region_name)


def lambda_handler(event, context):
    """
    :param event: Input from the EventBridge on the basis of schedule
    :param context: Any methods and properties that provide information about the invocation, function, and execution environment
    :return: THe response from Comprehend service about the creation and deletion of endpoint for custom model
    """
    try:
        LOG.info(f"Event is {event}")
        returnMsg = None

        dynamodb_table = event["dynamoDBTable"]
        dynamodb_obj = boto3.resource("dynamodb").Table(dynamodb_table)

        # Invoke Comprehend Create Endpoint API
        if event['eventType'] == 'CreateEndpoint':
            LOG.info(f'Scheduled action: CreateEndpoint')

            response = comprehend_obj.create_endpoint(
                EndpointName=event["customEndpoint"],
                ModelArn=event["customModelArn"],
                DesiredInferenceUnits=inference_unit,
                Tags=[
                    {"Key": "Workload", "Value": "IDP"},
                ],
            )
            LOG.info(f'Endpoint creation has been initiated with ARN: {response["EndpointArn"]} and record has been updated in DynamoDB table')
            dynamodb_obj.put_item(Item={"CustomModelType": event["modelType"], "timestamp": str(datetime.now()), "CustomEndpointName": event["customEndpoint"], "EndpointARN": response["EndpointArn"]})
            returnMsg = {"statusCode": http.HTTPStatus.OK, "endpointARN": response["EndpointArn"], "action": event['eventType']}
        
        elif event['eventType'] == 'DeleteEndpoint':
            LOG.info(f'Scheduled action: DeleteEndpoint')

            # Get the EndpointARN from DynamoDB by passing the CustomModelType and CustomEndpointName as Partition Key and Sort Key respectively
            EndpointQueryResp = dynamodb_obj.query(KeyConditionExpression=Key("CustomModelType").eq(event["modelType"]) & Key("CustomEndpointName").eq(event["customEndpoint"]))
            EndpointARN = EndpointQueryResp["Items"][0]["EndpointARN"]
            LOG.info(f'DeleteEndpoint method EndpointARN: {EndpointQueryResp}')

            response = comprehend_obj.delete_endpoint(
                EndpointArn=EndpointARN
            )
            LOG.info(f"Response from Comprehend Delete Endpoint API: {response}")
            
            dynamodb_obj.delete_item(Key={"CustomModelType": event["modelType"], "CustomEndpointName": event["customEndpoint"]})
            LOG.info(f'Endpoint has been deleted with ARN: {EndpointARN} and record has been deleted from DynamoDB table')
            returnMsg = {"statusCode": http.HTTPStatus.OK, "endpointARN": EndpointARN, "action": event['eventType']}

        # Return the execution code and EndpointARN
        return returnMsg

    except Exception as e:
        LOG.error("Custom model endpoint operation failed!!")
        raise e
