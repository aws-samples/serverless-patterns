# USE UV'S ARM64 PYTHON BASE IMAGE
FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# SET WORKING DIRECTORY
WORKDIR /app

# COPY UV FILES
COPY pyproject.toml uv.lock ./

# INSTALL DEPENDENCIES (INCLUDING STANDS AGENTS)
RUN uv sync --frozen --no-cache

# COPY AGENT FILE
COPY agent.py ./

# EXPOSE PORT 8080 (REQUIRED BY AGENTCORE)
EXPOSE 8080

# RUN THE AGENT APP
CMD ["uv", "run", "uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]