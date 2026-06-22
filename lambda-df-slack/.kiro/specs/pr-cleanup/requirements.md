# Requirements Document

## Introduction

This document captures the requirements for cleaning up and hardening the lambda-df-slack serverless pattern project. The cleanup addresses PR review feedback across four areas: build pipeline, security hardening, code quality, and documentation accuracy.

## Glossary

- **Build_Step**: A shell script or Terraform null_resource that installs Python dependencies into a build directory and copies application source before creating the Lambda deployment zip.
- **Secrets_Manager**: AWS Secrets Manager service used to store and retrieve sensitive credentials (Slack tokens) at runtime instead of passing them as Lambda environment variables.
- **Dedup_Module**: A Python module (`dedup.py`) that uses DynamoDB conditional writes to deduplicate Slack event processing across concurrent Lambda instances.
- **Orchestrator**: The durable Lambda function (`orchestrator.py`) that manages multi-turn conversation state using the AWS Durable Execution SDK.
- **Slack_Handler**: The entry-point Lambda function (`slack_handler.py`) that receives Slack webhook events via API Gateway.
- **Determinism**: The property that a durable function orchestrator produces identical results on replay — no dependency on wall-clock time or random values outside SDK-managed steps.
- **Structured_Logging**: Python `logging` module usage with consistent format strings replacing bare `print()` statements.
- **IAM_Policy**: AWS Identity and Access Management policy documents attached to Lambda execution roles.

## Requirements

### Requirement 1: Remove Vendored Dependencies

**User Story:** As a developer, I want vendored third-party libraries removed from the source tree, so that the repository is small, auditable, and dependencies are managed via standard tooling.

#### Acceptance Criteria

1. THE Build_Step SHALL ensure no vendored Python packages (boto3, botocore, urllib3, etc.) exist in the `src/` directory
2. WHEN the repository is cloned, THE source tree SHALL contain only application code files (`.py` files authored by the project) and a `requirements.txt`
3. THE `.gitignore` file SHALL include patterns to prevent vendored dependencies and build artifacts from being committed (e.g., `src/boto3/`, `src/botocore/`, `build/`, `*.dist-info/`)

### Requirement 2: Lambda Build Pipeline

**User Story:** As a developer, I want a proper build step that installs dependencies at deploy time, so that the deployment package is correct and the source tree stays clean.

#### Acceptance Criteria

1. THE Build_Step SHALL install all packages listed in `requirements.txt` into a `build/` directory using `pip install -t`
2. THE Build_Step SHALL copy application source files (all `.py` files and `utils/` directory) from `src/` into the `build/` directory
3. WHEN Terraform runs `archive_file`, THE archive source SHALL point to the `build/` directory rather than `src/` directly
4. THE Build_Step SHALL execute before Terraform creates the Lambda deployment zip (via `null_resource` with a `triggers` block that detects source or requirements changes)
5. IF the build step fails, THEN Terraform SHALL halt and report the error before attempting Lambda deployment

### Requirement 3: Secrets Manager Integration

**User Story:** As a security engineer, I want Slack credentials stored in AWS Secrets Manager and fetched at runtime, so that secrets are not exposed in Lambda environment variables or Terraform state.

#### Acceptance Criteria

1. THE Terraform configuration SHALL create an `aws_secretsmanager_secret` resource storing a JSON object with keys `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET`
2. THE Lambda environment variables SHALL contain `SLACK_SECRETS_ARN` (the secret ARN) instead of plaintext `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET` values
3. THE `secrets.py` module SHALL provide a `get_slack_secrets()` function that fetches and caches the secret for the Lambda container lifetime
4. WHEN `get_slack_secrets()` is called multiple times within a single Lambda invocation, THE Secrets_Manager API SHALL be called at most once (result is cached in module-level variable)
5. THE Slack_Handler SHALL use `get_slack_secrets()` to obtain the signing secret for request verification
6. THE `SlackClient` class SHALL use `get_slack_secrets()` to obtain the bot token instead of reading from environment variables
7. THE IAM_Policy for both Lambda roles SHALL grant `secretsmanager:GetSecretValue` scoped to the specific secret ARN only

### Requirement 4: IAM Policy Scoping

**User Story:** As a security engineer, I want IAM policies to follow least-privilege principles, so that compromised credentials have minimal blast radius.

#### Acceptance Criteria

1. THE IAM_Policy for `bedrock-agentcore:InvokeAgentRuntime` SHALL scope the Resource to the specific AgentCore runtime ARN rather than `"*"`
2. THE IAM_Policy for `lambda:SendDurableExecutionCallback*` actions SHALL scope the Resource to the orchestrator function ARN rather than `"*"`
3. THE IAM_Policy for ECR pull actions (`BatchCheckLayerAvailability`, `GetDownloadUrlForLayer`, `BatchGetImage`) SHALL scope the Resource to the specific ECR repository ARN (while `ecr:GetAuthorizationToken` remains on `"*"`)
4. THE DynamoDB table SHALL have `server_side_encryption` configured (AWS-managed KMS key at minimum)

### Requirement 5: DynamoDB-Based Event Deduplication

**User Story:** As a developer, I want event deduplication backed by DynamoDB, so that duplicate Slack events are correctly rejected even across concurrent Lambda instances.

#### Acceptance Criteria

1. THE `dedup.py` module SHALL use a DynamoDB conditional `PutItem` (with `attribute_not_exists` condition) to atomically check-and-record event IDs
2. WHEN two concurrent Lambda invocations process the same Slack event_id, THE Dedup_Module SHALL ensure exactly one returns `False` (new event) and all others return `True` (duplicate)
3. THE dedup DynamoDB items SHALL include a `ttl` attribute set to 5 minutes from write time, so old entries are automatically cleaned up
4. THE Slack_Handler SHALL replace the in-memory `_processed_events` dictionary with calls to `dedup.is_duplicate_event()`
5. THE dedup items SHALL be stored in the existing callbacks DynamoDB table using a key prefix pattern (e.g., `DEDUP#<event_id>`) to distinguish them from callback entries

### Requirement 6: Orchestrator Determinism

**User Story:** As a developer, I want the durable function orchestrator to be fully deterministic on replay, so that the durable execution SDK functions correctly without state corruption.

#### Acceptance Criteria

1. THE Orchestrator SHALL read `execution_id` from `event['execution_id']` (set by the Slack_Handler) rather than generating it with `datetime.now()`
2. THE Slack_Handler SHALL generate `execution_id` using `time.time()` (outside the durable context) before invoking the orchestrator
3. THE submitter callbacks (e.g., `request_destination`, `request_dates`) SHALL NOT call `datetime.now()` or any non-deterministic function
4. THE submitter callbacks SHALL NOT include a `timestamp` field in DynamoDB writes (removing the source of non-determinism)
5. WHEN the orchestrator replays, THE execution SHALL produce identical DynamoDB writes (same `user_id`, `callback_id`, `step`) as the original execution

### Requirement 7: Structured Logging and Error Handling

**User Story:** As an operator, I want structured logging and proper error propagation, so that I can debug issues efficiently and conversations don't silently stall.

#### Acceptance Criteria

1. THE Slack_Handler and all modules SHALL use Python `logging` module (via `logging.getLogger(__name__)`) instead of bare `print()` statements
2. THE `send_callback_to_orchestration` function SHALL re-raise exceptions from `send_durable_execution_callback_success` after logging them (not silently swallow errors)
3. THE `AgentCoreClient` SHALL read the AWS region from `os.environ['AWS_REGION']` (provided by Lambda runtime) instead of using a hardcoded fallback like `'us-east-1'`
4. THE `AgentCoreClient` SHALL read the Bedrock model ID from `os.environ.get('BEDROCK_MODEL_ID')` instead of hardcoding a specific model string in the source code

### Requirement 8: README Documentation Accuracy

**User Story:** As a developer evaluating this pattern, I want the README to accurately describe the architecture and setup, so that I can successfully deploy and understand the system.

#### Acceptance Criteria

1. THE README architecture diagram reference SHALL use valid Markdown image syntax (`![Architecture](Architecture.png)`) instead of `[Architecture.png]`
2. THE README SHALL refer to the correct Bedrock model name consistent with the `bedrock_model_id` Terraform variable default
3. THE README SHALL document the build step (how dependencies are installed before deploy)
4. THE README SHALL specify the minimum AWS CLI version required (v2.30.0+ for durable functions)
5. THE README SHALL reference the correct container tooling matching what Terraform uses (Docker or Finch)
6. THE README resource naming SHALL be consistent with the Terraform `prefix` variable usage (no stale `<project>-<env>` references)

