import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

import {
  convertDdbToOrder,
  DdbOrder,
  DdbOrderItem,
  Order,
  OrderSearchCriteria,
  OrderSearchResponse,
} from "@ordersCommonCode/order";
import { tracer } from "./powertools";

const DYNAMODB_TABLE_NAME = process.env["DYNAMODB_TABLE_NAME"];
if (!DYNAMODB_TABLE_NAME) {
  throw new Error("DYNAMODB_TABLE_NAME is not defined");
}
const client = tracer.captureAWSv3Client(new DynamoDBClient({}));
const docClient = DynamoDBDocumentClient.from(client);

/**
 * Sorts and paginates a list of orders based on search criteria
 * @param {Object} params - The parameters object
 * @param {Order[]} params.orders - Array of orders to sort and paginate
 * @param {OrderSearchCriteria} params.orderSearchCriteria - Criteria for sorting and pagination
 * @returns {OrderSearchResponse} Paginated and sorted orders with pagination metadata
 */
function sortAndPageLimitOrders({
  orders,
  orderSearchCriteria,
}: {
  orders: Order[];
  orderSearchCriteria: OrderSearchCriteria;
}): OrderSearchResponse {
  // default order: descending by createdAt
  if (orderSearchCriteria.sortBy === "status") {
    if (orderSearchCriteria.sortOrder === "asc") {
      orders.sort((a, b) => a.status.localeCompare(b.status));
    } else {
      orders.sort((a, b) => b.status.localeCompare(a.status));
    }
  } else {
    if (orderSearchCriteria.sortOrder === "asc") {
      orders.sort(
        (a, b) =>
          new Date(a.createdAt).getTime() - new Date(b.createdAt).getTime()
      );
    } else {
      orders.sort(
        (a, b) =>
          new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
      );
    }
  }

  const page = Math.max(1, orderSearchCriteria.page || 1);
  const limit = Math.max(1, orderSearchCriteria.limit || 20);
  const startIndex = (page - 1) * limit;
  const endIndex = startIndex + limit;
  const paginatedOrders = orders.slice(startIndex, endIndex);

  return {
    items: paginatedOrders,
    pagination: {
      total: orders.length,
      pages: Math.ceil(orders.length / limit),
      currentPage: page,
      limit,
    },
  };
}

/**
 * Filters orders based on search criteria
 * @param {Object} params - The parameters object
 * @param {DdbOrder[]} params.ddbOrders - Array of DynamoDB orders
 * @param {DdbOrderItem[]} params.ddbOrderItems - Array of DynamoDB order items
 * @param {OrderSearchCriteria} params.orderSearchCriteria - Criteria for filtering orders
 * @returns {Order[]} Filtered array of orders
 */
function getFilteredOrders({
  ddbOrders,
  ddbOrderItems,
  orderSearchCriteria,
}: {
  ddbOrders: DdbOrder[];
  ddbOrderItems: DdbOrderItem[];
  orderSearchCriteria: OrderSearchCriteria;
}): Order[] {
  const orders: Order[] = [];
  for (const ddbOrder of ddbOrders) {
    if (
      orderSearchCriteria.statuses &&
      !orderSearchCriteria.statuses.includes(ddbOrder.status)
    ) {
      continue;
    }

    const orderItems = ddbOrderItems.filter((item) =>
      item.s.startsWith(`${ddbOrder.s}#ITEMS#`)
    );

    const order = convertDdbToOrder({
      ddbItem: ddbOrder,
      ddbOrderItems: orderItems,
    });

    if (
      orderSearchCriteria.productIds &&
      !order.items.find((orderItem) =>
        orderSearchCriteria.productIds?.includes(orderItem.productId)
      )
    ) {
      continue;
    }

    orders.push(order);
  }

  return orders;
}

/**
 * Searches for orders in DynamoDB based on customer ID and search criteria
 * @param {Object} params - The parameters object
 * @param {OrderSearchCriteria} params.orderSearchCriteria - Search criteria for filtering and sorting orders
 * @param {string} params.customerId - Customer ID to search orders for
 * @returns {Promise<OrderSearchResponse>} Filtered, sorted, and paginated orders with metadata
 * @throws {Error} If DynamoDB query fails
 */
export async function searchOrders({
  orderSearchCriteria,
  customerId,
}: {
  orderSearchCriteria: OrderSearchCriteria;
  customerId: string;
}): Promise<OrderSearchResponse> {
  const queryResult = await docClient.send(
    new QueryCommand({
      TableName: DYNAMODB_TABLE_NAME,
      KeyConditionExpression: "p = :p",
      ExpressionAttributeValues: {
        ":p": `ORDERS#${customerId}`,
      },
    })
  );
  if (!queryResult.Items) {
    return {
      items: [],
      pagination: {
        total: 0,
        pages: 0,
        currentPage: 1,
        limit: orderSearchCriteria.limit || 20,
      },
    };
  }
  const ddbOrders: DdbOrder[] = [];
  const ddbOrderItems: DdbOrderItem[] = [];

  for (const item of queryResult.Items) {
    if (item.s.includes("#ITEMS#")) {
      ddbOrderItems.push(item as DdbOrderItem);
    } else {
      ddbOrders.push(item as DdbOrder);
    }
  }

  const filteredOrders = getFilteredOrders({
    ddbOrders,
    ddbOrderItems,
    orderSearchCriteria,
  });
  return sortAndPageLimitOrders({
    orders: filteredOrders,
    orderSearchCriteria,
  });
}
