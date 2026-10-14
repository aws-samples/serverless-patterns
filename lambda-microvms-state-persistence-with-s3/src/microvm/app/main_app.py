"""
Main application server - Sticky Notes Board REST API.
Runs on port 8080 (the default proxy port for MicroVM ingress).

Endpoints
---------
Notes:
  GET    /                 service status
  GET    /health           health check
  GET    /notes            list all notes
  POST   /notes            create a note
  GET    /notes/{id}       get one note
  PUT    /notes/{id}       edit a note (content/color/position)
  DELETE /notes/{id}       delete a note

Files (any type, persisted to S3 per client):
  GET    /files            list stored files
  POST   /files            upload a file (raw body, name via X-File-Name header)
  GET    /files/{name}     download a file (binary)
  GET    /files/{name}/text get a text file's contents as JSON (for editing)
  PUT    /files/{name}/text overwrite a text file's contents
  DELETE /files/{name}     delete a file

All responses include permissive CORS headers so a browser UI served from a
different origin can call the API with the X-aws-proxy-auth token.
"""

from __future__ import annotations

import json
import logging
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

from app.notes_board import Board
from app import file_store

logger = logging.getLogger(__name__)

# Global board instance — initialized by the lifecycle hooks server
board: Board | None = None

# Max bytes for a single file upload. This app is only reached through the
# session middleware's Lambda proxy, whose binding constraint is Lambda's 6 MB
# synchronous payload cap — not this app's own buffering. Keep this aligned with
# the middleware's MAX_UPLOAD_BYTES (~5.4 MB) so the app's 413 matches reality
# instead of accepting files the proxy can never deliver.
MAX_UPLOAD_BYTES = int(6 * 1024 * 1024 * 0.9)  # ~5.4 MB, matches middleware


def set_board(b: Board):
    global board
    board = b


def get_board() -> Board | None:
    return board


class NotesHandler(BaseHTTPRequestHandler):

    # ----- routing -------------------------------------------------------

    def do_OPTIONS(self):
        # CORS preflight
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def do_GET(self):
        path = self._path()
        if path == "/":
            self._send_json(200, {
                "service": "Sticky Notes Board",
                "status": "running",
                "client_id": board.client_id if board else "uninitialized",
                "note_count": len(board.notes) if board else 0,
                "hint": "POST /notes to add a note, GET /notes to list all",
            })
        elif path == "/health":
            self._send_json(200, {"status": "healthy"})
        elif path == "/notes":
            if not self._require_board():
                return
            self._send_json(200, board.to_dict())
        elif path == "/files":
            if not self._require_board():
                return
            self._send_json(200, {"files": file_store.list_files(board.client_id)})
        elif path.startswith("/files/") and path.endswith("/text"):
            self._get_file_text(self._file_name(path, suffix="/text"))
        elif path.startswith("/files/"):
            self._download_file(self._file_name(path))
        elif path.startswith("/notes/"):
            if not self._require_board():
                return
            note = board.get_note(path.split("/")[-1])
            if note:
                self._send_json(200, note.to_dict())
            else:
                self._send_json(404, {"error": "Note not found"})
        else:
            self._send_json(404, {"error": "Not found"})

    def do_POST(self):
        path = self._path()
        if path == "/notes":
            self._create_note()
        elif path == "/files":
            self._upload_file()
        else:
            self._send_json(404, {"error": "Not found"})

    def do_PUT(self):
        path = self._path()
        if path.startswith("/files/") and path.endswith("/text"):
            self._put_file_text(self._file_name(path, suffix="/text"))
        elif path.startswith("/notes/"):
            self._update_note(path.split("/")[-1])
        else:
            self._send_json(404, {"error": "Not found"})

    def do_DELETE(self):
        path = self._path()
        if path.startswith("/files/"):
            self._delete_file(self._file_name(path))
        elif path.startswith("/notes/"):
            self._delete_note(path.split("/")[-1])
        else:
            self._send_json(404, {"error": "Not found"})

    # ----- notes handlers ------------------------------------------------

    def _create_note(self):
        if not self._require_board():
            return
        body = self._read_json_body()
        if body is None:
            return
        content = body.get("content", "")
        if not content:
            self._send_json(400, {"error": "'content' is required"})
            return
        note = board.add_note(
            content=content,
            color=body.get("color", "yellow"),
            position_x=body.get("position_x", 0),
            position_y=body.get("position_y", 0),
        )
        logger.info("Note added: %s (total: %d)", note.id, len(board.notes))
        self._send_json(201, {
            "message": "Note created",
            "note": note.to_dict(),
            "total_notes": len(board.notes),
        })

    def _update_note(self, note_id: str):
        if not self._require_board():
            return
        body = self._read_json_body()
        if body is None:
            return
        note = board.update_note(
            note_id,
            content=body.get("content"),
            color=body.get("color"),
            position_x=body.get("position_x"),
            position_y=body.get("position_y"),
        )
        if note is None:
            self._send_json(404, {"error": "Note not found"})
            return
        logger.info("Note updated: %s", note_id)
        self._send_json(200, {"message": "Note updated", "note": note.to_dict()})

    def _delete_note(self, note_id: str):
        if not self._require_board():
            return
        if board.remove_note(note_id):
            self._send_json(200, {"message": f"Note '{note_id}' deleted"})
        else:
            self._send_json(404, {"error": "Note not found"})

    # ----- file handlers -------------------------------------------------

    def _upload_file(self):
        if not self._require_board():
            return
        filename = self.headers.get("X-File-Name", "").strip()
        if not filename:
            self._send_json(400, {"error": "X-File-Name header is required"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            length = 0
        if length <= 0:
            self._send_json(400, {"error": "Empty upload"})
            return
        if length > MAX_UPLOAD_BYTES:
            self._send_json(413, {"error": "File too large"})
            return
        data = self.rfile.read(length)
        content_type = self.headers.get("Content-Type", "")
        ok = file_store.save_file(board.client_id, filename, data, content_type)
        if ok:
            self._send_json(201, {
                "message": "File uploaded",
                "name": filename,
                "size": len(data),
                "is_text": file_store.is_text_file(filename, content_type),
            })
        else:
            self._send_json(500, {"error": "Failed to store file"})

    def _download_file(self, filename: str):
        if not self._require_board():
            return
        result = file_store.load_file(board.client_id, filename)
        if result is None:
            self._send_json(404, {"error": "File not found"})
            return
        data, content_type = result
        self.send_response(200)
        self._cors_headers()
        self.send_header("Content-Type", content_type or "application/octet-stream")
        self.send_header(
            "Content-Disposition", f'attachment; filename="{filename}"'
        )
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _get_file_text(self, filename: str):
        if not self._require_board():
            return
        result = file_store.load_file(board.client_id, filename)
        if result is None:
            self._send_json(404, {"error": "File not found"})
            return
        data, content_type = result
        if not file_store.is_text_file(filename, content_type):
            self._send_json(415, {"error": "File is not a text file"})
            return
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            self._send_json(415, {"error": "File is not valid UTF-8 text"})
            return
        self._send_json(200, {
            "name": filename,
            "content_type": content_type,
            "content": text,
        })

    def _put_file_text(self, filename: str):
        if not self._require_board():
            return
        body = self._read_json_body()
        if body is None:
            return
        if "content" not in body:
            self._send_json(400, {"error": "'content' is required"})
            return
        content_type = "text/plain; charset=utf-8"
        data = body["content"].encode("utf-8")
        ok = file_store.save_file(board.client_id, filename, data, content_type)
        if ok:
            self._send_json(200, {"message": "File saved", "name": filename, "size": len(data)})
        else:
            self._send_json(500, {"error": "Failed to save file"})

    def _delete_file(self, filename: str):
        if not self._require_board():
            return
        if file_store.delete_file(board.client_id, filename):
            self._send_json(200, {"message": f"File '{filename}' deleted"})
        else:
            self._send_json(404, {"error": "File not found"})

    # ----- helpers -------------------------------------------------------

    def _path(self) -> str:
        return urllib.parse.urlparse(self.path).path

    def _file_name(self, path: str, suffix: str = "") -> str:
        raw = path[len("/files/"):]
        if suffix and raw.endswith(suffix):
            raw = raw[: -len(suffix)]
        return urllib.parse.unquote(raw)

    def _require_board(self) -> bool:
        if not board:
            self._send_json(503, {"error": "Board not initialized"})
            return False
        return True

    def _read_json_body(self) -> dict | None:
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            return json.loads(raw) if raw else {}
        except (json.JSONDecodeError, ValueError) as e:
            self._send_json(400, {"error": f"Invalid JSON: {e}"})
            return None

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type, X-aws-proxy-auth, X-File-Name",
        )

    def _send_json(self, status: int, data: dict):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self._cors_headers()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        logger.debug("HTTP %s", format % args)


def run_app_server(port: int = 8080):
    server = HTTPServer(("0.0.0.0", port), NotesHandler)
    logger.info("Notes Board API listening on port %d", port)
    server.serve_forever()
