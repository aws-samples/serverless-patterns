import type { LambdaInterface } from "@aws-lambda-powertools/commons/types";
import { MetricUnit } from "@aws-lambda-powertools/metrics";
import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";

import type { Context } from "aws-lambda";
import { v4 as uuidv4 } from "uuid";
import {
  Order,
  OrderCreationInput,
  OrderUpdate,
} from "@ordersCommonCode/order";
import { getCustomerIdFromAuthInfo } from "@ordersCommonCode/customer";
import { writeOrder, getOrder, updateOrder, deleteOrder } from "./ddb";
import { logger, metrics, secretsProvider, tracer } from "./powertools";

/**
 * Simulates an external payment processing operation with X-Ray tracing
 * @async
 * @throws {Error} If secret retrieval fails
 * @returns {Promise<void>}
 */
async function simulateExternalPaymentProcessing() {
  const segment = tracer.getSegment();
  const subsegment = segment?.addNewSubsegment("### payment processing");
  await secretsProvider.get(process.env.API_KEY_SECRET_ARN!, {
    maxAge: 300,
  });
  await new Promise((resolve) =>
    setTimeout(resolve, Math.floor(Math.random() * 100) + 100)
  );
  subsegment?.close();
}

/**
 * Handles the creation of a new order
 * @async
 * @param {Object} params - The parameters object
 * @param {APIGatewayProxyEvent} params.event - The API Gateway event
 * @param {string} params.customerId - The customer's unique identifier
 * @returns {Promise<APIGatewayProxyResult>} The API response with the created order
 * @throws {Error} If order creation fails
 */
async function handleOrderCreationEvent({
  event,
  customerId,
}: {
  event: APIGatewayProxyEvent;
  customerId: string;
}) {
  const orderCreationInput: OrderCreationInput = JSON.parse(event.body || "{}");
  const order: Order = {
    ...orderCreationInput,
    customerId,
    orderId: `ORD-${uuidv4()}`,
    status: "PENDING",
    createdAt: new Date().toISOString(),
  };
  await simulateExternalPaymentProcessing();
  await writeOrder({
    order,
    update: false,
  });
  return {
    statusCode: 201,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(order),
  };
}

/**
 * Retrieves an order by ID for a specific customer
 * @async
 * @param {Object} params - The parameters object
 * @param {string} params.customerId - The customer's unique identifier
 * @param {string} params.orderId - The order's unique identifier
 * @returns {Promise<APIGatewayProxyResult>} The API response with the order details
 * @throws {Error} If order retrieval fails
 */
async function handleOrderGetEvent({
  customerId,
  orderId,
}: {
  customerId: string;
  orderId: string;
}) {
  const order = await getOrder({
    customerId,
    orderId: orderId,
  });
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(order),
  };
}

/**
 * Updates an existing order
 * @async
 * @param {Object} params - The parameters object
 * @param {APIGatewayProxyEvent} params.event - The API Gateway event
 * @param {string} params.customerId - The customer's unique identifier
 * @param {string} params.orderId - The order's unique identifier
 * @returns {Promise<APIGatewayProxyResult>} The API response with the updated order
 * @throws {Error} If order update fails
 */
async function handleOrderUpdateEvent({
  event,
  customerId,
  orderId,
}: {
  event: APIGatewayProxyEvent;
  customerId: string;
  orderId: string;
}) {
  const orderUpdateInput: OrderUpdate = JSON.parse(event.body || "{}");
  const order = await updateOrder({
    orderUpdate: orderUpdateInput,
    orderId: orderId,
    customerId,
  });
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(order),
  };
}

/**
 * Deletes an order by ID
 * @async
 * @param {Object} params - The parameters object
 * @param {string} params.customerId - The customer's unique identifier
 * @param {string} params.orderId - The order's unique identifier
 * @returns {Promise<APIGatewayProxyResult>} The API response confirming deletion
 * @throws {Error} If order deletion fails
 */
async function handleOrderDeleteEvent({
  customerId,
  orderId,
}: {
  customerId: string;
  orderId: string;
}) {
  await deleteOrder({
    customerId,
    orderId: orderId,
  });
  return {
    statusCode: 204,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  };
}

/**
 * Main Lambda handler class implementing CRUD operations for orders
 * @class
 * @implements {LambdaInterface}
 */
class HandleOrderLambda implements LambdaInterface {
  @tracer.captureLambdaHandler()
  @metrics.logMetrics()
  @logger.injectLambdaContext({
    flushBufferOnUncaughtError: true,
  })
  public async handler(
    event: APIGatewayProxyEvent,
    _context: Context
  ): Promise<APIGatewayProxyResult> {
    logger.logEventIfEnabled(event);

    const segment = tracer.getSegment();

    const customerId = getCustomerIdFromAuthInfo({ event });
    const orderId = event.pathParameters?.orderId;
    segment?.addAnnotation("customerId", customerId);
    if (orderId) {
      segment?.addAnnotation("orderId", orderId);
    }

    try {
      switch (event.httpMethod) {
        case "POST":
          if (event.path === "/order") {
            metrics.addMetric("OrdersCreated", MetricUnit.Count, 1);
            return await handleOrderCreationEvent({ event, customerId });
          }
          break;
        case "GET":
          if (event.path.match(/^\/order\/[^/]+$/)) {
            metrics.addMetric("OrdersGotten", MetricUnit.Count, 1);
            return await handleOrderGetEvent({ customerId, orderId: orderId! });
          }
          break;
        case "PUT":
          if (event.path.match(/^\/order\/[^/]+$/)) {
            metrics.addMetric("OrdersUpdated", MetricUnit.Count, 1);
            return await handleOrderUpdateEvent({
              event,
              customerId,
              orderId: orderId!,
            });
          }
          break;
        case "DELETE":
          if (event.path.match(/^\/order\/[^/]+$/)) {
            metrics.addMetric("OrdersDeleted", MetricUnit.Count, 1);
            return await handleOrderDeleteEvent({
              customerId,
              orderId: orderId!,
            });
          }
          break;
      }
      return {
        statusCode: 400,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: "Invalid request" }),
      };
    } catch (error) {
      segment?.addError(error as Error);
      console.error("Error:", error);
      return {
        statusCode: 500,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: "Internal Server Error" }),
      };
    }
  }
}

const handlerClass = new HandleOrderLambda();
export const handler = handlerClass.handler.bind(handlerClass);
