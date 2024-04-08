# Lambda event filtering using event source mapping for Amazon Managed Streaming for Apache Kafka (Amazon MSK)

AWS Lambda provides [content filtering options for Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-msk-smak) and other services. With event pattern content filtering, you can write complex rules so that your Lambda function is only triggered under filtering criteria you specify. This helps reduce traffic to your Lambda functions, simplifies code, and reduces overall cost.


This project includes a SAM template deploys multiple lambda functions. Each of the lambda function uses different filter criteria. We validate the expected behaviour by publishing different messages to a MSK topic, and verifying that the messages are present or absent in the corresponding function's Cloudwatch logs.

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Pre-requisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* An Amazon MSK cluster and a client machine that is configured to publish messages to a topic on that cluster. [Sample CloudFormation and instructions from Amazon MSK Labs](https://catalog.workshops.aws/msk-labs/en-US/msklambda/gsrschemareg/setup). 


## Deployment Instructions

The current project's SAM template does not create an MSK cluster. It creates lambda functions that are invoked when their mapped MSK topic recieves messages. The project relies on an existing MSK Cluster and a topic

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-esm-msk-filters-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file. Pass the MSK Cluster and Topic details as parameters to the SAM template:
    ```
    sam build
    sam deploy --stack-name lambda-msk-esm-stack --resolve-s3 --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset --parameter-overrides MSKStreamARN="ClusterARN" MSKTopicName="TopicName"
    ```

## Filtering scenarios
Each of the Lambda functions uses different [filter comparision operators](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) to demonstrate how to filter events based on the message body and metadata.


1. **No Filter** - A simple trigger without a filter criteria
    * Function name : 1-fn-esm-no-filter

2. **Equals** - A filter checking whether a particular **JSON** field value equals a string value. Filtering is based on the **message payload**.
    * Function name : 2-fn-filter-events
    
```
{
   "value":{
      "kind":[
         "Event"
      ]
   }
}
```

3. **Equals and Numeric (equals)** - A filter checking whether a particular **JSON** field value equals a string value and a different JSON field value equals a numeric value. Filtering is based on the **message payload**.
    * Function name : 3-fn-filter-events-and-response-code
    
```
{
   "value":{
      "kind":[
         "Event"
      ],
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  "=",
                  300
               ]
            }
         ]
      }
   }
}
```

4. **Numeric (range)** and **Equals**- Multiple filters pattern. One pattern filters by 'Numeric (range) operator'. Another pattern filters by 'Equals' operator. Filtering is based on the **message payload**.
    * Function name : 4-fn-filter-multiple-patterns
    
```
{
   "value":{
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  ">=",
                  300
               ]
            }
         ]
      }
   }
}
```
```
{
   "value":{
      "RBAC":[
         true
      ]
   }
}
```

5. **Not** - A filter checking whether a particular **JSON** field value is not equal to a string. Filtering is based on the **message payload**.
    * Function name : 5-fn-filter-not-event-kind
    
```
{
   "value":{
      "kind":[
         {
            "anything-but":[
               "Event"
            ]
         }
      ]
   }
}
```

6. **Begins with** - A filter checking whether a particular **JSON** field value begins with a string. Filtering is based on the **message payload**.
    * Function name : 6-fn-filter-starts-with
    
```
{
   "value":{
      "region":[
         {
            "prefix":"us-"
         }
      ]
   }
}
```

7. **Numeric (range)** - A filter checking whether a particular **JSON** field value is within a numeric range. Filtering is based on the **message payload**.
    * Function name : 7-fn-filter-between-inclusive
    
```
{
   "value":{
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  ">=",
                  300,
                  "<=",
                  350
               ]
            }
         ]
      }
   }
}
```


8. **Begins with** - A filter checking whether a particular **plain** string value is begins with a string. Filtering is based on 
the **message payload**.
    * Function name : 8-fn-filter-on-plain-string

```
{
   "value":[
      {
         "prefix":"OrderNumber"
      }
   ]
}
```

9. **Begins with** - A filter checking whether a particular **plain** string value is begins with a string. Filtering is based on the **message payload** and **message metadata**.
    * Function name : 9-fn-filter-on-plain-string-metadata

```
{
   "topic":[
      {
         "prefix":"ESMFiltersDemoTopic"
      }
   ],
   "value":{
      "region":[
         {
            "prefix":"us-"
         }
      ]
   }
}
```

## Sample events 
We use a mix of json and plain text messages to validate the functions are filtering events as expected.

1. **base-json.json**
```
{
    "fileNameForValidation": "base-json",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

2. **code-is-300.json**
```
{
    "fileNameForValidation": "code-is-300",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":300
    }
}
```

3. **custom-with-region.json**
```
{
    "fileNameForValidation": "custom-with-region",
    "kind": "Custom",
    "region": "us-east-1",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

4. **rbac-is-set.json**
```
{
    "fileNameForValidation": "rbac-is-set",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": true,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

5. **plain-string.txt**
```
OrderNumber:12345
```

## Testing

We validate the ESM filters by publishing each of the event messages(base-json.jon, code-is-300.json, custom-with-region.json, rbac-is-set.json, plain-string.txt) to the topic that the functions are mapped to.

Login to the client machine in the bastion environment that is configured to publish messages to the topic and run these commands.

```
#setting broker info
export BOOTSTRAP_SERVERS_CONFIG="enter cluster's bootstrap brokers"
#Instructions - https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html
#Sample server config
#export BOOTSTRAP_SERVERS_CONFIG="b-1.mskclustermsk.abcdef.c14.kafka.us-east-1.amazonaws.com:9092,b-3.mskclustermsk.abcdef.c14.kafka.us-east-1.amazonaws.com:9092,b-2.mskclustermsk.abcdef.c14.kafka.us-east-1.amazonaws.com:9092"

#Create topic if one does not exist
/home/ec2-user/kafka/bin/kafka-topics.sh --create --topic "enter topic name" --bootstrap-server $BOOTSTRAP_SERVERS_CONFIG

#set topic name
export ESMFiltersDemoTopic="enter topic name"

#get sample messages from repository
mkdir test-msk-esm
cd test-msk-esm/
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/lambda-esm-msk-filters-sam/events/

#publish messages to topic
jq -rc . base-json.json | /home/ec2-user/kafka/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVERS_CONFIG --topic $ESMFiltersDemoTopic
jq -rc . code-is-300.json | /home/ec2-user/kafka/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVERS_CONFIG --topic $ESMFiltersDemoTopic
jq -rc . custom-with-region.json | /home/ec2-user/kafka/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVERS_CONFIG --topic $ESMFiltersDemoTopic
jq -rc . rbac-is-set.json | /home/ec2-user/kafka/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVERS_CONFIG --topic $ESMFiltersDemoTopic
/home/ec2-user/kafka/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVERS_CONFIG --topic $ESMFiltersDemoTopic < plain-string.txt

```

Navigate to the CloudWatch log group for each of the lambda functions to validate which events appear in the logs, and which ones are missing. The ones that are missing were filtered out by the ESM filter that was applied to the function.

# Results

The below table captures the results from the above testing.

* Y - Message logged in CloudWatch logs. Event was passed by the Lambda resouce to the function as the filter criteria was met.
* N - Message not logged in CloudWatch logs. Event was filtered out by the Lambda resouce and event was discarded as the filter criteria was not met.

| Operators                                          | Filter Pattern                                                                                         | Function                             | base-json.json | code-is-300.json | custom-with-region.json | rbac-is-set.json | plain-string.txt |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------|----------------|------------------|-------------------------|------------------|------------------|
| None                                               | None                                                                                                   | 1-fn-esm-no-filter                   | Y              | Y                | Y                       | Y                | Y                |
| String Equals                                      | {"value":{"kind":["Event"]}}                                                                           | 2-fn-filter-events                   | Y              | Y                | N                       | Y                | N                |
| String Equals and Numeric   Equals(One pattern) | {"value":{"kind":["Event"],"responseStatus":{"code":[{"numeric":["=",300]}]}}}                         | 3-fn-filter-events-and-response-code | N              | Y                | N                       | N                | N                |
| String Equals and Numeric   range(Two patterns)      | {"value":{"responseStatus":{"code":[{"numeric":[">=",300]}]}}}      and      {"value":{"RBAC":[true]}} | 4-fn-filter-multiple-patterns        | N              | Y                | N                       | Y                | N                |
| Not                                                | {"value":{"kind":[{"anything-but":["Event"]}]}}                                                        | 5-fn-filter-not-event-kind           | N              | N                | Y                       | N                | N                |
| prefix                                             | {"value":{"region":[{"prefix":"us-"}]}}                                                                | 6-fn-filter-starts-with              | N              | N                | Y                       | N                | N                |
| Numeric range                                      | {"value":{"responseStatus":{"code":[{"numeric":[">=",300,"<=",350]}]}}}                                | 7-fn-filter-between-inclusive        | N              | Y                | N                       | N                | N                |
| prefix                                             | {"value":[{"prefix":"OrderNumber"}]}                                                                   | 8-fn-filter-on-plain-string          | N              | N                | N                       | N                | Y                |
| prefix                                             | {"topic":[{"prefix":"ESMFiltersDemoTopic"}],"value":[{"prefix":"Order"}]}                              | 9-fn-filter-on-plain-string-metadata | N              | N                | N                       | N                | Y                |



## Cleanup
 
1. Delete the ESM filter testing stack
    ```bash
    sam delete --stack-name lambda-msk-esm-stack
    ```
1. If you have created an MSK cluster and bastion environment using the sample instructions, delete the stack using corresponding [instructions](https://catalog.workshops.aws/msk-labs/en-US/msklambda/gsrschemareg/cleanup)
