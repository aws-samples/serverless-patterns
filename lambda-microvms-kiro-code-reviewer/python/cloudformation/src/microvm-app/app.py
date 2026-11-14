"""
app.py — Code Review Service using Kiro on AWS Lambda MicroVMs

A long-running HTTP service that accepts code review requests.
Each request specifies a CodeCommit repo and PR to review.
The Kiro API Key is fetched from AWS Secrets Manager at startup.

- Port 8080: Review API (POST /review, GET /health)
- Port 9000: MicroVM lifecycle hooks
"""

import json
import logging
import os
import shutil
import subprocess
import tempfile
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

import boto3

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

MICROVM_ID = None
KIRO_API_KEY = None  # Fetched from Secrets Manager on startup


# ── Secrets Manager integration ───────────────────────────────────────────────

def fetch_kiro_api_key() -> str:
    """Fetch the Kiro API Key from AWS Secrets Manager."""
    secret_arn = os.environ.get("KIRO_API_KEY_SECRET_ARN", "")
    if not secret_arn:
        logger.warning("KIRO_API_KEY_SECRET_ARN not set — Kiro reviews will fail")
        return ""

    region = os.environ.get("AWS_REGION", os.environ.get("AWS_DEFAULT_REGION", "us-east-2"))
    logger.info(f"Fetching Kiro API Key from secret: {secret_arn} in region: {region}")
    try:
        client = boto3.client("secretsmanager", region_name=region)
        response = client.get_secret_value(SecretId=secret_arn)
        secret_value = response["SecretString"]
        if secret_value:
            logger.info(f"Kiro API Key fetched successfully (length={len(secret_value)}, prefix={secret_value[:8]}...)")
        else:
            logger.warning("Kiro API Key fetched but value is empty")
        return secret_value
    except Exception as e:
        logger.error(f"Failed to fetch Kiro API Key from Secrets Manager: {e}")
        return ""


# ── Unified HTTP Handler (port 8080) ─────────────────────────────────────────
# Serves the Review API: POST /review, GET /health

class AppHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        logger.info(f"APP {format % args}")

    def send_json(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def read_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length)) if length else {}

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {
                "service": "kiro-code-review",
                "microvm_id": MICROVM_ID,
                "status": "ready",
                "kiro_key_loaded": bool(KIRO_API_KEY)
            })
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/review":
            global KIRO_API_KEY

            # Always fetch fresh from Secrets Manager to pick up rotated keys
            KIRO_API_KEY = fetch_kiro_api_key()

            if not KIRO_API_KEY:
                self.send_json(500, {"error": "Kiro API Key not loaded. Check KIRO_API_KEY_SECRET_ARN and IAM permissions."})
                return

            body = self.read_body()

            # Validate required fields
            required = ["repo_name", "pr_id", "source_commit", "destination_commit", "region"]
            missing = [f for f in required if f not in body]
            if missing:
                self.send_json(400, {"error": f"Missing required fields: {missing}"})
                return

            # Run the review
            result = run_review(
                repo_name=body["repo_name"],
                pr_id=body["pr_id"],
                source_commit=body["source_commit"],
                destination_commit=body["destination_commit"],
                region=body["region"]
            )
            status_code = 200 if result["success"] else 500
            self.send_json(status_code, result)

        else:
            self.send_json(404, {"error": "not found"})


# ── Review logic ──────────────────────────────────────────────────────────────

def run_review(repo_name: str, pr_id: str, source_commit: str,
               destination_commit: str, region: str) -> dict:
    """
    Clone the repo, build the diff, run Kiro headless, and post the review.
    """
    work_dir = tempfile.mkdtemp(prefix="review-")

    try:
        # Configure git to use AWS CLI credential helper for CodeCommit
        subprocess.run(
            ["git", "config", "--global", "credential.helper",
             "!aws codecommit credential-helper $@"],
            check=True, capture_output=True, text=True
        )
        subprocess.run(
            ["git", "config", "--global", "credential.UseHttpPath", "true"],
            check=True, capture_output=True, text=True
        )

        # 1. Clone the repository (fetch all branches)
        clone_url = f"https://git-codecommit.{region}.amazonaws.com/v1/repos/{repo_name}"
        logger.info(f"Cloning {repo_name} from {region}...")
        subprocess.run(
            ["git", "clone", "--no-checkout", clone_url, work_dir],
            check=True, capture_output=True, text=True, timeout=120
        )

        # Fetch all remote refs so both commits are available
        subprocess.run(
            ["git", "fetch", "--all"],
            cwd=work_dir, check=True, capture_output=True, text=True, timeout=60
        )

        # 2. Build the diff
        diff_result = subprocess.run(
            ["git", "diff", f"{destination_commit}..{source_commit}"],
            cwd=work_dir, capture_output=True, text=True, timeout=60
        )
        diff = diff_result.stdout

        if not diff.strip():
            return {"success": True, "message": "Empty diff — nothing to review", "review": ""}

        logger.info(f"Diff size: {len(diff.splitlines())} lines")

        # 3. Run Kiro headless review
        logger.info("Running Kiro headless review...")

        prompt = (
            "You are a senior software engineer performing a code review. "
            "Review the following git diff and provide structured feedback covering: "
            "1. Potential bugs or logic errors "
            "2. Security concerns "
            "3. Performance issues "
            "4. Code quality and readability "
            "5. Missing tests or edge cases. "
            "Be concise and actionable. Format your response in Markdown.\n\n"
            "```diff\n"
            f"{diff}\n"
            "```"
        )

        kiro_result = subprocess.run(
            ["kiro-cli", "chat", "--no-interactive", "--trust-tools=read,grep", prompt],
            capture_output=True, text=True, timeout=300,
            env={**os.environ, "KIRO_API_KEY": KIRO_API_KEY}
        )

        logger.info(f"Kiro CLI exit code: {kiro_result.returncode}")
        logger.info(f"Kiro CLI stdout length: {len(kiro_result.stdout)}")
        logger.info(f"Kiro CLI stderr length: {len(kiro_result.stderr)}")

        if kiro_result.returncode != 0:
            logger.error(f"Kiro CLI stderr: {kiro_result.stderr[-1000:]}")
            return {"success": False, "error": f"Kiro CLI failed: {kiro_result.stderr[-500:]}"}

        # Kiro may output to stdout or stderr depending on version
        review_text = kiro_result.stdout.strip() or kiro_result.stderr.strip()

        if not review_text:
            logger.warning("Kiro returned empty output on both stdout and stderr")
            return {"success": False, "error": "Kiro returned an empty review. Check KIRO_API_KEY and CLI version."}

        # 4. Post the review as a PR comment
        comment = (
            "## 🤖 Kiro AI Code Review\n\n"
            f"{review_text}\n\n"
            "---\n"
            "*Review generated by Kiro headless running inside a Lambda MicroVM*"
        )

        logger.info(f"Posting review to PR #{pr_id}...")
        subprocess.run(
            ["aws", "codecommit", "post-comment-for-pull-request",
             "--pull-request-id", str(pr_id),
             "--repository-name", repo_name,
             "--before-commit-id", destination_commit,
             "--after-commit-id", source_commit,
             "--content", comment,
             "--region", region],
            check=True, capture_output=True, text=True, timeout=30
        )

        logger.info(f"Review posted to PR #{pr_id} successfully")
        return {"success": True, "message": "Review posted", "review": review_text}

    except subprocess.TimeoutExpired as e:
        return {"success": False, "error": f"Timeout: {e}"}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": f"Command failed: {e.stderr[-500:]}"}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


# ── Lifecycle hook handler (port 9000) ────────────────────────────────────────

class HookHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        logger.info(f"HOOK {format % args}")

    def send_json(self, status, body):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def read_body(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length)) if length else {}

    def do_POST(self):
        global MICROVM_ID
        body = self.read_body()

        if self.path.endswith("/ready"):
            logger.info("/ready — snapshot point reached")
            self.send_json(200, {"status": "ready"})

        elif self.path.endswith("/run"):
            MICROVM_ID = body.get("microVmId")
            logger.info(f"/run — microVmId={MICROVM_ID}")
            self.send_json(200, {"status": "running"})

        elif self.path.endswith("/suspend"):
            self.send_json(200, {"status": "suspending"})

        elif self.path.endswith("/resume"):
            self.send_json(200, {"status": "resumed"})

        elif self.path.endswith("/terminate"):
            logger.info("/terminate — shutting down")
            self.send_json(200, {"status": "terminating"})

        else:
            self.send_json(404, {"error": "unknown hook"})


# ── Startup ───────────────────────────────────────────────────────────────────

def main():
    global KIRO_API_KEY

    # Try to fetch at startup; if env var isn't set yet (build phase), that's OK.
    # We'll retry on first /review request at runtime.
    KIRO_API_KEY = fetch_kiro_api_key()

    # Start lifecycle hook server on port 9000 in a background thread
    hook_server = HTTPServer(("0.0.0.0", 9000), HookHandler)
    hook_thread = threading.Thread(target=hook_server.serve_forever, daemon=True)
    hook_thread.start()
    logger.info("Lifecycle hook server on port 9000")

    # Start main API server on port 8080 (blocks)
    app_server = HTTPServer(("0.0.0.0", 8080), AppHandler)
    logger.info("Kiro Review API listening on port 8080 — POST /review to submit a review")
    app_server.serve_forever()


if __name__ == "__main__":
    main()
