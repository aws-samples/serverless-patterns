/**
 * Lambda triggered directly from S3. This then goes onto raise domain events for custom downstream event bus
 */
import { PutEventsCommand, EventBridgeClient, PutEventsRequestEntry } from '@aws-sdk/client-eventbridge';
const client = new EventBridgeClient({});
import { v4 } from 'uuid';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3Client = new S3Client({});

// example of enrichment, you could go to database or API to enrich event before passing it on
const getUser = async (id: string) => {
  return {
    id: id,
    firstName: 'Dave',
    lastName: 'Boyne',
  };
};

const getDetailTypeFromEvent = (event: any) => {
  return event['detail-type'] === 'Object Created' ? 'ClaimCreated' : 'ClaimProcessed';
};

const transformS3Event = async (event: any) => {
  const s3KeyParts = event?.detail?.object?.key.split('/');
  const userId = s3KeyParts[1];
  const user = await getUser(userId);

  const url = await getSignedUrl(
    s3Client,
    new GetObjectCommand({
      Bucket: event?.detail?.bucket?.name,
      Key: event?.detail?.object?.key,
    }),
    {
      expiresIn: 3600,
    }
  );

  return {
    EventBusName: process.env.EVENT_BUS_NAME,
    DetailType: getDetailTypeFromEvent(event),
    Detail: JSON.stringify({
      metadata: {
        domain: 'CLAIMS',
        'idempotency-key': v4(),
      },
      data: {
        user,
        claim: {
          signedURL: url,
        },
      },
    }),
    Source: 'insurance.claims',
  } as PutEventsRequestEntry;
};

export async function handler(event: any) {
  const transformedEvent = await transformS3Event(event);

  console.log('Sending event', transformedEvent);

  await client.send(
    new PutEventsCommand({
      Entries: [transformedEvent],
    })
  );
}
