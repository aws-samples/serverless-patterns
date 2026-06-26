FROM python:3.14-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Claude Code CLI (native installer — no Node.js required)
RUN curl -fsSL https://claude.ai/install.sh | bash
ENV PATH="/root/.local/bin:${PATH}"

# Verify the install at build time (fails the build if Claude is missing)
RUN claude --version

# Interactive shells opened via the SHELL_INGRESS connector are spawned by the
# shell agent and do NOT inherit this image's ENV. So (1) expose `claude` on the
# default PATH via a symlink, (2) replicate the Bedrock configuration into the
# shell init files read by both login and non-login bash, and (3) land interactive
# shells in /workspace so Claude Code loads the project-scope MCP config baked
# there. Credentials themselves are never baked in — they come from the MicroVM
# execution role at runtime.
#
# Configure Bedrock model via the Global cross-region inference profile.
# Change ANTHROPIC_MODEL to use a different Claude model.
RUN ln -sf /root/.local/bin/claude /usr/local/bin/claude && \
    printf '%s\n' \
      'export PATH="$PATH:/root/.local/bin"' \
      'export CLAUDE_CODE_USE_BEDROCK=1' \
      'export AWS_REGION=us-east-2' \
      'export ANTHROPIC_MODEL=us.anthropic.claude-sonnet-4-6' \
      '[ -n "$PS1" ] && cd /workspace' \
      > /etc/profile.d/claude-agent.sh && \
    echo '. /etc/profile.d/claude-agent.sh' >> /root/.bashrc && \
    echo '. /etc/profile.d/claude-agent.sh' >> /etc/bash.bashrc

# Install uv (provides uvx) on the default PATH so the SHELL_INGRESS shell can
# spawn the AWS API MCP server. pip places uv/uvx in /usr/local/bin.
RUN pip install --no-cache-dir uv

# Pre-install the AWS API MCP server at build time. This validates the package is
# resolvable (fails the build otherwise, like `claude --version` above) and warms
# the uv cache so the first spawn inside the VM is fast.
RUN uv tool install awslabs.aws-api-mcp-server@latest

# Pre-warm: send a full MCP initialize handshake so Python compiles all .pyc
# bytecode at build time. Without this, the first spawn inside the VM takes ~6s
# (vs ~2s warm) and can exceed Claude Code's MCP connection timeout.
RUN echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"warmup","version":"1.0"}}}' \
    | /root/.local/bin/awslabs.aws-api-mcp-server > /dev/null 2>&1 || true

# Bake Claude Code's project-scope MCP config into /workspace (the directory the
# shell lands in). The MCP command points at the pre-installed shim from
# `uv tool install` — starts in ~5s from the ready-made tool venv, eliminating
# the uvx ephemeral-env creation and @latest PyPI check that can exceed Claude's
# MCP startup timeout on cold start. READ_OPERATIONS_ONLY rejects non-read calls,
# and the execution role only grants ReadOnlyAccess. Credentials come from the
# execution role via boto3's default chain — no keys are baked in.
# enabledMcpjsonServers pre-approves the server so the interactive session does
# not block on the MCP trust prompt.
RUN mkdir -p /workspace/.claude && \
    printf '%s\n' \
      '{' \
      '  "mcpServers": {' \
      '    "awslabs.aws-api-mcp-server": {' \
      '      "command": "/root/.local/bin/awslabs.aws-api-mcp-server",' \
      '      "args": [],' \
      '      "env": {' \
      '        "AWS_REGION": "us-east-2",' \
      '        "READ_OPERATIONS_ONLY": "true"' \
      '      }' \
      '    }' \
      '  }' \
      '}' \
      > /workspace/.mcp.json && \
    printf '%s\n' \
      '{' \
      '  "enabledMcpjsonServers": ["awslabs.aws-api-mcp-server"]' \
      '}' \
      > /workspace/.claude/settings.json

WORKDIR /workspace

COPY app.py .

EXPOSE 8080 9000

CMD ["python3", "app.py"]
