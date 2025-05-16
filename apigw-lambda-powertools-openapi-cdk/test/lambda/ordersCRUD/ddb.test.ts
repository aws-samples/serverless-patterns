process.env.DYNAMODB_TABLE_NAME = 'test-orders-table';

import {
  DynamoDBDocumentClient,
  PutCommand,
  DeleteCommand,
  QueryCommand,
} from '@aws-sdk/lib-dynamodb';
import { mockClient } from 'aws-sdk-client-mock';
import 'aws-sdk-client-mock-jest';

jest.mock('../../../lib/lambda/ordersCRUD/powertools', () => ({
  tracer: {
    captureAWSv3Client: jest.fn().mockImplementation((client) => client),
  },
}));

import {
  writeOrder,
  getOrder,
  getDdbOrderItems,
  deleteOrder,
  updateOrder
} from '../../../lib/lambda/ordersCRUD/ddb';
import { Order, OrderUpdate } from '../../../lib/ordersCommonCode/order';

const ddbMock = mockClient(DynamoDBDocumentClient);

describe('DynamoDB Operations', () => {
  beforeEach(() => {
    ddbMock.reset();
    jest.clearAllMocks();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  const mockOrder: Order = {
    customerId: 'CUST123',
    orderId: 'ORD-abc123',
    items: [
      {
        productId: 'PROD789',
        productName: 'AnyCompany Run',
        quantity: 1,
        price: 129.99,
        sku: 'AC-AM24-BLK-42',
        variantId: 'SIZE-42-BLACK'
      }
    ],
    shippingAddress: {
      street: '123 Main Street',
      city: 'Anytown',
      state: 'WA',
      postalCode: '31415',
      country: 'USA'
    },
    billingAddress: {
      street: '123 Main Street',
      city: 'Anytown',
      state: 'WA',
      postalCode: '31415',
      country: 'USA'
    },
    giftWrapping: false,
    status: 'PENDING',
    createdAt: '2023-06-15T10:30:00Z'
  };

  describe('writeOrder', () => {
    it('should write a new order with condition expression when update is false', async () => {
      ddbMock.on(PutCommand).resolves({});

      await writeOrder({ order: mockOrder, update: false });

      // Verify the main order record was written with condition expression
      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123'
        }),
        ConditionExpression: 'attribute_not_exists(p) AND attribute_not_exists(s)'
      });

      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789'
        })
      });
    });

    it('should update an existing order without condition expression when update is true', async () => {
      ddbMock.on(PutCommand).resolves({});

      await writeOrder({ order: mockOrder, update: true });

      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123'
        })
      });
    });

    it('should handle orders with multiple items', async () => {
      const orderWithMultipleItems: Order = {
        ...mockOrder,
        items: [
          {
            productId: 'PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99
          },
          {
            productId: 'PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(PutCommand).resolves({});

      await writeOrder({ order: orderWithMultipleItems, update: false });

      // Verify both items were written
      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789'
        })
      });

      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD456'
        })
      });
    });

    it('should throw an error when DynamoDB operation fails', async () => {
      ddbMock.on(PutCommand).rejects(new Error('DynamoDB error'));

      await expect(
        writeOrder({ order: mockOrder, update: false })
      ).rejects.toThrow();
    });
  });

  describe('getOrder', () => {
    it('should retrieve an order and its items', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: mockOrder.shippingAddress,
            billingAddress: mockOrder.billingAddress,
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99,
            sku: 'AC-AM24-BLK-42',
            variantId: 'SIZE-42-BLACK'
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const result = await getOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(ddbMock).toHaveReceivedCommandWith(QueryCommand, {
        TableName: 'test-orders-table',
        KeyConditionExpression: 'p = :p AND begins_with(s, :s)',
        ExpressionAttributeValues: {
          ':p': 'ORDERS#CUST123',
          ':s': 'ORD-abc123'
        }
      });

      expect(result).toEqual(expect.objectContaining({
        orderId: 'ORD-abc123',
        customerId: 'CUST123',
        status: 'PENDING',
        items: [expect.objectContaining({
          productId: 'PROD789',
          productName: 'AnyCompany Run'
        })]
      }));
    });

    it('should throw an error when order is not found', async () => {
      ddbMock.on(QueryCommand).resolves({ Items: [] });

      await expect(
        getOrder({ customerId: 'CUST123', orderId: 'NON-EXISTENT' })
      ).rejects.toThrow('Order not found for orderId: NON-EXISTENT');
    });

    it('should throw an error when order record is missing', async () => {
      // Only return order items but not the main order record
      ddbMock.on(QueryCommand).resolves({
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99
          }
        ]
      });

      await expect(
        getOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' })
      ).rejects.toThrow('Order record not found for orderId: ORD-abc123');
    });

    it('should handle orders with multiple items', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: mockOrder.shippingAddress,
            billingAddress: mockOrder.billingAddress,
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const result = await getOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(result.items.length).toBe(2);
      expect(result.items[0].productId).toBe('PROD789');
      expect(result.items[1].productId).toBe('PROD456');
    });
  });

  describe('getDdbOrderItems', () => {
    it('should retrieve order items for a specific order', async () => {
      const mockItems = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          productName: 'AnyCompany Run',
          quantity: 1,
          price: 129.99
        }
      ];

      ddbMock.on(QueryCommand).resolves({ Items: mockItems });

      const result = await getDdbOrderItems({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(ddbMock).toHaveReceivedCommandWith(QueryCommand, {
        TableName: 'test-orders-table',
        KeyConditionExpression: 'p = :p AND begins_with(s, :s)',
        ExpressionAttributeValues: {
          ':p': 'ORDERS#CUST123',
          ':s': 'ORD-abc123#ITEMS#'
        }
      });

      expect(result).toEqual(mockItems);
    });

    it('should return an empty array when no items are found', async () => {
      ddbMock.on(QueryCommand).resolves({ Items: undefined });

      const result = await getDdbOrderItems({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(result).toEqual([]);
    });

    it('should handle multiple order items', async () => {
      const mockItems = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          productName: 'AnyCompany Run',
          quantity: 1,
          price: 129.99
        },
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD456',
          productName: 'Example Corp Running Shorts',
          quantity: 2,
          price: 34.99
        }
      ];

      ddbMock.on(QueryCommand).resolves({ Items: mockItems });

      const result = await getDdbOrderItems({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(result.length).toBe(2);
      expect(result[0].s).toBe('ORD-abc123#ITEMS#PROD789');
      expect(result[1].s).toBe('ORD-abc123#ITEMS#PROD456');
    });
  });

  describe('deleteOrder', () => {
    it('should delete an order and all its items', async () => {
      const mockItems = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          productName: 'AnyCompany Run'
        }
      ];

      ddbMock.on(QueryCommand).resolves({ Items: mockItems });
      ddbMock.on(DeleteCommand).resolves({});

      await deleteOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(ddbMock).toHaveReceivedCommandWith(DeleteCommand, {
        TableName: 'test-orders-table',
        Key: {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123'
        }
      });

      expect(ddbMock).toHaveReceivedCommandWith(DeleteCommand, {
        TableName: 'test-orders-table',
        Key: {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789'
        }
      });
    });

    it('should handle deletion of orders with no items', async () => {
      ddbMock.on(QueryCommand).resolves({ Items: [] });
      ddbMock.on(DeleteCommand).resolves({});

      await deleteOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(ddbMock).toHaveReceivedCommandTimes(DeleteCommand, 1);
      expect(ddbMock).toHaveReceivedCommandWith(DeleteCommand, {
        TableName: 'test-orders-table',
        Key: {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123'
        }
      });
    });

    it('should handle deletion of orders with multiple items', async () => {
      const mockItems = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          productName: 'AnyCompany Run'
        },
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD456',
          productName: 'Example Corp Running Shorts'
        }
      ];

      ddbMock.on(QueryCommand).resolves({ Items: mockItems });
      ddbMock.on(DeleteCommand).resolves({});

      await deleteOrder({ customerId: 'CUST123', orderId: 'ORD-abc123' });

      expect(ddbMock).toHaveReceivedCommandTimes(DeleteCommand, 3);
    });
  });

  describe('updateOrder', () => {
    it('should update an existing order with new values', async () => {
      // Mock getOrder response
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: mockOrder.shippingAddress,
            billingAddress: mockOrder.billingAddress,
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);
      ddbMock.on(PutCommand).resolves({});

      const orderUpdate: OrderUpdate = {
        shippingMethod: 'NEXT_DAY',
        customerNotes: 'Updated delivery instructions'
      };

      const result = await updateOrder({
        orderUpdate,
        orderId: 'ORD-abc123',
        customerId: 'CUST123'
      });

      expect(result).toEqual(expect.objectContaining({
        shippingMethod: 'NEXT_DAY',
        customerNotes: 'Updated delivery instructions'
      }));

      expect(ddbMock).toHaveReceivedCommandWith(PutCommand, {
        TableName: 'test-orders-table',
        Item: expect.objectContaining({
          shippingMethod: 'NEXT_DAY',
          customerNotes: 'Updated delivery instructions'
        })
      });
    });

    it('should throw an error when the order to update does not exist', async () => {
      ddbMock.on(QueryCommand).resolves({ Items: [] });

      const orderUpdate: OrderUpdate = {
        shippingMethod: 'NEXT_DAY'
      };

      await expect(
        updateOrder({
          orderUpdate,
          orderId: 'NON-EXISTENT',
          customerId: 'CUST123'
        })
      ).rejects.toThrow('Order not found for orderId: NON-EXISTENT');
    });

    it('should preserve existing order fields when updating', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: mockOrder.shippingAddress,
            billingAddress: mockOrder.billingAddress,
            giftWrapping: true,
            couponCode: 'SUMMER25',
            discountAmount: 10.00
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);
      ddbMock.on(PutCommand).resolves({});

      const orderUpdate: OrderUpdate = {
        shippingMethod: 'NEXT_DAY'
      };

      const result = await updateOrder({
        orderUpdate,
        orderId: 'ORD-abc123',
        customerId: 'CUST123'
      });

      expect(result).toEqual(expect.objectContaining({
        shippingMethod: 'NEXT_DAY',
        giftWrapping: true,
        couponCode: 'SUMMER25',
        discountAmount: 10.00
      }));
    });
  });
});