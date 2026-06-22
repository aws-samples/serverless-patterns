#!/bin/sh
# Simple entrypoint script for EventBridge ECS Cron Demo

# Log start of job with timestamp
echo "{\"timestamp\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\",\"level\":\"INFO\",\"message\":\"EventBridge ECS Cron Job Started\",\"task_family\":\"$TASK_FAMILY\",\"cluster_name\":\"$CLUSTER_NAME\"}"

# Simulate processing time
sleep 2

# Log processing status
echo "{\"timestamp\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\",\"level\":\"INFO\",\"message\":\"Processing sample data\",\"records_processed\":42}"

# Simulate more processing
sleep 1

# Calculate execution time (simple approximation)
echo "{\"timestamp\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\",\"level\":\"INFO\",\"message\":\"EventBridge ECS Cron Job Completed Successfully\",\"duration_seconds\":3}"

# Exit successfully
exit 0