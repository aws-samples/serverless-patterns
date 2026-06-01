# Event-Driven Data Pipeline with Lambda Durable Functions

This serverless pattern demonstrates how to build an event-driven data processing pipeline using AWS Lambda Durable Functions with **direct SQS Event Source Mapping** and Lambda invoke chaining.

## How It Works

This pattern demonstrates an event-driven data processing pipeline using AWS Lambda Durable Functions with direct SQS Event Source Mapping. When a message arrives in the SQS queue, it directly triggers the durable function (no intermediary Lambda needed). The durable function then orchestrates a series of specialized processing steps using Lambda invoke chaining - first validating the incoming data, then transforming it (converting data_source to uppercase), and finally storing the processed results in DynamoDB. Throughout this process, the durable function automatically creates checkpoints, enabling fault-tolerant execution that can recover from failures without losing progress. The entire pipeline operates within the 15-minute ESM execution limit, making it ideal for reliable batch processing workflows.

## Architecture Overview

The pattern showcases two key Durable Functions capabilities:
1. **Direct Event Source Mapping**: SQS directly triggers the durable function (15-minute limit)
2. **Lambda Invoke Chaining**: Orchestrates specialized processing functions

![Architecture Diagram](architecture-diagram.png)

## Key Features

- **Direct ESM Integration**: No intermediary function needed
- **15-minute execution constraint**: Demonstrates ESM time limits
- **Fault-tolerant processing**: Automatic checkpointing and recovery
- **Microservices coordination**: Chains specialized Lambda functions
- **Batch processing**: Handles multiple SQS records per invocation
- **Simple storage**: Uses DynamoDB for processed data

## Important ESM Constraints

⚠️ **15-Minute Execution Limit**: When using Event Source Mapping with Durable Functions, the total execution time cannot exceed 15 minutes. This includes:
- All processing steps
- Function invocations
- No long wait operations

## Use Cases

- ETL pipelines with validation and transformation
- Event-driven microservices orchestration
- Batch processing with fault tolerance
- Data processing workflows requiring checkpointing

## Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) configured with appropriate permissions
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) latest version installed
- [Python 3.14](https://www.python.org/downloads/release/python-3140/) runtime installed

## Deployment

1. **Build the application**:
   ```bash
   sam build
   ```

2. **Deploy to AWS**:
   ```bash
   sam deploy --guided
   ```
   
   Note the outputs after deployment:
   - `DataProcessingQueueUrl`: Use this for `<QUEUE_URL>`
   - `ProcessedDataTable`: Use this for `<PROCESSED_DATA_TABLE>`

3. **Test the pipeline**:
   ```bash
   # Send a test message to SQS
   aws sqs send-message \
     --queue-url <QUEUE_URL> \
     --message-body '{"data_source": "test.csv", "processing_type": "standard"}'
     --region <REPLACE_REGION>
   ```

4. **Verify successful processing**:
   ```bash
   # Check if data was processed and stored in DynamoDB
   aws dynamodb scan --table-name <PROCESSED_DATA_TABLE> --query 'Items[*]' --region <REPLACE_REGION>
   ```
   
   **Success indicators:**
   - You should see at least one item in the DynamoDB table
   - Original input data: `"data_source": "test.csv"`
   - Transformed data: `"data_source": "TEST.CSV"` (uppercase transformation applied)
   - Execution tracking with unique `execution_id`
   - Timestamps showing when data was processed and stored
   
   This confirms the entire pipeline worked: SQS → Durable Function → Validation → Transformation → Storage → DynamoDB

## Components

### 1. Durable Pipeline Function (`src/durable_pipeline/`)
- **Direct SQS Event Source Mapping**: Receives SQS events directly
- **15-minute execution limit**: Must complete all processing within ESM constraints
- **Batch processing**: Handles multiple SQS records per invocation
- **Lambda invoke chaining**: Orchestrates validation, transformation, and storage
- **Automatic checkpointing**: Recovers from failures without losing progress

### 2. Specialized Processing Functions
- **Validation Function**: Simple data validation checks
- **Transformation Function**: Basic data transformation
- **Storage Function**: Persists processed data to DynamoDB

## Monitoring

- CloudWatch Logs for execution tracking
- DynamoDB table for processed data
- SQS DLQ for failed messages

## Configuration

Key environment variables:
- `ENVIRONMENT`: Deployment environment (dev/prod)
- `PROCESSED_DATA_TABLE`: DynamoDB table for processed data
- `VALIDATION_FUNCTION_ARN`: ARN of validation function
- `TRANSFORMATION_FUNCTION_ARN`: ARN of transformation function
- `STORAGE_FUNCTION_ARN`: ARN of storage function

## ESM-Specific Considerations

- **Execution Timeout**: Set to 900 seconds (15 minutes) maximum
- **Batch Size**: Configured for optimal processing (5 records)
- **Error Handling**: Uses SQS DLQ for failed batches
- **Efficient Processing**: Optimized for speed to stay within time limits

## Error Handling

- Automatic retries with exponential backoff
- Dead Letter Queue for failed messages
- Partial batch failure support
- Checkpoint-based recovery

## Cost Optimization

- Pay only for active compute time
- Efficient batch processing
- Automatic scaling based on queue depth

## Cleanup

```bash
sam delete
```

## Learn More

- [AWS Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Event Source Mappings with Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking-esm.html)
- [Lambda Invoke Chaining](https://docs.aws.amazon.com/lambda/latest/dg/durable-examples.html#durable-examples-chained-invocations)
