process.env.DYNAMODB_TABLE_NAME = 'test-orders-table';

import { DynamoDBDocumentClient, QueryCommand } from '@aws-sdk/lib-dynamodb';
import { mockClient } from 'aws-sdk-client-mock';
import 'aws-sdk-client-mock-jest';

import { searchOrders } from '../../../lib/lambda/ordersSearch/ddb';
import { OrderSearchCriteria } from '../../../lib/ordersCommonCode/order';

jest.mock('../../../lib/ordersCommonCode/order', () => {
  const originalModule = jest.requireActual('../../../lib/ordersCommonCode/order');
  return {
    ...originalModule,
    convertDdbToOrder: jest.fn().mockImplementation(({ ddbItem, ddbOrderItems }) => {
      return {
        orderId: ddbItem.s,
        customerId: ddbItem.customerId,
        status: ddbItem.status,
        createdAt: ddbItem.createdAt,
        items: ddbOrderItems.map((item: { s: string; quantity: any; price: any; productName: any; }) => ({
          productId: item.s.split('#ITEMS#')[1],
          quantity: item.quantity,
          price: item.price,
          productName: item.productName
        })),
        shippingAddress: ddbItem.shippingAddress,
        billingAddress: ddbItem.billingAddress,
        giftWrapping: ddbItem.giftWrapping
      };
    }),
  };
});

const ddbMock = mockClient(DynamoDBDocumentClient);

describe('Orders Search DynamoDB Operations', () => {
  beforeEach(() => {
    ddbMock.reset();
    jest.clearAllMocks();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  describe('searchOrders', () => {
    it('should return empty results when no orders are found', async () => {
      ddbMock.on(QueryCommand).resolves({ Items: [] });

      const searchCriteria: OrderSearchCriteria = {
        page: 1,
        limit: 10,
        sortBy: 'createdAt',
        sortOrder: 'desc'
      };

      const result = await searchOrders({
        orderSearchCriteria: searchCriteria,
        customerId: 'CUST123'
      });

      expect(result.items).toEqual([]);
      expect(result.pagination).toEqual({
        total: 0,
        pages: 0,
        currentPage: 1,
        limit: 10
      });

      expect(ddbMock).toHaveReceivedCommandWith(QueryCommand, {
        TableName: 'test-orders-table',
        KeyConditionExpression: 'p = :p',
        ExpressionAttributeValues: {
          ':p': 'ORDERS#CUST123'
        }
      });
    });

    it('should filter orders by status', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-def456',
            customerId: 'CUST123',
            status: 'SHIPPED',
            createdAt: '2023-06-14T09:15:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
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
            s: 'ORD-def456#ITEMS#PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const searchCriteria: OrderSearchCriteria = {
        statuses: ['PENDING'],
        page: 1,
        limit: 10,
        sortBy: 'createdAt',
        sortOrder: 'desc'
      };

      const result = await searchOrders({
        orderSearchCriteria: searchCriteria,
        customerId: 'CUST123'
      }) as { items: any[]; pagination: any };

      expect(result.items.length).toBe(1);
      expect(result.items[0].orderId).toBe('ORD-abc123');
      expect(result.items[0].status).toBe('PENDING');
      expect(result.pagination.total).toBe(1);
    });

    it('should filter orders by product ID', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-def456',
            customerId: 'CUST123',
            status: 'SHIPPED',
            createdAt: '2023-06-14T09:15:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
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
            s: 'ORD-def456#ITEMS#PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const searchCriteria: OrderSearchCriteria = {
        productIds: ['PROD456'],
        page: 1,
        limit: 10,
        sortBy: 'createdAt',
        sortOrder: 'desc'
      };

      const result = await searchOrders({
        orderSearchCriteria: searchCriteria,
        customerId: 'CUST123'
      }) as { items: any[]; pagination: any };

      expect(result.items.length).toBe(1);
      expect(result.items[0].orderId).toBe('ORD-def456');
      expect(result.pagination.total).toBe(1);
    });

    it('should sort orders by createdAt in descending order by default', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-def456',
            customerId: 'CUST123',
            status: 'SHIPPED',
            createdAt: '2023-06-14T09:15:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
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
            s: 'ORD-def456#ITEMS#PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const searchCriteria: OrderSearchCriteria = {
        page: 1,
        limit: 10,
        sortBy: 'createdAt',
        sortOrder: 'desc'
      };

      const result = await searchOrders({
        orderSearchCriteria: searchCriteria,
        customerId: 'CUST123'
      }) as { items: any[]; pagination: any };

      expect(result.items.length).toBe(2);
      expect(result.items[0].orderId).toBe('ORD-abc123');
      expect(result.items[1].orderId).toBe('ORD-def456');
      expect(new Date(result.items[0].createdAt).getTime()).toBeGreaterThan(
        new Date(result.items[1].createdAt).getTime()
      );
    });

    it('should handle pagination correctly', async () => {
      const mockQueryResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            giftWrapping: false
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-def456',
            customerId: 'CUST123',
            status: 'SHIPPED',
            createdAt: '2023-06-14T09:15:00Z',
            shippingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
            billingAddress: { street: '123 Main St', city: 'Anytown', state: 'WA', postalCode: '12345', country: 'USA' },
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
            s: 'ORD-def456#ITEMS#PROD456',
            productName: 'Example Corp Running Shorts',
            quantity: 2,
            price: 34.99
          }
        ]
      };

      ddbMock.on(QueryCommand).resolves(mockQueryResponse);

      const searchCriteria: OrderSearchCriteria = {
        page: 2,
        limit: 1,
        sortBy: 'createdAt',
        sortOrder: 'desc'
      };

      const result = await searchOrders({
        orderSearchCriteria: searchCriteria,
        customerId: 'CUST123'
      }) as { items: any[]; pagination: any };

      expect(result.items.length).toBe(1);
      expect(result.items[0].orderId).toBe('ORD-def456');
      expect(result.pagination).toEqual({
        total: 2,
        pages: 2,
        currentPage: 2,
        limit: 1
      });
    });
  });
});
