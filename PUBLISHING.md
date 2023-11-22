# How to Publish a Serverless Pattern on [ServerlessLand](https://serverlessland.com/)

To submit a new serverless pattern, or to make changes to existing code, follow the instructions below.

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

1. If you are creating a new serverless pattern, copy the folder named "_pattern-model" to start with a template: `cp -r _pattern-model {new-folder-name}`
1. If you are modifying existing code, make your code changes now.
1. When your code is complete, stage the changes to your local branch: `git add .`
1. Commit the changes to your local branch: `git commit -m 'Comment here'`

## Pull Request

Push your code to the remote repos and [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

1. Push the local branch to the remote origin repo: `git push origin {branch-name}`

    If this is the first push to the remote origin repo, you will be asked to Connect to GitHub to authorize the connection. Sometimes the pop-up window appears behind other windows.

1. Go to the [upstream repo](https://github.com/aws-samples/serverless-patterns) in GitHub and click "Compare & pull request".
    1. Enter an appropriate title:
        
        Example title: `New serverless pattern - lambda-aurora-serverless`

    1. Add a description of the changes.
    1. Click "Create pull request".
1. Submit a [new issue](https://github.com/aws-samples/serverless-patterns/issues/new?assignees=jbesw&labels=&template=new-serverless-pattern-submission.md&title=New+pattern+submission) to provide the additional details that will be used to build the serverless pattern web page on ServerlessLand.com.
    1. Provide responses to each section (eg: Description, Language, Framework, etc.)
    1. Add a link to the pull request in the "GitHub PR for template" section. If you type a hashtag (#), it will display a list of the current pull requests to select from.
    1. Consider adding a few links to AWS documentation in the "Additional resources" section to provide more information about your serverless pattern.
    1. Be sure to provide your information in the "Author bio" section.
    1. Click "Submit new issue".
    1. Example issue: https://github.com/aws-samples/serverless-patterns/issues/57

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
