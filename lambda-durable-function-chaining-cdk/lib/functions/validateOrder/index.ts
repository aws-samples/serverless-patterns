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
    // Mock order validation logic
    const errors = [];

    // Validate items
    if (!items || items.length === 0) {
      errors.push("No items in order");
    }

    // Validate addresses
    if (!shippingAddress || shippingAddress.trim() === "") {
      errors.push("Invalid shipping address");
    }

    if (!billingAddress || billingAddress.trim() === "") {
      errors.push("Invalid billing address");
    }

    // Validate payment method
    if (!paymentMethod || !paymentMethod.cardNumber) {
      errors.push("Invalid payment method");
    }

    // Validate order total
    const calculatedTotal = items.reduce((sum, item) => sum + item.quantity * item.unitPrice, 0);
    if (Math.abs(calculatedTotal - orderTotal) > 0.01) {
      errors.push("Order total mismatch");
    }

    return {
      isValid: errors.length === 0,
      errors,
      validatedAt: new Date().toISOString(),
    };
  });

  if (!validation.isValid) {
    return {
      orderId,
      status: "rejected",
      reason: "validation_failed",
      errors: validation.errors,
      timestamp: new Date().toISOString(),
    };
  }

  const authorization = await context.step("authorize-payment", async () => {
    const response = await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.AUTHORIZE_PAYMENT_FUNCTION,
        Payload: JSON.stringify({
          orderId,
          customerId: event.customerId,
          paymentMethod,
          amount: orderTotal,
        }),
      }),
    );

    const payload = JSON.parse(new TextDecoder().decode(response.Payload));
    return payload;
  });

  if (authorization.status === "declined") {
    return {
      orderId,
      status: "payment_declined",
      reason: authorization.reason,
      timestamp: new Date().toISOString(),
    };
  }

  const allocation = await context.step("allocate-inventory", async () => {
    const response = await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.ALLOCATE_INVENTORY_FUNCTION,
        Payload: JSON.stringify({
          orderId,
          items,
        }),
      }),
    );

    const payload = JSON.parse(new TextDecoder().decode(response.Payload));
    return payload;
  });

  if (allocation.status === "failed") {
    return {
      orderId,
      status: "inventory_unavailable",
      reason: allocation.reason,
      productId: allocation.productId,
      timestamp: new Date().toISOString(),
    };
  }

  const fulfillment = await context.step("fulfill-order", async () => {
    const response = await lambdaClient.send(
      new InvokeCommand({
        FunctionName: process.env.FULFILL_ORDER_FUNCTION,
        Payload: JSON.stringify({
          orderId,
          customerId: event.customerId,
          items,
          shippingAddress,
          allocations: allocation.allocations,
        }),
      }),
    );

    const payload = JSON.parse(new TextDecoder().decode(response.Payload));
    return payload;
  });

  return {
    orderId,
    customerId: event.customerId,
    status: "completed",
    orderTotal,
    validation,
    payment: {
      authorizationId: authorization.authorizationId,
      amount: authorization.amount,
      cardBrand: authorization.cardBrand,
      lastFourDigits: authorization.lastFourDigits,
    },
    inventory: {
      totalItems: allocation.totalItems,
      allocations: allocation.allocations,
    },
    fulfillment: {
      trackingNumber: fulfillment.trackingNumber,
      carrier: fulfillment.carrier,
      estimatedDeliveryDate: fulfillment.estimatedDeliveryDate,
      shipments: fulfillment.shipments,
    },
    completedAt: new Date().toISOString(),
  };
});
