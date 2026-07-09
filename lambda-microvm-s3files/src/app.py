"""
Lambda MicroVMs + S3 Files demo application.

S3 Files (https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html) is a
shared NFS 4.2 file system, built on EFS, that presents an S3 bucket (or a prefix of
one) as a POSIX file tree. You read/write files on a local mount path and S3 Files
synchronizes changes to and from the bucket in both directions.

This app exposes the mounted tree over HTTP so you can prove the round-trip:

  GET  /                  -> status + whether the file system is mounted
  GET  /files             -> list the mount root
  GET  /files/<path>      -> list a directory, or read a file
  PUT  /files/<path>      -> write a file (body = contents); syncs to S3
  DELETE /files/<path>    -> delete a file
  GET  /sync-proof        -> write a uniquely-named file and report where it
                             will appear in S3 (s3://<bucket>/<prefix>/<name>)
  GET  /lifecycle         -> everything the hooks have recorded so far

Two HTTP listeners:
  - Application:   port 8080  (the service the client talks to)
  - Lifecycle:     port 9000  (hooks the platform invokes)

The S3 Files mount is NOT part of the snapshot: the VPC egress network connector and
the execution-role credentials are bound at run time, and the NFS connection is killed
across snapshot/suspend. So we mount in the /run hook and re-mount in /resume. See
hook_run() / hook_resume() below.

Hooks live at POST /aws/lambda-microvms/runtime/v1/{ready,validate,run,resume,suspend,terminate}.
"""
import json
import os
import secrets
import shutil
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, request, Response

# ---------------------------------------------------------------------------
# Configuration. Anything that is the SAME for every MicroVM can be a build-time
# env var (burnt into the snapshot). Anything per-VM (the file system to mount,
# its mount-target IP) arrives in the /run hook payload — never in the snapshot.
# ---------------------------------------------------------------------------
MOUNT_PATH = os.environ.get("S3FILES_MOUNT_PATH", "/mnt/s3files")
HOOK_PATH = "/aws/lambda-microvms/runtime/v1"

# Populated from the /run (and /resume) hook payload. Live mount status is NOT
# tracked here — _is_mounted() derives it authoritatively from findmnt.
MOUNT = {
    "file_system_id": None,
    "access_point_id": None,
    "mount_target_ip": None,
    "region": None,
    "bucket": None,
    "prefix": None,
    "last_error": None,
}

STATE = {
    "boot_time": datetime.now(timezone.utc).isoformat(),
    "host": socket.gethostname(),
    "instance_id": secrets.token_hex(8),
    "request_count": 0,
    "lifecycle_events": [],
}


def log(msg, **kw):
    """Structured log so it shows up cleanly in CloudWatch."""
    print(json.dumps({"ts": datetime.now(timezone.utc).isoformat(), "msg": msg, **kw}), flush=True)


def record_event(name, detail=None):
    STATE["lifecycle_events"].append(
        {"event": name, "at": datetime.now(timezone.utc).isoformat(), "detail": detail}
    )
    log(f"lifecycle:{name}", detail=detail)


# ---------------------------------------------------------------------------
# S3 Files mount helpers
# ---------------------------------------------------------------------------
def _is_mounted() -> bool:
    """True if something is mounted at MOUNT_PATH (survives stale MOUNT dict)."""
    try:
        out = subprocess.run(
            ["findmnt", "-T", MOUNT_PATH, "-n"],
            capture_output=True, text=True, timeout=5,
        )
        return out.returncode == 0 and bool(out.stdout.strip())
    except Exception:
        return False


def _mount_usable(timeout: int = 5) -> bool:
    """True once the mount actually carries I/O, not just once findmnt sees it.

    amazon-efs-utils registers the mountpoint (so `findmnt` reports it) a few
    seconds before the efs-proxy TLS tunnel is fully carrying data. A file written
    in that window lands *under* the not-yet-ready mount and never syncs to S3.
    Do a write -> read -> delete round trip on the mount (bounded by `timeout` via
    subprocess so a stuck tunnel can't hang the run hook) and only treat the mount
    as ready once it succeeds. The probe file is a hidden dotfile that is removed
    immediately, so it leaves nothing behind in the bucket."""
    probe = f"{MOUNT_PATH}/.s3files-readycheck-{secrets.token_hex(4)}"
    try:
        res = subprocess.run(
            ["sh", "-c", f'echo ready > "{probe}" && cat "{probe}" >/dev/null && rm -f "{probe}"'],
            capture_output=True, text=True, timeout=timeout,
        )
        return res.returncode == 0
    except Exception:
        return False


def mount_s3files() -> bool:
    """Mount the S3 file system at MOUNT_PATH using the amazon-efs-utils helper.

    Uses `mount -t s3files`. The helper always adds TLS + IAM. We pass the
    mount-target IP explicitly (`-o mounttargetip=`) because a MicroVM reaches
    the file system over a VPC egress connector — the regional mount-target DNS
    name may not resolve from inside the guest, but the AZ-local mount-target IP
    always works. An access point scopes us to a sub-directory and pins the
    POSIX uid/gid.
    """
    fsid = MOUNT["file_system_id"]
    if not fsid:
        MOUNT["last_error"] = "no file_system_id in run payload"
        log("mount_skipped", reason=MOUNT["last_error"])
        return False

    if _is_mounted():
        log("mount_already_present", path=MOUNT_PATH)
        return True

    Path(MOUNT_PATH).mkdir(parents=True, exist_ok=True)

    opts = ["tls", "iam"]
    if MOUNT.get("access_point_id"):
        opts.append(f"accesspoint={MOUNT['access_point_id']}")
    if MOUNT.get("mount_target_ip"):
        opts.append(f"mounttargetip={MOUNT['mount_target_ip']}")
    if MOUNT.get("region"):
        opts.append(f"region={MOUNT['region']}")

    cmd = ["mount", "-t", "s3files", "-o", ",".join(opts), f"{fsid}:/", MOUNT_PATH]
    log("mount_attempt", cmd=" ".join(cmd))
    try:
        # This whole function runs inside the /run (or /resume) hook, which the
        # platform bounds by RunTimeoutInSeconds (60, the max). Keep the worst
        # case comfortably under that: mount is capped at 35s and the readiness
        # probe below at a ~12s deadline (~50s worst case). If either stage runs
        # long, we return False and the app reports mounted:false rather than
        # letting the hook get killed mid-mount.
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
        if res.returncode != 0 or not _is_mounted():
            MOUNT["last_error"] = (res.stderr or res.stdout or "mount failed").strip()
            log("mount_failed", rc=res.returncode, err=MOUNT["last_error"])
            return False
        # The mount is registered, but the efs-proxy TLS tunnel may still be
        # coming up. Block until a real I/O round trip succeeds so callers (and
        # run.sh) never see mounted=true before the mount can actually carry data
        # — otherwise a write issued immediately after run can be lost. Bound by a
        # monotonic deadline (not an iteration count) because each probe can hang
        # up to its own timeout when the tunnel is not yet carrying I/O; in the
        # happy path the very first probe succeeds in well under a second.
        probe_deadline = time.monotonic() + 12
        while time.monotonic() < probe_deadline:
            if _mount_usable(timeout=3):
                MOUNT["last_error"] = None
                log("mount_ok", path=MOUNT_PATH)
                return True
            time.sleep(1)
        MOUNT["last_error"] = "mount registered but not usable (efs-proxy tunnel not ready)"
        log("mount_not_usable", err=MOUNT["last_error"])
        return False
    except Exception as e:  # noqa: BLE001
        MOUNT["last_error"] = str(e)
        log("mount_exception", err=str(e))
        return False


def _apply_run_payload(raw: str):
    """Parse the /run (or /resume) hook body and pull out mount parameters.

    The platform wraps our payload in an envelope:
        { "microvmId": "...", "runHookPayload": <our-json> }
    where `runHookPayload` is the opaque blob passed to RunMicrovm. Its value may
    arrive as a JSON string or as an already-parsed object. We unwrap that key
    (or the alternate `runPayload`), and also accept a bare, unwrapped payload.
    """
    if not raw:
        return
    try:
        env = json.loads(raw)
    except Exception:
        log("run_payload_not_json", sample=raw[:200])
        return
    inner = env
    if isinstance(env, dict):
        val = next((env[k] for k in ("runHookPayload", "runPayload") if k in env), env)
        if isinstance(val, dict):
            inner = val
        elif isinstance(val, str):
            try:
                inner = json.loads(val)
            except Exception:
                pass
    if not isinstance(inner, dict):
        return
    for k_src, k_dst in (
        ("fileSystemId", "file_system_id"),
        ("accessPointId", "access_point_id"),
        ("mountTargetIp", "mount_target_ip"),
        ("region", "region"),
        ("bucket", "bucket"),
        ("prefix", "prefix"),
    ):
        if inner.get(k_src):
            MOUNT[k_dst] = inner[k_src]


# ---------------------------------------------------------------------------
# Path safety: keep every file operation inside MOUNT_PATH.
# ---------------------------------------------------------------------------
def _safe_target(rel: str) -> Path:
    base = Path(MOUNT_PATH).resolve()
    target = (base / rel.lstrip("/")).resolve()
    if target != base and base not in target.parents:
        raise ValueError("path escapes the mount root")
    return target


# ---------------------------------------------------------------------------
# Application server (port 8080)
# ---------------------------------------------------------------------------
app = Flask("s3files-demo")


@app.get("/")
def index():
    STATE["request_count"] += 1
    return jsonify(
        {
            "service": "lambda-microvms-s3files-demo",
            "message": "S3 bucket mounted as a file system inside a Firecracker microVM",
            "instance_id": STATE["instance_id"],
            "host": STATE["host"],
            "boot_time": STATE["boot_time"],
            "now": datetime.now(timezone.utc).isoformat(),
            "request_count": STATE["request_count"],
            "python": sys.version.split()[0],
            "mount": {
                "path": MOUNT_PATH,
                "mounted": _is_mounted(),
                "file_system_id": MOUNT["file_system_id"],
                "access_point_id": MOUNT["access_point_id"],
                "bucket": MOUNT["bucket"],
                "prefix": MOUNT["prefix"],
                "last_error": MOUNT["last_error"],
            },
            "endpoints": ["/files", "/files/<path>", "/sync-proof", "/lifecycle"],
        }
    )


def _require_mount():
    if not _is_mounted():
        return (
            jsonify(
                {
                    "error": "s3files not mounted",
                    "hint": "the /run hook mounts the file system; check /lifecycle and CloudWatch",
                    "last_error": MOUNT["last_error"],
                }
            ),
            503,
        )
    return None


@app.get("/files")
@app.get("/files/")
@app.get("/files/<path:rel>")
def get_files(rel=""):
    """List a directory, or stream a file if `rel` points at one."""
    guard = _require_mount()
    if guard:
        return guard
    try:
        target = _safe_target(rel)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if not target.exists():
        return jsonify({"error": "not found", "path": f"/{rel}"}), 404

    if target.is_dir():
        entries = []
        for child in sorted(target.iterdir(), key=lambda p: (p.is_file(), p.name)):
            st = child.stat()
            entries.append(
                {
                    "name": child.name + ("/" if child.is_dir() else ""),
                    "type": "dir" if child.is_dir() else "file",
                    "size": st.st_size if child.is_file() else None,
                    "modified": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(),
                }
            )
        return jsonify({"path": "/" + rel.strip("/"), "entries": entries})

    # File: stream it back. Large reads are served straight from S3 by S3 Files.
    data = target.read_bytes()
    return Response(data, mimetype="application/octet-stream")


@app.put("/files/<path:rel>")
def put_file(rel):
    """Write a file. The bytes land on the high-performance storage and S3 Files
    exports them to the bucket (typically within ~1 minute)."""
    guard = _require_mount()
    if guard:
        return guard
    try:
        target = _safe_target(rel)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    target.parent.mkdir(parents=True, exist_ok=True)
    body = request.get_data()
    target.write_bytes(body)
    st = target.stat()
    log("file_written", path=f"/{rel}", bytes=st.st_size)
    return (
        jsonify(
            {
                "written": "/" + rel,
                "bytes": st.st_size,
                "syncs_to_s3": _s3_uri(rel),
                "note": "S3 Files exports changes to the bucket asynchronously (~1 min).",
            }
        ),
        201,
    )


@app.delete("/files/<path:rel>")
def delete_file(rel):
    guard = _require_mount()
    if guard:
        return guard
    try:
        target = _safe_target(rel)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if not target.exists():
        return jsonify({"error": "not found"}), 404
    if target.is_dir():
        shutil.rmtree(target)
    else:
        target.unlink()
    log("file_deleted", path=f"/{rel}")
    return jsonify({"deleted": "/" + rel})


def _s3_uri(rel: str) -> str:
    if not MOUNT["bucket"]:
        return "(set bucket in run payload to compute the s3:// path)"
    parts = [MOUNT["bucket"]]
    if MOUNT["prefix"]:
        parts.append(MOUNT["prefix"].strip("/"))
    parts.append(rel.strip("/"))
    return "s3://" + "/".join(p for p in parts if p)


@app.get("/sync-proof")
def sync_proof():
    """Write a uniquely-named file through the mount and report where it will
    appear in S3. Poll the bucket (or `aws s3 ls`) to watch it sync out."""
    guard = _require_mount()
    if guard:
        return guard
    name = f"sync-proof/{STATE['instance_id']}-{secrets.token_hex(4)}.txt"
    target = _safe_target(name)
    target.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat()
    target.write_text(f"written by microVM {STATE['instance_id']} at {stamp}\n")
    log("sync_proof_written", path=f"/{name}")
    return jsonify(
        {
            "wrote_file": "/" + name,
            "on_mount": f"{MOUNT_PATH}/{name}",
            "will_appear_in_s3_at": _s3_uri(name),
            "verify": f"aws s3 ls {_s3_uri(name)}",
            "written_at": stamp,
        }
    )


@app.get("/lifecycle")
def lifecycle():
    return jsonify(
        {
            "instance_id": STATE["instance_id"],
            "mount": {**MOUNT, "mounted": _is_mounted()},
            "events": STATE["lifecycle_events"],
        }
    )


# ---------------------------------------------------------------------------
# Lifecycle hooks server (port 9000)
# ---------------------------------------------------------------------------
hooks = Flask("s3files-hooks")
_app_ready = threading.Event()


def _simulate_warmup():
    """Pretend the app has some non-trivial init before it's snapshot-ready."""
    time.sleep(1.5)
    _app_ready.set()
    log("warmup_complete")


@hooks.post(f"{HOOK_PATH}/ready")
def hook_ready():
    """Image build: 200 = snapshot-ready, 503 = retry. We do NOT mount here —
    the network connector and credentials don't exist at build time."""
    if _app_ready.is_set():
        record_event("ready")
        return jsonify({"status": "ready"}), 200
    return jsonify({"status": "warming_up"}), 503


@hooks.post(f"{HOOK_PATH}/validate")
def hook_validate():
    """Post-snapshot validation. Exercise the app so the platform can sample
    snapshot pages for prefetch. The mount isn't available here, so we only
    validate the HTTP surface."""
    try:
        with app.test_client() as c:
            ok = c.get("/").status_code == 200
        record_event("validate", detail={"ok": ok})
        return jsonify({"status": "valid" if ok else "invalid"}), 200 if ok else 503
    except Exception as e:  # noqa: BLE001
        log("validate_error", error=str(e))
        return jsonify({"error": str(e)}), 503


@hooks.post(f"{HOOK_PATH}/run")
def hook_run():
    """Fires once after run from snapshot. This is where we (a) reseed per-VM
    identity and (b) mount the S3 file system, using parameters from the run
    payload. Both the connector and the execution-role credentials are now live."""
    STATE["instance_id"] = secrets.token_hex(8)
    STATE["boot_time"] = datetime.now(timezone.utc).isoformat()
    raw = request.get_data(as_text=True) or ""
    _apply_run_payload(raw)
    mounted = mount_s3files()
    record_event(
        "run",
        detail={
            "payload_bytes": len(raw),
            "file_system_id": MOUNT["file_system_id"],
            "mounted": mounted,
        },
    )
    return jsonify({"status": "ok", "mounted": mounted, "instance_id": STATE["instance_id"]}), 200


@hooks.post(f"{HOOK_PATH}/resume")
def hook_resume():
    """Fires after SUSPENDED -> RUNNING. The NFS connection was torn down on
    suspend, so re-mount. Reseed identity entropy too."""
    STATE["instance_id"] = secrets.token_hex(8)
    mounted = mount_s3files()
    record_event("resume", detail={"mounted": mounted, "instance_id": STATE["instance_id"]})
    return jsonify({"status": "ok", "mounted": mounted}), 200


@hooks.post(f"{HOOK_PATH}/suspend")
def hook_suspend():
    """Fires before RUNNING -> SUSPENDED. Acknowledge fast (1-60s timeout)."""
    record_event("suspend")
    return jsonify({"status": "ok"}), 200


@hooks.post(f"{HOOK_PATH}/terminate")
def hook_terminate():
    """Final flush opportunity before the VM goes away."""
    record_event("terminate")
    return jsonify({"status": "ok"}), 200


@hooks.get("/health")
def hook_health():
    return jsonify({"app_ready": _app_ready.is_set(), "mounted": _is_mounted()}), 200


def _run_app():
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8080")),
            threaded=True, use_reloader=False)


def _run_hooks():
    hooks.run(host="0.0.0.0", port=int(os.environ.get("HOOKS_PORT", "9000")),
              threaded=True, use_reloader=False)


if __name__ == "__main__":
    log("startup", pid=os.getpid(), mount_path=MOUNT_PATH)
    threading.Thread(target=_simulate_warmup, daemon=True).start()
    threading.Thread(target=_run_hooks, daemon=True).start()
    _run_app()
