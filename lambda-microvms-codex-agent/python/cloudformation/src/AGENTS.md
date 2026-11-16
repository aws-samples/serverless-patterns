# Environment notes

You are running as the Codex CLI inside an AWS Lambda MicroVM (Firecracker),
reached over an interactive shell. Inference goes to Amazon Bedrock.

- Credentials come from the MicroVM **execution role**. There are no AWS keys on
  this filesystem and nothing here needs one.
- The role grants **ReadOnlyAccess** plus the Amazon Bedrock inference permission
  this CLI needs. Mutating AWS calls are denied by IAM, wherever they come from.
  Report that limitation rather than trying to work around it.
- Use the **AWS MCP tools** for anything AWS: live API calls, AWS documentation
  search, and AWS skills. They are already authenticated and scoped, and they
  reach AWS through an AWS-managed MCP server. Describe what you want and let the
  tool selection follow; do not assume a particular tool name. The AWS CLI is not
  installed, so do not shell out to `aws`.
- The documentation and Region-availability tools do not need credentials, so they
  keep working even if a credential problem breaks the API tools.
- `/workspace` is the writable working directory and a Git repository. Treat
  anything outside it as read-only.
- This VM suspends once idle, is terminated after a period suspended, and has a
  hard maximum lifetime regardless of activity. Nothing written here is durable
  and the role cannot write to AWS storage, so include anything worth keeping in
  your final message.
