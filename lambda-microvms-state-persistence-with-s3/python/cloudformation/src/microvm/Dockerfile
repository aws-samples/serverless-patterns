FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY entrypoint.py .

# Expose ports:
#   8080 - Main application API (default MicroVM proxy port)
#   9000 - Lifecycle hooks server
EXPOSE 8080 9000

# Start the application
CMD ["python", "entrypoint.py"]
