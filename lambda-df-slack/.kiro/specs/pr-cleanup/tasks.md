# Implementation Plan: PR Cleanup & Hardening

## Overview

This plan addresses PR review feedback by removing vendored dependencies, adding a proper build pipeline, hardening security (Secrets Manager + IAM scoping), fixing durable function determinism issues, improving code quality, and correcting README inaccuracies. Tasks are ordered to minimize conflicts — the vendored file removal comes first, build pipeline second, then security and code quality changes can proceed.

## Tasks

- [x] 1. Remove vendored dependencies and add .gitignore
  - [x] 1.1 Delete all vendored directories from `src/` (boto3/, botocore/, urllib3/, s3transfer/, jmespath/, dateutil/, bin/, *.dist-info/, and any other third-party packages)
    - Remove everything in `src/` except: `slack_handler.py`, `orchestrator.py`, `activities.py`, `agentcore_client.py`, `utils/` directory
    - _Requirements: 1.1, 1.2_
  - [x] 1.2 Create/update `.gitignore` with vendored dependency and build artifact patterns
    - Add patterns: `src/boto3/`, `src/botocore/`, `src/urllib3/`, `src/s3transfer/`, `src/jmespath/`, `src/dateutil/`, `src/bin/`, `src/*.dist-info/`, `build/`, `terraform/lambda_deployment.zip`, `terraform/*.txt`, `__pycache__/`, `.DS_Store`
    - _Requirements: 1.3_

- [x] 2. Create Lambda build/packaging step
  - [x] 2.1 Create `terraform/build.sh` script
    - Script should: clean `build/` dir, run `pip install -r ../requirements.txt -t build/ --platform manylinux2014_x86_64 --only-binary=:all:`, then copy all `.py` files and `utils/` from `../src/` into `build/`
    - Make script executable (`chmod +x`)
    - _Requirements: 2.1, 2.2_
  - [x] 2.2 Update `terraform/main.tf` to use the build step
    - Add a `null_resource "lambda_build"` with a `local-exec` provisioner that runs `build.sh`
    - Add `triggers` block that detects changes in source files and requirements.txt (use `filemd5` or `sha1`)
    - Change `data "archive_file" "lambda_zip"` to use `source_dir = "${path.module}/build"` instead of `local.lambda_source_dir` (which points to `../src`)
    - Add `depends_on = [null_resource.lambda_build]` to the archive_file or to both Lambda function resources
    - _Requirements: 2.3, 2.4, 2.5_

- [x] 3. Security hardening — Secrets Manager integration
  - [x] 3.1 Add Secrets Manager Terraform resources
    - Create `aws_secretsmanager_secret "slack_secrets"` resource
    - Create `aws_secretsmanager_secret_version` storing JSON with `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET` from variables
    - _Requirements: 3.1_
  - [x] 3.2 Update Lambda environment variables in Terraform
    - Replace `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET` in `local.common_lambda_env` with `SLACK_SECRETS_ARN = aws_secretsmanager_secret.slack_secrets.arn`
    - _Requirements: 3.2_
  - [x] 3.3 Add IAM policy for Secrets Manager access
    - Grant `secretsmanager:GetSecretValue` to both Lambda roles, scoped to `aws_secretsmanager_secret.slack_secrets.arn`
    - _Requirements: 3.7_
  - [x] 3.4 Create `src/secrets.py` module
    - Implement `get_slack_secrets()` with module-level `_secrets_cache` for container-lifetime caching
    - Read `SLACK_SECRETS_ARN` from env, call `secretsmanager:GetSecretValue`, parse JSON, cache result
    - Use `logging.getLogger(__name__)` for structured logging
    - _Requirements: 3.3, 3.4_
  - [x] 3.5 Update `src/slack_handler.py` to use secrets module
    - Remove direct `os.environ['SLACK_SIGNING_SECRET']` read
    - Import and call `get_slack_secrets()` in `verify_slack_request()`
    - _Requirements: 3.5_
  - [x] 3.6 Update `src/utils/slack_client.py` to use secrets module
    - Remove `os.environ.get('SLACK_BOT_TOKEN')` in `__init__`
    - Import and call `get_slack_secrets()` to get bot token
    - _Requirements: 3.6_
  - [ ]* 3.7 Write property test for secrets caching
    - **Property 2: Secrets caching invariant**
    - Mock Secrets Manager client, call `get_slack_secrets()` N times (random N from 1-100), verify API called exactly once
    - **Validates: Requirements 3.3, 3.4**

- [x] 4. Security hardening — IAM policy scoping + DynamoDB encryption
  - [x] 4.1 Scope `bedrock-agentcore:InvokeAgentRuntime` to specific runtime ARN
    - Replace `Resource: "*"` with the AgentCore runtime ARN (from `data.local_file.agent_runtime_arn`)
    - _Requirements: 4.1_
  - [x] 4.2 Scope `lambda:SendDurableExecutionCallback*` to orchestrator ARN
    - Replace `Resource: "*"` with `aws_lambda_function.orchestrator.arn` (and qualified ARN with `:*`)
    - _Requirements: 4.2_
  - [x] 4.3 Scope ECR pull actions to specific repository ARN
    - Split ECR statement: `ecr:GetAuthorizationToken` stays on `"*"`, pull actions scope to `aws_ecr_repository.agentcore_agent.arn`
    - _Requirements: 4.3_
  - [x] 4.4 Add DynamoDB server-side encryption
    - Add `server_side_encryption { enabled = true }` to the callbacks table resource
    - _Requirements: 4.4_

- [x] 5. Code quality — DynamoDB-based dedup
  - [x] 5.1 Create `src/dedup.py` module
    - Implement `is_duplicate_event(event_id)` using conditional `PutItem` with `attribute_not_exists(user_id)` condition
    - Use key format `DEDUP#{event_id}` for `user_id` field, `'event'` for `step` field
    - Set `ttl` to `int(time.time()) + 300`
    - Return `False` if write succeeds (new event), `True` if `ConditionalCheckFailedException` (duplicate)
    - Use `logging.getLogger(__name__)` for logging
    - _Requirements: 5.1, 5.3, 5.5_
  - [x] 5.2 Update `src/slack_handler.py` to use DynamoDB dedup
    - Remove the in-memory `_processed_events` dictionary and the old `is_duplicate_event()` function
    - Import `is_duplicate_event` from `dedup` module
    - _Requirements: 5.4_
  - [ ]* 5.3 Write property test for dedup atomicity
    - **Property 1: Event deduplication atomicity**
    - Mock DynamoDB: first call succeeds (new), second call raises ConditionalCheckFailedException (duplicate)
    - Generate random event_ids, verify first call returns False, subsequent calls return True
    - **Validates: Requirements 5.1, 5.2**
  - [ ]* 5.4 Write property test for dedup TTL and key format
    - **Property 5: Dedup TTL correctness**
    - Generate random event_ids, mock time.time(), verify TTL = mock_time + 300 and key = "DEDUP#{event_id}"
    - **Validates: Requirements 5.3, 5.5**

- [x] 6. Code quality — Orchestrator determinism fixes
  - [x] 6.1 Fix `execution_id` sourcing in orchestrator
    - In `src/orchestrator.py`, change `execution_id = event.get('execution_id', f"{user_id}_{int(datetime.now().timestamp())}")` to `execution_id = event['execution_id']` (no fallback)
    - Remove `from datetime import datetime` import if no longer needed
    - _Requirements: 6.1_
  - [x] 6.2 Fix `execution_id` generation in slack_handler
    - In `src/slack_handler.py` `handle_message_event()`, change `f"{user_id}_{int(datetime.now().timestamp())}"` to `f"{user_id}_{int(time.time())}"`
    - Ensure `import time` is present (it already is for other uses)
    - Remove `from datetime import datetime` import if no longer needed
    - _Requirements: 6.2_
  - [x] 6.3 Remove `datetime.now()` from submitter callbacks
    - In `src/orchestrator.py`, remove the `'timestamp': int(datetime.now().timestamp())` field from all submitter callback `put_item` calls (request_destination, request_dates, request_budget, request_interests)
    - _Requirements: 6.3, 6.4_
  - [ ]* 6.4 Write property test for orchestrator replay determinism
    - **Property 3: Orchestrator replay determinism**
    - Use durable execution testing SDK to run orchestrator, replay, verify DynamoDB writes are identical
    - **Validates: Requirements 6.1, 6.3, 6.4, 6.5**

- [x] 7. Code quality — Structured logging, callback error propagation, env-var model/region
  - [x] 7.1 Replace all `print()` with structured logging in `src/slack_handler.py`
    - Add `import logging` and `logger = logging.getLogger(__name__)` at module level
    - Replace all `print(f"...")` calls with `logger.info(...)`, `logger.warning(...)`, or `logger.error(...)` as appropriate
    - _Requirements: 7.1_
  - [x] 7.2 Replace all `print()` with structured logging in `src/agentcore_client.py`
    - Same pattern: `logger = logging.getLogger(__name__)`, replace print() calls
    - _Requirements: 7.1_
  - [x] 7.3 Replace all `print()` with structured logging in `src/utils/slack_client.py`
    - Same pattern
    - _Requirements: 7.1_
  - [x] 7.4 Fix callback error propagation in `send_callback_to_orchestration`
    - In `src/slack_handler.py`, change the `except Exception as e: print(...)` block to `except Exception: logger.exception("Failed to send callback for user %s", user_id); raise`
    - Ensure the exception is re-raised, not swallowed
    - _Requirements: 7.2_
  - [x] 7.5 Fix `AgentCoreClient` region and model configuration
    - Change `region_name=os.environ.get('BEDROCK_REGION', 'us-east-1')` to `region_name=os.environ['AWS_REGION']`
    - Change hardcoded model ID in `generate_itinerary()` to `os.environ.get('BEDROCK_MODEL_ID', 'us.anthropic.claude-sonnet-4-6')`
    - _Requirements: 7.3, 7.4_
  - [ ]* 7.6 Write property test for callback error propagation
    - **Property 4: Callback failure propagation**
    - Mock `send_durable_execution_callback_success` to raise various exception types, verify they propagate through `send_callback_to_orchestration`
    - **Validates: Requirements 7.2**

- [x] 8. Documentation — README fixes
  - [x] 8.1 Fix architecture diagram reference and model name
    - Change `[Architecture.png]` to `![Architecture](Architecture.png)`
    - Update Bedrock model reference to match the Terraform variable default (`us.anthropic.claude-sonnet-4-6`)
    - _Requirements: 8.1, 8.2_
  - [x] 8.2 Add build step documentation and CLI version requirement
    - Add a section explaining the build process (run `build.sh` or `terraform apply` handles it automatically)
    - Add requirement: AWS CLI v2.30.0+ for durable function support
    - _Requirements: 8.3, 8.4_
  - [x] 8.3 Fix container tooling reference and resource naming
    - Ensure README references Finch (matching Terraform provisioners) or documents both Docker/Finch
    - Replace stale `<project>-<env>` references with `<prefix>-` pattern matching Terraform usage
    - _Requirements: 8.5, 8.6_

- [x] 9. Final checkpoint
  - Ensure all tests pass, ask the user if questions arise.
  - Verify `terraform validate` passes on the updated configuration
  - Verify the build script runs successfully and produces a valid zip

## Task Dependency Graph

## Notes

- Tasks marked with `*` are optional property-based tests and can be skipped for faster delivery
- Task 1 must be done first (removes 2000+ vendored files that would create merge conflicts)
- Task 2 depends on Task 1 (creates the build pipeline that replaces vendored deps)
- Tasks 3 and 4 can be done in parallel but both depend on Task 2 (they modify Terraform)
- Tasks 5, 6, 7 depend on Task 3 (they modify slack_handler.py which needs the secrets module changes in place)
- Task 8 can be done in parallel with Tasks 5-7
- Property tests validate universal correctness properties defined in the design document
