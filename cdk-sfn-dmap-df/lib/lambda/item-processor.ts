import {
  DurableContext,
  withDurableExecution,
} from "@aws/durable-execution-sdk-js";

interface ProductItem {
  itemId: string;
  productName: string;
  category: string;
  price: number;
}

interface ProcessedProduct {
  itemId: string;
  productName: string;
  category: string;
  price: number;
  priceTier: string;
  validatedAt: string;
  status: string;
  processedAt: string;
}

function computePriceTier(price: number): string {
  if (price < 25) return "budget";
  if (price < 100) return "standard";
  return "premium";
}

export const handler = withDurableExecution(
  async (
    event: ProductItem,
    context: DurableContext,
  ): Promise<ProcessedProduct> => {
    context.logger.info("Starting product catalog update", {
      itemId: event.itemId,
      productName: event.productName,
    });

    // Note: No try/catch here by design. Errors thrown inside steps are
    // checkpointed by the durable SDK — the execution is marked as failed
    // and won't re-execute on replay. The Step Functions Distributed Map
    // handles failed items at the orchestration level (visible in map results).

    // Step 1: Validate the product record and enrich with pricing tier
    const validated = await context.step("validate-item", async (stepCtx) => {
      if (!event.itemId || !event.productName || !event.category) {
        throw new Error(`Missing required fields for item ${event.itemId}`);
      }
      if (event.price <= 0) {
        throw new Error(
          `Invalid price ${event.price} for item ${event.itemId}`,
        );
      }

      const priceTier = computePriceTier(event.price);
      const validatedAt = new Date().toISOString();

      stepCtx.logger.info("Item validated", {
        itemId: event.itemId,
        priceTier,
        validatedAt,
      });

      return { priceTier, validatedAt };
    });

    // Wait: Simulate downstream rate limiting / backpressure
    await context.wait("rate-limit-delay", { seconds: 5 });

    // Step 2: Update the catalog entry
    const result = await context.step("update-catalog", async (stepCtx) => {
      const processedAt = new Date().toISOString();

      stepCtx.logger.info("Catalog entry updated", {
        itemId: event.itemId,
        processedAt,
      });

      return {
        itemId: event.itemId,
        productName: event.productName,
        category: event.category,
        price: event.price,
        priceTier: validated.priceTier,
        validatedAt: validated.validatedAt,
        status: "completed",
        processedAt,
      };
    });

    context.logger.info("Product catalog update finished", {
      itemId: result.itemId,
      status: result.status,
    });

    return result;
  },
);
