# OpenClaw on Lambda MicroVMs — EFS-persisted state variant (arm64).
# Runs as ROOT (mounting NFS needs privileges + ALL os capabilities at image level).
# Pinned: from 2026.8.1 the image no longer bundles the duckduckgo web search plugin that openclaw.json uses.
FROM ghcr.io/openclaw/openclaw:2026.7.35-slim@sha256:8dc86a49392f4af8f7bc1db0cccced7f06d2f2d425585a408d6a43510a3bc706

USER root
RUN apt-get update && apt-get install -y --no-install-recommends nfs-common \
    && rm -rf /var/lib/apt/lists/*

COPY openclaw.json hooks.py start.sh efs-monitor.sh gw-bridge.cjs materialize-models.mjs /opt/poc/
RUN chmod +x /opt/poc/start.sh /opt/poc/efs-monitor.sh \
    && mkdir -p /home/node/.openclaw /mnt/efs \
    && cp /opt/poc/openclaw.json /home/node/.openclaw/openclaw.json \
    && HOME=/home/node node /app/openclaw.mjs plugins install @openclaw/amazon-bedrock-provider \
    && chown -R node:node /home/node \
    # Gateway runs as root; OpenClaw blocks plugins whose files aren't root-owned
    # ("suspicious ownership" guard), so the plugin tree must stay root:root.
    && chown -R root:root /home/node/.openclaw/npm

ENV HOME=/home/node
EXPOSE 18789 8080
ENTRYPOINT ["tini", "-s", "--"]
CMD ["/opt/poc/start.sh"]
