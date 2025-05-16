// Set up environment variables BEFORE importing any modules
process.env.DYNAMODB_TABLE_NAME = 'test-orders-table';
process.env.API_KEY_SECRET_ARN = 'arn:aws:secretsmanager:region:account:secret:api-key';

import { APIGatewayProxyEvent, Context } from 'aws-lambda';
import { mockClient } from 'aws-sdk-client-mock';
import { DynamoDBDocumentClient, QueryCommand, PutCommand, DeleteCommand } from '@aws-sdk/lib-dynamodb';
import { SecretsManagerClient, GetSecretValueCommand } from '@aws-sdk/client-secrets-manager';
import 'aws-sdk-client-mock-jest';



jest.mock('../../../lib/lambda/ordersCRUD/ddb', () => {
  const originalModule = jest.requireActual('../../../lib/lambda/ordersCRUD/ddb');
  return {
    ...originalModule,
    getOrder: jest.fn(),
    writeOrder: jest.fn(),
    updateOrder: jest.fn(),
    deleteOrder: jest.fn(),
  };
});

jest.mock('../../../lib/lambda/ordersCRUD/powertools', () => {
  return {
    logger: {
      injectLambdaContext: jest.fn().mockImplementation((config) => {
        return (target: any, propertyKey: string, descriptor: PropertyDescriptor) => {
          return descriptor;
        };
      }),
      logEventIfEnabled: jest.fn(),
      error: jest.fn(),
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
        addNewSubsegment: jest.fn().mockReturnValue({
          close: jest.fn(),
        }),
        addAnnotation: jest.fn(),
        addError: jest.fn(),
      }),
      captureAWSv3Client: jest.fn().mockImplementation((client) => client),
    },
    secretsProvider: {
      get: jest.fn().mockResolvedValue('mock-api-key'),
    },
  };
});

jest.mock('uuid', () => ({
  v4: jest.fn().mockReturnValue('mocked-uuid'),
}));

jest.mock('../../../lib/ordersCommonCode/customer', () => ({
  getCustomerIdFromAuthInfo: jest.fn().mockReturnValue('CUST123'),
}));

import { handler } from '../../../lib/lambda/ordersCRUD/index';
import * as ddbModule from '../../../lib/lambda/ordersCRUD/ddb';

const ddbMock = mockClient(DynamoDBDocumentClient);
const secretsManagerMock = mockClient(SecretsManagerClient);

describe('Lambda Handler', () => {
  beforeEach(() => {
    ddbMock.reset();
    secretsManagerMock.reset();
    jest.clearAllMocks();
    
    secretsManagerMock.on(GetSecretValueCommand).resolves({
      SecretString: JSON.stringify({ apiKey: 'test-api-key' }),
    });
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });
  

  const mockContext = {} as Context;

  describe('POST /order', () => {
    it('should create a new order successfully', async () => {
      const mockDate = new Date('2023-06-15T10:30:00Z');
      const originalDate = global.Date;
      global.Date = class extends Date {
        constructor() {
          super();
          return mockDate;
        }
        static now = originalDate.now;
        static parse = originalDate.parse;
        static UTC = originalDate.UTC;
      } as any;

      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'POST',
        path: '/order',
        body: JSON.stringify({
          items: [
            {
              productId: 'PROD789',
              productName: 'AnyCompany Run',
              quantity: 1,
              price: 129.99,
            },
          ],
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
        }),
      };

      (ddbModule.writeOrder as jest.Mock).mockResolvedValue(undefined);

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(201);
      expect(JSON.parse(response.body)).toMatchObject({
        orderId: 'ORD-mocked-uuid',
        customerId: 'CUST123',
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00.000Z',
      });

      expect(ddbModule.writeOrder).toHaveBeenCalledWith({
        order: expect.objectContaining({
          orderId: 'ORD-mocked-uuid',
          customerId: 'CUST123',
        }),
        update: false,
      });
    });
  });
  describe('GET /order/{orderId}', () => {
    it('should retrieve an order successfully', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'GET',
        path: '/order/ORD-abc123',
        pathParameters: {
          orderId: 'ORD-abc123',
        },
      };

      (ddbModule.getOrder as jest.Mock).mockResolvedValue({
        orderId: 'ORD-abc123',
        customerId: 'CUST123',
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z',
        items: [
          {
            productId: 'PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99,
          }
        ],
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
      });

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      expect(JSON.parse(response.body)).toEqual(expect.objectContaining({
        orderId: 'ORD-abc123',
        customerId: 'CUST123',
        status: 'PENDING',
      }));
    });

  });

  describe('PUT /order/{orderId}', () => {
    it('should update an order successfully', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'PUT',
        path: '/order/ORD-abc123',
        pathParameters: {
          orderId: 'ORD-abc123',
        },
        body: JSON.stringify({
          shippingMethod: 'NEXT_DAY',
          customerNotes: 'Updated delivery instructions',
        }),
      };

      (ddbModule.updateOrder as jest.Mock).mockResolvedValue({
        orderId: 'ORD-abc123',
        customerId: 'CUST123',
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z',
        shippingMethod: 'NEXT_DAY',
        customerNotes: 'Updated delivery instructions',
        items: [
          {
            productId: 'PROD789',
            productName: 'AnyCompany Run',
            quantity: 1,
            price: 129.99,
          }
        ],
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
      });

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(200);
      expect(JSON.parse(response.body)).toEqual(expect.objectContaining({
        orderId: 'ORD-abc123',
        shippingMethod: 'NEXT_DAY',
        customerNotes: 'Updated delivery instructions',
      }));
    });

  describe('DELETE /order/{orderId}', () => {
    it('should delete an order successfully', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'DELETE',
        path: '/order/ORD-abc123',
        pathParameters: {
          orderId: 'ORD-abc123',
        },
      };

      (ddbModule.deleteOrder as jest.Mock).mockResolvedValue(undefined);

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(204);
    });

  });

  describe('Invalid requests', () => {
    it('should return 400 for invalid request paths', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'GET',
        path: '/invalid-path',
      };

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(400);
      expect(JSON.parse(response.body)).toEqual({
        message: 'Invalid request',
      });
    });

    it('should return 400 for unsupported HTTP methods', async () => {
      const event: Partial<APIGatewayProxyEvent> = {
        httpMethod: 'PATCH',
        path: '/order/ORD-abc123',
        pathParameters: {
          orderId: 'ORD-abc123',
        },
      };

      const response = await handler(event as APIGatewayProxyEvent, mockContext);

      expect(response.statusCode).toBe(400);
      expect(JSON.parse(response.body)).toEqual({
        message: 'Invalid request',
      });
    });
  });
});
});
