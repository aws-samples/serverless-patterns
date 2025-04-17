import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { GetSecretValueCommand, SecretsManager } from '@aws-sdk/client-secrets-manager';
import type { Context } from 'aws-lambda';
import { v4 as uuidv4 } from 'uuid';

const orderCache = new Map<string, any>();

// Sample data
const sampleOrders = [
  {
    orderId: 'ORD-2024-001',
    customerId: 'CUST123',
    items: [
      {
        productId: 'PROD789',
        productName: 'Nike Air Max 2024',
        quantity: 1,
        price: 129.99,
        sku: 'NK-AM24-BLK-42',
        variantId: 'SIZE-42-BLACK'
      }
    ],
    status: 'DELIVERED',
    createdAt: '2024-01-15T10:00:00Z',
    updatedAt: '2024-01-15T10:00:00Z',
    shippingAddress: {
      street: '123 Main Street',
      city: 'Seattle',
      state: 'WA',
      postalCode: '98101',
      country: 'USA'
    },
    trackingNumber: '1Z999AA1234567890'
  },
  {
    orderId: 'ORD-2024-002',
    customerId: 'CUST456',
    items: [
      {
        productId: 'PROD456',
        productName: 'Adidas Running Shorts',
        quantity: 2,
        price: 34.99,
        sku: 'AD-RS-BLU-M',
        variantId: 'SIZE-M-BLUE'
      }
    ],
    status: 'PROCESSING',
    createdAt: '2024-01-16T15:30:00Z',
    updatedAt: '2024-01-16T15:30:00Z',
    shippingAddress: {
      street: '456 Pine Street',
      city: 'Portland',
      state: 'OR',
      postalCode: '97201',
      country: 'USA'
    }
  }
];

// Initialize cache with sample data
sampleOrders.forEach(order => orderCache.set(order.orderId, order));


const logger = new Logger();
const metrics = new Metrics();
const tracer = new Tracer();
const secretsManager = new SecretsManager();
let apiKey: string | undefined;

interface ErrorResponse {
  message: string;
}

class HandleOrderLambda implements LambdaInterface {
  @tracer.captureLambdaHandler()
  @metrics.logMetrics()
  @logger.injectLambdaContext()
  public async handler(_event: APIGatewayProxyEvent, _context: Context): Promise<APIGatewayProxyResult> {
    logger.appendKeys({
      stage: process.env.STAGE,
    });
    logger.info('Processing event', { _event });
    metrics.addMetric('ProcessedEvents', MetricUnit.Count, 1);
    tracer.getSegment();
    const apiKey = await getApiKey();
    // TODO test both branches: exists or not
    if (apiKey) {
      logger.debug("API key found")

    }
    // use api key to call external service
    try {
      switch (_event.httpMethod) {
        case 'POST':
          if (_event.path === '/order') {
            return await createOrder(_event);
          }
          break;
        case 'GET':
          if (_event.path.match(/^\/order\/[^/]+$/)) {
            return await getOrder(_event);
          }
          break;
        case 'PUT':
          if (_event.path.match(/^\/order\/[^/]+$/)) {
            return await updateOrder(_event);
          }
          break;
        case 'DELETE':
          if (_event.path.match(/^\/order\/[^/]+$/)) {
            return await deleteOrder(_event);
          }
          break;
      }  
      return errorResponse(404, { message: 'Not Found' });
    } catch (error) {
      console.error('Error:', error);
      return errorResponse(500, { message: 'Internal Server Error' });
    }
  }
}


async function getApiKey(): Promise<string | undefined> {

  if (apiKey) {
    return apiKey;
  }
  const secretArn = process.env.API_KEY_SECRET_ARN;
  if (!secretArn) {
    throw new Error('API_KEY_SECRET_ARN environment variable is not set');
  }

  const command = new GetSecretValueCommand({
    SecretId: secretArn,
  });

  const response = await secretsManager.send(command);

  if (!response.SecretString) {
    throw new Error('Secret string is empty');
  }

  const secretData = response.SecretString;
  if (!secretData){
    throw new Error('API KEY does not exist');
  }
  apiKey = secretData;
  return apiKey

}

async function createOrder(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  try {
    // TODO add validation
    const order = JSON.parse(event.body || '{}');
    const timestamp = new Date().toISOString();
    
    const newOrder = {
      ...order,
      orderId: `ORD-${uuidv4()}`,
      status: 'PENDING',
      createdAt: timestamp,
      updatedAt: timestamp
    };

    orderCache.set(newOrder.orderId, newOrder);

    const response = {
      orderId: newOrder.orderId,
      status: newOrder.status,
      createdAt: newOrder.createdAt,
    };

    return {
      statusCode: 201,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(response)
    };
  } catch (error) {
    console.error('Create Order Error:', error);
    return errorResponse(400, { message: 'Invalid request body' });
  }
}

async function getOrder(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
    const orderId = event.pathParameters?.orderId;
    const order = orderCache.get(orderId || '');

    if (!order) {
      return errorResponse(404, { message: 'Order not found' });
    }

    const response = {
      orderId: order.orderId,
      status: order.status,
      createdAt: order.createdAt,
      trackingNumber: order.trackingNumber
    };

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(response)
    };
}

async function updateOrder(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  const orderId = event.pathParameters?.orderId;
  const updates = JSON.parse(event.body || '{}');

  const existingOrder = orderCache.get(orderId || '');
  if (!existingOrder) {
    return errorResponse(404, { message: 'Order not found' });
  }

  const updatedOrder = {
    ...existingOrder,
    ...updates,
    updatedAt: new Date().toISOString()
  };

  orderCache.set(orderId!, updatedOrder);

  const response = {
    orderId: updatedOrder.orderId,
    status: updatedOrder.status,
    createdAt: updatedOrder.createdAt,
    updatedAt: updatedOrder.updatedAt,
    trackingNumber: updatedOrder.trackingNumber
  };

  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(response)
  };
}

async function deleteOrder(event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> {
  const orderId = event.pathParameters?.orderId;

  if (!orderCache.has(orderId || '')) {
    return errorResponse(404, { message: 'Order not found' });
  }

  orderCache.delete(orderId!);

  return {
    statusCode: 204,
    body: ''
  };
}

function errorResponse(statusCode: number, error: ErrorResponse): APIGatewayProxyResult {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(error)
  };
}

const handlerClass = new HandleOrderLambda();
export const handler = handlerClass.handler.bind(handlerClass);