"""
Lambda MicroVMs + Amazon EFS demo application.

Amazon EFS is a fully managed, elastic NFS 4.1 file system. Unlike an object
store bolted onto a POSIX facade, it *is* a shared file system: many MicroVMs
mount the same tree at the same time, see each other's writes, and the data
outlives every one of them. This app exposes the mount over HTTP so you can
prove exactly that:

    GET  /                  -> status + whether the file system is mounted
    GET  /files             -> list the mount root
    GET  /files/<path>      -> list a directory, or read a file
    PUT  /files/<path>      -> write a file (body = contents)
    DELETE /files/<path>    -> delete a file
    GET  /shared-log        -> append this MicroVM's visit to a file on EFS and
                               return the whole history, including entries
                               written by OTHER (and now-terminated) MicroVMs.
                               This is the headline proof: shared, durable state.
    GET  /benchmark/seed    -> create the read-test file (do this once)
    GET  /benchmark         -> measure real read throughput to EFS with parallel
                               O_DIRECT streams, sampled per second
    GET  /lifecycle         -> everything the hooks have recorded so far

Two HTTP listeners:
  - Application: port 8080 (the service the client talks to)
  - Lifecycle:   port 9000 (hooks the platform invokes)

The EFS mount is NOT part of the snapshot. The VPC egress network connector and
the execution-role credentials are bound at run time, and an NFS session does not
survive a snapshot: a resumed MicroVM has a new network identity and may be on a
different host, so a mount captured in the snapshot is dead on arrival and returns
ENOTCONN. So we mount in /run, UNMOUNT in /suspend, and re-mount in /resume.
See hook_run() / hook_suspend() / hook_resume() below.

Hooks live at POST /aws/lambda-microvms/runtime/v1/{ready,validate,run,resume,suspend,terminate}.
"""

import errno
import fcntl
import json
import mmap
import os
import secrets
import shutil
import socket
import statistics
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, Response, jsonify, request

# ---------------------------------------------------------------------------
# Configuration. Anything that is the SAME for every MicroVM can be a build-time
# env var (burnt into the snapshot). Anything per-VM (the file system to mount,
# its mount-target IP) arrives in the /run hook payload — never in the snapshot.
# ---------------------------------------------------------------------------
MOUNT_PATH = os.environ.get("EFS_MOUNT_PATH", "/mnt/efs")
HOOK_PATH = "/aws/lambda-microvms/runtime/v1"

# Shared artefacts on the file system. These are paths every MicroVM agrees on;
# that is the whole point — they are how separate VMs find each other's data.
SHARED_LOG = "shared/visits.jsonl"
BENCH_DIR = ".bench"

# Populated from the /run (and /resume) hook payload. Live mount status is NOT
# tracked here — _is_mounted() derives it authoritatively from /proc/self/mounts.
MOUNT = {
    "file_system_id": None,
    "access_point_id": None,
    "mount_target_ip": None,
    "region": None,
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
# EFS mount helpers
# ---------------------------------------------------------------------------
def _is_mounted() -> bool:
    """True if MOUNT_PATH is itself a mount point, read from /proc/self/mounts.

    Deliberately NOT `findmnt -T <path>` and NOT os.stat(): `findmnt -T` falls back
    to the mount point of the filesystem *containing* the path, so on an unmounted
    directory it happily reports `/` and exits 0 — i.e. it would report "mounted"
    forever. And stat() on a stale NFS mount can return ENOTCONN or hang outright.
    Parsing the mount table for an exact mountpoint match is the only check that is
    both cheap and correct.
    """
    want = os.path.normpath(MOUNT_PATH)
    try:
        with open("/proc/self/mounts", "r") as fh:
            for line in fh:
                parts = line.split()
                if len(parts) < 3:
                    continue
                # Field 2 is the mount point, with octal escapes for odd characters.
                mountpoint = parts[1].encode().decode("unicode_escape")
                if os.path.normpath(mountpoint) == want and parts[2].startswith("nfs"):
                    return True
    except Exception:  # noqa: BLE001
        return False
    return False


def _mount_usable(timeout: int = 5) -> bool:
    """True once the mount actually carries I/O, not just once it appears in the
    mount table.

    amazon-efs-utils registers the mountpoint a few seconds before the efs-proxy
    TLS tunnel is fully carrying data. A file written in that window can land
    under the not-yet-ready mount. Do a write -> read -> delete round trip
    (bounded by `timeout` via subprocess so a stuck tunnel cannot hang the run
    hook) and only treat the mount as ready once it succeeds. The probe file is a
    hidden dotfile removed immediately, so it leaves nothing behind.
    """
    probe = f"{MOUNT_PATH}/.efs-readycheck-{secrets.token_hex(4)}"
    try:
        res = subprocess.run(
            ["sh", "-c", f'echo ready > "{probe}" && cat "{probe}" >/dev/null && rm -f "{probe}"'],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return res.returncode == 0
    except Exception:  # noqa: BLE001
        return False


def mount_efs() -> bool:
    """Mount the EFS file system at MOUNT_PATH using the amazon-efs-utils helper.

    Uses `mount -t efs`, which adds TLS + IAM. We pass the mount-target IP
    explicitly (`-o mounttargetip=`) because a MicroVM reaches the file system
    over a VPC egress connector: the regional mount DNS name may not resolve from
    inside the guest, but the AZ-local mount-target IP always works. An access
    point scopes us to a sub-directory and pins the POSIX uid/gid.
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

    cmd = ["mount", "-t", "efs", "-o", ",".join(opts), f"{fsid}:/", MOUNT_PATH]
    log("mount_attempt", cmd=" ".join(cmd))

    try:
        # This whole function runs inside the /run (or /resume) hook, which the
        # platform bounds by RunTimeoutInSeconds (60, the max). Keep the worst
        # case comfortably under that: mount is capped at 35s and the readiness
        # probe below at a ~12s deadline (~47s worst case). If either stage runs
        # long we return False and the app reports mounted:false rather than
        # letting the hook get killed mid-mount.
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
        if res.returncode != 0 or not _is_mounted():
            MOUNT["last_error"] = (res.stderr or res.stdout or "mount failed").strip()
            log("mount_failed", rc=res.returncode, err=MOUNT["last_error"])
            return False

        # Registered, but the efs-proxy TLS tunnel may still be coming up. Block
        # until a real I/O round trip succeeds so callers never see mounted=true
        # before the mount can carry data. Bounded by a monotonic deadline (not an
        # iteration count) because each probe can hang up to its own timeout; in
        # the happy path the first probe succeeds in well under a second.
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


def unmount_efs() -> bool:
    """Unmount before the VM is suspended.

    An NFS session cannot survive the snapshot, so leaving it mounted guarantees
    the first I/O after resume fails with ENOTCONN (or hangs). Unmounting on the
    way down is what makes the /resume re-mount clean. `-f` (force) then `-l`
    (lazy) so a half-dead tunnel cannot wedge the suspend hook.
    """
    if not _is_mounted():
        return True
    for args in (["umount", "-f", MOUNT_PATH], ["umount", "-l", MOUNT_PATH]):
        try:
            res = subprocess.run(args, capture_output=True, text=True, timeout=5)
            if res.returncode == 0 and not _is_mounted():
                log("unmount_ok", how=" ".join(args))
                return True
        except Exception as e:  # noqa: BLE001
            log("unmount_attempt_failed", how=" ".join(args), err=str(e))
    still = _is_mounted()
    log("unmount_incomplete", still_mounted=still)
    return not still


def _apply_run_payload(raw: str):
    """Parse the /run (or /resume) hook body and pull out mount parameters.

    The platform wraps our payload in an envelope:
        { "microvmId": "...", "runHookPayload": <string|object> }
    where `runHookPayload` is the opaque blob passed to RunMicrovm. Its value may
    arrive as a JSON string or as an already-parsed object. We unwrap that key (or
    the alternate `runPayload`), and also accept a bare, unwrapped payload.
    """
    if not raw:
        return
    try:
        env = json.loads(raw)
    except Exception:  # noqa: BLE001
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
            except Exception as e:  # noqa: BLE001
                log("run_payload_inner_not_json", err=str(e), sample=val[:200])
    if not isinstance(inner, dict):
        return

    for k_src, k_dst in (
        ("fileSystemId", "file_system_id"),
        ("accessPointId", "access_point_id"),
        ("mountTargetIp", "mount_target_ip"),
        ("region", "region"),
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
app = Flask("efs-demo")


@app.get("/")
def index():
    STATE["request_count"] += 1
    return jsonify(
        {
            "service": "lambda-microvms-efs-demo",
            "message": "Amazon EFS mounted as a shared POSIX file system inside a Firecracker microVM",
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
                "mount_target_ip": MOUNT["mount_target_ip"],
                "last_error": MOUNT["last_error"],
            },
            "endpoints": [
                "/files",
                "/files/<path>",
                "/shared-log",
                "/benchmark/seed",
                "/benchmark",
                "/lifecycle",
            ],
        }
    )


def _require_mount():
    if not _is_mounted():
        return (
            jsonify(
                {
                    "error": "efs not mounted",
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

    return Response(target.read_bytes(), mimetype="application/octet-stream")


@app.put("/files/<path:rel>")
def put_file(rel):
    """Write a file. It is durable and visible to every other MicroVM on this
    file system the moment the write returns — no export step, no eventual
    consistency window."""
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
                "on_mount": f"{MOUNT_PATH}/{rel.lstrip('/')}",
                "note": "Immediately readable by any other MicroVM mounting this file system.",
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


# ---------------------------------------------------------------------------
# The headline proof: shared, durable state across MicroVM lifetimes.
# ---------------------------------------------------------------------------
@app.get("/shared-log")
def shared_log():
    """Append this MicroVM's visit to a single file on EFS, then return the whole
    file.

    Every MicroVM that ever mounted this file system has a line in here — so the
    response shows entries from VMs running concurrently with this one AND from
    VMs that were terminated long ago. That is the property EFS gives you and an
    object store does not: one mutable POSIX file, many writers, no sync step.
    """
    guard = _require_mount()
    if guard:
        return guard

    target = _safe_target(SHARED_LOG)
    target.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "instance_id": STATE["instance_id"],
        "host": STATE["host"],
        "at": datetime.now(timezone.utc).isoformat(),
        "boot_time": STATE["boot_time"],
    }

    # O_APPEND plus an advisory lock. NFS 4.1 supports byte-range locks, so this
    # is safe against other MicroVMs appending at the same moment.
    line = (json.dumps(entry) + "\n").encode()
    fd = os.open(str(target), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        fcntl.lockf(fd, fcntl.LOCK_EX)
        try:
            os.write(fd, line)
        finally:
            fcntl.lockf(fd, fcntl.LOCK_UN)
    finally:
        os.close(fd)

    visits = []
    for raw in target.read_text().splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            visits.append(json.loads(raw))
        except Exception:  # noqa: BLE001
            continue

    others = sorted({v.get("instance_id") for v in visits} - {STATE["instance_id"]})
    log("shared_log_appended", total_visits=len(visits), distinct_others=len(others))

    return jsonify(
        {
            "file": "/" + SHARED_LOG,
            "on_mount": f"{MOUNT_PATH}/{SHARED_LOG}",
            "this_instance": STATE["instance_id"],
            "total_visits": len(visits),
            "distinct_instances": len({v.get("instance_id") for v in visits}),
            "other_instances_seen": others,
            "proves": (
                "Entries from other instance_ids are writes by different MicroVMs — "
                "concurrent or already terminated — to this same file."
            ),
            "visits": visits[-50:],
        }
    )


# ---------------------------------------------------------------------------
# Throughput measurement.
#
# EFS traffic leaves the MicroVM over the VPC egress connector, so it is governed
# by the MicroVM's EGRESS bandwidth allocation — NOT by the documented 8-128 Mbps
# request/response figures, which describe the service-managed HTTPS endpoint only.
# Two things matter for measuring it honestly:
#
#   1. O_DIRECT. Without it the guest page cache absorbs re-reads and you measure
#      memory bandwidth, not the network path to EFS.
#   2. Parallel streams. A single stream does not saturate the allocation; 8 is
#      where it flattens out.
#
# Throughput is read from /proc/net/dev inside the guest, so it is bytes on the
# virtual NIC including NFS and TCP overhead — the number comparable to a
# bandwidth allocation. Application payload rate is reported separately.
# ---------------------------------------------------------------------------
def _nic_rx_bytes() -> int:
    total = 0
    try:
        with open("/proc/net/dev", "r") as fh:
            for line in fh:
                if ":" not in line:
                    continue
                name, rest = line.split(":", 1)
                if name.strip() == "lo":
                    continue
                fields = rest.split()
                if fields:
                    total += int(fields[0])
    except Exception:  # noqa: BLE001
        return 0
    return total


def _seed_path(size_mib: int) -> Path:
    return _safe_target(f"{BENCH_DIR}/seed-{size_mib}mib.dat")


@app.get("/benchmark/seed")
def benchmark_seed():
    """Create the file /benchmark reads. Run once per size; it lives on EFS, so
    later MicroVMs reuse it and can skip straight to /benchmark."""
    guard = _require_mount()
    if guard:
        return guard

    size_mib = max(16, min(4096, request.args.get("mib", default=256, type=int)))
    target = _seed_path(size_mib)
    target.parent.mkdir(parents=True, exist_ok=True)

    want = size_mib * (1 << 20)
    if target.exists() and target.stat().st_size >= want:
        return jsonify(
            {"seed": str(target), "size_mib": size_mib, "created": False, "note": "already present"}
        )

    chunk = b"\0" * (1 << 20)
    started = time.monotonic()
    with open(target, "wb") as fh:
        for _ in range(size_mib):
            fh.write(chunk)
        fh.flush()
        os.fsync(fh.fileno())
    elapsed = time.monotonic() - started

    log("bench_seed_written", size_mib=size_mib, seconds=round(elapsed, 2))
    return jsonify(
        {
            "seed": str(target),
            "size_mib": size_mib,
            "created": True,
            "seconds": round(elapsed, 2),
            "write_mib_per_s": round(size_mib / elapsed, 1) if elapsed > 0 else None,
        }
    )


def _reader(path, block, nblocks, idx, nstreams, deadline, results, use_direct):
    """Read `block`-sized aligned chunks in a strided loop until the deadline."""
    flags = os.O_RDONLY
    if use_direct and hasattr(os, "O_DIRECT"):
        flags |= os.O_DIRECT
    total = 0
    try:
        fd = os.open(str(path), flags)
    except OSError as e:
        results[idx] = (0, f"open failed: {e}")
        return
    # An anonymous mmap is page-aligned, which O_DIRECT requires.
    buf = mmap.mmap(-1, block)
    try:
        # Stagger each stream a third of the file apart so they are not reading
        # the same offsets in lockstep.
        pos = (nblocks // max(1, nstreams)) * idx
        while time.monotonic() < deadline:
            offset = (pos % nblocks) * block
            try:
                n = os.preadv(fd, [buf], offset)
            except OSError as e:
                results[idx] = (total, f"read failed at {offset}: {e}")
                return
            if n <= 0:
                break
            total += n
            pos += 1
        results[idx] = (total, None)
    finally:
        buf.close()
        os.close(fd)


@app.get("/benchmark")
def benchmark():
    """Measure read throughput from EFS with parallel O_DIRECT streams.

    Query params: seconds (default 10, max 60), streams (default 8, max 32),
    block_kib (default 1024), mib (seed size to read, default 256).
    """
    guard = _require_mount()
    if guard:
        return guard

    seconds = max(3, min(60, request.args.get("seconds", default=10, type=int)))
    streams = max(1, min(32, request.args.get("streams", default=8, type=int)))
    block_kib = max(4, min(8192, request.args.get("block_kib", default=1024, type=int)))
    size_mib = max(16, min(4096, request.args.get("mib", default=256, type=int)))

    block = block_kib * 1024
    if block % 4096:
        return jsonify({"error": "block_kib must be a multiple of 4 so O_DIRECT stays aligned"}), 400

    seed = _seed_path(size_mib)
    if not seed.exists() or seed.stat().st_size < size_mib * (1 << 20):
        return (
            jsonify(
                {
                    "error": "seed file missing",
                    "hint": f"GET /benchmark/seed?mib={size_mib} first",
                    "expected": str(seed),
                }
            ),
            409,
        )

    nblocks = max(1, (size_mib * (1 << 20)) // block)
    results = [(0, None)] * streams
    deadline = time.monotonic() + seconds

    # Probe whether O_DIRECT works at all on this mount before starting the run.
    use_direct = True
    try:
        probe_fd = os.open(str(seed), os.O_RDONLY | getattr(os, "O_DIRECT", 0))
        os.close(probe_fd)
    except OSError as e:
        if e.errno in (errno.EINVAL, errno.ENOTSUP, errno.EOPNOTSUPP):
            use_direct = False
        else:
            return jsonify({"error": f"cannot open seed file: {e}"}), 500

    threads = [
        threading.Thread(
            target=_reader,
            args=(seed, block, nblocks, i, streams, deadline, results, use_direct),
            daemon=True,
        )
        for i in range(streams)
    ]

    rx_start = _nic_rx_bytes()
    wall_start = time.monotonic()
    for t in threads:
        t.start()

    # Sample the NIC once a second while the readers run. The per-second series is
    # the point: the egress allocation is a token bucket, so an idle MicroVM bursts
    # well above its sustained rate for the first few seconds. A single average
    # over the whole run blends the two into a number that describes neither.
    samples = []
    prev_rx, prev_t = rx_start, wall_start
    while time.monotonic() < deadline:
        time.sleep(1)
        now_rx, now_t = _nic_rx_bytes(), time.monotonic()
        dt = now_t - prev_t
        if dt > 0:
            samples.append(round((now_rx - prev_rx) * 8 / dt / 1e6, 1))
        prev_rx, prev_t = now_rx, now_t

    for t in threads:
        t.join(timeout=10)

    rx_total = _nic_rx_bytes() - rx_start
    elapsed = time.monotonic() - wall_start
    payload = sum(r[0] for r in results)
    errors = [r[1] for r in results if r[1]]

    # Sustained = median of the second half of the series, after the burst credit
    # has drained. Peak = the first sample, which is where the burst shows up.
    sustained = None
    if len(samples) >= 4:
        sustained = round(statistics.median(samples[len(samples) // 2 :]), 1)
    elif samples:
        sustained = round(statistics.median(samples), 1)

    out = {
        "config": {
            "seconds": seconds,
            "streams": streams,
            "block_kib": block_kib,
            "seed_mib": size_mib,
            "o_direct": use_direct,
        },
        "nic_mbps": {
            "peak_first_second": samples[0] if samples else None,
            "sustained_median_2nd_half": sustained,
            "mean_over_run": round(rx_total * 8 / elapsed / 1e6, 1) if elapsed > 0 else None,
            "per_second": samples,
        },
        "payload": {
            "bytes_read": payload,
            "mib_per_s": round(payload / (1 << 20) / elapsed, 1) if elapsed > 0 else None,
            "mbps": round(payload * 8 / elapsed / 1e6, 1) if elapsed > 0 else None,
        },
        "elapsed_seconds": round(elapsed, 2),
        "notes": [
            "nic_mbps is read from /proc/net/dev inside the guest: bytes on the virtual "
            "NIC including NFS and TCP overhead. That is the figure comparable to a "
            "bandwidth allocation.",
            "EFS traffic uses the MicroVM's EGRESS allocation via the VPC connector. The "
            "documented 8-128 Mbps table describes the managed HTTPS endpoint (ingress) "
            "and does not apply here.",
            "Sustained throughput scales with MinimumMemoryInMiB. A single stream will "
            "not saturate the allocation; 8 is where it flattens.",
        ],
    }
    if not use_direct:
        out["notes"].append(
            "O_DIRECT was not available on this mount, so the guest page cache may "
            "inflate these numbers."
        )
    if errors:
        out["errors"] = errors

    log("bench_complete", sustained_mbps=sustained, peak_mbps=samples[0] if samples else None)
    return jsonify(out)


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
hooks = Flask("efs-hooks")
_app_ready = threading.Event()


def _simulate_warmup():
    """Pretend the app has some non-trivial init before it's snapshot-ready."""
    time.sleep(1.5)
    _app_ready.set()
    log("warmup_complete")


@hooks.post(f"{HOOK_PATH}/ready")
def hook_ready():
    """Image build: 200 = snapshot-ready, 503 = retry. We do NOT mount here — the
    network connector and credentials do not exist at build time."""
    if _app_ready.is_set():
        record_event("ready")
        return jsonify({"status": "ready"}), 200
    return jsonify({"status": "warming_up"}), 503


@hooks.post(f"{HOOK_PATH}/validate")
def hook_validate():
    """Post-snapshot validation. Exercise the app so the platform can sample
    snapshot pages for prefetch. The mount is not available here, so we only
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
    identity and (b) mount EFS using parameters from the run payload. Both the
    connector and the execution-role credentials are now live."""
    STATE["instance_id"] = secrets.token_hex(8)
    STATE["boot_time"] = datetime.now(timezone.utc).isoformat()
    raw = request.get_data(as_text=True) or ""
    _apply_run_payload(raw)
    mounted = mount_efs()
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
    """Fires after SUSPENDED -> RUNNING. The mount was torn down in /suspend, so
    re-mount. Reseed identity entropy too."""
    STATE["instance_id"] = secrets.token_hex(8)
    mounted = mount_efs()
    record_event("resume", detail={"mounted": mounted, "instance_id": STATE["instance_id"]})
    return jsonify({"status": "ok", "mounted": mounted}), 200


@hooks.post(f"{HOOK_PATH}/suspend")
def hook_suspend():
    """Fires before RUNNING -> SUSPENDED. Unmount: an NFS session cannot survive
    the snapshot, and a stale mount makes the first post-resume I/O fail with
    ENOTCONN or hang."""
    unmounted = unmount_efs()
    record_event("suspend", detail={"unmounted": unmounted})
    return jsonify({"status": "ok", "unmounted": unmounted}), 200


@hooks.post(f"{HOOK_PATH}/terminate")
def hook_terminate():
    """Final flush opportunity before the VM goes away. Data written to EFS is
    already durable; we just release the mount cleanly."""
    record_event("terminate")
    unmount_efs()
    return jsonify({"status": "ok"}), 200


@hooks.get("/health")
def hook_health():
    return jsonify({"app_ready": _app_ready.is_set(), "mounted": _is_mounted()}), 200


def _run_app():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("APP_PORT", "8080")),
        threaded=True,
        use_reloader=False,
    )


def _run_hooks():
    hooks.run(
        host="0.0.0.0",
        port=int(os.environ.get("HOOKS_PORT", "9000")),
        threaded=True,
        use_reloader=False,
    )


if __name__ == "__main__":
    log("startup", pid=os.getpid(), mount_path=MOUNT_PATH)
    threading.Thread(target=_simulate_warmup, daemon=True).start()
    threading.Thread(target=_run_hooks, daemon=True).start()
    _run_app()
