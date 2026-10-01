#!/usr/bin/env bash
# MicroVM entrypoint (EFS variant): hook sidecar (8080) + EFS mount daemon +
# supervised OpenClaw gateway (18789). Runs as root so we can mount NFS.
set -u
# DEMO FALLBACK ONLY: the template injects OPENCLAW_GATEWAY_TOKEN into every MicroVM
# (deploy.sh mints a random one), so this literal is never used in a real deploy. It
# stays as a last-resort so the VM still boots if the var is somehow unset. For a
# hardened build, drop the default so an unset token fails the boot loudly.
export OPENCLAW_GATEWAY_TOKEN="${OPENCLAW_GATEWAY_TOKEN:-poc-microvm-token-42}"
export HOME=/home/node

python3 /opt/poc/hooks.py &
echo "[start] hook sidecar on :8080 (pid $!)"

/opt/poc/efs-monitor.sh &
echo "[start] efs mount daemon (pid $!)"

# Persistent gateway bridge (warm WS to :18789) — kills per-message CLI spawn cost.
# Supervise it so it comes back if the gateway bounces during EFS adoption.
( while true; do node /opt/poc/gw-bridge.cjs; echo "[start] gw-bridge exited; restart in 2s"; sleep 2; done ) &
echo "[start] gw-bridge supervisor on :8090 (pid $!)"

# Supervise the gateway: efs-monitor kills it once EFS is bound so it
# restarts against the EFS-backed state dir.
while true; do
  node /app/openclaw.mjs gateway \
    --allow-unconfigured \
    --port 18789 \
    --auth token \
    --token "$OPENCLAW_GATEWAY_TOKEN"
  echo "[start] gateway exited (rc=$?); restarting in 2s"
  sleep 2
done
