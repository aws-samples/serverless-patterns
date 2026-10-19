"""
Lifecycle Hooks Server for Lambda MicroVM.

Listens on port 9000 and handles MicroVM lifecycle hooks:
  POST .../ready     — signals the app is ready for snapshotting (build-time)
  POST .../run       — called once after boot from snapshot; loads state from S3
  POST .../resume    — called after suspend → running transition
  POST .../suspend   — called before running → suspended transition
  POST .../terminate — called before termination; saves state to S3

The /run hook receives a JSON body with microvmId and runHookPayload.
The runHookPayload contains the clientId, used to isolate each client's state in S3.
"""

import json
import logging
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from app.notes_board import Board
from app.state_store import save_state, load_state
from app.main_app import set_board, get_board
from app import file_store

logger = logging.getLogger(__name__)

HOOKS_PORT = int(os.environ.get("HOOKS_PORT", "9000"))


class HooksHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        body = self._read_body()

        if self.path.endswith("/ready"):
            logger.info("/ready — snapshot point reached")
            self._send_response(200, {"status": "ready"})

        elif self.path.endswith("/run"):
            self._handle_run(body)

        elif self.path.endswith("/resume"):
            self._handle_resume(body)

        elif self.path.endswith("/suspend"):
            self._handle_suspend(body)

        elif self.path.endswith("/terminate"):
            self._handle_terminate(body)

        else:
            logger.warning("Unknown hook path: %s", self.path)
            self._send_response(404, {"error": "unknown hook"})

    def _handle_run(self, payload: dict):
        """
        Called once when the MicroVM boots from snapshot.
        The payload contains microvmId and runHookPayload (string).
        The runHookPayload has our clientId for state isolation.

        IMPORTANT: Respond 200 immediately, then load state in background.
        The hook timeout is short — we can't block on S3 calls.
        """
        logger.info("/run — payload: %s", json.dumps(payload))

        # Parse runHookPayload — it arrives as a JSON string
        run_hook_payload = payload.get("runHookPayload", "{}")
        if isinstance(run_hook_payload, str):
            try:
                run_hook_payload = json.loads(run_hook_payload)
            except json.JSONDecodeError:
                run_hook_payload = {}

        client_id = run_hook_payload.get("clientId", "default")
        microvm_id = payload.get("microvmId", "unknown")
        state_bucket = run_hook_payload.get("stateBucket", "")
        logger.info("/run — client_id: %s, microvm_id: %s, bucket: %s", client_id, microvm_id, state_bucket)

        # Set the state bucket for the state_store module
        if state_bucket:
            from app.state_store import set_bucket
            set_bucket(state_bucket)

        # Respond 200 immediately so the hook doesn't timeout
        self._send_response(200, {
            "status": "running",
            "client_id": client_id,
        })

        # Load state from S3 in background thread
        def _load_state_background():
            board = load_state(client_id)
            if board:
                logger.info(
                    "/run — restored board for client '%s' with %d notes",
                    client_id,
                    len(board.notes),
                )
            else:
                board = Board(client_id=client_id)
                logger.info(
                    "/run — no previous state, created fresh board for client '%s'",
                    client_id,
                )
            set_board(board)

            # Restore this client's uploaded files from S3 into the local
            # MicroVM filesystem. Files only live on S3 between sessions.
            try:
                restored = file_store.sync_from_s3(client_id)
                logger.info("/run — restored %d files from S3", restored)
            except Exception as e:  # pragma: no cover - defensive
                logger.error("/run — failed to restore files: %s", e)

        threading.Thread(target=_load_state_background, daemon=True).start()

    def _handle_resume(self, payload: dict):
        """Called after suspend → running transition. State is already in memory."""
        logger.info("/resume — MicroVM resumed")
        self._send_response(200, {"status": "resumed"})

    def _handle_suspend(self, payload: dict):
        """Called before running → suspended. Save state to S3 as precaution."""
        logger.info("/suspend — saving state before suspend")
        board = get_board()
        if board:
            save_state(board)
            uploaded = file_store.sync_to_s3(board.client_id)
            logger.info(
                "/suspend — state saved (%d notes, %d files)",
                len(board.notes),
                uploaded,
            )
        self._send_response(200, {"status": "suspending"})

    def _handle_terminate(self, payload: dict):
        """
        Called before termination. This is our last chance to persist state.
        Save the full board state to S3 so the next MicroVM can restore it.
        """
        logger.info("/terminate — saving state before termination")
        board = get_board()
        if board:
            success = save_state(board)
            uploaded = file_store.sync_to_s3(board.client_id)
            logger.info(
                "/terminate — state %s (%d notes, %d files)",
                "saved" if success else "FAILED to save",
                len(board.notes),
                uploaded,
            )
        else:
            logger.warning("/terminate — no board to save")

        self._send_response(200, {"status": "terminating"})

    def _read_body(self) -> dict:
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            return json.loads(raw) if raw else {}
        except (json.JSONDecodeError, ValueError):
            return {}

    def _send_response(self, status: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        logger.info("HOOK %s", format % args)


def run_hooks_server(port: int = HOOKS_PORT):
    server = HTTPServer(("0.0.0.0", port), HooksHandler)
    logger.info("Lifecycle hooks server listening on port %d", port)
    server.serve_forever()
