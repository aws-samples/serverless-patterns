# A preview URL for every pull request with AWS Lambda Web Functions (SAM)

This pattern gives every pull request in your GitHub repository its own live preview URL, the way hosting platforms such as Vercel and Netlify do, using a single AWS Lambda Web Function. A GitHub Actions workflow deploys each pull request to an endpoint named `pr-<number>`, comments the URL on the pull request, updates it on every push and deletes it when the pull request is closed. Production runs on its own `prod` endpoint and never serves pull request code.

It works because a Web Function can have up to 10 endpoints, each with its own HTTPS domain, and an endpoint whose auto-deployment mode is `Disabled` keeps serving the revision you point it at. Idle previews scale to zero, so open pull requests cost nothing while nobody looks at them.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-pr-previews-nodejs-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

![Architecture diagram: a pull request in GitHub triggers a GitHub Actions workflow, which assumes an AWS IAM role with OpenID Connect, uploads the code to a versioned Amazon S3 bucket and creates a revision and a pr-number endpoint on an AWS Lambda Web Function. The prod endpoint serves the production revision.](images/architecture.png)

1. A pull request is opened or updated. The `Preview` workflow assumes the `PreviewDeployRole` with GitHub OpenID Connect (OIDC), so the repository stores no AWS keys.
1. The workflow zips `src/`, uploads it to the versioned Amazon S3 bucket under `previews/`, and creates a Web Function revision that runs with the `PreviewExecutionRole`.
1. It points the `pr-<number>` endpoint at the new revision, creating the endpoint on the first push, and comments the endpoint URL on the pull request. Every later push updates the same endpoint, so the URL does not change.
1. When the pull request is closed, the workflow deletes the endpoint and its revisions.
1. A push to `main` runs the `Production` workflow, which deploys a new revision to the `prod` endpoint with the `ProductionDeployRole` and the `ProductionExecutionRole`.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The AWS Identity and Access Management (AWS IAM) user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2.37.13 or later, installed and configured. Earlier versions do not have the `aws lambda-web` commands. Check with `aws --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* `zip`, which the deploy script uses to package the app
* A GitHub repository where you can add workflows and repository variables, and the [GitHub CLI](https://cli.github.com/) (`gh`) signed in to it, for the GitHub part of this pattern

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-pr-previews/nodejs/sam
    ```
1. Check whether your account already has a GitHub OIDC provider. An account can have only one:
    ```bash
    aws iam list-open-id-connect-providers --query "OpenIDConnectProviderList[?ends_with(Arn, 'token.actions.githubusercontent.com')].Arn" --output text
    ```
1. Get the subject prefix that GitHub puts in the OIDC tokens of your repository. Replace `my-org/my-repo` with your repository:
    ```bash
    gh api repos/my-org/my-repo/actions/oidc/customization/sub --jq .sub_claim_prefix
    ```
    Repositories created after July 15, 2026 print a prefix with immutable owner and repository IDs, such as `repo:my-org@123456/my-repo@456789`. Older repositories print `repo:my-org/my-repo`. The deploy roles trust only tokens with this exact prefix. See [Immutable subject claims](https://docs.github.com/en/actions/reference/security/oidc#immutable-subject-claims).
1. Deploy the stack. Replace the `GitHubSubjectPrefix` value with the prefix from the previous step and `us-east-1` with your Region. If the OIDC provider check printed an ARN, add `GitHubOidcProviderArn=<that ARN>` to the parameter overrides:
    ```bash
    sam deploy --stack-name lambda-web-pr-previews --region us-east-1 --capabilities CAPABILITY_IAM --parameter-overrides GitHubSubjectPrefix=repo:my-org@123456/my-repo@456789
    ```
    The stack creates the code bucket, the execution roles, the log groups and the two deploy roles. It does not create the Web Function: the deploy script does, because a Web Function is created together with its first revision.
1. Deploy production from your terminal. This creates the Web Function and its `prod` endpoint and prints the production URL:
    ```bash
    AWS_REGION=us-east-1 scripts/deploy.sh production
    ```

### Connect your GitHub repository

1. Copy the app, the deploy script and the workflows into the root of your repository:
    ```bash
    cp -R src scripts .github /path/to/my-repo/
    ```
1. Print the two deploy role ARNs:
    ```bash
    aws cloudformation describe-stacks --stack-name lambda-web-pr-previews --region us-east-1 --query "Stacks[0].Outputs[?ends_with(OutputKey, 'DeployRoleArn')].[OutputKey,OutputValue]" --output text
    ```
1. In your repository, open **Settings**, **Secrets and variables**, **Actions**, **Variables**, and add these repository variables:

    | Variable | Value |
    |---|---|
    | `AWS_REGION` | The Region you deployed to, for example `us-east-1` |
    | `AWS_PREVIEW_ROLE_ARN` | The `PreviewDeployRoleArn` output |
    | `AWS_PRODUCTION_ROLE_ARN` | The `ProductionDeployRoleArn` output |

    If you deployed the stack with a name other than `lambda-web-pr-previews`, also add `STACK_NAME`.
1. Commit and push the copied files to `main`.

## How it works

### Endpoints and revisions

A Web Function revision is an immutable snapshot of code and configuration, and an endpoint is an HTTPS domain that routes traffic to one or two revisions. This pattern uses one Web Function with one endpoint per environment:

| Endpoint | Serves | Deployed by |
|---|---|---|
| `prod` | The latest revision from `main` | `scripts/deploy.sh production`, run by the `Production` workflow |
| `pr-<number>` | The latest commit of that pull request | `scripts/deploy.sh preview <number>`, run by the `Preview` workflow |

The app reads the `lambda-web-endpoint-name` header that Lambda adds to every request, so it can show a "Preview of pull request #N" banner. The deploy script sets a `GIT_SHA` environment variable on each revision, so the page and `/api/version` show which commit is running.

### Why production uses `Disabled` auto-deployment

An endpoint with `autoDeploymentMode` set to `LatestRevision` routes all traffic to the newest revision of the function as soon as it becomes Active. Every preview is a new revision of the same function, so a `LatestRevision` production endpoint would start serving the code of whichever pull request was pushed last. `LatestRevision` is the default for HomeRegion endpoints that you create with the Lambda console or `aws lambda-web deploy`.

The `prod` endpoint and every `pr-<number>` endpoint therefore use `Disabled`, and the deploy script sets their revision weights explicitly. See [Deployment patterns](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-deployment.html).

### Limits

* **Nine previews at a time.** A Web Function can have up to 10 endpoints, and `prod` uses one. When a tenth preview is requested, the script prints the `ServiceQuotaExceededException` error and asks you to close a pull request or run `scripts/deploy.sh delete-preview <number>`.
* **Preview capacity.** Each preview endpoint is limited to 2 execution environments and 100 requests per second, so a preview cannot use the capacity of production.
* **Revisions.** Lambda keeps up to 50 revisions per Web Function and automatically deletes the oldest ones that no endpoint routes to. The script also deletes a preview's previous revision after each push, and all of its revisions when the pull request closes.

### What each workflow is allowed to do

The deploy roles trust only GitHub OIDC tokens whose subject starts with your repository's prefix: the preview role trusts `<prefix>:pull_request`, and the production role trusts `<prefix>:ref:refs/heads/main`. With the immutable prefix, a repository that someone else later creates with the same name cannot assume the roles. GitHub does not issue OIDC tokens to workflows that run for pull requests from forks, and the workflow also skips them.

| Permission | `PreviewDeployRole` | `ProductionDeployRole` |
|---|---|---|
| Change and delete endpoints | `pr-*` only | `prod` only, no delete |
| Create the Web Function | No | Yes |
| Pass an execution role | `PreviewExecutionRole` only | `ProductionExecutionRole` only |
| Upload code to the bucket | `previews/*` only | `production/*` only |

Because each Web Function endpoint has its own Amazon Resource Name (ARN), IAM can scope endpoint actions to `endpoint/pr-*`, so a pull request cannot change or delete the production endpoint. Preview revisions run with a separate execution role, so code that nobody has merged yet never runs with production permissions.

### Files

| File | Purpose |
|---|---|
| `template.yaml` | Code bucket, execution roles, log groups, GitHub OIDC provider and deploy roles |
| `scripts/deploy.sh` | Packages `src/`, uploads it and creates revisions and endpoints |
| `.github/workflows/preview.yml` | Deploys, updates and deletes previews, and comments the URL |
| `.github/workflows/production.yml` | Deploys `main` to the `prod` endpoint |
| `src/index.js` | A zero-dependency Node.js HTTP server |

## Testing

1. Store the Web Function name in a shell variable. Replace `us-east-1` with the Region you deployed to in this and the following steps:
    ```bash
    FUNCTION=$(aws cloudformation describe-stacks --stack-name lambda-web-pr-previews --region us-east-1 --query "Stacks[0].Outputs[?OutputKey=='FunctionName'].OutputValue" --output text)
    ```
1. Store the production URL and call it. The response names the `prod` endpoint and the commit it runs. From your terminal, the script uses the current commit of your Git working copy, or `unknown` outside a Git repository. The workflows set the commit of the push:
    ```bash
    PROD_URL=https://$(aws lambda-web get-web-function-endpoint --function-name "$FUNCTION" --endpoint-name prod --region us-east-1 --query domainName --output text)/
    ```
    ```bash
    curl -s "${PROD_URL}api/version"
    ```
    Example output:
    ```
    {"endpoint":"prod","pullRequest":null,"commit":"7255bd8d68d662f5185a8efe009f742100b4fcd5"}
    ```
1. Create a preview for pull request 1 from your terminal, the same way the workflow does. The script prints the preview URL:
    ```bash
    AWS_REGION=us-east-1 scripts/deploy.sh preview 1
    ```
1. List the endpoints. There is now a `pr-1` endpoint next to `prod`:
    ```bash
    aws lambda-web list-web-function-endpoints --function-name "$FUNCTION" --region us-east-1 --query "endpoints[].[endpointName,domainName]" --output text
    ```
1. Call the preview. Replace the URL with the one that the script printed. The response names the `pr-1` endpoint, and the page in a browser shows a "Preview of pull request #1" banner:
    ```bash
    curl -s "https://abcdefghij123456.9dy.lambda-web.us-east-1.on.aws/api/version"
    ```
    Example output:
    ```
    {"endpoint":"pr-1","pullRequest":1,"commit":"7255bd8d68d662f5185a8efe009f742100b4fcd5"}
    ```
1. Confirm that production still serves its own revision:
    ```bash
    curl -s "${PROD_URL}api/version"
    ```
1. Delete the preview:
    ```bash
    AWS_REGION=us-east-1 scripts/deploy.sh delete-preview 1
    ```
1. If you connected a GitHub repository, open a pull request from a branch in that repository. When the `Preview` workflow finishes, it comments the preview URL on the pull request. Push another commit: the comment shows the new commit and the URL stays the same. Merge or close the pull request: the workflow deletes the preview and changes the comment to "Preview deleted.", and a merge also runs the `Production` workflow.

## Cleanup

1. Delete the Web Function, with all its endpoints and revisions, and empty the versioned code bucket. Replace `us-east-1` with the Region you deployed to in this and the following steps:
    ```bash
    AWS_REGION=us-east-1 scripts/deploy.sh destroy
    ```
1. Delete the stack. If the stack created the GitHub OIDC provider (you did not pass `GitHubOidcProviderArn`), deleting it also deletes the provider, so delete stacks in other Regions that use the provider first:
    ```bash
    sam delete --stack-name lambda-web-pr-previews --region us-east-1 --no-prompts
    ```
1. Confirm that the stack has been deleted. The command returns an error that the stack does not exist:
    ```bash
    aws cloudformation describe-stacks --stack-name lambda-web-pr-previews --region us-east-1
    ```
1. If you connected a GitHub repository, delete the copied workflows and the `AWS_REGION`, `AWS_PREVIEW_ROLE_ARN` and `AWS_PRODUCTION_ROLE_ARN` repository variables.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
