from aws_cdk import (
    Aws,
    Stack,
    CfnOutput,
    Duration,
    aws_s3 as s3,
    aws_glue as glue,
    aws_stepfunctions as sf,
    aws_stepfunctions_tasks as tasks,
)
region = Aws.REGION
account = Aws.ACCOUNT_ID

from constructs import Construct

class SfnAthenaCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #the S3 bucket where CloudFront Access Logs will be stored
        cf_access_logs = s3.Bucket(self, "LogBucket")

        #S3 bucket where Athena will put the results
        athena_results = s3.Bucket(self, "AthenaResultsBucket")

        #create an Athena database
        glue_database_name = "serverlessland_database"
        myDatabase = glue.CfnDatabase(
            self,
            id=glue_database_name,
            catalog_id=account,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                description=f"Glue database '{glue_database_name}'",
                name=glue_database_name,
            )
        )

        #define a table with the structure of CloudFront Logs https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html
        athena_table = glue.CfnTable(self,
            id='cfaccesslogs',
            catalog_id=account,
            database_name=glue_database_name,
            table_input=glue.CfnTable.TableInputProperty(
                name='cf_access_logs',
                description='CloudFront access logs',
                table_type='EXTERNAL_TABLE',
                parameters = {
                    'skip.header.line.count': '2',
                },
                storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                    location="s3://"+cf_access_logs.bucket_name+"/",
                    input_format='org.apache.hadoop.mapred.TextInputFormat',
                    output_format='org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    compressed=False,
                    serde_info=glue.CfnTable.SerdeInfoProperty(
                        serialization_library='org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        parameters={
                            'field.delim' : '	'
                        }
                    ),
                    columns=[
                        glue.CfnTable.ColumnProperty(name='date', type='date'),
                        glue.CfnTable.ColumnProperty(name='time', type='string'),
                        glue.CfnTable.ColumnProperty(name='location', type='string'),
                        glue.CfnTable.ColumnProperty(name='bytes', type='bigint'),
                        glue.CfnTable.ColumnProperty(name='request_ip', type='string'),
                        glue.CfnTable.ColumnProperty(name='method', type='string'),
                        glue.CfnTable.ColumnProperty(name='host', type='string'),
                        glue.CfnTable.ColumnProperty(name='uri', type='string'),
                        glue.CfnTable.ColumnProperty(name='status', type='string'),
                        glue.CfnTable.ColumnProperty(name='referer', type='string'),
                        glue.CfnTable.ColumnProperty(name='user_agent', type='string'),
                        glue.CfnTable.ColumnProperty(name='query_string', type='string'),
                        glue.CfnTable.ColumnProperty(name='cookie', type='string'),
                        glue.CfnTable.ColumnProperty(name='result_type', type='string'),
                        glue.CfnTable.ColumnProperty(name='request_id', type='string'),
                        glue.CfnTable.ColumnProperty(name='host_header', type='string'),
                        glue.CfnTable.ColumnProperty(name='request_protocol', type='string'),
                        glue.CfnTable.ColumnProperty(name='request_bytes', type='bigint'),
                        glue.CfnTable.ColumnProperty(name='time_taken', type='float'),
                        glue.CfnTable.ColumnProperty(name='xforwarded_for', type='string'),
                        glue.CfnTable.ColumnProperty(name='ssl_protocol', type='string'),
                        glue.CfnTable.ColumnProperty(name='ssl_cipher', type='string'),
                        glue.CfnTable.ColumnProperty(name='response_result_type', type='string'),
                        glue.CfnTable.ColumnProperty(name='http_version', type='string'),
                        glue.CfnTable.ColumnProperty(name='fle_status', type='string'),
                        glue.CfnTable.ColumnProperty(name='fle_encrypted_fields', type='int'),
                        glue.CfnTable.ColumnProperty(name='c_port', type='int'),
                        glue.CfnTable.ColumnProperty(name='time_to_first_byte', type='float'),
                        glue.CfnTable.ColumnProperty(name='x_edge_detailed_result_type', type='string'),
                        glue.CfnTable.ColumnProperty(name='sc_content_type', type='string'),
                        glue.CfnTable.ColumnProperty(name='sc_content_len', type='string'),
                        glue.CfnTable.ColumnProperty(name='sc_range_start', type='bigint'),
                        glue.CfnTable.ColumnProperty(name='sc_range_end', type='bigint')
                    ]
                ),
            )
        )

        #submit the query and wait for the results
        start_query_execution_job = tasks.AthenaStartQueryExecution(self, "Start Athena Query",
            query_string="SELECT uri FROM cf_access_logs limit 10",
            integration_pattern=sf.IntegrationPattern.RUN_JOB, #executes the command in SYNC mode
            query_execution_context=tasks.QueryExecutionContext(
                database_name=glue_database_name
            ),
            result_configuration=tasks.ResultConfiguration(
                output_location=s3.Location(
                    bucket_name=athena_results.bucket_name,
                    object_key="results"
                )
            )
        )

        #get the results
        get_query_results_job = tasks.AthenaGetQueryResults(self, "Get Query Results",
            query_execution_id=sf.JsonPath.string_at("$.QueryExecution.QueryExecutionId"),
            result_path=sf.JsonPath.string_at("$.GetQueryResults"),
        )

        #prepare the query to see if more results are available (up to 1000 can be retrieved)
        prepare_next_params = sf.Pass(self, "Prepare Next Query Params",
            parameters={
                "QueryExecutionId.$": "$.StartQueryParams.QueryExecutionId",
                "NextToken.$": "$.GetQueryResults.NextToken"
            },
            result_path=sf.JsonPath.string_at("$.StartQueryParams")
        )

        #check to see if more results are available
        has_more_results = sf.Choice(self, "Has More Results?").when(
                    sf.Condition.is_present("$.GetQueryResults.NextToken"),
                    prepare_next_params.next(get_query_results_job)
                ).otherwise(sf.Succeed(self, "Done"))


        #do something with each result
        #here add your own logic
        map = sf.Map(self, "Map State",
            max_concurrency=1,
            input_path=sf.JsonPath.string_at("$.GetQueryResults.ResultSet.Rows[1:]"),
            result_path = sf.JsonPath.DISCARD
        )
        map.iterator(sf.Pass(self, "DoSomething"))


        # Step function to orchestrate Athena query and retrieving the results
        workflow = sf.StateMachine(self, "AthenaQuery",
            definition=start_query_execution_job.next(get_query_results_job).next(map).next(has_more_results),
            timeout=Duration.minutes(60)
        )

        CfnOutput(self, "Logs",
            value=cf_access_logs.bucket_name, export_name='LogsBucket')

        CfnOutput(self, "SFName",
            value=workflow.state_machine_name, export_name='SFName')

        CfnOutput(self, "SFArn",
            value = workflow.state_machine_arn,
            export_name = 'StepFunctionArn',
            description = 'Step Function arn')

