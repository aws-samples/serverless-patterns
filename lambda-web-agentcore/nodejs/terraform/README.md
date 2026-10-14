# Streaming AI agent chat app with AWS Lambda Web Functions and Amazon Bedrock AgentCore Runtime (Terraform)

This pattern deploys a fully serverless chat app for an AI agent. A Node.js web server running as an AWS Lambda Web Function serves the chat UI and calls a [Strands](https://strandsagents.com) agent hosted on Amazon Bedrock AgentCore Runtime. The agent's answer streams token by token from the model, through AgentCore Runtime and the Web Function, to the browser. Amazon CloudFront sits in front of the app as its single public URL.

Both compute services are serverless: they scale with traffic and scale to zero when idle. Both bill for the CPU your code actually uses, not for CPU time spent waiting, and an AI workload spends most of its time waiting for the model. Memory is billed while an execution environment or session exists. See [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-agentcore-nodejs-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

![Architecture diagram: the browser calls Amazon CloudFront, which forwards to an AWS Lambda Web Function, which invokes a Strands agent on Amazon Bedrock AgentCore Runtime, which calls Claude Sonnet 5.5 on Amazon Bedrock. The answer streams back token by token along the same path.](images/architecture.png)

1. The browser loads the chat UI from Amazon CloudFront and posts each message to `/api/chat`, together with a session ID that the tab generates once.
1. CloudFront forwards the request to the Lambda Web Function endpoint without caching it, and adds a secret `X-Origin-Verify` header.
1. The Web Function is a standard Express server. It rejects any request without the correct header with HTTP 403, so the endpoint cannot be used to bypass CloudFront. It then calls `InvokeAgentRuntime` for the session and pipes the server-sent events (SSE) that come back straight into the response.
1. AgentCore Runtime runs each session in its own isolated microVM. The Strands agent in it calls Claude Sonnet 5.5 on Amazon Bedrock with a streaming request and yields every chunk as soon as it arrives.
1. The chunks travel back along the same path, and the browser renders the Markdown as it streams.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The AWS Identity and Access Management (AWS IAM) user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured with credentials for the target account
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://developer.hashicorp.com/terraform/install) 1.6 or later
* [Node.js](https://nodejs.org/en/download/) 24 and npm, matching the `nodejs24.x` runtime. Terraform runs `npm install` to package the web app
* [uv](https://docs.astral.sh/uv/getting-started/installation/). Terraform uses it to download Linux arm64 wheels for the agent's dependencies, because AgentCore Runtime runs on arm64. No Docker is needed: the agent is deployed as a .zip file with [direct code deployment](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy-python.html)
* Access to Claude Sonnet 5.5 in Amazon Bedrock, in a Region that offers AWS Lambda Web Functions and Amazon Bedrock AgentCore Runtime. By default the agent uses the cross-Region inference profile for your Region's geography: `us.anthropic.claude-sonnet-5-5` in US Regions, `eu.anthropic.claude-sonnet-5-5` in Europe and `global.anthropic.claude-sonnet-5-5` elsewhere. Set the `model_id` variable to use a different profile. This pattern was tested in `us-east-1` and `eu-central-1`

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
1. Note the outputs. The `app_url` output is the address of the chat app:
    ```
    app_url = "https://d111111abcdef8.cloudfront.net/"
    ```

## How it works

### The web app

`webapp/index.js` is a plain Express server. A Web Function runs it as a long-lived process: the runtime passes the address to listen on in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable, and the server listens there as it would anywhere else. There is no handler function and no adapter. Because the process stays alive, the server can hold the `/api/chat` response open and write each SSE frame as it arrives from the agent.

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Chat UI (static HTML, CSS and JavaScript) |
| `POST` | `/api/chat` | Takes `{"prompt": "...", "sessionId": "<UUID>"}` and streams the agent's answer as server-sent events |

### The agent

`agent/main.py` is a Strands agent that the AgentCore Python SDK (`BedrockAgentCoreApp`) turns into the HTTP service AgentCore Runtime expects. Its entrypoint is an async generator, so every chunk that the agent yields is sent to the caller at once as an SSE frame.

AgentCore Runtime keeps each session in its own microVM for as long as the session is active. The web app sends one session ID per browser tab, so the agent object in that microVM holds one conversation: it remembers the earlier turns of the tab's conversation and nothing from anyone else's. Close the tab, or let the session go idle, and the conversation ends.

### The infrastructure

| File | What it creates |
|---|---|
| `main.tf` | Shared names, the model selection, and the versioned S3 bucket for both code packages |
| `agent.tf` | The agent package (built with uv), its execution role, and the AgentCore runtime |
| `webapp.tf` | The web app package (built with npm), its execution role, and the Web Function with its revision and endpoint |
| `cloudfront.tf` | The CloudFront distribution in front of the Web Function endpoint |

Notes on the choices in the templates:

* **No container image.** The agent is a .zip file in Amazon S3 that contains `main.py` and Linux arm64 wheels for its dependencies. AgentCore Runtime runs it on its managed Python 3.13 runtime, so there is no Dockerfile, no image build and no Amazon ECR repository.
* **Immutable revisions.** A Web Function revision is an immutable snapshot of code and configuration. When you change the web app and run `terraform apply` again, Terraform creates a new revision, moves the endpoint to it, and then deletes the old one (`create_before_destroy`), so the app keeps serving during the change.
* **Least privilege.** The web app's role can invoke only this agent runtime and write only its own logs. The agent's role can invoke the model only through the configured inference profile.
* **Streaming through CloudFront.** The distribution uses the managed `CachingDisabled` cache policy and turns compression off, so every SSE frame reaches the browser as soon as the Web Function writes it.
* **A request timeout for long answers.** A streamed response lasts as long as the Web Function's request timeout, so the revision sets `timeout_seconds = 300`.

## Testing

1. Open the `app_url` output in a browser and ask the agent something. The answer appears word by word as the model generates it. Ask a follow-up question, for example "Can you say that more briefly?", to see that the agent remembers the conversation. A new tab starts a new conversation.

1. Call the chat API through CloudFront from a terminal. Set `APP_URL` to the `app_url` output first. The `-N` flag turns off output buffering, so you see each frame as it arrives:
    ```bash
    APP_URL=$(terraform output -raw app_url)
    curl -N "${APP_URL}api/chat" \
      -H "Content-Type: application/json" \
      -d '{"prompt": "In one sentence, what is AWS Lambda?", "sessionId": "6f1c2a9e-1b2c-4d3e-8f4a-0123456789ab"}'
    ```
    The answer arrives as a series of SSE frames, for example:
    ```
    data: {"type": "chunk", "data": "AWS Lambda is"}

    data: {"type": "chunk", "data": " a serverless comp"}

    data: {"type": "chunk", "data": "ute service that run"}
    ```

1. Confirm that the Web Function endpoint cannot be called directly, bypassing CloudFront:
    ```bash
    curl -i "$(terraform output -raw web_function_endpoint_url)api/chat" \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Hello", "sessionId": "6f1c2a9e-1b2c-4d3e-8f4a-0123456789ab"}'
    ```
    The response has status code `403` and the body `{"error":"Forbidden. Use the CloudFront URL."}`.

1. Read the web app logs. Replace `us-east-1` with the Region you deployed to. The server logs when it starts and when an agent call fails, and Lambda adds a platform record for each execution environment. New log events can take a minute to appear:
    ```bash
    aws logs tail "/aws/lambda/web/$(terraform output -raw web_function_name)" --region us-east-1 --since 10m
    ```

## Security considerations

This pattern is a starting point. Before you put it in front of real users, review the following:

* **There is no sign-in.** Anyone who has the CloudFront URL can chat with the agent, and every message invokes the model in your account. The endpoint's `rate_limit` (100 requests per second by default) and `max_environments` (2 by default) variables cap the traffic it accepts. To restrict access, add authentication, for example with Amazon Cognito, and attach AWS WAF with a rate-based rule to the CloudFront distribution. See [Lambda Web Function endpoint access control](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) and [Using AWS WAF to control access to your content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html).
* **The origin header is a shared secret.** Terraform generates it and stores it in the Terraform state and in the Web Function revision's environment variables. Protect the state file, for example with an encrypted remote backend. Run `terraform apply -replace=random_password.origin_verify` to rotate it.
* **Sessions are per browser tab.** The session ID only separates conversations. It is not an identity, so do not use it to authorize access to user data.

## Cleanup

1. Delete all the resources that Terraform created. Use the same Region you deployed to:
    ```bash
    terraform destroy -var "aws_region=us-east-1"
    ```
    Enter `yes` when Terraform asks you to confirm. Deleting the CloudFront distribution takes a few minutes.
1. Confirm that the resources have been deleted. The command prints an empty list:
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
