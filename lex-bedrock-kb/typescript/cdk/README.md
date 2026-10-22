# Amazon Lex bot answering from an Amazon Bedrock knowledge base on Amazon S3 Vectors

This pattern deploys an Amazon Lex V2 bot whose built-in `AMAZON.QnAIntent` answers questions from an Amazon Bedrock knowledge base. The knowledge base reads documents from an Amazon S3 bucket and keeps its vectors in an Amazon S3 Vectors index. You talk to the bot with the Lex runtime API. There is no AWS Lambda function in the request path.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Use a recent version, because the Amazon S3 Vectors and Amazon Lex V2 commands are new.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) installed and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`npx cdk bootstrap`)
* Access in the target Region to the two Amazon Bedrock models used by the stack (see [Models and Regions](#models-and-regions)).
* Permission for the identity that calls the bot to run `lex:RecognizeText` on the bot alias.

## Models and Regions

The stack takes the Region from your AWS CLI profile or the `AWS_REGION` environment variable. Nothing in the template is hardcoded to a Region.

* The default generation model is `amazon.nova-lite-v1:0` and the embedding model is `amazon.titan-embed-text-v2:0` (1024 dimensions). Both ids are constants at the top of `lib/lex-bedrock-kb-stack.ts` and can be overridden at deploy time with `-c generationModelId=<model-id>` and `-c embeddingModelId=<model-id>`. If you change the embedding model, also change `EMBEDDING_DIMENSIONS` so that it matches the model output size. The embedding settings of the knowledge base (`embeddingDataType` and `dimensions`) are written for Titan Text Embeddings V2, so another model can need more changes in `lib/lex-bedrock-kb-stack.ts`.
* The pattern was deployed and tested in **us-east-1** and **us-west-2**. In both, the Lex locale built with `amazon.nova-lite-v1:0` as the QnA model and the bot answered from the knowledge base. I could not find a list of the models that `AMAZON.QnAIntent` accepts in the Amazon Lex documentation, so other Regions and other models are not covered by that result. If the bot fails to build with a model error, open any Lex bot in the console, add the `AMAZON.QnAIntent`, pick a model from its model list and pass that model with `-c generationModelId=<model-id>`.
* The Amazon Lex V2 API documents the `ModelArn` of the QnA intent model as a foundation model ARN (`arn:aws:bedrock:<region>::foundation-model/<model-id>`), so the generation model is expected to be invocable in the deployment Region without a cross-Region inference profile. In eu-central-1, `aws bedrock list-foundation-models` lists Nova Lite with the inference type `INFERENCE_PROFILE` only (no on-demand), so in that Region choose another model that is invocable in-Region and offered for the Lex QnA intent. The pattern was not deployed in eu-central-1.
* Before you deploy in another Region, check that Amazon Lex V2, Amazon Bedrock Knowledge Bases, Amazon S3 Vectors and both models are available there. Models are retired over time, so check the [Amazon Bedrock model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html) page and the model list of the Lex QnA intent before you reuse an id.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lex-bedrock-kb/typescript/cdk
    ```
1. Install the dependencies:
    ```
    npm install
    ```
1. Bootstrap the account and Region if you have not done so before:
    ```
    npx cdk bootstrap
    ```
1. Deploy the stack:
    ```
    npx cdk deploy
    ```
    To use another generation model, add `-c generationModelId=<model-id>`.
1. Note the outputs from the deployment: the documents bucket name, the knowledge base ID, the data source ID, the bot ID, the locale ID and the generation model ID. They are used for testing.

## How it works

The stack creates the following resources:

* **Amazon S3**: a private bucket for the source documents (block public access, S3-managed encryption, TLS required, `DESTROY` removal policy with `autoDeleteObjects`). The `autoDeleteObjects` option adds a small CDK helper function that empties the bucket when the stack is deleted. It is not part of the request path.
* **Amazon S3 Vectors**: a vector bucket and a vector index (`float32`, 1024 dimensions, cosine distance). The index marks `AMAZON_BEDROCK_TEXT` and `AMAZON_BEDROCK_METADATA` as non-filterable metadata keys, as the Amazon Bedrock documentation asks for. Names are generated by AWS CloudFormation.
* **Amazon Bedrock**: a knowledge base with the `S3_VECTORS` storage type that points at the index, and an Amazon S3 data source for the `docs/` prefix of the bucket. The data source uses the `RETAIN` data deletion policy so that deleting the stack does not depend on the vector store. The vectors are removed when CloudFormation deletes the index.
* **Amazon Lex V2**: a bot with an `en_US` locale that has two intents, `QnAIntent` (`AMAZON.QnAIntent`, configured with the generation model and the knowledge base ARN) and the `FallbackIntent`. Lex adds a `FallbackIntent` to every locale, and the template declares it explicitly. Lex routes an utterance to the QnA intent when no other intent matches it, and here there is no other intent. `autoBuildBotLocales` builds the locale during deployment, and you test the DRAFT version through the built-in `TSTALIASID` alias, so no bot version or alias is created.
* **AWS IAM**: two roles. The knowledge base role can invoke the embedding model, list the bucket and read `docs/*` (with `aws:ResourceAccount`), and read, write, delete and query the one vector index. The Lex role can invoke the generation model and call `bedrock:Retrieve` on the one knowledge base. Both trust policies use `aws:SourceAccount` and `aws:SourceArn` conditions, and all ARNs use the stack partition and Region. The `aws:SourceArn` values are patterns for any knowledge base, bot or bot alias in the account and Region (`knowledge-base/*`, `bot/*`, `bot-alias/*`), because each role has to exist before the resource that assumes it. The Lex role has only these two actions, and the bot answered questions in the tests with no others. If a question returns an access error, look in AWS CloudTrail for the denied action before you widen the role.

The data flow has three links:

1. **Ingestion** (S3 to the knowledge base to S3 Vectors): you copy documents to the bucket and start an ingestion job. The knowledge base chunks the documents, embeds the chunks with the embedding model and writes the vectors to the index.
1. **Retrieval** (Lex to the knowledge base): when a user asks a question, `QnAIntent` calls the knowledge base to retrieve the matching passages.
1. **Answer** (Lex to the foundation model): Lex sends the passages and the question to the generation model and returns the generated answer.

If you remove the knowledge base, `QnAIntent` has no knowledge store to answer from. If you remove Lex, there is no conversational front end and no model step, only a searchable index. The existing S3 Vectors patterns in this repository call S3 Vectors from AWS Lambda; this one wires the knowledge base into Amazon Lex natively.

The ingestion job is deliberately a documented CLI step and not a custom resource. A knowledge base without an ingestion job returns no passages, so run the job before you test the bot.

### Exposure

The bot has no public endpoint. Callers need AWS credentials with `lex:RecognizeText` on the bot alias. The documents bucket blocks public access and denies requests without TLS. The vector bucket has no resource policy, so only IAM principals of the account can use it. The stack creates no API, load balancer or security group.

### Cost and logs

The stack has no resource that bills by the hour (no OpenSearch Serverless collection, no provisioned capacity and no NAT gateway). You pay for what you use: Amazon S3 storage and requests, Amazon S3 Vectors storage and queries, embedding tokens during ingestion, generation tokens and Lex text requests for each question. See the pricing pages of the services for current rates.

The stack defines no log groups and does not turn on Lex conversation logs. The CDK helper function that empties the documents bucket on delete writes to an Amazon CloudWatch Logs log group that AWS Lambda creates when the function first runs. CloudFormation does not manage that log group, so it has no retention setting and `cdk destroy` does not remove it. The Cleanup section shows how to delete it. Ingestion status is read with `aws bedrock-agent get-ingestion-job`. The stack outputs list the identifiers you need for testing.

## Testing

All commands run from the pattern directory. They assume the stack name `LexBedrockKbStack` and the AWS Region that you deployed to.

1. Read the stack outputs into variables:
    ```bash
    STACK=LexBedrockKbStack
    out() { aws cloudformation describe-stacks --stack-name $STACK --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    BUCKET=$(out DocsBucketName); KB_ID=$(out KnowledgeBaseId); DS_ID=$(out DataSourceId); BOT_ID=$(out BotId); LOCALE=$(out LocaleId)
    ```
1. Check that the bot locale is built.
    ```bash
    aws lexv2-models describe-bot-locale --bot-id $BOT_ID --bot-version DRAFT --locale-id $LOCALE --query botLocaleStatus --output text
    ```
    Expected output: `Built`. If the status is `Building`, wait a minute and run the command again. If it is `Failed`, run the command again without `--query` to read the failure reasons.
1. Enable the locale on the built-in test alias. On a new bot `TSTALIASID` has no language enabled, and `recognize-text` fails with `The BotAliasId TSTALIASID does not have Language en_US enabled.` Run this once. `--bot-version DRAFT` is required: without it the call fails with `The associated version cannot be null when updating TestBotAlias`.
    ```bash
    aws lexv2-models update-bot-alias --bot-id $BOT_ID --bot-alias-id TSTALIASID --bot-alias-name TestBotAlias \
      --bot-version DRAFT --bot-alias-locale-settings "{\"$LOCALE\":{\"enabled\":true}}"
    ```
1. Copy the sample documents to the bucket:
    ```bash
    aws s3 cp sample-docs/ s3://$BUCKET/docs/ --recursive
    ```
1. Start the ingestion job and wait for it to finish:
    ```bash
    JOB=$(aws bedrock-agent start-ingestion-job --knowledge-base-id $KB_ID --data-source-id $DS_ID --query ingestionJob.ingestionJobId --output text)
    aws bedrock-agent get-ingestion-job --knowledge-base-id $KB_ID --data-source-id $DS_ID --ingestion-job-id $JOB --query "ingestionJob.{status:status,statistics:statistics}"
    ```
    Repeat the second command until `status` is `COMPLETE`. Expected: `numberOfDocumentsScanned` is 3 and `numberOfDocumentsFailed` is 0.
1. Check that the knowledge base returns passages from the documents, without Lex and without the generation model:
    ```bash
    aws bedrock-agent-runtime retrieve --knowledge-base-id $KB_ID --retrieval-query text="return policy" \
      --query "retrievalResults[].content.text"
    ```
    Expected: a passage that contains `45 days`, taken from `sample-docs/returns-policy.md`. An empty list means the ingestion has not finished or has failed.
1. Ask a question that the documents answer:
    ```bash
    aws lexv2-runtime recognize-text --bot-id $BOT_ID --bot-alias-id TSTALIASID --locale-id $LOCALE \
      --session-id test-1 --text "How many days do I have to return an item?" \
      --query "{intent:sessionState.intent.name,answer:messages[].content}"
    ```
    Expected: `answer` holds a sentence that says returns are accepted within 45 days of delivery. The wording is generated by the model and differs between runs. `intent` was `null` for these answers in the tests (us-east-1 and us-west-2): Lex did not put the QnA intent in `sessionState.intent`, and `interpretations` listed only `FallbackIntent`, so use the answer text, not the intent name, to tell that the knowledge base answered.
1. Ask two more questions that the documents answer. Expected: free standard shipping from 80 dollars, and a 3-year warranty on tents and backpacks.
    ```bash
    aws lexv2-runtime recognize-text --bot-id $BOT_ID --bot-alias-id TSTALIASID --locale-id $LOCALE \
      --session-id test-1 --text "What is the order value for free shipping?" --query "messages[].content"
    aws lexv2-runtime recognize-text --bot-id $BOT_ID --bot-alias-id TSTALIASID --locale-id $LOCALE \
      --session-id test-1 --text "How long is the warranty on a tent?" --query "messages[].content"
    ```
1. Ask a question that the documents do not answer. Expected: `intent` is `FallbackIntent` and `answer` is `null`, because the reply has no message. The bot gives the same reply to any question while the knowledge base is empty, which is the case before the first ingestion job.
    ```bash
    aws lexv2-runtime recognize-text --bot-id $BOT_ID --bot-alias-id TSTALIASID --locale-id $LOCALE \
      --session-id test-2 --text "What is the capital of France?" --query "{intent:sessionState.intent.name,answer:messages[].content}"
    ```

If the bot cannot answer a question that the documents cover, work from the data to the model:

1. Run the `retrieve` command above. An empty list points at ingestion, so check that the ingestion job is `COMPLETE` and that `numberOfDocumentsFailed` is 0.
1. If `retrieve` returns the passage but Lex does not answer, check that the locale status is `Built`, that the locale is enabled on `TSTALIASID` (see the alias step above) and that the generation model is invocable in your Region (see [Models and Regions](#models-and-regions)).
1. If a call returns an access error, read the denied action in AWS CloudTrail.

## Cleanup

1. Delete the stack:
    ```bash
    npx cdk destroy
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'LexBedrockKbStack')].StackStatus"
    ```
    The output shows `DELETE_COMPLETE` for the stack.
1. Look for the log group of the CDK bucket-emptying helper function and delete it if it is listed. It has no retention setting:
    ```bash
    aws logs describe-log-groups --log-group-name-prefix /aws/lambda/LexBedrockKbStack- --query "logGroups[].logGroupName" --output text
    aws logs delete-log-group --log-group-name <log-group-name-from-the-previous-command>
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
