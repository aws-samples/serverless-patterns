# The base image is pinned by the pattern and only changes when this line is
# edited. The Python version itself is not significant: the image needs a
# recent python3 for app.py and for the MCP proxy's virtual environment.
FROM python:3.14-slim

# The two third-party components are installed at their latest release by
# default, so every rebuild picks up new Codex and proxy versions, including any
# behaviour changes. For reproducible rebuilds, pin them by editing these two
# defaults; they are the only place a version needs to change.
#   CODEX_VERSION      "latest" or an x.y.z release (passed to the installer as CODEX_RELEASE)
#   MCP_PROXY_VERSION  "latest" or an exact PyPI version such as 1.2.3
ARG CODEX_VERSION=latest
ARG MCP_PROXY_VERSION=latest

# git is not optional here: Codex refuses to run outside a Git repository unless
# --skip-git-repo-check is passed, and /workspace is initialised as one below.
# bubblewrap backs Codex's workspace-write sandbox on Linux. Codex ships a
# bundled copy and warns on every run when it finds none on PATH; installing the
# distro package silences that and uses the kernel-matched build.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        curl \
        ca-certificates \
        bubblewrap \
    && rm -rf /var/lib/apt/lists/*

# ── Codex CLI ────────────────────────────────────────────────────────────────
# Official standalone installer. CODEX_NON_INTERACTIVE stops it prompting during
# the image build; CODEX_INSTALL_DIR is its documented default, pinned here so
# the symlink below cannot drift if that default ever changes.
ENV CODEX_HOME=/root/.codex
RUN curl -fsSL https://chatgpt.com/codex/install.sh \
    | CODEX_NON_INTERACTIVE=1 CODEX_INSTALL_DIR=/root/.local/bin CODEX_RELEASE="${CODEX_VERSION}" sh

# Fail the build now rather than at first connect if the binary is missing.
RUN /root/.local/bin/codex --version

# Interactive shells opened through the SHELL_INGRESS connector are spawned by
# the shell agent and do NOT inherit this image's ENV, so expose `codex` on the
# default PATH explicitly. The rest of the shell environment is written to
# /etc/profile.d/codex-agent.sh by app.py at runtime; see codex-profile.sh.tmpl.
RUN ln -sf /root/.local/bin/codex /usr/local/bin/codex

# Source the generated profile from both login and non-login bash. The guard
# matters: the file does not exist until app.py renders it, and a missing-file
# error here would break every shell.
RUN SOURCE_LINE='[ -r /etc/profile.d/codex-agent.sh ] && . /etc/profile.d/codex-agent.sh' && \
    echo "${SOURCE_LINE}" >> /root/.bashrc && \
    echo "${SOURCE_LINE}" >> /etc/bash.bashrc

# ── MCP Proxy for AWS ────────────────────────────────────────────────────────
# The AWS MCP Server itself is AWS-managed and remote; what is installed here is
# the proxy that signs requests to it with SigV4. uv provides the tool installer.
# pip places uv/uvx in /usr/local/bin, already on the default PATH.
RUN pip install --no-cache-dir uv

# Pre-install at build time rather than letting Codex run `uvx ...@latest` per
# session. That validates the package is resolvable (failing the build if not,
# like `codex --version` above), produces a ready-made tool venv so the first
# spawn inside the VM skips uvx's ephemeral-env creation and its PyPI check, and
# means the image does not reach out to PyPI every time it resumes.
#
# The -cli distribution is the one to install for command-line use: it pins its
# entire transitive dependency tree to tested versions. The unsuffixed
# mcp-proxy-for-aws is the library distribution, with loose ranges meant for
# importing into another project.
RUN uv tool install "mcp-proxy-for-aws-cli@${MCP_PROXY_VERSION}"

# Expose the proxy on the default PATH, for the same reason codex is symlinked
# above: the tool directory uv installs into is uv's choice, and the Codex config
# should not depend on it. The config references the proxy by name.
RUN ln -sf /root/.local/bin/mcp-proxy-for-aws-cli /usr/local/bin/mcp-proxy-for-aws-cli

# Pre-warm: importing the proxy forces Python to compile its .pyc bytecode now.
# Without it the first spawn inside the VM is several seconds slower and can
# outlast Codex's MCP startup timeout on a cold resume. --help is used rather
# than a real handshake because the build environment has neither the execution
# role's credentials nor a Region.
RUN mcp-proxy-for-aws-cli --help > /dev/null 2>&1 || true

# ── Workspace ────────────────────────────────────────────────────────────────
# Codex needs a Git repository to run in, and a committer identity to make any
# commit it is asked for. safe.directory keeps Git quiet about ownership now that
# the repo is created at build time and used at runtime.
RUN mkdir -p /workspace \
    && git config --global user.email "codex-agent@microvm.local" \
    && git config --global user.name "Codex MicroVM Agent" \
    && git config --global init.defaultBranch main \
    && git config --global --add safe.directory /workspace \
    && git init -q /workspace

# AGENTS.md is Codex's project-instruction file: it tells the agent about the
# read-only role and the ephemeral filesystem so it does not waste turns
# rediscovering them.
COPY AGENTS.md /workspace/AGENTS.md

# Config templates live outside /workspace so the agent cannot edit its own
# provider settings mid-session.
RUN mkdir -p /opt/codex-agent
COPY codex-config.toml.tmpl codex-profile.sh.tmpl /opt/codex-agent/

WORKDIR /workspace

COPY app.py /opt/codex-agent/app.py

EXPOSE 8080 9000

CMD ["python3", "/opt/codex-agent/app.py"]
