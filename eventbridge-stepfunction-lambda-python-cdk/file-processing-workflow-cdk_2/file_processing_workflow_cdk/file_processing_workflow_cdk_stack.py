from constructs import Construct
 
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets,
    aws_stepfunctions as sfn,
    aws_lambda as _lambda,
    aws_iam as iam
)
import json
import os


class FileProcessingWorkflowCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # Define the desired bucket name
        source_bucket_name = "fileprocessingworkflowstore.capstonesource.demo.v92223-1"
        destination_bucket_name = "fileprocessingworkflowstore.capstonedestination.demo.v92223-1"

        source_bucket = s3.Bucket(

                self,
                "SourceBucket",
                bucket_name=source_bucket_name,
                event_bridge_enabled=True
        )

        destination_bucket = s3.Bucket(
                self,
                "DestinationBucket",
                bucket_name=destination_bucket_name,
                event_bridge_enabled=True
            )
        


        
       
         # Define environment variables
        environment_variables = {
            'destination_bucket_name': 'fileprocessingworkflowstore.capstonedestination.demo.v92223-1'
        }


         # Create the Basic Execution Role
        basic_execution_role = iam.Role(
            self,
            "CapstoneLambdaBasicRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole'
                )
            ],
        )


        basic_and_s3_execution_role = iam.Role(
            self, "CapstoneLambdaS3Role",
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com')
        )

        basic_and_s3_execution_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')
        )

        
        # Attach full S3 access policy to the role for both buckets
        basic_and_s3_execution_role.add_to_policy(
            iam.PolicyStatement(
                actions=['s3:*'],
                resources=[source_bucket.bucket_arn + '/*', destination_bucket.bucket_arn + '/*']
            )
        )



        # Create the FileTypeHandler Lambda function
        file_type_handler_lambda = _lambda.Function(
            self,
            "FileTypeHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="fileType.lambda_handler",  # As your handler function is named lambda_handler in a file named fileType.py
            code=_lambda.Code.from_asset("lambda"),  # As your Lambda code is in a directory named "lambda"
            role=basic_execution_role          # Attach the role to the Lambda function

        )


        file_processor_xml_lambda = _lambda.Function(
            self,
            "FileHandlerXML",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="fileProcessorXML.lambda_handler",  # As your handler function is named lambda_handler in a file named fileProcessorXML
            code=_lambda.Code.from_asset("lambda"),  # As your Lambda code is in a directory named "lambda"
            environment=environment_variables,
            role=basic_and_s3_execution_role          # Attach the role to the Lambda function

        )

        file_processor_json_lambda = _lambda.Function(
            self,
            "FileHandlerJSON",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="fileProcessorJSON.lambda_handler",  # As your handler function is named lambda_handler in a file named fileProcessorJSON.py
            code=_lambda.Code.from_asset("lambda"),  # As your Lambda code is in a directory named "lambda"
            environment=environment_variables,
            role=basic_and_s3_execution_role          # Attach the role to the Lambda function
        )


        # Create an IAM role for Step Functions execution
        step_function_execution_role = iam.Role(
            self, 'StepFunctionExecutionRole',
            assumed_by=iam.ServicePrincipal('states.amazonaws.com')
        )

        # Attach CloudWatchLogsFullAccess policy
        step_function_execution_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchLogsFullAccess')
        )

        # Attach XRayAccessPolicy
        step_function_execution_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('AWSXrayWriteOnlyAccess')
        )


        # Attach Lambda invoke policies for each lambda function
        lambda_functions = [file_type_handler_lambda.function_arn, file_processor_xml_lambda.function_arn, file_processor_json_lambda.function_arn]
        for function_arn in lambda_functions:
            step_function_execution_role.add_to_policy(
                iam.PolicyStatement(
                    actions=['lambda:InvokeFunction'],
                    resources=[function_arn]
                )
            )

        
        

        
        # Get the directory of the script
        cdk_script_dir = os.path.dirname(os.path.abspath(__file__))
        print(cdk_script_dir)

        # Construct the path to the JSON file
        state_machine_definition_file_path = os.path.join(cdk_script_dir, "state_machine_definition.json")
        print(state_machine_definition_file_path)

        # Open the JSON file
        with open(state_machine_definition_file_path, "r") as definition_file:
            state_machine_definition = json.load(definition_file)


        state_machine_definition["States"]["FileGateway"]["Parameters"]["FunctionName"] = file_type_handler_lambda.function_arn
        state_machine_definition["States"]["XMLHandler"]["Parameters"]["FunctionName"] = file_processor_xml_lambda.function_arn
        state_machine_definition["States"]["JsonHandler"]["Parameters"]["FunctionName"] = file_processor_json_lambda.function_arn

        #Convert state machine definition to string
        state_machine_definition_string = json.dumps(state_machine_definition, indent=2)
        # Add a target to the rule (you can customize the target based on your needs)
        # Define your Step Function
       # print(state_machine_definition_string)

        # Add a target to the rule (you can customize the target based on your needs)
        # Define your Step Function
        #file_processor_state_machine = sfn.StateMachine(
        #    self,
        #    "Dummy",
        #    definition_body=sfn.DefinitionBody.from_string(state_machine_definition_string)
        #)

        
        # Add a target to the rule (you can customize the target based on your needs)
        # Define your Step Function
        #file_processor_cfn_state_machine = sfn.CfnStateMachine(
        #    self,
        #    "CfnStateMachine",
        #    role_arn=step_function_execution_role.role_arn,
        #    definition_string=state_machine_definition_string
        #)


        file_processor_state_machine = sfn.StateMachine(self, "FileProcessorStateMachine",
                                         definition_body=sfn.StringDefinitionBody.from_string(state_machine_definition_string),
                                         role=step_function_execution_role
        )


       

        # Create an EventBridge rule
        rule = events.Rule(
            self,
            "MonitorS3ObjectCreated",
            event_pattern= {
                "source":["aws.s3"],
                "detail_type":["Object Created"],
                "detail": {
                    "bucket": {
                        "name":[source_bucket.bucket_name]
                    }
                }  
            }
        )
    
    
        

       
        # Add the Step Function as a target to the EventBridge rule
        rule.add_target(targets.SfnStateMachine(file_processor_state_machine))

       


        





        