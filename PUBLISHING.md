# How to Publish a Serverless Pattern on [ServerlessLand](https://serverlessland.com/)

To submit a new serverless pattern, or to make changes to existing code, follow the instructions below.

**Check for an existing pattern first.** Search [Serverless Land patterns](https://serverlessland.com/patterns) and the folders in this repo for the same services. If a pattern already exists, add your language or framework as a new variant in that pattern's family folder instead of creating a new pattern. See [folder structure](#folder-structure).

## Repo Names

* **local:** Your local copy of the forked repository.
* **origin:** Your forked, remote copy of the original repository.
* **upstream:** The original, remote serverless-patterns repository.

## Initial Setup

[Fork and Clone](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the serverless-patterns repo.

1. Fork the original serverless-patterns repo to create a copy of the repo in your own GitHub account: https://github.com/aws-samples/serverless-patterns
1. Clone your copy of the repo to download it locally: `git clone https://github.com/{your-github-username}/serverless-patterns.git`
1. Change into the new local directory: `cd serverless-patterns`
1. Add the original serverless-patterns repo as another remote repo called "upstream": `git remote add upstream https://github.com/aws-samples/serverless-patterns`
1. For verification, display the remote repos: `git remote -v`

    The output should look like this:

    ```
	origin  https://github.com/{your-github-username}/serverless-patterns.git (fetch)
	origin  https://github.com/{your-github-username}/serverless-patterns.git (push)
	upstream        https://github.com/aws-samples/serverless-patterns (fetch)
	upstream        https://github.com/aws-samples/serverless-patterns (push)
	```

## Create Branch

Create a new local branch for each serverless pattern or modification being made. This allows you to create separate pull requests in the upstream repo.

1. Create and checkout a new local branch before making code changes: `git checkout -b {branch-name}`
    
    Branch name syntax: `{username}-{feature|fix}-{description}`
    
    Example branch name: `myusername-feature-lambda-aurora-serverless`

1. For verification, display all branches: `git branch -a`

    The output should look like this:

    ```
    * {branch-name}
    main
    remotes/origin/HEAD → origin/main
    remotes/origin/main
    ```

## Your Code

Now is the time to create your new serverless pattern or modify existing code.

1. If you are creating a new serverless pattern, start from a template. Either copy the folder named "_pattern-model", or copy a similar existing pattern, such as another variant in the same family.For example: `mkdir -p sqs-lambda/python && cp -r _pattern-model sqs-lambda/python/sam`
    If you copy an existing pattern, update everything that refers to the original: `example-pattern.json` (title, description, language, framework, `gitHub.template` paths and authors), the README, and resource and stack names in the template. Remove build output and anything the new variant doesn't use.
2. If you are modifying existing code, make your code changes now.
3. Work through the [pattern checklist](#pattern-checklist) below.
4. When your code is complete, stage the changes in your pattern folder: `git add {family}/{language}/{framework}`
5. Commit the changes to your local branch: `git commit -m 'Comment here'`

## Pattern checklist

Use this checklist whether you write the pattern yourself or use an AI coding agent. Agents also read [AGENTS.md](AGENTS.md).

- **Check for an existing pattern** with the same services before you start. Add a variant to it rather than creating a duplicate.
- **One pattern variant per pull request.** Put everything in one variant folder. Don't change other pattern folders.
- <a id="folder-structure"></a>**Folder structure:** `{family}/{language}/{framework}`, all lowercase, e.g. `sqs-lambda/python/sam`.
  - The family folder names the services, hyphenated, e.g. `sqs-lambda`. It groups patterns that differ only by language or framework.
  - Each variant folder holds a complete pattern: `README.md`, `example-pattern.json`, the template and the code.
  - Older patterns still use single folders such as `sqs-lambda-python-sam`. Use the new structure for new patterns.
- **Scope:** patterns are infrastructure as code for 2–4 AWS services with minimal custom code. Utilities, demos and full applications belong in [Serverless Land repos](https://serverlessland.com/repos).
- **README.md:** keep the headings from `_pattern-model/README.md` and fill in every section: requirements, deployment, how it works, testing and cleanup.
- **example-pattern.json:** this file builds the pattern page on Serverless Land. Pull requests check it against the [pattern schema](_scripts/pattern-schema.mjs). The rules people most often miss:
  - The first mention of each service in `title` uses its official name: "AWS Lambda to Amazon DynamoDB", not "Lambda to DynamoDB".
  - `title` is 100 characters or fewer and `description` is 175 or fewer.
  - `language`, `framework` and `level` must use one of the values in the schema, e.g. `"framework": "AWS SAM"`.
  - `gitHub.template.templateFile` is relative to `projectFolder`: `"template.yaml"`, not `"my-pattern/template.yaml"`.
  - In `authors`, `linkedin` is your profile ID (`jane-doe`) and `twitter` is your handle (`jane_doe`), not URLs. If you have a page at `serverlessland.com/about/your-name`, you can use `"contributors": ["content/contributors/your-name.json"]` instead.
  - The `deploy` and `cleanup` commands match your framework, e.g. `sam deploy` and `sam delete`, or `cdk deploy` and `cdk destroy`.
- **Check the pattern file** from the repo root:

    ```bash
    cd _scripts && npm i && cd ..
    node _scripts/validate.js {family}/{language}/{framework}/example-pattern.json
    ```

- **Check the template builds**, e.g. `sam validate --lint`, `cdk synth` or `terraform validate`, and deploy and test it in your own account before you open the pull request.
- **Leave out:** account IDs, secrets, build output such as `.aws-sam/`, `cdk.out/` and `node_modules/`, and architecture diagrams. The Serverless Land team creates the diagrams.

## Pull Request

Push your code to the remote repos and [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

1. Push the local branch to the remote origin repo: `git push origin {branch-name}`

    If this is the first push to the remote origin repo, you will be asked to Connect to GitHub to authorize the connection. Sometimes the pop-up window appears behind other windows.

1. Go to the [upstream repo](https://github.com/aws-samples/serverless-patterns) in GitHub and click "Compare & pull request".
    1. Enter an appropriate title:
        
        Example title: `New serverless pattern - lambda-aurora-serverless`

    1. Add a description of the changes.
    1. Click "Create pull request".

## Sync Repos

After your pull request has been accepted into the upstream repo:

1. Switch to your local main branch: `git checkout main`
1. Pull changes that occurred in the upstream repo: `git fetch upstream`
1. Merge the upstream main branch with your local main branch: `git merge upstream/main main`
1. Push changes from you local repo to the remote origin repo: `git push origin main`

## Delete Branches

Delete any unnecessary local and origin branches.

1. Switch to your local main branch: `git checkout main`
1. For verification, display all branches: `git branch -a`
1. Delete any unnecessary local branches: `git branch -d {branch-name}`
1. Delete any unnecessary remote origin branches: `git push origin --delete {branch-name}`

## Helpful Tips

1. When creating a README file for your serverless pattern, place example code and commands within a `code block`.
1. When deploying with SAM, use [SAM policy templates](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html) for permissions whenever possible.
1. Within your code and the SAM template, use comments liberally to help others understand what is going on.
1. You do not need to create the architecture diagram image that appears above each serverless pattern on ServerlessLand.com. The team that manages the website is responsible for creating the image.
1. For Lambda functions, include test cases in both CLI and JSON with example data.
    
    Example CLI Lambda invoke with test event:

    ```
    aws lambda invoke --function-name YOUR_FUNCTION_NAME --invocation-type Event --payload '{"Key1": "Value1","Key2": "Value2"}' output.txt
    ```
    
    Example JSON Lambda test event:

    ```json
    {
        "Key1": "Value1",
        "Key2": "Value2"
    }
    ```

## Example Patterns

1. API Gateway HTTP API to Lambda: [Website](https://serverlessland.com/patterns/apigw-lambda) | [GitHub](https://github.com/aws-samples/serverless-patterns/tree/main/apigw-http-api-lambda)
2. API Gateway REST API to DynamoDB: [Website](https://serverlessland.com/patterns/apigw-dynamodb) | [GitHub](https://github.com/aws-samples/serverless-patterns/tree/main/apigw-rest-api-dynamodb)
3. Lambda to SSM Parameter Store: [Website](https://serverlessland.com/patterns/lambda-ssm) | [GitHub](https://github.com/aws-samples/serverless-patterns/tree/main/lambda-ssm-parameter)
4. Lambda to S3 via a Custom Resource: [Website](https://serverlessland.com/patterns/lambda-s3-cfn) | [GitHub](https://github.com/aws-samples/serverless-patterns/tree/main/cfn-custom-resource-s3-create)
