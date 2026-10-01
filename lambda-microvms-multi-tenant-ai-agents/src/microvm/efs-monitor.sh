#!/usr/bin/env bash
# Tenant-aware persistent EFS mount daemon.
# Stays COMPLETELY quiet during image build (hard-NFS against unreachable IP
# wedges the snapshot). Waits until the orchestrator injects a tenant id via
# the sidecar (POST /tenant -> /var/run/tenant-id), then mounts the EFS and
# binds THIS TENANT's subdir over the state dir, then bounces the gateway.
STATE_DIR=/home/node/.openclaw
EFS_DIR=/mnt/efs
MARKER=/var/run/efs-mounted
TENANT_FILE=/var/run/tenant-id
# Mount target: prefer the EFS DNS name (regional, resolves to the AZ mount-target
# IP inside the VPC) built from EFS_ID; fall back to an explicit EFS_MOUNT_IP.
if [ -n "${EFS_ID:-}" ]; then
  EFS_HOST="${EFS_ID}.efs.${AWS_REGION:-us-east-1}.amazonaws.com"
elif [ -n "${EFS_MOUNT_IP:-}" ]; then
  EFS_HOST="${EFS_MOUNT_IP}"
else
  echo "[efs-monitor] need EFS_ID or EFS_MOUNT_IP"; exit 1
fi

mkdir -p "$EFS_DIR"
until [ -s "$TENANT_FILE" ]; do sleep 2; done
TENANT=$(tr -cd 'a-zA-Z0-9_-' < "$TENANT_FILE")
echo "[efs-monitor] tenant '$TENANT' assigned; mount target ${EFS_HOST}; starting mount attempts"

while true; do
  if [ ! -f "$MARKER" ]; then
    if timeout 15 mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=150,retrans=2 \
         "${EFS_HOST}:/" "$EFS_DIR" 2>/tmp/efs-mount.err; then
      echo "[efs-monitor] EFS mounted from ${EFS_HOST} at $(date -u +%FT%TZ)"
      TDIR="$EFS_DIR/tenants/$TENANT"
      mkdir -p "$TDIR"
      if [ ! -f "$TDIR/openclaw.json" ]; then
        echo "[efs-monitor] tenant $TENANT first generation: seeding from local state"
        cp -a "$STATE_DIR/." "$TDIR/"
      else
        echo "[efs-monitor] tenant $TENANT has prior state - adopting it"
      fi
      # Config is image-owned; only agent state persists across generations. Without
      # this, a stale EFS openclaw.json shadows every config change shipped in the image.
      # Also drop OpenClaw's backups: its watchdog restores .last-good over any config
      # that lacks the meta stamp (missing-meta-vs-last-good), undoing the overwrite.
      cp /opt/poc/openclaw.json "$TDIR/openclaw.json"
      rm -f "$TDIR/openclaw.json.last-good" "$TDIR/openclaw.json.bak"
      # Materialize live Bedrock model discovery into the config (~1.3-3.3s once
      # per cold start). The gateway's image guard and models list only read the
      # explicit models array, never the plugin's live catalog — so we bake the
      # discovered catalog (with correct text+image modalities) in here. On any
      # failure the static seed list shipped in the image stays as fallback.
      node /opt/poc/materialize-models.mjs "$TDIR/openclaw.json" || true
      # Plugins must be root-owned or the gateway blocks them (see Dockerfile note);
      # fix up trees seeded by older generations.
      [ -d "$TDIR/npm" ] && chown -R root:root "$TDIR/npm" 2>/dev/null
      # Clear per-session /model pins on cold start. A pin to a since-retired Bedrock
      # model fails every turn INCLUDING the /model command that would clear it,
      # permanently deadlocking the session. Cold start (reap -> relaunch) is the safe
      # reset point: the gateway isn't running against this dir yet. Pins still
      # survive suspend/resume; they only reset when the tenant went fully cold.
      python3 - "$TDIR/agents/main/sessions/sessions.json" <<'HEAL' 2>/dev/null || true
import json, sys
p = sys.argv[1]
try:
    d = json.load(open(p))
except Exception:
    sys.exit(0)
changed = False
for k, e in d.items():
    if not isinstance(e, dict) or not e.get("modelOverride"):
        continue
    print(f"[efs-monitor] clearing model pin on {k}: {e['modelOverride']}")
    for f in ("providerOverride", "modelOverride", "modelOverrideSource",
              "model", "modelProvider"):
        e.pop(f, None)
    changed = True
if changed:
    json.dump(d, open(p, "w"), indent=1)
HEAL
      mount --bind "$TDIR" "$STATE_DIR"
      touch "$MARKER"
      echo "[efs-monitor] state dir now EFS-backed for tenant $TENANT; bouncing gateway"
      pkill -f "openclaw.mjs gateway" || true
    fi
  fi
  sleep 5
done
