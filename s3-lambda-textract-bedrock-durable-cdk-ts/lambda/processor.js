const {
  withDurableExecution,
  createWaitStrategy,
} = require("@aws/durable-execution-sdk-js");
const {
  TextractClient,
  StartDocumentTextDetectionCommand,
  GetDocumentTextDetectionCommand,
} = require("@aws-sdk/client-textract");
const {
  BedrockRuntimeClient,
  InvokeModelCommand,
} = require("@aws-sdk/client-bedrock-runtime");
const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");

const textractClient = new TextractClient();
const bedrockClient = new BedrockRuntimeClient();
const dynamoClient = new DynamoDBClient();

const RESULTS_TABLE_NAME = process.env.RESULTS_TABLE_NAME;
const BEDROCK_MODEL_ID =
  process.env.BEDROCK_MODEL_ID || "eu.amazon.nova-lite-v1:0";

/**
 * Durable document processing pipeline:
 * 1. Start Amazon Textract async job
 * 2. Poll for Textract job completion (using waitForCondition)
 * 3. Retrieve extracted text
 * 4. Summarize with Amazon Bedrock (Claude 3 Haiku)
 * 5. Store results in Amazon DynamoDB
 */
exports.handler = withDurableExecution(async (event, context) => {
  // Parse S3 event — get bucket and key from the first record
  const s3Record = event.Records[0].s3;
  const bucket = s3Record.bucket.name;
  const key = decodeURIComponent(s3Record.object.key.replace(/\+/g, " "));

  context.logger.info(`Processing document: s3://${bucket}/${key}`);

  // Step 1: Start Textract async text detection
  const jobId = await context.step("start-textract", async () => {
    const response = await textractClient.send(
      new StartDocumentTextDetectionCommand({
        DocumentLocation: {
          S3Object: { Bucket: bucket, Name: key },
        },
      }),
    );
    return response.JobId;
  });

  context.logger.info(`Textract job started: ${jobId}`);

  // Step 2: Poll for Textract job completion using waitForCondition
  const textractResult = await context.waitForCondition(
    "wait-textract-complete",
    async (state) => {
      const response = await textractClient.send(
        new GetDocumentTextDetectionCommand({
          JobId: state.jobId,
        }),
      );
      return {
        jobId: state.jobId,
        status: response.JobStatus,
        blockCount: (response.Blocks || []).length,
      };
    },
    {
      initialState: { jobId, status: "IN_PROGRESS", blockCount: 0 },
      waitStrategy: createWaitStrategy({
        maxAttempts: 60,
        initialDelaySeconds: 3,
        maxDelaySeconds: 30,
        backoffRate: 1.5,
        shouldContinuePolling: (result) => result.status === "IN_PROGRESS",
      }),
      timeout: { minutes: 30 },
    },
  );

  if (textractResult.status !== "SUCCEEDED") {
    throw new Error(
      `Textract job failed with status: ${textractResult.status}`,
    );
  }

  // Step 3: Retrieve full Textract results and extract text
  const extractedText = await context.step("extract-text", async () => {
    const response = await textractClient.send(
      new GetDocumentTextDetectionCommand({
        JobId: jobId,
      }),
    );
    const lines = (response.Blocks || [])
      .filter((block) => block.BlockType === "LINE")
      .map((block) => block.Text);
    return lines.join("\n");
  });

  context.logger.info(`Extracted ${extractedText.length} characters of text`);

  // Step 4: Summarize extracted text with Amazon Bedrock (Amazon Nova Lite)
  const summary = await context.step("bedrock-summarize", async () => {
    // Truncate text to fit within model context window
    const truncatedText = extractedText.substring(0, 15000);

    const response = await bedrockClient.send(
      new InvokeModelCommand({
        modelId: BEDROCK_MODEL_ID,
        contentType: "application/json",
        accept: "application/json",
        body: JSON.stringify({
          schemaVersion: "messages-v1",
          messages: [
            {
              role: "user",
              content: [
                {
                  text: `Summarize the following document text. Provide a concise summary, key topics, and any important entities (names, dates, amounts) found.\n\nDocument text:\n${truncatedText}`,
                },
              ],
            },
          ],
          inferenceConfig: {
            max_new_tokens: 1024,
          },
        }),
      }),
    );

    const result = JSON.parse(new TextDecoder().decode(response.body));
    return result.output.message.content[0].text;
  });

  context.logger.info("Bedrock summarization complete");

  // Step 5: Store results in DynamoDB
  await context.step("store-results", async () => {
    await dynamoClient.send(
      new PutItemCommand({
        TableName: RESULTS_TABLE_NAME,
        Item: {
          documentKey: { S: key },
          bucket: { S: bucket },
          textractJobId: { S: jobId },
          extractedTextLength: { N: String(extractedText.length) },
          summary: { S: summary },
          processedAt: { S: new Date().toISOString() },
        },
      }),
    );
  });

  context.logger.info(`Results stored for document: ${key}`);

  return {
    statusCode: 200,
    body: {
      document: `s3://${bucket}/${key}`,
      textractJobId: jobId,
      extractedCharacters: extractedText.length,
      summary,
    },
  };
});
