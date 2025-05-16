import { MetricUnit } from "@aws-lambda-powertools/metrics";
import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";
import type { Context } from "aws-lambda";
import type { LambdaInterface } from "@aws-lambda-powertools/commons/types";
import { logger, metrics, tracer } from "./powertools";
import { OrderSearchCriteria } from "@ordersCommonCode/order";
import { searchOrders } from "./ddb";
import { getCustomerIdFromAuthInfo } from "@ordersCommonCode/customer";

/**
 * Lambda class handling order search operations through API Gateway
 * @class
 * @implements {LambdaInterface}
 */
class SearchOrderLambda implements LambdaInterface {
  /**
   * Main Lambda handler method for processing order search requests
   * @async
   * @param {APIGatewayProxyEvent} event - The API Gateway event containing search criteria
   * @param {Context} _context - AWS Lambda context
   * @returns {Promise<APIGatewayProxyResult>} API response with search results or error
   * @throws {Error} If search operation fails
   */
  @tracer.captureLambdaHandler()
  @metrics.logMetrics()
  @logger.injectLambdaContext({
    flushBufferOnUncaughtError: true,
  })
  public async handler(
    event: APIGatewayProxyEvent,
    _context: Context
  ): Promise<APIGatewayProxyResult> {
    logger.appendKeys({
      stage: process.env.STAGE,
    });

    logger.logEventIfEnabled(event);

    metrics.addMetric("ProcessedEvents", MetricUnit.Count, 1);
    const segment = tracer.getSegment();

    const customerId = getCustomerIdFromAuthInfo({ event });
    segment?.addAnnotation("customerId", customerId);

    try {
      const orderSearchCriteria: OrderSearchCriteria = JSON.parse(
        event.body || "{}"
      );

      const response = await searchOrders({
        customerId,
        orderSearchCriteria,
      });

      return {
        statusCode: 200,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(response),
      };
    } catch (error) {
      console.error("Search Orders Error:", error);
      return {
        statusCode: 500,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: "Invalid search criteria or internal error occured" }),
      };
    }
  }
}

const searchClass = new SearchOrderLambda();
export const handler = searchClass.handler.bind(searchClass);
