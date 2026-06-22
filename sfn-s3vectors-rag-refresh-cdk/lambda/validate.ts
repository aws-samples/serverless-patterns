import { BedrockRuntimeClient, InvokeModelCommand } from '@aws-sdk/client-bedrock-runtime';
import { S3VectorsClient, QueryVectorsCommand } from '@aws-sdk/client-s3vectors';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';

const bedrock = new BedrockRuntimeClient();
const s3vectors = new S3VectorsClient();
const s3 = new S3Client();

const VECTOR_BUCKET_NAME = process.env.VECTOR_BUCKET_NAME!;
const VECTOR_INDEX_NAME = process.env.VECTOR_INDEX_NAME!;
const MODEL_ID = 'amazon.titan-embed-text-v2:0';

interface ResultWriterEvent {
  ResultWriterDetails: { Bucket: string; Key: string };
}

export async function handler(event: ResultWriterEvent) {
  // Read the Distributed Map result manifest from S3
  const { Bucket, Key } = event.ResultWriterDetails;
  const manifestResp = await s3.send(new GetObjectCommand({ Bucket, Key }));
  const manifest = JSON.parse(await manifestResp.Body!.transformToString());

  // Read succeeded results file(s) to extract vector keys
  const destBucket = manifest.DestinationBucket;
  const vectorKeys: string[] = [];
  for (const result of manifest.ResultFiles?.SUCCEEDED ?? []) {
    const fileResp = await s3.send(new GetObjectCommand({ Bucket: destBucket, Key: result.Key }));
    const results = JSON.parse(await fileResp.Body!.transformToString());
    for (const r of results) {
      const output = typeof r.Output === 'string' ? JSON.parse(r.Output) : r.Output;
      if (output?.vectorKey) vectorKeys.push(output.vectorKey);
    }
  }

  if (vectorKeys.length === 0) {
    return { valid: false, vectorKeys };
  }

  // Generate a probe embedding and query the index
  const probeText = 'vector storage and embeddings for AI applications';
  const invokeResp = await bedrock.send(new InvokeModelCommand({
    modelId: MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({ inputText: probeText, dimensions: 1024, normalize: true }),
  }));
  const probeEmbedding: number[] = JSON.parse(new TextDecoder().decode(invokeResp.body)).embedding;

  const queryResp = await s3vectors.send(new QueryVectorsCommand({
    vectorBucketName: VECTOR_BUCKET_NAME,
    indexName: VECTOR_INDEX_NAME,
    queryVector: { float32: probeEmbedding },
    topK: 5,
    returnMetadata: true,
  }));

  // Validate: at least one newly ingested vector appears in results
  const returnedKeys = new Set(queryResp.vectors?.map(v => v.key) ?? []);
  const found = vectorKeys.some(k => returnedKeys.has(k));

  return { valid: found, vectorKeys };
}
