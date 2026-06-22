#!/usr/bin/env python3
"""
Simple Data Processing Job - EventBridge ECS Cron Pattern Demo
This job fetches data from an API, processes it, and logs the results.
Perfect for demonstrating scheduled batch processing with ECS.
"""

import os
import json
import time
import requests
from datetime import datetime


def log_message(level, message, **extra):
    """Simple structured logging for CloudWatch"""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": message,
        "task_family": os.getenv("TASK_FAMILY", "eventbridge-ecs-cron"),
        "cluster_name": os.getenv("CLUSTER_NAME", "eventbridge-ecs-cron-cluster"),
        **extra
    }
    print(json.dumps(log_entry))


def fetch_sample_data():
    """Fetch sample data from a public API"""
    try:
        log_message("INFO", "Fetching sample data from API")
        
        # Use a free public API for demonstration
        response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
        response.raise_for_status()
        
        data = response.json()
        log_message("INFO", f"Successfully fetched {len(data)} posts from API")
        return data
        
    except Exception as e:
        log_message("ERROR", f"Failed to fetch data: {str(e)}")
        raise


def process_data(posts):
    """Process the fetched data - simple data transformation"""
    log_message("INFO", f"Starting to process {len(posts)} posts")
    
    processed_data = []
    
    for post in posts:
        # Simple data processing: extract key information and add metadata
        processed_post = {
            "id": post["id"],
            "user_id": post["userId"],
            "title_length": len(post["title"]),
            "body_length": len(post["body"]),
            "word_count": len(post["body"].split()),
            "processed_at": datetime.utcnow().isoformat() + "Z"
        }
        
        processed_data.append(processed_post)
        
        # Add a small delay to simulate processing time
        time.sleep(0.01)
    
    log_message("INFO", f"Successfully processed {len(processed_data)} posts")
    return processed_data


def generate_report(processed_data):
    """Generate a simple report from processed data"""
    log_message("INFO", "Generating summary report")
    
    # Calculate some basic statistics
    total_posts = len(processed_data)
    avg_title_length = sum(p["title_length"] for p in processed_data) / total_posts
    avg_word_count = sum(p["word_count"] for p in processed_data) / total_posts
    
    # Find the longest and shortest posts
    longest_post = max(processed_data, key=lambda x: x["body_length"])
    shortest_post = min(processed_data, key=lambda x: x["body_length"])
    
    report = {
        "summary": {
            "total_posts_processed": total_posts,
            "average_title_length": round(avg_title_length, 2),
            "average_word_count": round(avg_word_count, 2),
            "longest_post_id": longest_post["id"],
            "longest_post_length": longest_post["body_length"],
            "shortest_post_id": shortest_post["id"],
            "shortest_post_length": shortest_post["body_length"]
        },
        "processing_completed_at": datetime.utcnow().isoformat() + "Z"
    }
    
    log_message("INFO", "Report generated successfully", report=report)
    return report


def save_results(report):
    """Save results - in this demo, we just log them"""
    log_message("INFO", "Saving processing results")
    
    # In a real scenario, you might save to S3, database, etc.
    # For this demo, we'll just log the results
    
    # Simulate saving to different destinations
    destinations = ["database", "s3_bucket", "cache"]
    
    for dest in destinations:
        log_message("INFO", f"Saving results to {dest}")
        time.sleep(0.1)  # Simulate save time
    
    log_message("INFO", "Results saved successfully to all destinations")


def main():
    """Main job execution"""
    start_time = datetime.utcnow()
    
    try:
        log_message("INFO", "=== Starting Data Processing Job ===")
        log_message("INFO", f"Job started at: {start_time.isoformat()}Z")
        
        # Step 1: Fetch data from external API
        posts = fetch_sample_data()
        
        # Step 2: Process the data
        processed_data = process_data(posts)
        
        # Step 3: Generate report
        report = generate_report(processed_data)
        
        # Step 4: Save results
        save_results(report)
        
        # Calculate execution time
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()
        
        log_message("INFO", "=== Job Completed Successfully ===", 
                   duration_seconds=duration,
                   posts_processed=len(processed_data))
        
    except Exception as e:
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()
        
        log_message("ERROR", f"Job failed: {str(e)}", 
                   duration_seconds=duration,
                   error_type=type(e).__name__)
        
        # Exit with error code so ECS marks the task as failed
        exit(1)


if __name__ == "__main__":
    main()