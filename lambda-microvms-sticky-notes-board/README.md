# AWS Lambda MicroVMs Sticky Notes Board

This pattern demonstrates **Lambda MicroVMs state persistence**. A user adds sticky notes and uploads files inside a Firecracker MicroVM; when that MicroVM is terminated and a new one launches for the same user, everything is restored from Amazon S3. A small session middleware (AWS Lambda + Amazon DynamoDB behind Amazon API Gateway) reconnects a returning user to their running MicroVM, or launches a fresh one that restores their last session.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Access to **Lambda MicroVMs** in your target region
* `python3` + `pip`, `zip`, and `jq` on your PATH

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-microvms-sticky-notes-board
    ```
1. Deploy the resources with a single command. `deploy.sh` is a thin bootstrap around a CloudFormation stack (`template.yaml`):
    ```bash
    ./deploy.sh
    ```
    The script:
    1. Creates the S3 state/staging bucket (CLI — it must exist *before* the stack, because the MicroVM image's `CodeArtifact.Uri` points at the staged artifact).
    1. Packages and uploads two artifacts: the `src/microvm/` folder (the image artifact) and the middleware Lambda zip (its code + a current boto3 + the vendored `lambda-microvms` SDK model).
    1. Runs `aws cloudformation deploy template.yaml`, which creates the MicroVM image, the build + execution IAM roles, the DynamoDB session table, the middleware Lambda, and the API Gateway HTTP API.
    1. Prints the stack outputs — including the **Middleware URL** for the web UI.
1. Configuration is via environment variables (all optional):

    | Variable | Default | Purpose |
    |----------|---------|---------|
    | `AWS_REGION` | `us-east-1` | Target region |
    | `STACK_NAME` | `sticky-notes-board-demo` | CloudFormation stack name + resource label |
    | `STATE_BUCKET` | `<STACK_NAME>-state-<accountId>` | S3 bucket for staging + notes/files |
    | `API_STAGE` | `prod` | API Gateway stage |

    ```bash
    AWS_REGION=us-east-1 STACK_NAME=my-notes ./deploy.sh
    ```
1. Note the outputs from the deployment. The **Middleware URL** (the API Gateway URL, e.g. `https://abc123.execute-api.us-east-1.amazonaws.com/prod`) is used by the web UI.

## How it works

A static **web UI** (`src/web/`) talks only to an API Gateway HTTP API backed by a **session middleware** Lambda (`src/middleware/`). The middleware owns the MicroVM lifecycle and auth tokens, so the browser never holds AWS credentials or the MicroVM endpoint. It tracks sessions by `clientId` in DynamoDB and reverse-proxies every `/api/*` call to the client's MicroVM, injecting the `X-aws-proxy-auth` token server-side.

![Sticky notes](./images/sticky-notes.png)

The **MicroVM app** (`src/microvm/`) runs a notes + files REST API plus lifecycle hooks. Notes live in MicroVM memory and uploaded files in the MicroVM's local filesystem (`/tmp/microvm-files`) while it runs — both are ephemeral. State is persisted to S3 **only at lifecycle boundaries**: the `/suspend` and `/terminate` hooks push notes (`microvm-state/<clientId>/board.json`) and files (`microvm-files/<clientId>/*`) to S3; the `/run` hook restores both on boot. The `clientId` becomes the S3 key prefix, so one client can never see another's notes or files.

| Component | Port | Purpose |
|-----------|------|---------|
| Web UI (`src/web/`) | — | Static browser app (notes + files, two-pane) |
| Session middleware (`src/middleware/`) | — | API Gateway + Lambda + DynamoDB; session lifecycle, auth tokens, `/api` reverse proxy |
| Hooks server (`src/microvm/app/hooks_server.py`) | 9000 | MicroVM lifecycle hooks (`/ready`, `/run`, `/resume`, `/suspend`, `/terminate`) |
| Notes + Files API (`src/microvm/app/main_app.py`) | 8080 | Notes CRUD + any-file upload/download + text-file editing |

### Project structure

```
.
├── deploy.sh                     # Bootstrap: bucket + stage artifacts + deploy stack
├── template.yaml                 # CloudFormation: image, IAM, DynamoDB, Lambda, API GW
├── example-pattern.json          # Serverless Land pattern metadata
├── images/
│   └── sticky-notes.png          # Architecture diagram
└── src/
    ├── microvm/                  # ── MicroVM image artifact (zipped as-is) ──
    │   ├── Dockerfile            # Container image
    │   ├── requirements.txt      # App deps (boto3)
    │   ├── entrypoint.py         # Starts hooks server (9000) + app server (8080)
    │   └── app/                  # Application package
    │       ├── hooks_server.py   # Lifecycle hooks; syncs files to/from S3
    │       ├── main_app.py       # Notes + Files REST API (CORS enabled)
    │       ├── notes_board.py    # In-memory board model (create/edit/delete)
    │       ├── file_store.py     # Local-FS file store + S3 sync at lifecycle
    │       └── state_store.py    # S3 save/load for the notes board
    ├── middleware/               # ── Session middleware (Lambda) ──
    │   ├── handler.py            # API Gateway entrypoint: session routes + /api proxy
    │   ├── session_store.py      # DynamoDB session records (keyed by clientId)
    │   ├── microvm_control.py    # lambda-microvms control-plane wrapper
    │   └── botocore_models/      # Vendored lambda-microvms SDK model
    └── web/                      # ── Browser UI (static) ──
        ├── index.html
        ├── styles.css
        └── app.js
```

### API reference

#### Session middleware (API Gateway)

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/session` | Open/reconnect a session. Body `{clientId}`. Returns `{microvmId, restored, reused, ...}` |
| `POST` | `/session/token` | Mint a fresh auth token for the current MicroVM |
| `POST` | `/session/close` | Mark the UI closed (keeps the record for next restore) |
| `DELETE` | `/session` | Terminate the MicroVM (state flushes to S3) |
| ANY | `/api/{proxy+}` | Reverse-proxy to the client's MicroVM; clientId via `X-Client-Id` header |

#### MicroVM app (reached through the `/api` proxy)

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/notes` | List notes |
| `POST` | `/notes` | Create a note — `{content, color?, position_x?, position_y?}` |
| `PUT` | `/notes/{id}` | Edit a note |
| `DELETE` | `/notes/{id}` | Delete a note |
| `GET` | `/files` | List files |
| `POST` | `/files` | Upload any file — raw body, filename in `X-File-Name` |
| `GET` | `/files/{name}` | Download a file |
| `DELETE` | `/files/{name}` | Delete a file |
| `GET` | `/files/{name}/text` | Get a text file's contents (`415` if not text) |
| `PUT` | `/files/{name}/text` | Edit a text file — `{content}` |

> File transfers go through API Gateway, which caps payloads at ~10 MB, so uploads via the UI are limited to ~9 MB.

## Testing

1. Serve the static web UI (no build step):
    ```bash
    cd src/web
    python3 -m http.server 5173
    # open http://localhost:5173
    ```
1. In the UI, paste the **Middleware URL** from the deployment outputs, enter a **Client ID** (e.g. `demo-user`), and click **Open my workspace**. The top bar shows your Client ID, the launched MicroVM ID, and a pill for whether the session was reused, restored, or new.
1. Add a few notes and upload a file. Notes (left) and Files (right) sit side by side — click a note to edit its content, color, and position; upload/download/delete files, and edit text files in the browser.
1. Verify persistence: **Switch workspace** (or let the MicroVM idle out) so state flushes to S3, then open the workspace again with the **same Client ID**. The MicroVM relaunches, the `/run` hook restores your notes and files, and the top-bar pill reads "restored from S3".

## Cleanup

MicroVMs are created at runtime, not by the stack, so CloudFormation won't remove them. Terminate them first, then delete the stack and the bucket.

1. Terminate any running MicroVMs for this image:
    ```bash
    export AWS_REGION=us-east-1
    aws lambda-microvms list-microvms --region "$AWS_REGION" \
      --query "microvms[].microvmId" --output text | tr '\t' '\n' | while read -r id; do
        [ -n "$id" ] && aws lambda-microvms terminate-microvm --microvm-identifier "$id" --region "$AWS_REGION"
      done
    ```
1. Delete the stack:
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME --region "$AWS_REGION"
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
1. Empty and remove the S3 state bucket (not managed by the stack):
    ```bash
    export STATE_BUCKET=STACK_NAME-state-$(aws sts get-caller-identity --query Account --output text)
    aws s3 rb "s3://$STATE_BUCKET" --force
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
