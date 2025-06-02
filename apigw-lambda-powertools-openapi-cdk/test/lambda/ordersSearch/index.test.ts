process.env.DYNAMODB_TABLE_NAME = 'test-orders-table';

import { APIGatewayProxyEvent, Context } from 'aws-lambda';
import { mockClient } from 'aws-sdk-client-mock';
import { DynamoDBDocumentClient, QueryCommand } from '@aws-sdk/lib-dynamodb';
import 'aws-sdk-client-mock-jest';
import { handler } from '../../../lib/lambda/ordersSearch/index';

jest.mock('../../../lib/lambda/ordersSearch/powertools', () => {
  return {
    logger: {
      injectLambdaContext: jest.fn().mockImplementation((config) => {
        return (target: any, propertyKey: string, descriptor: PropertyDescriptor) => {
          return descriptor;
        };
      }),
      logEventIfEnabled: jest.fn(),
      appendKeys: jest.fn(),
    },
    metrics: {
      logMetrics: jest.fn().mockImplementation(() => {
        return (target: any, propertyKey: string, descriptor: PropertyDescriptor) => {
          return descriptor;
        };
      }),
      addMetric: jest.fn(),
    },
    tracer: {
      captureLambdaHandler: jest.fn().mockImplementation(() => {
        return (target: any, propertyKey: string, descriptor: PropertyDescriptor) => {
          return descriptor;
        };
      }),
      getSegment: jest.fn().mockReturnValue({
        addAnnotation: jest.fn(),
        addError: jest.fn(),
      }),
      captureAWSv3Client: jest.fn().mockImplementation((client) => client),
    },
  };
});

jest.mock('../../../lib/ordersCommonCode/customer', () => ({
  getCustomerIdFromAuthInfo: jest.fn().mockReturnValue('CUST123'),
}));

const ddbMock = mockClient(DynamoDBDocumentClient);

describe('Orders Search Lambda Handler', () => {
  beforeEach(() => {
    ddbMock.reset();
    jest.clearAllMocks();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  const mockContext = {} as Context;

  describe('POST /orders/search', () => {
    it('should search orders successfully with default pagination', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'POST',
        path: '/orders/search',
        body: JSON.stringify({
          statuses: ['PENDING', 'CONFIRMED'],
          page: 1,
          limit: 10,
          sortBy: 'createdAt',
          sortOrder: 'desc'
        }),
      };

      const mockOrdersResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            billingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            giftWrapping: false,
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-def456',
            customerId: 'CUST123',
            status: 'CONFIRMED',
            createdAt: '2023-06-14T09:15:00Z',
            shippingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            billingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            giftWrapping: false,
          }
        ],
        Count: 2,
      };

      ddbMock.on(QueryCommand)
        .resolvesOnce(mockOrdersResponse);

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      const responseBody = JSON.parse(response.body);
      
      expect(responseBody.pagination).toEqual({
        total: 2,
        pages: 1,
        currentPage: 1,
        limit: 10
      });
      
      expect(responseBody.items.length).toBe(2);
      expect(responseBody.items[0].orderId).toBe('ORD-abc123');
      expect(responseBody.items[0].status).toBe('PENDING');
      expect(responseBody.items[1].orderId).toBe('ORD-def456');
      expect(responseBody.items[1].status).toBe('CONFIRMED');
      
      expect(ddbMock).toHaveReceivedCommandWith(QueryCommand, {
        TableName: 'test-orders-table',
        KeyConditionExpression: 'p = :p',
        ExpressionAttributeValues: {
          ':p': 'ORDERS#CUST123',
        },
      });
    });

    it('should handle search with product filtering', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'POST',
        path: '/orders/search',
        body: JSON.stringify({
          productIds: ['PROD789'],
          page: 1,
          limit: 20,
          sortBy: 'createdAt',
          sortOrder: 'desc'
        }),
      };

      const mockOrderResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
            shippingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            billingAddress: {
              street: '123 Main Street',
              city: 'Anytown',
              state: 'WA',
              postalCode: '31415',
              country: 'USA',
            },
            giftWrapping: false,
          },
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123#ITEMS#PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99,
          }
        ]
      };

      ddbMock.on(QueryCommand)
        .resolvesOnce(mockOrderResponse)

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      const responseBody = JSON.parse(response.body);
      
      expect(responseBody.items.length).toBe(1);
      expect(responseBody.items[0].orderId).toBe('ORD-abc123');
      expect(responseBody.items[0].items[0].productId).toBe('PROD789');
    });

    it('should handle invalid sort parameters', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'POST',
        path: '/orders/search',
        body: JSON.stringify({
          page: 1,
          limit: 10,
          sortBy: 'invalidField',
          sortOrder: 'invalid'
        }),
      };

      const mockOrdersResponse = {
        Items: [
          {
            p: 'ORDERS#CUST123',
            s: 'ORD-abc123',
            customerId: 'CUST123',
            status: 'PENDING',
            createdAt: '2023-06-15T10:30:00Z',
          }
        ],
        Count: 1,
      };

      ddbMock.on(QueryCommand)
        .resolvesOnce(mockOrdersResponse);

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      const responseBody = JSON.parse(response.body);
      expect(responseBody.items.length).toBe(1);
    });

    it('should handle empty search results', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'POST',
        path: '/orders/search',
        body: JSON.stringify({
          statuses: ['CANCELLED'],
          page: 1,
          limit: 10,
        }),
      };

      ddbMock.on(QueryCommand).resolves({
        Items: [],
        Count: 0,
      });

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      const responseBody = JSON.parse(response.body);
      
      expect(responseBody.items).toEqual([]);
      
      expect(responseBody.pagination).toEqual({
        total: 0,
        pages: 0,
        currentPage: 1,
        limit: 10
      });
    });
  });
});