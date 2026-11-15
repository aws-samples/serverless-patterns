FROM python:3.13-slim

WORKDIR /app

# Create non-root user first
RUN useradd -m -u 1000 bedrock_agentcore

# Install dependencies as root (system-wide)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER bedrock_agentcore

# Expose ports for AgentCore
EXPOSE 8080 8000

# Copy application code
COPY --chown=bedrock_agentcore:bedrock_agentcore . .

# Run the agent as a module
CMD ["python", "-m", "agent"]
