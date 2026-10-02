# Serverless semantic cache for Amazon Bedrock using Amazon S3 Vectors

This pattern puts an AWS Lambda function in front of Amazon Bedrock and returns a cached answer whenever an incoming prompt is semantically similar to one that was already answered, so the large language model (LLM) call is skipped on repeats and near repeats. The cache lives in an Amazon S3 Vectors index: the prompt embedding is the vector and the answer is stored in the vector metadata, so there is no separate database and nothing is running when traffic stops.

This is different from the prompt caching that Amazon Bedrock offers natively. Native prompt caching reuses an exact prompt prefix, so a single changed character is a miss (see [Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)). This pattern matches on meaning instead, so "What is the capital of France?" and "Which city is the capital of France?" hit the same cache entry. The two features complement each other.

```
prompt --> [AWS Lambda] --embed-----> Amazon Bedrock (Amazon Titan Text Embeddings V2, 1024 dimensions)
                 |
                 |--search---------> Amazon S3 Vectors (cosine top 5; the answer is in the vector metadata)
                 |                      |-- HIT (similar enough, fresh, current epoch, same negation parity)
                 |                      |      --> return the cached answer, no LLM call
                 |                      |-- MISS
                 |--generate-------> Amazon Bedrock text model (writes the answer)
                 |--store----------> Amazon S3 Vectors (embedding + answer + model + created_at + epoch)
                 |--return
  (the force invalidation epoch is held in AWS Systems Manager Parameter Store)
```

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-semantic-cache-s3vectors-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Request access to the Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) used by this pattern, so that they are enabled in the Region you deploy to: the embeddings model `amazon.titan-embed-text-v2:0` and the text model `amazon.nova-lite-v1:0`
* A Region where both [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html) and Amazon Bedrock are available. This pattern was built and tested in `us-east-1`
* Python 3 available as `python3`. The Testing section uses it to print the JSON response returned by the function

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/bedrock-semantic-cache-s3vectors-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file. The function has no dependencies to install, so no build step is needed:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * **Stack Name**: enter a stack name, for example `semantic-cache`
    * **AWS Region**: enter the Region to deploy to, for example `us-east-1`
    * **Parameter VectorBucketName**: there is no default because an Amazon S3 Vectors bucket name must be unique in your account for that Region. Enter a free name, 3 to 63 characters, lowercase letters, numbers and hyphens only, for example `my-semantic-cache-01`
    * **Parameter VectorIndex [prompt-cache]**: press Enter to accept the default index name
    * **Parameter SimThreshold [0.85]**: press Enter to accept the default cosine similarity threshold for a cache hit
    * **Parameter TtlSeconds [86400]**: press Enter to accept the default freshness window of one day
    * **Parameter ApiKeyParameterName []**: press Enter to leave this blank. The function URL already requires AWS Identity and Access Management (IAM) authentication. Only fill this in if you first created the parameter described in "Optional: application level API key" below
    * **Parameter EmbedModel [amazon.titan-embed-text-v2:0]**: press Enter to accept the default embeddings model
    * **Parameter LlmModel [amazon.nova-lite-v1:0]**: press Enter to accept the default answer model
    * **Confirm changes before deploy**: enter `N`, or `Y` if you want to review the change set before it is executed
    * **Allow SAM CLI IAM role creation**: enter `Y`. The template creates the function execution role
    * **Disable rollback**: enter `N`
    * **Save arguments to configuration file**: enter `Y`
    * **SAM configuration file [samconfig.toml]**: press Enter
    * **SAM configuration environment [default]**: press Enter

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing. The Testing section uses the `FunctionName` and `LogGroupName` outputs.

## How it works

1. The Lambda function receives a prompt over an IAM signed function URL (auth type `AWS_IAM`, so every caller must be authorized by IAM and sign the request: see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html)) or over a direct `aws lambda invoke` call.
2. It embeds the prompt with Amazon Titan Text Embeddings V2, whose default output vector size is 1,024 dimensions, which is why the Amazon S3 Vectors index is created with `Dimension: 1024` and `DistanceMetric: cosine`.
3. It queries the Amazon S3 Vectors index for the 5 nearest stored prompts, asking for the distance and the metadata in the same call. Because the answer is kept in the metadata, one query returns both the match and the text to serve.
4. A candidate is served as a HIT only if all of these hold: cosine similarity (1 minus the returned distance) is at or above the threshold, the entry is younger than `TTL_SECONDS`, the entry carries the current cache epoch, and the candidate has the same negation parity as the incoming prompt.
5. On a MISS the function calls the Amazon Bedrock text model with the Converse API, stores the embedding plus the answer, model, timestamp and epoch in Amazon S3 Vectors, and returns the fresh answer.

Why each service is there:

* **Amazon Bedrock** is used twice: for embeddings (turning text into a vector so that matching is semantic) and for the answer on a miss.
* **Amazon S3 Vectors** is both the cache store and the similarity search, charged per use with nothing provisioned, which is what makes a serverless semantic cache practical.
* **AWS Lambda** is stateless glue. The cache lives entirely in Amazon S3 Vectors, so it survives cold starts, redeploys and execution environment recycling.
* **AWS Systems Manager Parameter Store** holds the cache epoch used for force invalidation, and optionally the application level API key as a SecureString.

Correctness controls:

* **Tunable similarity threshold**, cosine 0.85 by default, set per deployment with the `SimThreshold` parameter or per request with a `threshold` field.
* **Freshness time to live (TTL)**: entries older than `TTL_SECONDS` are treated as a miss.
* **Force invalidation**: bumping one epoch number makes every earlier entry miss immediately, with no deletes and no scanning. Useful after a data or policy change that cannot wait for the TTL.
* **Negation parity guard**: "is X" and "is NOT X" embed almost identically but mean the opposite, so a candidate whose negation parity differs from the prompt is rejected.
* **Top 5 and iterate**: a stale or invalidated near neighbour does not block a valid hit further down the list.

## Testing

1. Set a shell variable to the `FunctionName` output from the deployment, for example:
    ```
    FUNCTION=semantic-cache-SemanticCacheFunction-abc123DEF456
    ```
1. Send a prompt. This is the first time it is asked, so it is a MISS and the answer comes from the model:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"prompt\":\"What is the capital of France?\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    The first command prints the invoke result and the second prints the function response without the long answer text:
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'cached': False, 'similarity': None, 'epoch': '1', 'model': 'amazon.nova-lite-v1:0', 'latency_ms': 2509}
    response: The capital of France is Paris. Paris is not only the capital but also the large
    ```
    `latency_ms` and the wording of the answer vary from run to run.
1. Send the same prompt again. It is now a HIT, served from the cache with no model call:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"prompt\":\"What is the capital of France?\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'cached': True, 'similarity': 0.9996, 'epoch': '1', 'matched_prompt': 'What is the capital of France?', 'model': 'amazon.nova-lite-v1:0', 'latency_ms': 232}
    response: The capital of France is Paris. Paris is not only the capital but also the large
    ```
1. Ask the same question in different words. This is the semantic hit: the text does not match, the meaning does, and `matched_prompt` shows which entry was served:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"prompt\":\"Which city is the capital of France?\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'cached': True, 'similarity': 0.9854, 'epoch': '1', 'matched_prompt': 'What is the capital of France?', 'model': 'amazon.nova-lite-v1:0', 'latency_ms': 237}
    response: The capital of France is Paris. Paris is not only the capital but also the large
    ```
1. Negate the question. The wording is close enough to pass the similarity threshold, but the negation parity guard rejects the candidate, so this is a MISS and the model answers the question that was actually asked:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"prompt\":\"Which city is not the capital of France?\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'cached': False, 'similarity': None, 'epoch': '1', 'model': 'amazon.nova-lite-v1:0', 'latency_ms': 1264}
    response: To answer this question, it's important to know that the capital of France is Pa
    ```
1. Force invalidate the whole cache. This bumps the epoch held in AWS Systems Manager Parameter Store:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"action\":\"invalidate\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'invalidated': True, 'epoch': '2', 'note': 'all entries cached before this epoch now miss'}
    response: 
    ```
1. Ask the first question once more. Every entry cached under the previous epoch now misses, so the model answers again and the entry is re-cached under the new epoch. An execution environment that has not refreshed its cached epoch yet, which it does at most every 30 seconds, can still serve one hit:
    ```
    aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"body":"{\"prompt\":\"What is the capital of France?\"}"}' response.json
    python3 -c "import json;d=json.loads(json.load(open('response.json'))['body']);r=d.pop('response','');print(d);print('response:',r[:80])"
    ```
    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {'cached': False, 'similarity': None, 'epoch': '2', 'model': 'amazon.nova-lite-v1:0', 'latency_ms': 1144}
    response: The capital of France is Paris. Paris is not only the capital but also the large
    ```
1. To read the function logs, use the `LogGroupName` output. The stack owns this log group, so it is deleted with the stack:
    ```
    LOG_GROUP=semantic-cache-SemanticCacheLogGroup-abc123DEF456
    aws logs tail $LOG_GROUP --since 10m
    ```

In the runs above, a cache hit answered in roughly 190 to 280 ms while a miss took roughly 1.0 to 2.5 s, because the miss includes the model call. Your own figures will depend on the models, the Region and the prompt length.

## Tuning

| Setting | Where | Effect |
|---|---|---|
| Similarity threshold | `SimThreshold` parameter, `SIM_THRESHOLD` environment variable, or a `threshold` field in the request | Higher is stricter: fewer hits, less risk of serving a near miss |
| Freshness | `TtlSeconds` parameter, `TTL_SECONDS` environment variable | Maximum age of an answer that may be served |
| Force invalidation | `{"action":"invalidate"}` in the request body | Makes every earlier entry miss at once |
| Models | `EmbedModel` and `LlmModel` parameters | Swap the embeddings model or the answer model. A different embeddings model usually means a different vector size, which requires a new index |

## Optional: application level API key

The function URL already requires IAM authentication. If you also want an application level key checked against the `x-api-key` header, create the key as a SecureString parameter first and then pass only the parameter name to the stack. The value is read at runtime with decryption and is never placed in a Lambda environment variable.

```
aws ssm put-parameter --name /semantic-cache/api-key --value "your-secret-key" --type SecureString
```

Then deploy with `ApiKeyParameterName` set to `/semantic-cache/api-key` (the name must start with a forward slash), and send the header with each request:

```
aws lambda invoke --function-name $FUNCTION --cli-binary-format raw-in-base64-out --payload '{"headers":{"x-api-key":"your-secret-key"},"body":"{\"prompt\":\"What is the capital of France?\"}"}' response.json
```

A request with a missing or wrong key returns `{"statusCode": 401, ... "body": "{\"error\": \"unauthorized\"}"}`.

## Notes

* The function uses only the AWS SDK for Python (Boto3) that ships with the Python 3.13 managed runtime, so there is no `requirements.txt` and no build step.
* Amazon S3 Vectors allows up to 40 KB of metadata per vector, so a very long answer cannot be cached as metadata. See [Limitations and restrictions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html). The answer, prompt, model, timestamp and epoch are declared as non-filterable metadata keys so that they do not consume the smaller filterable metadata budget.
* Semantic caching serves an answer that was written for a similar prompt, not the same prompt. It suits FAQ and support assistants, documentation question answering and other repetitive traffic. It does not suit answers that must be exact, fresh or specific to one user unless you also namespace entries per user, invalidate aggressively or verify equivalence before serving.
* The negation parity guard covers negation words. It does not catch opposites such as "cheapest" and "most expensive". For high stakes content, raise the threshold or verify a borderline candidate before serving it.

## Cleanup

1. Delete the stack, which also deletes the Lambda function, its execution role, the log group, the epoch parameter, and the Amazon S3 Vectors index and vector bucket with the cached vectors in them:
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. If you created the optional API key parameter, delete it:
    ```bash
    aws ssm delete-parameter --name /semantic-cache/api-key
    ```
1. Delete the response file written by the Testing commands:
    ```bash
    rm response.json
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
