import boto3
import json
import time
#********************** CREATE LOG GROUP*********************** 
def create_log_group(log_group_name):
    # Initialize AWS Logs client
    logs_client = boto3.client('logs')
    
    try:
        # Check if the log group already exists
        logs_client.create_log_group(logGroupName=log_group_name)
        # Now, describe the log group to get its ARN
        response = logs_client.describe_log_groups(logGroupNamePrefix=log_group_name)

        if 'logGroups' in response:
            for log_group in response['logGroups']:
                if log_group['logGroupName'] == log_group_name:
                    return log_group['arn']
    
    except logs_client.exceptions.ResourceAlreadyExistsException:
          # Log group already exists
        response = logs_client.describe_log_groups(logGroupNamePrefix=log_group_name)

        if 'logGroups' in response:
            for log_group in response['logGroups']:
                if log_group['logGroupName'] == log_group_name:
                    return log_group['arn']
    
    

#********************** ENABLE ACCESS LOGS FOR REST/HTTP API*********************** 
def enable_access_logs(api_id, api_type, stage, destinationArn):
    # Initialize AWS clients
    apigateway_client = boto3.client('apigateway')
    apigatewayv2_client = boto3.client('apigatewayv2')
    logs_client = boto3.client('logs')
    
    # Define the parameters for enabling access logs
    if api_type == 'REST':
        #print("inside rest if")
        if destinationArn[-2:] == ':*' :
            destinationArn = destinationArn[:-2]
        print(destinationArn)
        params = {
            'restApiId': api_id,
            'stageName': stage,
            'patchOperations': [
                {
                    'op': 'add',
                    'path': '/accessLogSettings/destinationArn',
                    'value': destinationArn
                },
                {
                    'op': 'add',
                    'path': '/accessLogSettings/format',
                    'value': '{"RequestId": "$context.requestId", "DomainName": "$context.domainName", "APIId": "$context.apiId", "RequestPath": "$context.path", "DomainPrefix": "$context.domainPrefix", "Stage": "$context.stage", "ResourcePath": "$context.resourcePath", "BasePathMatched": "$context.customDomain.basePathMatched", "Status": "$context.status"}'
                }
            ]
        }
        
        log_enable = apigateway_client.update_stage(**params)
        print("access:", log_enable)

    else :
        params_v2 = {
                'ApiId': api_id,
                'StageName': stage,
                'AccessLogSettings': {
                    'DestinationArn': destinationArn,
                    'Format': '{"RequestId": "$context.requestId", "DomainName": "$context.domainName", "APIId": "$context.apiId", "RequestPath": "$context.path", "DomainPrefix": "$context.domainPrefix", "Stage": "$context.stage", "ResourcePath": "$context.resourcePath", "BasePathMatched": "$context.customDomain.basePathMatched", "Status": "$context.status"}'
                }
            }
        log_enable = apigatewayv2_client.update_stage(**params_v2)
        print("access HTTP: ", log_enable)



#********************** HANDLER FUNCTION *************************************


def lambda_handler(event, context):
    # Initialize AWS clients
    apigateway_client = boto3.client('apigateway')
    apigatewayv2_client = boto3.client('apigatewayv2')
    cloudwatch_client = boto3.client('cloudwatch')
    cloudwatch_log_client = boto3.client('logs')
    # Define the CloudWatch Logs log group name
    log_group_name = '/aws/api-gateway/access-logs'

    # Create the log group if it doesn't exist
    log_group_arn = create_log_group(log_group_name)
    print("arn:",log_group_arn)
    arn=""
    # Find custom domain names using get-domain-names
    try:
        custom_domain_names_response = apigateway_client.get_domain_names()
        custom_domain_names = custom_domain_names_response['items']

        rest_api_ids = []
        http_api_ids = []

#The below code checks and creates two lists for rest api ids and http api ids

        for domain_name in custom_domain_names:
            domain_name_value = domain_name['domainName']
            print(f'Custom Domain Name: {domain_name_value}')

            # Find the API ID associated with the custom domain using get-base-path-mappings
            base_path_mappings = apigateway_client.get_base_path_mappings(
                domainName=domain_name_value
            )
            print("BPM :", base_path_mappings)
            if 'items' in base_path_mappings:
                for item in base_path_mappings['items']:
                    print("Item :", item)
                    api_id = item['restApiId']
                    stage = item['stage']
                    print(f'API ID associated with {domain_name_value}: {api_id}')

                    # Check if it is a REST API or HTTP API
                    try:
                        api_type_response = apigateway_client.get_rest_api(
                            restApiId=api_id
                        )
                        if 'name' in api_type_response:
                            rest_api_ids.append(api_id)
                            print(f'{api_id} is a REST API')
                            # Check if access logs are enabled, and if not, enable them
                            stage_settings = apigateway_client.get_stage(
                                restApiId=api_id,
                                stageName=stage
                            )
                            print("Stage settings:",stage_settings)
                            try:
                                destination_arn = stage_settings['accessLogSettings']['destinationArn']
                                enable_access_logs(api_id, 'REST', stage, destination_arn)
                                arn=destination_arn
                            except Exception as e:
                                #print("inside except of rest api")
                                enable_access_logs(api_id, 'REST', stage, log_group_arn)
                                #print("after except of rest api", res1)
                                arn=log_group_arn
                                
                    except Exception as e:
                        try:
                            api_type_response_v2 = apigatewayv2_client.get_api(
                                ApiId=api_id
                            )
                            if 'ApiEndpoint' in api_type_response_v2:
                                http_api_ids.append(api_id)
                                print(f'{api_id} is an HTTP API (v2)')
                                # Check if access logs are enabled, and if not, enable them
                                stage_settings_v2 = apigatewayv2_client.get_stage(
                                    ApiId=api_id,
                                    StageName=stage
                                )
                                try:
                                    destination_arn = stage_settings_v2['accessLogSettings']['destinationArn']
                                    enable_access_logs(api_id, 'HTTP', stage, destination_arn)
                                    arn=destination_arn
                                except Exception as e:
                                    enable_access_logs(api_id, 'HTTP', stage, log_group_arn)
                                    arn=log_group_arn
                                    
                        except apigatewayv2_client.exceptions.NotFoundException:
                            print(f'{api_id} is neither a REST API nor an HTTP API')
                    
                    
                    ## for 2xx metrics
                    filterPattern= '{$.Status = "200"}'
                    print(filterPattern)
                    
                    arn = str(arn)
                    print("init arn:",arn)
                    log_name=arn.split(':')[-1]
                    
                    if log_name == "*":
                        log_name=arn.split(':')[-2]
                    print("Final ARN :", log_name)
                    
                    response = cloudwatch_log_client.put_metric_filter(
                        logGroupName=log_name,
                        filterName='CountHTTP200',
                        filterPattern=filterPattern,
                        metricTransformations=[
                            {
                                'metricName': 'HTTP-200',
                                'metricNamespace': 'CDN_DASHBOARD',
                                'metricValue': '1',
                                'unit':'Count',
                                'dimensions': {
                                    'DomainName': '$.DomainName',
                                    'APIId': '$.APIId'
                                }
                            },
                        ]
                    )
                    time.sleep(0.2)
                    print(response)
                    
                    ##for 4xx metrics
                    filterPattern= '{ ($.Status = "4*") }'
                    print(filterPattern)
                    
                    arn = str(arn)
                    print("init arn:",arn)
                    log_name=arn.split(':')[-1]
                    
                    if log_name == "*":
                        log_name=arn.split(':')[-2]
                    print("Final ARN :", log_name)
                    
                    response = cloudwatch_log_client.put_metric_filter(
                        logGroupName=log_name,
                        filterName='CountHTTP4XX',
                        filterPattern=filterPattern,
                        metricTransformations=[
                            {
                                'metricName': 'HTTP-4XX',
                                'metricNamespace': 'CDN_DASHBOARD',
                                'metricValue': '1',
                                'unit':'Count',
                                'dimensions': {
                                    'DomainName': '$.DomainName',
                                    'APIId': '$.APIId'
                                }
                            },
                        ]
                    )
                    time.sleep(0.2)
                    print(response)
                    
                    ##for 5xx metrics
                    filterPattern= '{ ($.Status = "5*") }'
                    print(filterPattern)
                    
                    arn = str(arn)
                    print("init arn:",arn)
                    log_name=arn.split(':')[-1]
                    
                    if log_name == "*":
                        log_name=arn.split(':')[-2]
                    print("Final ARN :", log_name)
                    
                    response = cloudwatch_log_client.put_metric_filter(
                        logGroupName=log_name,
                        filterName='CountHTTP5XX',
                        filterPattern=filterPattern,
                        metricTransformations=[
                            {
                                'metricName': 'HTTP-5XX',
                                'metricNamespace': 'CDN_DASHBOARD',
                                'metricValue': '1',
                                'unit':'Count',
                                'dimensions': {
                                    'DomainName': '$.DomainName',
                                    'APIId': '$.APIId'
                                }
                            },
                        ]
                    )
                    time.sleep(0.2)
                    print(response)
                    
        print(rest_api_ids)
        print(http_api_ids)
        
        
        

        return {
            'statusCode': 200,
            'body': 'Custom domain names and associated API IDs found and categorized.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
