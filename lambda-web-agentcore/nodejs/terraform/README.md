# Streaming AI agent chat app with AWS Lambda Web Functions and Amazon Bedrock AgentCore Runtime (Terraform)

This pattern deploys a fully serverless chat app for an AI agent. A Node.js web server running as an AWS Lambda Web Function serves the chat UI and calls a [Strands](https://strandsagents.com) agent hosted on Amazon Bedrock AgentCore Runtime. The agent's answer streams token by token from the model, through AgentCore Runtime and the Web Function, to the browser. Amazon CloudFront sits in front of the app as its single public URL. A login secret, signed session tokens and caps on prompt length and answer tokens keep the public demo from being used as open access to the model.

Both compute services are serverless: they scale with traffic and scale to zero when idle. Both bill for the CPU your code actually uses, not for CPU time spent waiting, and an AI workload spends most of its time waiting for the model. Memory is billed while an execution environment or session exists. See [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

This pattern is based on the [Lambda Web Functions and AgentCore Runtime integration sample](https://github.com/aws-samples/sample-genai-strats/tree/main/agentcore/lambda-web-function-integration) by Anton Aleksandrov.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-agentcore-nodejs-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

![Architecture diagram: the browser calls Amazon CloudFront, which forwards to an AWS Lambda Web Function, which invokes a Strands agent on Amazon Bedrock AgentCore Runtime, which calls Claude Haiku 5.5 on Amazon Bedrock. The answer streams back token by token along the same path. The Web Function reads its login secret and signing key from AWS Secrets Manager.](images/architecture.png)

1. The browser loads the chat UI from Amazon CloudFront. The user enters the login secret, and the browser posts it to `/connect`, which returns a signed session token. The browser then posts each message to `/api/chat` with that token.
1. CloudFront forwards every request to the Lambda Web Function endpoint without caching it, and adds a secret `X-Origin-Verify` header.
1. The Web Function is a standard Express server. It rejects any request without the correct header with HTTP 403, so the endpoint cannot be used to bypass CloudFront. It checks the session token and the prompt length, then calls `InvokeAgentRuntime` for the session and pipes the server-sent events (SSE) that come back straight into the response. It reads the login secret and the token signing key from AWS Secrets Manager when it starts.
1. AgentCore Runtime runs each session in its own isolated microVM. The Strands agent in it calls Claude Haiku 5.5 on Amazon Bedrock with a streaming request and yields every chunk as soon as it arrives.
1. The chunks travel back along the same path, and the browser renders the Markdown as it streams.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The AWS Identity and Access Management (AWS IAM) user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured with credentials for the target account
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://developer.hashicorp.com/terraform/install) 1.6 or later
* [Node.js](https://nodejs.org/en/download/) 24 and npm, matching the `nodejs24.x` runtime. Terraform runs `npm install` to package the web app
* [uv](https://docs.astral.sh/uv/getting-started/installation/). Terraform uses it to download Linux arm64 wheels for the agent's dependencies, because AgentCore Runtime runs on arm64. No Docker is needed: the agent is deployed as a .zip file with [direct code deployment](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy-python.html)
* Access to Claude Haiku 5.5 in Amazon Bedrock, in a Region that offers AWS Lambda Web Functions and Amazon Bedrock AgentCore Runtime. By default the agent uses the cross-Region inference profile for your Region's geography: `us.anthropic.claude-haiku-5-5` in US Regions, `eu.anthropic.claude-haiku-5-5` in Europe and `global.anthropic.claude-haiku-5-5` elsewhere. Set the `model_id` variable to use a different profile. This pattern was tested in `us-east-1` and `eu-central-1`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-agentcore/nodejs/terraform
    ```
1. Initialize Terraform:
    ```
    terraform init
    ```
1. Deploy the pattern. Replace `us-east-1` with your Region if you want to deploy elsewhere:
    ```
    terraform apply -var "aws_region=us-east-1"
    ```
    Enter `yes` when Terraform asks you to confirm. Terraform packages both apps, uploads them to a versioned Amazon S3 bucket and creates the resources. The first deployment takes about 5 minutes, most of it for the CloudFront distribution.
1. Note the outputs. The `app_url` output is the address of the chat app, and `login_secret_arn` is the secret that holds its login secret:
    ```
    app_url = "https://d111111abcdef8.cloudfront.net/"
    ```

## How it works

### The web app

`webapp/index.js` is a plain Express server. A Web Function runs it as a long-lived process: the runtime passes the address to listen on in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable, and the server listens there as it would anywhere else. There is no handler function and no adapter. Because the process stays alive, the server can hold the `/api/chat` response open and write each SSE frame as it arrives from the agent.

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Chat UI (static HTML, CSS and JavaScript) |
| `POST` | `/connect` | Takes `{"secret": "<login secret>"}` and returns `{"sessionToken": "..."}`, or HTTP 401 for a wrong secret |
| `POST` | `/api/chat` | Takes `{"prompt": "..."}` with the `X-Session-Token` header and streams the agent's answer as server-sent events. Returns HTTP 401 without a valid token and HTTP 400 for a prompt over 100 characters |

### Sign-in and sessions

Terraform generates a random login secret and a token signing key and stores both in AWS Secrets Manager. The web app reads them once, when an execution environment starts.

The browser sends the login secret only to `/connect`. The server picks a new random session ID, signs it with HMAC-SHA256 and returns `<session ID>.<signature>` as the session token. The browser keeps the token in memory and sends it with every chat request, and the server checks the signature before it uses the session ID. A browser cannot choose or guess the session ID of another conversation, and reloading the page signs in again and starts a new conversation.

### The agent

`agent/main.py` is a Strands agent that the AgentCore Python SDK (`BedrockAgentCoreApp`) turns into the HTTP service AgentCore Runtime expects. Its entrypoint is an async generator, so every chunk that the agent yields is sent to the caller at once as an SSE frame.

AgentCore Runtime keeps each session in its own microVM for as long as the session is active. Each sign-in gets its own session, so the agent object in that microVM holds one conversation: it remembers the earlier turns of that conversation and nothing from anyone else's. The Strands `SlidingWindowConversationManager` sends only the last 10 messages (5 turns) to the model, so a long conversation does not keep growing the input tokens. Reload the page, or let the session go idle, and the conversation ends.

Each answer is capped at 200 output tokens (`max_tokens` on the Strands `BedrockModel`). Thinking tokens count against that cap, so the agent turns thinking off (`"thinking": {"type": "disabled"}`). Otherwise Claude Haiku 5.5 can spend the whole budget thinking about a longer question and return no answer. When an answer reaches the cap, Strands keeps the partial answer in the conversation and raises `MaxTokensReachedException`. The agent then sends any text that was not streamed yet and a note that the answer was cut off.

### The infrastructure

| File | What it creates |
|---|---|
| `main.tf` | Shared names, the model selection, and the versioned S3 bucket for both code packages |
| `agent.tf` | The agent package (built with uv), its execution role, and the AgentCore runtime |
| `secrets.tf` | The login secret and the session token signing key in AWS Secrets Manager |
| `webapp.tf` | The web app package (built with npm), its execution role, and the Web Function with its revision and endpoint |
| `cloudfront.tf` | The CloudFront distribution in front of the Web Function endpoint |

You can set these variables with `-var` on `terraform apply`:

| Variable | Default | Description |
|---|---|---|
| `aws_region` | `us-east-1` | Region to deploy to |
| `model_id` | empty | Amazon Bedrock inference profile for the agent. Empty picks Claude Haiku 5.5 for the Region's geography |
| `rate_limit` | `100` | Requests per second the Web Function endpoint accepts before it returns HTTP 429 |
| `max_environments` | `2` | Maximum number of Web Function execution environments |
| `log_retention_days` | `7` | Days to keep the Web Function and agent logs |

Notes on the choices in the templates:

* **No container image.** The agent is a .zip file in Amazon S3 that contains `main.py` and Linux arm64 wheels for its dependencies. AgentCore Runtime runs it on its managed Python 3.13 runtime, so there is no Dockerfile, no image build and no Amazon ECR repository.
* **Immutable revisions.** A Web Function revision is an immutable snapshot of code and configuration. When you change the web app and run `terraform apply` again, Terraform creates a new revision, moves the endpoint to it, and then deletes the old one (`create_before_destroy`), so the app keeps serving during the change.
* **Least privilege.** The web app's role can invoke only this agent runtime, read only its two secrets and write only its own logs. The agent's role can invoke the model only through the configured inference profile.
* **Streaming through CloudFront.** The distribution uses the managed `CachingDisabled` cache policy and turns compression off, so every SSE frame reaches the browser as soon as the Web Function writes it.
* **A request timeout for long answers.** A streamed response lasts as long as the Web Function's request timeout, so the revision sets `timeout_seconds = 300`.

## Testing

1. Print the login secret. Replace `us-east-1` with the Region you deployed to:
    ```bash
    aws secretsmanager get-secret-value --secret-id "$(terraform output -raw login_secret_arn)" --region us-east-1 --query SecretString --output text
    ```

1. Open the `app_url` output in a browser and enter the login secret. Ask the agent something: the answer appears word by word as the model generates it. Ask a follow-up question, for example "Can you say that more briefly?", to see that the agent remembers the conversation. Reloading the page asks for the secret again and starts a new conversation.

1. Call the API through CloudFront from a terminal. First store the app URL and the login secret in shell variables. Replace `us-east-1` with the Region you deployed to:
    ```bash
    APP_URL=$(terraform output -raw app_url)
    ```
    ```bash
    LOGIN_SECRET=$(aws secretsmanager get-secret-value --secret-id "$(terraform output -raw login_secret_arn)" --region us-east-1 --query SecretString --output text)
    ```

1. Exchange the login secret for a session token, and print it:
    ```bash
    SESSION_TOKEN=$(curl -s "${APP_URL}connect" -H "Content-Type: application/json" -d "{\"secret\": \"${LOGIN_SECRET}\"}" | sed -E 's/.*"sessionToken":"([^"]*)".*/\1/')
    ```
    ```bash
    echo "$SESSION_TOKEN"
    ```
    The token is a session ID and a signature, for example `0b0e3f6a-5c1d-4f7e-9a2b-3c4d5e6f7a8b.Xy3...`. If you see a JSON error instead, check the login secret.

1. Send a prompt with the token. The `-N` flag turns off output buffering, so you see each frame as it arrives:
    ```bash
    curl -N "${APP_URL}api/chat" -H "Content-Type: application/json" -H "X-Session-Token: ${SESSION_TOKEN}" -d '{"prompt": "In one sentence, what is AWS Lambda?"}'
    ```
    The answer arrives as a series of SSE frames, for example:
    ```
    data: {"type": "chunk", "data": "AWS Lambda is"}

    data: {"type": "chunk", "data": " a serverless comp"}

    data: {"type": "chunk", "data": "ute service that run"}
    ```

1. Send a follow-up with the same token. The agent answers from the earlier turn:
    ```bash
    curl -N "${APP_URL}api/chat" -H "Content-Type: application/json" -H "X-Session-Token: ${SESSION_TOKEN}" -d '{"prompt": "Now say that in five words."}'
    ```

1. Confirm that a chat request without a session token is rejected:
    ```bash
    curl -i "${APP_URL}api/chat" -H "Content-Type: application/json" -d '{"prompt": "Hello"}'
    ```
    The response has status code `401` and the body `{"error":"Invalid or missing session token"}`.

1. Confirm that the Web Function endpoint cannot be called directly, bypassing CloudFront:
    ```bash
    curl -i "$(terraform output -raw web_function_endpoint_url)connect" -H "Content-Type: application/json" -d "{\"secret\": \"${LOGIN_SECRET}\"}"
    ```
    The response has status code `403` and the body `{"error":"Forbidden. Use the CloudFront URL."}`, even with the correct login secret.

1. Read the web app logs. Replace `us-east-1` with the Region you deployed to. The server logs when it starts and when an agent call fails, and Lambda adds a platform record for each execution environment. New log events can take a minute to appear:
    ```bash
    aws logs tail "/aws/lambda/web/$(terraform output -raw web_function_name)" --region us-east-1 --since 10m
    ```

## Security considerations

This pattern is a sample, not a production-ready deployment. Before you put it in front of real users, review the following:

* **The login secret is not user authentication.** Everyone who has the secret shares it, and it identifies no one. It keeps the demo from being open access to the model in your account. For real users, add authentication with Amazon Cognito or another identity provider, and attach AWS WAF with a rate-based rule to the CloudFront distribution. For an API with no web UI, set the endpoint's `auth_type` to `IamAuth`, so callers must sign requests with SigV4. See [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) and [Using AWS WAF to control access to your content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html).
* **Token use is capped.** Prompts are limited to 100 characters, answers to 200 output tokens, and the history sent to the model to the last 10 messages. The endpoint's `rate_limit` (100 requests per second by default) and `max_environments` (2 by default) variables cap the traffic it accepts.
* **Session tokens do not expire.** A token is valid until the signing key changes, which happens when the `random_password.session_signing_key` resource is replaced. A token only reaches its own conversation, and the conversation ends when the AgentCore session ends.
* **Secrets in the Terraform state.** Terraform generates the login secret, the signing key and the origin header, so all three are in the Terraform state. The origin header is also in the Web Function revision's environment variables. Protect the state file, for example with an encrypted remote backend.

## Cleanup

1. Delete all the resources that Terraform created. Use the same Region you deployed to:
    ```bash
    terraform destroy -var "aws_region=us-east-1"
    ```
    Enter `yes` when Terraform asks you to confirm. Deleting the CloudFront distribution takes a few minutes.
1. Confirm that the resources have been deleted. The command prints nothing:
    ```bash
    terraform state list
    ```
1. Delete the local build files and Terraform working directory:
    ```bash
    rm -rf build .terraform webapp/node_modules
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
