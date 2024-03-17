from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_s3 as s3,
    aws_iam as iam,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as sfn_tasks,
    RemovalPolicy
)
from constructs import Construct

class SfnCfnStacksetsPatternStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ##########################################################################
        #   Step Functions State Machine                                         #
        ##########################################################################

        ''' The SFN needs the following input to be provided:
        Input Params: 
        {
            "operation": "create"|"delete",
            "runInManagementAcount": "true"|"false",
            "managementAccountId": "XXXXXXXXXXXX",
            "templateURL": "<The location of the tempalte file in an Amazon S3 bucket>"
        }
        '''

        sfn_name = "sfn-cfn-stackset"

        # Task - call organizations:listRoots
        # SFN needs IAM permisson to call organizations:listRoots
        list_roots = sfn_tasks.CallAwsService(self, "ListRoots",
            service="organizations",
            action="listRoots",
            iam_resources=["*"],
            result_path="$.org",
            result_selector={
                "rootOU.$": "$.Roots[0].Id"
            },
        )

        # Fail states - to catch errors and exit
        invalid_inputs = sfn.Fail(self, "InvalidInput",
            cause="Input Params should be ( \"operation\": \"create\"|\"delete\" }",
            error="InvalidInput"
        )
        stack_set_exists = sfn.Fail(self, "StackSetExists",
            cause="StackSet already exists",
            error="CreateStackSetsFailed"
        )
        delete_stack_set_failed = sfn.Fail(self, "DeleteStackSetFailed",
            cause="StackSet not found or StackSet Status was one of \'FAILED | STOPPING | STOPPED\'",
            error="Failed to Delete StackSets"
        )
        create_stack_set_failed = sfn.Fail(self, "CreateStackSetFailed",
            error_path="$.error",
            cause_path="$.cause"
        )

        # Task - call cloudformation:createStackSet
        # SFN needs IAM permission to call cloudformation:createStackSet
        # Use the template passed as input params
        create_stack_set = sfn_tasks.CallAwsService(self, "CreateStackSet",
                                                    service="cloudformation",
                                                    action="createStackSet",
                                                    iam_resources=["*"],
                                                    parameters={
                                                        "StackSetName": sfn_name,
                                                        "Description": "StackSet for creating IAM roles in linked accounts",
                                                        "ManagedExecution": {
                                                            "Active": True
                                                        },
                                                        "PermissionModel": "SERVICE_MANAGED",
                                                        "Capabilities": ["CAPABILITY_NAMED_IAM"],
                                                        "AutoDeployment": {
                                                            "Enabled": True,
                                                            "RetainStacksOnAccountRemoval": False
                                                        },
                                                        "Parameters": [{
                                                            "ParameterKey": "ManagementAccountId",
                                                            "ParameterValue.$": "$.managementAccountId"
                                                        }],
                                                        "TemplateURL.$": "$.templateURL"
                                                    },
                                                    result_path="$.StackSetId"
        )
        create_stack_set.add_catch(stack_set_exists, errors=["CloudFormation.NameAlreadyExistsException"])

        create_stack_instances = sfn_tasks.CallAwsService(self, "CreateStackInstances",
                                                          service="cloudformation",
                                                          action="createStackInstances",
                                                          iam_resources=["*"],
                                                          parameters={
                                                                "StackSetName": sfn_name,
                                                                "Regions": ["us-east-1"],
                                                                "DeploymentTargets": {
                                                                    "OrganizationalUnitIds.$": "States.Array($.org.rootOU)"
                                                                }
                                                          }
        )

        creating_wait_x = sfn.Wait(self, "CreatingWaitX",
                                   state_name = "Creating, Wait 5s",
                                   time=sfn.WaitTime.duration(Duration.seconds(5))
        )                                                        

        check_creating_stack_set_status = sfn_tasks.CallAwsService(self, "CheckCreatingStackSetStatus",
                                                                    service="cloudformation",
                                                                    action="describeStackSetOperation",
                                                                    iam_resources=["*"],
                                                                    parameters={
                                                                        "StackSetName": sfn_name,
                                                                        "OperationId.$": "$.OperationId"
                                                                    }
        )

        delete_stack_instances = sfn_tasks.CallAwsService(self, "DeleteStackInstances",
                                                    service="cloudformation",
                                                    action="deleteStackInstances",
                                                    iam_resources=["*"],
                                                    parameters={
                                                        "StackSetName": sfn_name,
                                                        "Regions": ["us-east-1"],
                                                        "DeploymentTargets": {
                                                            "OrganizationalUnitIds.$": "States.Array($.org.rootOU)"
                                                        },
                                                        "RetainStacks": "false"
                                                    }
        )
        delete_stack_instances.add_catch(delete_stack_set_failed, errors=["CloudFormation.StackSetNotFoundException"])
        
        deleting_wait_x = sfn.Wait(self, "DeletingWaitX",
                                   state_name = "Deleting, Wait 5s",
                                   time=sfn.WaitTime.duration(Duration.seconds(5))
        )

        check_deleting_stack_set_status = sfn_tasks.CallAwsService(self, "CheckDeletingStackSetStatus",
                                                                    service="cloudformation",
                                                                    action="describeStackSetOperation",
                                                                    iam_resources=["*"],
                                                                    parameters={
                                                                        "StackSetName": sfn_name,
                                                                        "OperationId.$": "$.OperationId"
                                                                    }
        )

        delete_stack_set = sfn_tasks.CallAwsService(self, "DeleteStackSet",
                                                    service="cloudformation",
                                                    action="deleteStackSet",
                                                    iam_resources=["*"],
                                                    parameters={
                                                        "StackSetName": sfn_name
                                                    }
        )

        # Chain of states
        
        create_stack_set_chain = create_stack_set.next(create_stack_instances).next(creating_wait_x).next(check_creating_stack_set_status).next(
            sfn.Choice(self, "Create Completed?", output_path="$.StackSetOperation")
            .when(sfn.Condition.or_(sfn.Condition.string_equals("$.StackSetOperation.Status", "RUNNING"), sfn.Condition.string_equals("$.StackSetOperation.Status","QUEUED")), creating_wait_x)
            .when(sfn.Condition.string_equals("$.StackSetOperation.Status", "SUCCEEDED"), sfn.Succeed(self, "StackSet Created"))
            .otherwise(create_stack_set_failed)
        )

        delete_stack_set_chain = delete_stack_instances.next(deleting_wait_x).next(check_deleting_stack_set_status).next(
            sfn.Choice(self, "Delete Completed?", output_path="$.StackSetOperation")
            .when(sfn.Condition.or_(sfn.Condition.string_equals("$.StackSetOperation.Status", "RUNNING"), sfn.Condition.string_equals("$.StackSetOperation.Status", "QUEUED")), deleting_wait_x)
            .when(sfn.Condition.string_equals("$.StackSetOperation.Status", "SUCCEEDED"), delete_stack_set)
            .otherwise(delete_stack_set_failed)
        )

        definition = list_roots.next(
            sfn.Choice(self, "CreateOrDelete?")
            .when(sfn.Condition.string_equals("$.operation", "create"), create_stack_set_chain)
            .when(sfn.Condition.string_equals("$.operation", "delete"), delete_stack_set_chain)
            .otherwise(invalid_inputs))
        
        
        sfn_workflow = sfn.StateMachine(self, "SFN-CFN-StackSets-Pattern",
                                             comment="SFN Pattern to Create/Delete CFN StackSets",
                                             definition_body=sfn.DefinitionBody.from_chainable(definition)
        )

        ''' 
        Grant the SFN permission to read the S3 bucket where the CFn StackSet Template is saved/uploaded
        Replace the bucket name with the name of your S3 bucket
        '''
        s3_bucket_name = "dummy-public-bucket"
        s3_template_bucket = s3.Bucket.from_bucket_name(self, "S3TemplateBucket", s3_bucket_name)
        s3_template_bucket.grant_read(sfn_workflow)

        CfnOutput(self, "SFName",
            value=sfn_workflow.state_machine_name, 
            export_name='StepFunctionName',
            description='Step Function Name')

        CfnOutput(self, "SFArn",
            value=sfn_workflow.state_machine_arn,
            export_name='StepFunctionArn',
            description='Step Function ARN')