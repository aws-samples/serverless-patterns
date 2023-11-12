import time
import traceback
import boto3
import logging
import json
from collections import OrderedDict
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    content = event["body"]
    json_object = json.loads(content)

    # json_object = event

    # input parameters passed from the caller event
    # Amazon Redshift Serverless Workgroupname
    redshift_workgroup_name = json_object["redshift_workgroup_name"]
    # database name for the Amazon Redshift serverless instance
    redshift_database_name = json_object["redshift_database"]
    # IAM Role of Amazon Redshift sererless instance having access to S3
    redshift_iam_role = os.environ["Exec_Redshift_Role"]
    # run_type can be either asynchronous or synchronous; try tweaking based on your requirement
    run_type = json_object["run_type"]
    # Query
    sql_query = json_object["sql_query"]

    max_wait_cycle = json_object["max_wait_cycle"]

    sql_statements = OrderedDict()

    if run_type != "synchronous" and run_type != "asynchronous":
        raise Exception(
            "Invalid Event run_type. \n run_type has to be synchronous or asynchronous."
        )

    isSynchronous = True if run_type == "synchronous" else False

    # initiate redshift-data redshift_data_api_client in boto3
    redshift_data_api_client = boto3.client("redshift-data")

    logger.info("Running sql queries in {} mode!\n".format(run_type))

    try:
        res = execute_sql_data_api(
            redshift_data_api_client,
            redshift_database_name,
            sql_query,
            redshift_workgroup_name,
            isSynchronous,
            max_wait_cycle,
        )
        response = json.dumps(res)
        json_response = json.loads(response)

    except Exception as e:
        raise Exception(str(e) + "\n" + traceback.format_exc())

    return {"statusCode": 200, "body": json_response}


def execute_sql_data_api(
    redshift_data_api_client,
    redshift_database_name,
    query,
    redshift_workgroup_name,
    isSynchronous,
    max_wait_cycle,
):
    MAX_WAIT_CYCLES = max_wait_cycle
    attempts = 0
    # Calling Redshift Data API with executeStatement()
    result = redshift_data_api_client.execute_statement(
        Database=redshift_database_name,
        WorkgroupName=redshift_workgroup_name,
        Sql=query,
    )
    query_id = result["Id"]
    desc = redshift_data_api_client.describe_statement(Id=query_id)
    query_status = desc["Status"]
    logger.info("Query status: {} .... for query-->{}".format(query_status, query))
    done = False
    res = json.dumps(
        "query status is: {} for query id: {} ".format(query_status, query_id)
    )
    # Wait until query is finished or max cycles limit has been reached.
    while not done and isSynchronous and attempts < MAX_WAIT_CYCLES:
        attempts += 1
        time.sleep(1)
        desc = redshift_data_api_client.describe_statement(Id=query_id)
        query_status = desc["Status"]

        if query_status == "FAILED":
            res = json.dumps("SQL query failed:" + query_id + ": " + desc["Error"])

        elif query_status == "FINISHED":
            logger.info(
                "query status is: {} for query id: {} ".format(query_status, query_id)
            )
            res = json.dumps(
                "query status is: {} for query id: {} ".format(query_status, query_id)
            )
            done = True
            # print result if there is a result (typically from Select statement)
            if desc["HasResultSet"]:
                response = redshift_data_api_client.get_statement_result(Id=query_id)
                res = json.dumps(response["Records"])
                logger.info(
                    "Printing response of  query --> {}".format(response["Records"])
                )
        else:
            logger.info("Current working... query status is: {} ".format(query_status))

    # Timeout Precaution
    if done == False and attempts >= MAX_WAIT_CYCLES and isSynchronous:
        logger.info(
            "Limit for MAX_WAIT_CYCLES has been reached before the query was able to finish. We have exited out of the while-loop. You may increase the limit accordingly. \n"
        )
        res = json.dumps(
            "Limit for MAX_WAIT_CYCLES has been reached before the query was able to finish. We have exited out of the while-loop. You may increase the limit accordingly."
        )

    return res
