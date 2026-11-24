# Roll out Amazon Bedrock model settings with AWS AppConfig and AWS Lambda

This pattern keeps the Amazon Bedrock model ID, inference parameters and system prompt in an AWS AppConfig AI model invocation configuration profile (type `AWS.AppConfig.AIModelInvocation`). An AWS Lambda function reads the deployed configuration through the AWS AppConfig Agent Lambda extension and maps it onto an Amazon Bedrock Converse request. A model or prompt change is a configuration deployment with a gradual strategy, and an Amazon CloudWatch alarm on the function's errors makes AWS AppConfig roll a bad change back automatically.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appconfig-ai-model-lambda-bedrock-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. The stack has no resources that bill per hour: the CloudWatch alarm is billed per alarm per month while it exists, Amazon Bedrock bills per token, AWS AppConfig bills per configuration request received, AWS Lambda bills per request and duration, and Amazon CloudWatch Logs bills per GB ingested and stored. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html), with your account and Region bootstrapped (`npx cdk bootstrap`). The commands below use `npx cdk`, which runs the CDK CLI version this project installs, so no global install is needed.
* Access to Amazon Nova 2 Lite and Amazon Nova Micro in [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in your Region

## Supported Regions

The stack supports us-east-1, us-east-2, us-west-2, eu-central-1, eu-north-1, eu-west-1 and eu-west-3, and `cdk synth` stops with an error in any other Region. These are source Regions of the `us.` and `eu.` geo inference profiles on the [Nova 2 Lite](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html) and [Nova Micro](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-micro.html) model cards, and the stack maps each one to the arm64 layer ARN of the AWS AppConfig Agent Lambda extension from the [extension versions page](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html). Both tables are in `lib/appconfig-ai-model-lambda-bedrock-stack.ts`.

## How it works

1. Each hosted version of the profile is a JSON document with `schemaVersion`, `model`, `inferenceParameters` and `messages`. AWS AppConfig checks it against the [AI model invocation schema](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-ai-model-configuration.html) when the version is created: out-of-range inference parameters, a missing `schemaVersion` and a message without `role` are rejected. In our tests a document without `model` was accepted; calls with such a version fail as function errors, so the alarm rolls it back like any other bad version. The stack creates version 1 (Nova 2 Lite, temperature 0.2, a two-sentence system prompt) and deploys it at once.
2. The function calls the agent on `localhost:2772`, sends the `system` messages as `system`, the other messages as earlier turns, `inferenceParameters` as `inferenceConfig` and `customParameters` (when present) as `additionalModelRequestFields`, then appends the caller's prompt. It returns the model, the inference parameters and the answer.
3. Later versions are deployed with the rollout strategy: 50 percent of the targets, then 100 percent, over 4 minutes, then a 5 minute bake time. The percentage applies to the clients that poll AWS AppConfig (each execution environment runs its own agent), not to individual requests.
4. The environment monitors the alarm. If it goes to `ALARM` (or `INSUFFICIENT_DATA`) during the deployment or the bake time, AWS AppConfig rolls back to the previous version and the deployment ends in `ROLLED_BACK`.
5. The function role may invoke only the two Nova models (inference profile and destination Region model ARNs), so the AWS Identity and Access Management (IAM) policy is the list of models a configuration can switch to. Any other model fails with `AccessDeniedException`, which is a function error.

## Important Notes

* This pattern uses the AI model invocation profile only. To version prompts separately from the model settings, AWS AppConfig also has [AI prompt configuration profiles](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-ai-prompt-configuration.html).
* The profile is an L1 `CfnConfigurationProfile` because the aws-cdk-lib `ConfigurationType` enum has no AI model invocation value. Hosted versions here use the content type `application/json; type=AWS.AppConfig.AIModelInvocation`: AWS CloudFormation rejects plain `application/json` for this profile type, although the user guide CLI example shows plain `application/json`.
* An invalid prompt is answered with an `error` field instead of an exception, so caller mistakes cannot roll back a configuration. A failed Converse call is rethrown.
* The environment and profile set `DeletionProtectionCheck` to `BYPASS` so `cdk destroy` works right after a test. Remove it for long-lived environments.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/appconfig-ai-model-lambda-bedrock/typescript/cdk
    ```

2. Install dependencies and type-check:
    ```bash
    npm install
    npm run build
    ```

3. If the account and Region have never been used with the AWS CDK, bootstrap them once:
    ```bash
    npx cdk bootstrap
    ```

4. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

5. Note the stack outputs: `FunctionName`, `LogGroupName`, `ApplicationId`, `EnvironmentId`, `ConfigurationProfileId`, `RolloutStrategyId`, `AlarmName` and `GeoPrefix`.

## Testing

Use the AWS CLI configured for the Region you deployed to. Start every new shell with these variables and helpers:

```bash
STACK=AppconfigAiModelLambdaBedrockStack
out() { aws cloudformation describe-stacks --stack-name "$STACK" --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
FN=$(out FunctionName); APP=$(out ApplicationId); ENV=$(out EnvironmentId); CFG=$(out ConfigurationProfileId)
ROLLOUT=$(out RolloutStrategyId); ALARM=$(out AlarmName); GEO=$(out GeoPrefix)
ask() { aws lambda invoke --function-name "$FN" --cli-binary-format raw-in-base64-out --payload "{\"prompt\":\"$1\"}" /tmp/answer.json >/dev/null; cat /tmp/answer.json; echo; }
new_version() { aws appconfig create-hosted-configuration-version --application-id "$APP" --configuration-profile-id "$CFG" --content-type 'application/json; type=AWS.AppConfig.AIModelInvocation' --content "fileb://$1" --query VersionNumber --output text /tmp/version-out.json; }
wait_alarm_ok() { until [ "$(aws cloudwatch describe-alarms --alarm-names "$ALARM" --query 'MetricAlarms[0].StateValue' --output text)" = OK ]; do sleep 15; done; }
deploy() { wait_alarm_ok; aws appconfig start-deployment --application-id "$APP" --environment-id "$ENV" --configuration-profile-id "$CFG" --deployment-strategy-id "$ROLLOUT" --configuration-version "$1" --query DeploymentNumber --output text; }
watch_deployment() { [ -n "$1" ] || { echo "no deployment number"; return 1; }; while true; do S=$(aws appconfig get-deployment --application-id "$APP" --environment-id "$ENV" --deployment-number "$1" --query '[State,PercentageComplete]' --output text); echo "$(date -u +%H:%M:%S) $S"; ask "Name one AWS Region in Europe."; case "$S" in COMPLETE*|ROLLED_BACK*|REVERTED*) break ;; esac; sleep 20; done; }
```

1. Ask a question. Expected: a JSON object with `model` set to `us.amazon.nova-2-lite-v1:0` (or `eu.` in Europe), `temperature` 0.2 and an answer of at most two sentences.
    ```bash
    ask "What does AWS AppConfig do?"
    ```

2. Create version 2, which switches to Nova Micro with a one-sentence prompt, and roll it out. `deploy` first waits until the alarm is `OK`: a new alarm stays `INSUFFICIENT_DATA` for a few minutes after the stack is created, and AWS AppConfig rolls back a deployment that starts in that state (our first test did, within 24 seconds). The helper then prints the deployment state and an answer every 20 seconds until the deployment ends (about 9 minutes). Expected: the `model` in the answers changes to the Nova Micro profile during the rollout, and the last state is `COMPLETE 100.0`.
    ```bash
    printf '{"schemaVersion":"1","model":"%s.amazon.nova-micro-v1:0","inferenceParameters":{"temperature":0.5,"maxTokens":200},"messages":[{"role":"system","content":"Answer in one sentence."}]}' "$GEO" > /tmp/model-v2.json
    V2=$(new_version /tmp/model-v2.json); echo "version $V2"
    watch_deployment "$(deploy "$V2")"
    ```

3. Schema validation. A document with `topP` above 1 is rejected when it is created. Expected: `BadRequestException ... Configuration content did not adhere to json schema: [message: "numeric instance is greater than the required maximum (maximum: 1, found: 2)" - parent node: /inferenceParameters/topP]`, and no version is created.
    ```bash
    echo '{"schemaVersion":"1","model":"any","inferenceParameters":{"topP":2}}' > /tmp/model-invalid.json
    new_version /tmp/model-invalid.json
    ```

4. Automatic rollback. Version 3 passes the schema but names a model the function role may not invoke. `deploy` waits until the alarm is `OK` again, then rolls the version out. Expected: answers turn into `"errorType":"AccessDeniedException"` once the execution environment receives version 3, the alarm goes to `ALARM` and the state reaches `ROLLED_BACK`. The last answer of the loop can still be an error, because the agent polls every 15 seconds; the `ask` about 20 seconds later is answered by the Nova Micro profile (version 2) again.
    ```bash
    printf '{"schemaVersion":"1","model":"%s.amazon.nova-pro-v1:0","messages":[{"role":"system","content":"Answer in one sentence."}]}' "$GEO" > /tmp/model-v3.json
    V3=$(new_version /tmp/model-v3.json); DEP=$(deploy "$V3"); watch_deployment "$DEP"
    sleep 20; ask "Name one AWS Region in Europe."
    aws appconfig get-deployment --application-id "$APP" --environment-id "$ENV" --deployment-number "$DEP" --query 'EventLog[].[EventType,TriggeredBy]' --output text
    ```
   Expected in the event log (newest first): `ROLLBACK_COMPLETED CLOUDWATCH_ALARM`, then `BAKE_TIME_STARTED` if the rollback came during the bake, `PERCENTAGE_UPDATED APPCONFIG` and `DEPLOYMENT_STARTED USER`. The test calls reach one execution environment, which receives version 3 either at 50 percent or at 100 percent: in our runs the first error came at 50 percent (twice in us-west-2) or during the bake (eu-central-1), and the rollback 1.5 to 2 minutes after the first error. The alarm returns to `OK` a few minutes after the errors stop; the next `deploy` waits for that. The function logs each failure: `aws logs tail "$(out LogGroupName)" --since 30m`.

## Cleanup

1. Make sure no deployment is still running (the last `watch_deployment` ended). In a new shell, paste the variable block from Testing first. Then delete the versions that the Testing section created:
    ```bash
    for v in $(aws appconfig list-hosted-configuration-versions --application-id "$APP" --configuration-profile-id "$CFG" --query 'Items[?VersionNumber>`1`].VersionNumber' --output text); do
      aws appconfig delete-hosted-configuration-version --application-id "$APP" --configuration-profile-id "$CFG" --version-number "$v"
    done
    ```

2. Delete the stack. This deletes the AWS AppConfig application with its environment, profile, version 1 and deployment strategies, the function, its log group with the logs, the alarm and the IAM roles:
    ```bash
    npx cdk destroy
    ```

3. Delete the local test files: `rm -f /tmp/answer.json /tmp/version-out.json /tmp/model-*.json`

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
