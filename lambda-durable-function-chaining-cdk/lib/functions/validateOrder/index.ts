import { DurableContext, withDurableExecution } from "@aws/durable-execution-sdk-js";
import { LambdaClient, InvokeCommand } from "@aws-sdk/client-lambda";

interface Order {
  orderId: string;
  customerId: string;
  items: {
    productId: string;
    quantity: number;
    unitPrice: number;
  }[];
  shippingAddress: string;
  billingAddress: string;
  paymentMethod: {
    type: "credit" | "debit";
    cardNumber: number;
    cardBrand: "Visa" | "Mastercard" | "Amex";
  };
  orderTotal: number;
  orderTimestamp: string;
}

const lambdaClient = new LambdaClient();

export const handler = withDurableExecution(async (event: Order, context: DurableContext) => {
  const { orderId, items, shippingAddress, billingAddress, paymentMethod, orderTotal } = event;

  const validation = await context.step("validate-order", async () => {
    return { isValid: true };
  });

  if (!validation.isValid) {
    return { orderId, status: "rejected", reason: "invalid_items" };
  }

  const authorization = await context.step("authorize-payment", async () => {
    return await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.AUTHORIZE_PAYMENT_FUNCTION,
      }),
    );
  });

  const allocation = await context.step("allocate-inventory", async () => {
    return await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.ALLOCATE_INVENTORY_FUNCTION,
      }),
    );
  });

  const fulfillment = await context.step("fulfill-order", async () => {
    return await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.FULFILL_ORDER_FUNCTION,
      }),
    );
  });

  return {
    orderId,
    status: "completed",
    timestamp: new Date().toISOString(),
  };
});
