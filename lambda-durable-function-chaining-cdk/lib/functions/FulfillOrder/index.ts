interface FulfillmentEvent {
  orderId: string;
  customerId: string;
  items: {
    productId: string;
    quantity: number;
    unitPrice: number;
    itemTotal: number;
  }[];
  shippingAddress: string;
  allocations: {
    allocationId: string;
    productId: string;
    quantity: number;
    warehouseLocation: string;
  }[];
}

export async function handler(event: FulfillmentEvent) {
  console.log("Fulfilling order:", event.orderId);

  const { orderId, customerId, items, shippingAddress, allocations } = event;

  // Mock shipping carrier selection
  const carriers = ["Amazon Prime", "My Carrier", "Mock Carrier"];
  const selectedCarrier = carriers[Math.floor(crypto.getRandomValues(new Uint32Array(1))[0] / 0x100000000 * carriers.length)];

  const trackingNumber = `${selectedCarrier}-${Date.now()}-${crypto.randomUUID()}`;

  const estimatedDeliveryDays = Math.floor(crypto.getRandomValues(new Uint32Array(1))[0] / 0x100000000 * 5) + 3;
  const estimatedDeliveryDate = new Date(Date.now() + estimatedDeliveryDays * 24 * 60 * 60 * 1000);

  // Create shipments with pricing information
  const shipments = allocations.map((allocation) => {
    const item = items.find(i => i.productId === allocation.productId);
    return {
      shipmentId: `SHIP-${allocation.warehouseLocation}-${crypto.randomUUID()}`,
      warehouseLocation: allocation.warehouseLocation,
      productId: allocation.productId,
      quantity: allocation.quantity,
      unitPrice: item?.unitPrice || 0,
      itemTotal: item?.itemTotal || 0,
      status: "preparing",
    };
  });

  // Mock order fulfillment details
  return {
    orderId,
    customerId,
    status: "fulfilled",
    trackingNumber,
    carrier: selectedCarrier,
    shippingAddress,
    shipments,
    estimatedDeliveryDate: estimatedDeliveryDate.toISOString(),
    totalItems: items.reduce((sum, item) => sum + item.quantity, 0),
    fulfillmentTimestamp: new Date().toISOString(),
    notifications: {
      emailSent: true,
      smsSent: true,
    },
  };
}
