"""
Entrypoint for the Lambda MicroVM Sticky Notes Board demo.

Starts two servers:
  1. Lifecycle hooks server on port 9000 (handles /run, /terminate, etc.)
  2. Main application server on port 8080 (REST API for notes)

The hooks server manages state lifecycle:
  - On /run: loads persisted state from S3 (keyed by clientId)
  - On /terminate: saves current state to S3
  - On /suspend: saves state as precaution

The main app provides the user-facing API to create/list/delete notes.
"""

import logging
import threading

from app.hooks_server import run_hooks_server
from app.main_app import run_app_server

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)

logger = logging.getLogger("entrypoint")


def main():
    logger.info("Starting Lambda MicroVM Sticky Notes Board demo")
    logger.info("  - Hooks server: port 9000")
    logger.info("  - Notes API:    port 8080")

    # Start hooks server in a background thread
    hooks_thread = threading.Thread(target=run_hooks_server, daemon=True)
    hooks_thread.start()

    # Run the main app on the main thread
    run_app_server(port=8080)


if __name__ == "__main__":
    main()
