FROM codercom/code-server:latest

# Use root only for installing packages
USER root

# Install Python, AWS CLI, and dependencies
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        curl \
        unzip \
        sudo && \
    # Install AWS CLI v2 for ARM64
    curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up Python symlinks for convenience
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Copy lifecycle hooks handler and startup script
COPY app.py /opt/hooks/app.py
COPY start.sh /opt/start.sh
RUN chmod +x /opt/start.sh

# Create workspace and set ownership to coder user
RUN mkdir -p /home/project && chown -R coder:coder /home/project /opt/hooks

# Drop privileges — run as the unprivileged coder user
USER coder

EXPOSE 8080 9000

# Override the default entrypoint (which invokes fixuid requiring setuid)
ENTRYPOINT []
CMD ["/opt/start.sh"]
