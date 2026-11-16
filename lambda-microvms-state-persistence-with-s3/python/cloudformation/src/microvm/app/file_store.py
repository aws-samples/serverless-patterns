"""
File storage for the Sticky Notes Board.

Files live in the MicroVM's LOCAL filesystem while the MicroVM is alive. They
are only pushed to / pulled from S3 at state-persistence boundaries, exactly
like the notes board:

  - /run       -> sync_from_s3(): download this client's files from S3 into
                  the local files dir (restore last session's files)
  - /suspend   -> sync_to_s3():  upload local files to S3 (precaution)
  - /terminate -> sync_to_s3():  upload local files to S3 (last chance)

Local layout:   <FILES_DIR>/<filename>
S3 layout:      s3://<bucket>/microvm-files/<clientId>/<filename>

While the MicroVM runs, uploads/downloads/edits all hit the local filesystem,
so they are fast and do not touch S3. One client == one MicroVM session, so a
single local dir (no per-client subdir) is all we need on the box.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import boto3
from botocore.exceptions import ClientError

# Shared bucket with the note state store; set at runtime by the /run hook.
from app import state_store

logger = logging.getLogger(__name__)

# Local directory where files are kept while the MicroVM is running.
FILES_DIR = os.environ.get("FILES_DIR", "/tmp/microvm-files")
# S3 key prefix under which a client's files are persisted.
FILES_PREFIX = os.environ.get("FILES_PREFIX", "microvm-files/")

# Extensions / content-types we treat as editable text in the UI.
_TEXT_EXTENSIONS = {
    ".txt", ".md", ".markdown", ".json", ".yaml", ".yml", ".xml", ".csv",
    ".tsv", ".log", ".ini", ".cfg", ".conf", ".toml", ".env", ".properties",
    ".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".htm", ".css", ".scss",
    ".sh", ".bash", ".zsh", ".sql", ".java", ".c", ".h", ".cpp", ".go",
    ".rs", ".rb", ".php", ".pl", ".r", ".kt", ".swift", ".gradle",
}


@dataclass
class StoredFile:
    name: str
    size: int
    content_type: str
    last_modified: str
    is_text: bool


# ----- helpers -----------------------------------------------------------

def _ensure_dir() -> str:
    os.makedirs(FILES_DIR, exist_ok=True)
    return FILES_DIR


def _safe_path(filename: str) -> str:
    """Resolve a filename to a path inside FILES_DIR, blocking traversal."""
    name = os.path.basename(filename).strip()
    if not name or name in (".", ".."):
        raise ValueError("invalid filename")
    return os.path.join(_ensure_dir(), name)


def is_text_file(filename: str, content_type: str = "") -> bool:
    """Decide whether a file should be treated as editable text."""
    _, ext = os.path.splitext(filename.lower())
    if ext in _TEXT_EXTENSIONS:
        return True
    if content_type.startswith("text/"):
        return True
    if content_type in ("application/json", "application/xml", "application/x-yaml"):
        return True
    return False


def _guess_content_type(filename: str) -> str:
    return "text/plain" if is_text_file(filename) else "application/octet-stream"


# ----- local filesystem operations (used while MicroVM is running) -------

def list_files(client_id: str | None = None) -> list[dict]:
    """List files currently in the local MicroVM filesystem."""
    directory = _ensure_dir()
    results: list[dict] = []
    for name in sorted(os.listdir(directory)):
        full = os.path.join(directory, name)
        if not os.path.isfile(full):
            continue
        stat = os.stat(full)
        results.append(
            StoredFile(
                name=name,
                size=stat.st_size,
                content_type=_guess_content_type(name),
                last_modified=_iso(stat.st_mtime),
                is_text=is_text_file(name),
            ).__dict__
        )
    return results


def save_file(client_id: str | None, filename: str, data: bytes, content_type: str = "") -> bool:
    """Write (or overwrite) a file in the local filesystem."""
    try:
        path = _safe_path(filename)
    except ValueError:
        logger.warning("Rejected unsafe filename: %r", filename)
        return False
    try:
        with open(path, "wb") as f:
            f.write(data)
        logger.info("File saved locally: %s (%d bytes)", path, len(data))
        return True
    except OSError as e:
        logger.error("Failed to write file locally: %s", e)
        return False


def load_file(client_id: str | None, filename: str) -> tuple[bytes, str] | None:
    """Read a file's bytes and content-type from local disk."""
    try:
        path = _safe_path(filename)
    except ValueError:
        return None
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "rb") as f:
            data = f.read()
        return data, _guess_content_type(filename)
    except OSError as e:
        logger.error("Failed to read file locally: %s", e)
        return None


def delete_file(client_id: str | None, filename: str) -> bool:
    """Delete a file from local disk."""
    try:
        path = _safe_path(filename)
    except ValueError:
        return False
    if not os.path.isfile(path):
        return False
    try:
        os.remove(path)
        logger.info("File deleted locally: %s", path)
        return True
    except OSError as e:
        logger.error("Failed to delete file locally: %s", e)
        return False


# ----- S3 sync (used only at lifecycle boundaries) -----------------------

def sync_to_s3(client_id: str) -> int:
    """
    Upload every local file to S3 under this client's prefix. Mirrors the
    local dir to S3 (deletes S3 objects that no longer exist locally).
    Returns the number of files uploaded.
    """
    bucket = state_store._get_bucket()
    if not bucket:
        logger.warning("STATE_BUCKET not set, skipping file sync to S3")
        return 0

    directory = _ensure_dir()
    prefix = f"{FILES_PREFIX}{client_id}/"
    s3 = boto3.client("s3")

    local_names = {
        n for n in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, n))
    }

    uploaded = 0
    for name in local_names:
        path = os.path.join(directory, name)
        try:
            with open(path, "rb") as f:
                s3.put_object(
                    Bucket=bucket,
                    Key=f"{prefix}{name}",
                    Body=f.read(),
                    ContentType=_guess_content_type(name),
                )
            uploaded += 1
        except (OSError, ClientError) as e:
            logger.error("Failed to upload %s to S3: %s", name, e)

    # Remove S3 objects that were deleted locally so S3 reflects current state.
    try:
        _prune_s3(s3, bucket, prefix, keep=local_names)
    except ClientError as e:
        logger.error("Failed to prune S3 files: %s", e)

    logger.info("Synced %d files to s3://%s/%s", uploaded, bucket, prefix)
    return uploaded


def sync_from_s3(client_id: str) -> int:
    """
    Download this client's files from S3 into the local dir (restore).
    Clears the local dir first so it reflects exactly what is in S3.
    Returns the number of files restored.
    """
    bucket = state_store._get_bucket()
    if not bucket:
        logger.warning("STATE_BUCKET not set, cannot restore files from S3")
        return 0

    directory = _ensure_dir()
    # Start from a clean local dir for this session.
    for name in os.listdir(directory):
        full = os.path.join(directory, name)
        if os.path.isfile(full):
            try:
                os.remove(full)
            except OSError:
                pass

    prefix = f"{FILES_PREFIX}{client_id}/"
    s3 = boto3.client("s3")
    restored = 0
    try:
        paginator = s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                name = obj["Key"][len(prefix):]
                if not name:
                    continue
                try:
                    resp = s3.get_object(Bucket=bucket, Key=obj["Key"])
                    with open(os.path.join(directory, os.path.basename(name)), "wb") as f:
                        f.write(resp["Body"].read())
                    restored += 1
                except (OSError, ClientError) as e:
                    logger.error("Failed to restore %s from S3: %s", name, e)
    except ClientError as e:
        logger.error("Failed to list files in S3: %s", e)
        return restored

    logger.info("Restored %d files from s3://%s/%s", restored, bucket, prefix)
    return restored


def _prune_s3(s3, bucket: str, prefix: str, keep: set[str]) -> None:
    """Delete S3 objects under prefix whose basename isn't in `keep`."""
    paginator = s3.get_paginator("list_objects_v2")
    to_delete = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            name = obj["Key"][len(prefix):]
            if name and name not in keep:
                to_delete.append({"Key": obj["Key"]})
    if to_delete:
        s3.delete_objects(Bucket=bucket, Delete={"Objects": to_delete})
        logger.info("Pruned %d stale files from S3", len(to_delete))


def _iso(mtime: float) -> str:
    from datetime import datetime, timezone
    return datetime.fromtimestamp(mtime, tz=timezone.utc).isoformat()
