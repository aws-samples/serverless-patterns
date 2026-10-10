# Use Python 3.14 as the base runtime
FROM python:3.14-slim

WORKDIR /app

COPY app.py .

# Expose application port (8080) and lifecycle hooks port (9000)
EXPOSE 8080 9000

# Start the application
# Lambda will call the /ready hook on port 9000 to confirm startup
CMD ["python3", "app.py"]
