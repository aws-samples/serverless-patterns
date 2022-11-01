import { DynamoDBClient, PutItemCommand } from '@aws-sdk/client-dynamodb';
const client = new DynamoDBClient({});
import { marshall } from '@aws-sdk/util-dynamodb';
import { v4 } from 'uuid';
// @ts-ignore
import { faker } from '@faker-js/faker';

/**
 * Example function that inserts data into DDB, rather than raising EventBridge event straight after, we will use DDB streams to process
 * the change and raise events from that (outbox pattern)
 */
export async function handler(event: any) {
  try {
    const data = await client.send(
      new PutItemCommand({
        TableName: process.env.TABLE_NAME,
        Item: marshall({
          id: v4(),
          username: faker.internet.userName(),
          email: faker.internet.email(),
          avatar: faker.image.avatar(),
          birthdate: faker.date.birthdate().toISOString(),
          registeredAt: faker.date.past().toISOString(),
        }),
      })
    );
    console.log('Done', data);
  } catch (error) {
    console.log(error);
  }
}
