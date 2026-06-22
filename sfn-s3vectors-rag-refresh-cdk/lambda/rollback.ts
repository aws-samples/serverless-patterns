import { S3VectorsClient, DeleteVectorsCommand } from '@aws-sdk/client-s3vectors';

const s3vectors = new S3VectorsClient();

const VECTOR_BUCKET_NAME = process.env.VECTOR_BUCKET_NAME!;
const VECTOR_INDEX_NAME = process.env.VECTOR_INDEX_NAME!;

interface RollbackEvent {
  vectorKeys: string[];
}

export async function handler(event: RollbackEvent) {
  const { vectorKeys } = event;

  // DeleteVectors accepts up to 500 keys per call
  const BATCH_SIZE = 500;
  for (let i = 0; i < vectorKeys.length; i += BATCH_SIZE) {
    const batch = vectorKeys.slice(i, i + BATCH_SIZE);
    await s3vectors.send(new DeleteVectorsCommand({
      vectorBucketName: VECTOR_BUCKET_NAME,
      indexName: VECTOR_INDEX_NAME,
      keys: batch,
    }));
  }

  return { deleted: vectorKeys.length };
}
