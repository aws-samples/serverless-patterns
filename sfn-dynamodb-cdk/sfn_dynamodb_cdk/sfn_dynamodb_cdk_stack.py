from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import (
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as sfn_tasks,
    aws_dynamodb as ddb,
    core
)
from aws_cdk.aws_dynamodb import Attribute

table_name = "MyDDBTableName"


class SfnDynamodbCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # table_props = ddb.TableProps(self, partition_key={"name": "id", "type": ddb.AttributeType.STRING})
        ddb_table = ddb.Table(self, table_name, billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
                              partition_key=Attribute(name="id", type=ddb.AttributeType.STRING))

        send_to_ddb = sfn_tasks.DynamoPutItem(self, "SendToDDB",
                                              item={
                                                  "id": sfn_tasks.DynamoAttributeValue.from_string(
                                                      sfn.JsonPath.string_at("$.id")),
                                                  "description": sfn_tasks.DynamoAttributeValue.from_string(
                                                      sfn.JsonPath.string_at(
                                                          "States.Format('Hello, my id is {}.', $.id)"))
                                              },
                                              table=ddb_table,
                                              result_path=sfn.JsonPath.string_at("$.output_from_ddb_put")
                                              )

        read_from_ddb = sfn_tasks.DynamoGetItem(self, "ReadFromDDb",
                                                key={
                                                    "id": sfn_tasks.DynamoAttributeValue.from_string(
                                                        sfn.JsonPath.string_at("$.id"))
                                                },
                                                table=ddb_table,
                                                result_path=sfn.JsonPath.string_at("$.output_from_ddb_get"),
                                                output_path=sfn.JsonPath.string_at("$.output_from_ddb_get.Item")
                                                )

        definition = send_to_ddb.next(read_from_ddb)
        state_machine = sfn.StateMachine(
            self, "SfnToDDBWorkflowStateMachine",
            definition=definition,
            timeout=core.Duration.minutes(5)
        )

        core.CfnOutput(scope=self, id='StateMachineArn',
                       value=state_machine.state_machine_arn)

        core.CfnOutput(scope=self, id='TableName',
                       value=ddb_table.table_name)
