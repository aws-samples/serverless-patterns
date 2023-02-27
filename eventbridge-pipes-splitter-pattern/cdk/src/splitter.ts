import { unmarshall } from '@aws-sdk/util-dynamodb';
import {DynamoDBRecord} from 'aws-lambda';

interface Ticket {
  id: string
}

export async function handler(records: DynamoDBRecord[]) {

  const newOrderRaw = records[0]?.dynamodb?.NewImage || {};
  const newOrder = unmarshall(newOrderRaw);

  const { id:orderId, userId, tickets = [] } = newOrder;

  if(!tickets){
    // return empty array for Pipes so it can continue the enrichment and not trigger downstream consumer
    return [];
  }

  // Each event will be the `detail` of the EventBridge event.
  const events = tickets.map((ticket: Ticket) => {
    return {
      id: ticket?.id,
      orderId,
      userId
    }
  });

  return events;
}


// {
//   "eventID": "06dc77b3fb330170e2328a59df882f83",
//   "eventName": "INSERT",
//   "eventVersion": "1.1",
//   "eventSource": "aws:dynamodb",
//   "awsRegion": "us-west-2",
//   "dynamodb": {
//       "ApproximateCreationDateTime": 1677498996,
//       "Keys": {
//           "id": {
//               "S": "905fa520-4d4a-4850-97c5-1d429f8c23ba"
//           }
//       },
//       "NewImage": {
//           "tickets": {
//               "L": [
//                   {
//                       "M": {
//                           "id": {
//                               "S": "5c27a12d-f33f-4b64-8afe-844a8a297660"
//                           }
//                       }
//                   },
//                   {
//                       "M": {
//                           "id": {
//                               "S": "2208130e-4f78-48d4-b3e3-bf94912ae71d"
//                           }
//                       }
//                   },
//                   {
//                       "M": {
//                           "id": {
//                               "S": "0325bf78-a162-4486-adb1-218aadf41fdc"
//                           }
//                       }
//                   }
//               ]
//           },
//           "id": {
//               "S": "905fa520-4d4a-4850-97c5-1d429f8c23ba"
//           },
//           "userId": {
//               "S": "b507de3e-d9d4-4e88-9e61-28416394777f"
//           }
//       },
//       "SequenceNumber": "400000000032021070652",
//       "SizeBytes": 257,
//       "StreamViewType": "NEW_IMAGE"
//   },
//   "eventSourceARN": "arn:aws:dynamodb:us-west-2:670852811695:table/Orders-Table/stream/2023-02-27T11:41:38.304"
// }

// ]


