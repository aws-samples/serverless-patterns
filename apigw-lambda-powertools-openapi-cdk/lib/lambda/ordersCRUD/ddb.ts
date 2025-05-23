import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  PutCommand,
  DeleteCommand,
  QueryCommand,
  PutCommandInput,
} from "@aws-sdk/lib-dynamodb";

import {
  convertDdbToOrder,
  convertOrderToDdb,
  DdbOrder,
  DdbOrderItem,
  Order,
  OrderUpdate,
} from "@ordersCommonCode/order";
import { tracer } from "./powertools";

const DYNAMODB_TABLE_NAME = process.env["DYNAMODB_TABLE_NAME"];
if (!DYNAMODB_TABLE_NAME) {
  throw new Error("DYNAMODB_TABLE_NAME is not defined");
}
const client = tracer.captureAWSv3Client(new DynamoDBClient({}));
const docClient = DynamoDBDocumentClient.from(client);

/**
 * Writes or updates an order and its items to DynamoDB
 * @async
 * @param {Object} params - The parameters object
 * @param {Order} params.order - The order to write to DynamoDB
 * @param {boolean} params.update - If true, updates existing order; if false, creates new order
 * @throws {Error} If DynamoDB operation fails
 * @returns {Promise<void>}
 */
export async function writeOrder({
  order,
  update,
}: {
  order: Order;
  update: boolean;
}): Promise<void> {
  const { ddbOrder, ddbOrderItems } = convertOrderToDdb({ order });

  const putCommandInput: PutCommandInput = {
    TableName: DYNAMODB_TABLE_NAME,
    Item: ddbOrder,
  };
  if (!update) {
    putCommandInput.ConditionExpression =
      "attribute_not_exists(p) AND attribute_not_exists(s)";
  }

  const promises = [docClient.send(new PutCommand(putCommandInput))];

  for (const item of ddbOrderItems) {
    promises.push(
      docClient.send(
        new PutCommand({
          TableName: DYNAMODB_TABLE_NAME,
          Item: item,
        })
      )
    );
  }
  await Promise.all(promises);
}

/**
 * Retrieves an order and its items from DynamoDB
 * @async
 * @param {Object} params - The parameters for retrieving the order
 * @param {string} params.customerId - The ID of the customer who owns the order
 * @param {string} params.orderId - The ID of the order to retrieve
 * @returns {Promise<Order>} The order if found
 * @throws {Error} If order not found or query fails
 */
export async function getOrder({
  customerId,
  orderId,
}: {
  customerId: string;
  orderId: string;
}): Promise<Order> {
  try {
    const result = await docClient.send(
      new QueryCommand({
        TableName: DYNAMODB_TABLE_NAME,
        KeyConditionExpression: "p = :p AND begins_with(s, :s)",
        ExpressionAttributeValues: {
          ":p": `ORDERS#${customerId}`,
          ":s": `${orderId}`,
        },
      })
    );
    if (!result.Items || result.Items.length === 0) {
      throw new Error(`Order not found for orderId: ${orderId}`);
    }
    let orderRecord: DdbOrder | null = null;
    const orderItems: DdbOrderItem[] = [];

    for (const item of result.Items) {
      if (item.s === orderId) {
        orderRecord = item as DdbOrder;
      } else if (item.s.startsWith(`${orderId}#ITEMS#`)) {
        orderItems.push(item as DdbOrderItem);
      }
    }

    if (!orderRecord) {
      throw new Error(`Order record not found for orderId: ${orderId}`);
    }

    return convertDdbToOrder({
      ddbItem: orderRecord,
      ddbOrderItems: orderItems,
    });
  } catch (error) {
    throw new Error(`Failed to get order: ${(error as Error).message}`);
  }
}

/**
 * Retrieves all order items for a specific order from DynamoDB
 * @async
 * @param {Object} params - The parameters for retrieving order items
 * @param {string} params.customerId - The ID of the customer who owns the order
 * @param {string} params.orderId - The ID of the order whose items to retrieve
 * @returns {Promise<DdbOrderItem[]>} Array of order items
 * @throws {Error} If DynamoDB query fails
 */
export async function getDdbOrderItems({
  customerId,
  orderId,
}: {
  customerId: string;
  orderId: string;
}): Promise<DdbOrderItem[]> {
  const queryResult = await docClient.send(
    new QueryCommand({
      TableName: DYNAMODB_TABLE_NAME,
      KeyConditionExpression: "p = :p AND begins_with(s, :s)",
      ExpressionAttributeValues: {
        ":p": `ORDERS#${customerId}`,
        ":s": `${orderId}#ITEMS#`,
      },
    })
  );
  if (!queryResult.Items) {
    return [];
  } else {
    return queryResult.Items as DdbOrderItem[];
  }
}

/**
 * Deletes an order and all its items from DynamoDB
 * @async
 * @param {Object} params - The parameters for deleting the order
 * @param {string} params.customerId - The ID of the customer who owns the order
 * @param {string} params.orderId - The ID of the order to delete
 * @throws {Error} If DynamoDB operation fails
 * @returns {Promise<void>}
 */
export async function deleteOrder({
  customerId,
  orderId,
}: {
  customerId: string;
  orderId: string;
}) {
  const ddbOrderItems = await getDdbOrderItems({ customerId, orderId });
  const promises = [
    docClient.send(
      new DeleteCommand({
        TableName: DYNAMODB_TABLE_NAME,
        Key: {
          p: `ORDERS#${customerId}`,
          s: orderId,
        },
      })
    ),
  ];
  for (const item of ddbOrderItems) {
    promises.push(
      docClient.send(
        new DeleteCommand({
          TableName: DYNAMODB_TABLE_NAME,
          Key: {
            p: item.p,
            s: item.s,
          },
        })
      )
    );
  }
  await Promise.all(promises);
}

/**
 * Updates an existing order in DynamoDB
 * @async
 * @param {Object} params - The parameters for updating the order
 * @param {OrderUpdate} params.orderUpdate - The update data for the order
 * @param {string} params.orderId - The ID of the order to update
 * @param {string} params.customerId - The ID of the customer who owns the order
 * @returns {Promise<Order>} The updated order
 * @throws {Error} If order not found or update fails
 */
export async function updateOrder({
  orderUpdate,
  orderId,
  customerId,
}: {
  orderUpdate: OrderUpdate;
  orderId: string;
  customerId: string;
}): Promise<Order> {
  const order = await getOrder({ customerId, orderId });
  const updatedOrder = {
    ...order,
    ...orderUpdate,
  };
  await writeOrder({ order: updatedOrder, update: true });
  return updatedOrder;
}
