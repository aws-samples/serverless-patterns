# Simple container for EventBridge ECS Cron Demo
FROM public.ecr.aws/amazonlinux/amazonlinux:2

# Set working directory
WORKDIR /app

# Copy entrypoint script
COPY entrypoint.sh .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Set default environment variables
ENV TASK_FAMILY="eventbridge-ecs-cron-task"
ENV CLUSTER_NAME="eventbridge-ecs-cron-cluster"

# Run the entrypoint script
CMD ["./entrypoint.sh"]