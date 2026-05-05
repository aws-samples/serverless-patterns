FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV TASK_FAMILY="eventbridge-ecs-cron-task"
ENV CLUSTER_NAME="eventbridge-ecs-cron-cluster"

CMD ["python", "app.py"]
