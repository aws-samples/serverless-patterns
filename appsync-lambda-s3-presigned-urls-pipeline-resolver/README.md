# AppSync Pipeline Resolvers with S3 Presigned URLs

This pattern creates an AWS AppSync GraphQL API with pipeline resolvers that orchestrate Lambda functions, DynamoDB, and S3 to enable secure file uploads and downloads through presigned URLs.

Learn more about this pattern at Serverless Land Patterns: http://serverlessland.com/patterns/appsync-lambda-s3-presigned-cdk-python

**Important:** this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Python 3.9+](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:
    ```bash
    cd appsync-lambda-s3-presigned-cdk-python
    ```

3. Create a virtual environment for Python:
    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
    For Windows:
    ```bash
    .venv\Scripts\activate.bat
    ```

5. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Bootstrap your AWS account for CDK (if you haven't done this already):
    ```bash
    cdk bootstrap
    ```

7. Deploy the stack:
    ```bash
    cdk deploy
    ```

8. Note the outputs from the CDK deployment process. These contain the GraphQL API endpoint, API key, S3 bucket name, and DynamoDB table name which are used for testing.

## How it works

This pattern demonstrates AWS AppSync pipeline resolvers that chain multiple operations together:

### Architecture

The stack deploys:
- **AWS AppSync GraphQL API** with API Key authentication
- **AWS Lambda function** (Python 3.12) for generating S3 presigned URLs
- **Amazon DynamoDB table** for storing note metadata
- **Amazon S3 bucket** with CORS configuration for file attachments

### Pipeline Resolvers

**saveNote Mutation Pipeline:**
1. Lambda function generates a presigned upload URL for S3
2. DynamoDB saves the note with the attachment key and upload URL
3. Returns note data including the temporary upload URL to the client

**getNote Query Pipeline:**
1. DynamoDB retrieves the note data
2. Lambda conditionally generates a presigned download URL (only if attachment exists)
3. Returns note data with download URL if applicable

The pipeline resolvers use VTL (Velocity Template Language) mapping templates to pass data between stages using `$ctx.prev.result`, enabling complex orchestration without additional code.

## Testing

### Using GraphQL Queries

1. After deployment, copy the **GraphQLApiEndpoint** and **APIKey** from the CDK outputs.

2. Use a GraphQL client (like Postman, Insomnia, or the AppSync console) to test the API.

3. Set the authorization header:
   - Header name: `x-api-key`
   - Value: [Your API Key from outputs]

4. **Create a note with file attachment:**

    ```graphql
    mutation CreateNote {
      saveNote(
        NoteId: "note-001"
        title: "My First Note"
        content: "This note has an attachment"
        fileName: "document.pdf"
      ) {
        NoteId
        title
        content
        attachmentKey
        uploadUrl
      }
    }
    ```

    The response includes an `uploadUrl` field - a presigned S3 URL valid for 1 hour.

5. **Upload a file using the presigned URL:**

    ```bash
    curl -X PUT \
      -H "Content-Type: application/pdf" \
      --data-binary @/path/to/your/document.pdf \
      "[uploadUrl from previous response]"
    ```

6. **Retrieve the note with download URL:**

    ```graphql
    query GetNote {
      getNote(NoteId: "note-001") {
        NoteId
        title
        content
        attachmentKey
        downloadUrl
      }
    }
    ```

    The response includes a `downloadUrl` field - a presigned S3 URL for downloading the file.

7. **Download the file:**

    ```bash
    curl "[downloadUrl from previous response]" -o downloaded-file.pdf
    ```

8. **Query all notes:**

    ```graphql
    query ListNotes {
      allNotes(limit: 10) {
        notes {
          NoteId
          title
          content
        }
        nextToken
      }
    }
    ```

9. **Delete a note:**

    ```graphql
    mutation DeleteNote {
      deleteNote(NoteId: "note-001") {
        NoteId
        title
      }
    }
    ```

### Automated Testing

Run the included test suite:

```bash
# Configure test credentials
python test_notes_api.py
```

Update the `APPSYNC_URL` and `API_KEY` in the test file before running.

## Cleanup

1. Delete the stack:
    ```bash
    cdk destroy
    ```

2. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'NotesAppSyncStack')].StackStatus"
    ```

**Note:** The S3 bucket and DynamoDB table are configured with `DESTROY` removal policy and will be automatically deleted. If you changed the removal policy to `RETAIN`, you'll need to manually delete these resources.

## Documentation

* [AWS AppSync Pipeline Resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html)
* [Amazon S3 Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html)
* [VTL Mapping Templates for AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html)
* [AWS AppSync - Managed GraphQL Service](https://aws.amazon.com/appsync/)
* [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
