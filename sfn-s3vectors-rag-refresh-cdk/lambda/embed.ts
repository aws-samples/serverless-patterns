import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { BedrockRuntimeClient, InvokeModelCommand } from '@aws-sdk/client-bedrock-runtime';
import { S3VectorsClient, PutVectorsCommand } from '@aws-sdk/client-s3vectors';

const s3 = new S3Client();
const bedrock = new BedrockRuntimeClient();
const s3vectors = new S3VectorsClient();

const DOCUMENT_BUCKET = process.env.DOCUMENT_BUCKET!;
const VECTOR_BUCKET_NAME = process.env.VECTOR_BUCKET_NAME!;
const VECTOR_INDEX_NAME = process.env.VECTOR_INDEX_NAME!;
const MODEL_ID = 'amazon.titan-embed-text-v2:0';

interface S3ItemEvent {
  Key: string;
}

export async function handler(event: S3ItemEvent) {
  const { Key } = event;

  // 1. Read document from S3
  const getObj = await s3.send(new GetObjectCommand({
    Bucket: DOCUMENT_BUCKET,
    Key,
  }));
  const text = await getObj.Body!.transformToString('utf-8');

  // 2. Generate embedding via Bedrock Titan Embeddings V2
  const invokeResp = await bedrock.send(new InvokeModelCommand({
    modelId: MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({ inputText: text, dimensions: 1024, normalize: true }),
  }));
  const embeddingResult = JSON.parse(new TextDecoder().decode(invokeResp.body));
  const embedding: number[] = embeddingResult.embedding;

  // 3. Store vector with PutVectors
  const vectorKey = Key.replace(/\//g, '_');
  await s3vectors.send(new PutVectorsCommand({
    vectorBucketName: VECTOR_BUCKET_NAME,
    indexName: VECTOR_INDEX_NAME,
    vectors: [{
      key: vectorKey,
      data: { float32: embedding },
      metadata: { source: Key },
    }],
  }));

  return { vectorKey, documentKey: Key };
}
