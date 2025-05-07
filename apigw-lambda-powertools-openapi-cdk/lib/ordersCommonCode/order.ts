import { components, paths } from "./types";

export type Address = components["schemas"]["Address"];
export type Order = components["schemas"]["Order"];
export type OrderCreationInput = components["schemas"]["OrderCreationInput"];
export type OrderItem = components["schemas"]["OrderItem"];
export type OrderResponse = components["schemas"]["Order"];
export type OrderSearchCriteria = components["schemas"]["OrderSearchCriteria"];
export type OrderSearchResponse = paths["/orders/search"]["post"]["responses"]["200"]["content"]["application/json"]
export type OrderStatus = components["schemas"]["OrderStatus"];
export type OrderUpdate = components["schemas"]["OrderUpdate"];
export type PaymentMethod = components["schemas"]["PaymentMethod"];
export type ShippingMethod = components["schemas"]["ShippingMethod"];

/**
 * Represents an order record in DynamoDB
 * @interface DdbOrder
 * @property {string} p - Partition key in format "ORDERS#{customerId}"
 * @property {string} s - Sort key containing the orderId
 * @property {string} customerId - Unique identifier for the customer
 * @property {Address} shippingAddress - Shipping address details
 * @property {Address} billingAddress - Billing address details
 * @property {number} [tax] - Tax amount applied to the order
 * @property {number} [shippingCost] - Shipping cost for the order
 * @property {PaymentMethod} [paymentMethod] - Method of payment
 * @property {ShippingMethod} [shippingMethod] - Method of shipping
 * @property {string} [customerNotes] - Additional notes from the customer
 * @property {boolean} giftWrapping - Whether gift wrapping was requested
 * @property {string} [couponCode] - Applied coupon code
 * @property {number} [discountAmount] - Discount amount applied
 * @property {OrderStatus} status - Current status of the order
 * @property {string} createdAt - Timestamp of order creation
 */
export interface DdbOrder {
  p: string;
  s: string;
  customerId: string;
  shippingAddress: Address;
  billingAddress: Address;
  tax?: number;
  shippingCost?: number;
  paymentMethod?: PaymentMethod;
  shippingMethod?: ShippingMethod;
  customerNotes?: string;
  giftWrapping: boolean;
  couponCode?: string;
  discountAmount?: number;
  status: OrderStatus;
  createdAt: string;
}

/**
 * Represents an order item record in DynamoDB
 * @interface DdbOrderItem
 * @property {string} p - Partition key in format "ORDERS#{customerId}#{orderId}"
 * @property {string} s - Sort key in format "{orderId}#{productId}"
 * @property {string} [productName] - Name of the product
 * @property {number} quantity - Quantity ordered
 * @property {number} price - Price per unit
 * @property {string} [sku] - Stock Keeping Unit
 * @property {string} [variantId] - Identifier for product variant
 */
export interface DdbOrderItem {
  p: string;
  s: string;
  productName?: string;
  quantity: number;
  price: number;
  sku?: string;
  variantId?: string;
}

/**
 * Converts an Order object to DynamoDB format
 * @param {Order} order - The order to convert
 * @returns {Object} Object containing the converted order and its items
 * @property {DdbOrder} ddbOrder - The main order record for DynamoDB
 * @property {DdbOrderItem[]} ddbOrderItems - Array of order item records for DynamoDB
 */
export function convertOrderToDdb({ order }: { order: Order }): {
  ddbOrder: DdbOrder;
  ddbOrderItems: DdbOrderItem[];
} {
  const ddbItem: DdbOrder = {
    p: `ORDERS#${order.customerId}`,
    s: order.orderId,
    customerId: order.customerId,
    shippingAddress: order.shippingAddress,
    billingAddress: order.billingAddress,
    shippingCost: order.shippingCost,
    paymentMethod: order.paymentMethod,
    shippingMethod: order.shippingMethod,
    customerNotes: order.customerNotes,
    giftWrapping: order.giftWrapping,
    couponCode: order.couponCode,
    discountAmount: order.discountAmount,
    status: order.status,
    createdAt: order.createdAt,
  };
  const ddbItems: DdbOrderItem[] = order.items.map((item) => ({
    p: `ORDERS#${order.customerId}`,
    s: `${order.orderId}#ITEMS#${item.productId}`,
    productName: item.productName,
    quantity: item.quantity,
    price: item.price,
    sku: item.sku,
    variantId: item.variantId,
  }));
  Object.keys(ddbItem).forEach((key) => {
    if (ddbItem[key as keyof DdbOrder] === undefined) {
      delete ddbItem[key as keyof DdbOrder];
    }
  });
  ddbItems.forEach((item) => {
    Object.keys(item).forEach((key) => {
      if (item[key as keyof DdbOrderItem] === undefined) {
        delete item[key as keyof DdbOrderItem];
      }
    });
  });
  return {
    ddbOrder: ddbItem,
    ddbOrderItems: ddbItems,
  };
}

/**
 * Converts a DynamoDB order item record to an OrderItem object
 * @param {DdbOrderItem} ddbOrderItem - The order item record from DynamoDB
 * @returns {OrderItem} The converted OrderItem object
 */
export function convertDdbToOrderItem({
  ddbOrderItem,
}: {
  ddbOrderItem: DdbOrderItem;
}): OrderItem {
  return {
    productId: ddbOrderItem.s.split("#ITEMS#")[1]!,
    productName: ddbOrderItem.productName,
    quantity: ddbOrderItem.quantity,
    price: ddbOrderItem.price,
    sku: ddbOrderItem.sku,
    variantId: ddbOrderItem.variantId,
  };
}

/**
 * Converts DynamoDB order records back to an Order object
 * @param {DdbOrder} ddbItem - The main order record from DynamoDB
 * @param {DdbOrderItem[]} ddbOrderItems - Array of order item records from DynamoDB
 * @returns {Order} The reconstructed Order object
 */
export function convertDdbToOrder({
  ddbItem,
  ddbOrderItems,
}: {
  ddbItem: DdbOrder;
  ddbOrderItems: DdbOrderItem[];
}): Order {
  const order: Order = {
    orderId: ddbItem.s,
    customerId: ddbItem.customerId,
    items: ddbOrderItems.map((item) =>
      convertDdbToOrderItem({ ddbOrderItem: item })
    ),
    shippingAddress: ddbItem.shippingAddress,
    billingAddress: ddbItem.billingAddress,
    shippingCost: ddbItem.shippingCost,
    paymentMethod: ddbItem.paymentMethod,
    shippingMethod: ddbItem.shippingMethod,
    customerNotes: ddbItem.customerNotes,
    giftWrapping: ddbItem.giftWrapping,
    couponCode: ddbItem.couponCode,
    discountAmount: ddbItem.discountAmount,
    status: ddbItem.status,
    createdAt: ddbItem.createdAt,
  };
  return order;
}
