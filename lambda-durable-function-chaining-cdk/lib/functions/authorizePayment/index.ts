import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";

interface PaymentEvent {
  orderId: string;
  customerId: string;
  items: {
    productId: string;
    quantity: number;
  }[];
  paymentMethod: {
    type: "credit" | "debit";
    cardNumber: string;
    cardBrand: "Visa" | "Mastercard" | "Amex";
  };
}

const dynamoClient = new DynamoDBClient();

export async function handler(event: PaymentEvent) {
  console.log("Authorizing payment for order:", event.orderId);

  const { paymentMethod, orderId, customerId, items } = event;

  // Fetch pricing from DynamoDB and calculate total
  let amount = 0;
  const itemsWithPricing = [];

  for (const item of items) {
    const result = await dynamoClient.send(
      new GetItemCommand({
        TableName: process.env.PRODUCT_CATALOG_TABLE,
        Key: { productId: { S: item.productId } },
      }),
    );

    if (!result.Item) {
      return {
        orderId,
        status: "declined",
        reason: "product_not_found",
        productId: item.productId,
        timestamp: new Date().toISOString(),
      };
    }

    const price = parseFloat(result.Item.price.N!);
    const itemTotal = price * item.quantity;
    amount += itemTotal;

    itemsWithPricing.push({
      productId: item.productId,
      quantity: item.quantity,
      unitPrice: price,
      itemTotal,
    });
  }

  // Simulate payment gateway call
  const authorizationId = `AUTH-${Date.now()}-${crypto.randomUUID()}`;
  
  // Mock validation - reject if amount is too high (for demo purposes)
  if (amount > 10000) {
    return {
      orderId,
      status: "declined",
      reason: "amount_exceeds_limit",
      amount,
      timestamp: new Date().toISOString(),
    };
  }

  // Mock card validation
  const lastFourDigits = String(paymentMethod.cardNumber).slice(-4);
  
  return {
    orderId,
    customerId,
    status: "authorized",
    authorizationId,
    amount,
    items: itemsWithPricing,
    cardBrand: paymentMethod.cardBrand,
    lastFourDigits,
    timestamp: new Date().toISOString(),
    expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(), // 7 days
  };
}
