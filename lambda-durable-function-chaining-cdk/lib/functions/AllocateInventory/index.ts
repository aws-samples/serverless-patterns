import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";

interface InventoryEvent {
  orderId: string;
  items: {
    productId: string;
    quantity: number;
    unitPrice: number;
  }[];
}

const dynamoClient = new DynamoDBClient();

export async function handler(event: InventoryEvent) {
  console.log("Allocating inventory for order:", event.orderId);

  const { orderId, items } = event;
  const allocations = [];

  for (const item of items) {
    const { productId, quantity } = item;

    // Get product from catalog
    const result = await dynamoClient.send(
      new GetItemCommand({
        TableName: process.env.PRODUCT_CATALOG_TABLE,
        Key: { productId: { S: productId } },
      }),
    );

    if (!result.Item) {
      return {
        orderId,
        status: "failed",
        reason: "product_not_found",
        productId,
        timestamp: new Date().toISOString(),
      };
    }

    const stockLevel = parseInt(result.Item.stockLevel.N!);
    const warehouseLocation = result.Item.warehouseLocation.S!;

    if (stockLevel < quantity) {
      return {
        orderId,
        status: "failed",
        reason: "insufficient_inventory",
        productId,
        requested: quantity,
        available: stockLevel,
        timestamp: new Date().toISOString(),
      };
    }

    const allocationId = `ALLOC-${productId}-${crypto.randomUUID()}`;

    allocations.push({
      allocationId,
      productId,
      quantity,
      warehouseLocation,
      reservedUntil: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
    });
  }

  return {
    orderId,
    status: "allocated",
    allocations,
    totalItems: items.reduce((sum, item) => sum + item.quantity, 0),
    timestamp: new Date().toISOString(),
  };
}
