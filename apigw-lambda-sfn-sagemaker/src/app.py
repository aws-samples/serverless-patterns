import json
import os

import boto3

print("Loading function")


def get_domain_id(domain_arn):
    return domain_arn.split("/")[1]


def validate_request(event):
    if "domain_name" not in event:
        return False
    return True


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    event = event["body"]
    event = json.loads(event)

    if not validate_request(event):
        return {"statusCode": 400,
                "body": json.dumps("Invalid request")}

    response = create_sagemaker_domain(event)
    invoke_statemachine(event["domain_name"], response)

    return {"statusCode": 200,
            "body": json.dumps(f"SageMaker Domain ID: {get_domain_id(response['DomainArn'])} created!!")}


def prepare_subnet_ids():
    subnets = os.environ["SUBNETS"]
    subnets = subnets.split(", ")
    return subnets


def create_sagemaker_domain(event):
    sagemaker_client = boto3.client("sagemaker")
    domain_name = event["domain_name"]
    response = sagemaker_client.create_domain(
        DomainName=domain_name,
        AuthMode="IAM",
        VpcId=os.environ["VPC_ID"],
        SubnetIds=prepare_subnet_ids(),
        DefaultUserSettings={
            "ExecutionRole": os.environ["SAGEMAKER_ROLE"],
            "StudioWebPortal": "ENABLED",
            "DefaultLandingUri": "studio::"
        },
        Tags=[
            {"Key": "Name", "Value": domain_name},
        ],
    )
    return response


# write a method to invoke a stepfunctions statemachine
def invoke_statemachine(domain_name, sagemaker_response):
    stepfunctions_client = boto3.client("stepfunctions")
    statemachine_arn = os.environ["STATEMACHINE_ARN"]
    input_object = {
        "domain_name": domain_name,
        "domain_id": get_domain_id(sagemaker_response["DomainArn"]),
        "domain_arn": sagemaker_response["DomainArn"]
    }
    stepfunctions_client.start_execution(
        stateMachineArn=statemachine_arn,
        input=json.dumps(input_object)
    )
