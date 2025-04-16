import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import type { Context } from 'aws-lambda';
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';

const logger = new Logger();
const metrics = new Metrics();
const tracer = new Tracer();


interface SearchCriteria {
  customerIds?: string[];
  statuses?: string[];
  productIds?: string[];
  page?: number;
  limit?: number;
  sortBy?: 'createdAt' | 'total' | 'status';
  sortOrder?: 'asc' | 'desc';
}

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
    total: 129.99,
    shippingAddress: {
      street: '123 Main Street',
      city: 'Seattle',
      state: 'WA',
      postalCode: '98101',
      country: 'USA'
    },
    shippingMethod: 'EXPRESS',
    trackingNumber: '1Z999AA1234567890'
  },
  // Add more sample orders here
];


class SearchOrderLambda implements LambdaInterface {
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

    try {
      // TODO validate object
      const criteria: SearchCriteria = JSON.parse(_event.body || '{}');
      let filteredOrders = [...sampleOrders];
  
      // Apply filters
      if (criteria.customerIds?.length) {
        filteredOrders = filteredOrders.filter(order => 
          criteria.customerIds!.includes(order.customerId)
        );
      }
  
      if (criteria.statuses?.length) {
        filteredOrders = filteredOrders.filter(order => 
          criteria.statuses!.includes(order.status)
        );
      }
  
      if (criteria.productIds?.length) {
        filteredOrders = filteredOrders.filter(order => 
          order.items.some(item => criteria.productIds!.includes(item.productId))
        );
      }
  
      // Sort results
      const sortBy = criteria.sortBy || 'createdAt';
      const sortOrder = criteria.sortOrder || 'desc';
  
      filteredOrders.sort((a, b) => {
        let comparison = 0;
        switch (sortBy) {
          case 'total':
            comparison = a.total - b.total;
            break;
          case 'status':
            comparison = a.status.localeCompare(b.status);
            break;
          case 'createdAt':
          default:
            comparison = new Date(a.createdAt).getTime() - new Date(b.createdAt).getTime();
            break;
        }
        return sortOrder === 'desc' ? -comparison : comparison;
      });
  
      // Handle pagination
      const page = Math.max(1, criteria.page || 1);
      const limit = Math.min(Math.max(1, criteria.limit || 20), 100);
      const startIndex = (page - 1) * limit;
      const endIndex = startIndex + limit;
      const paginatedOrders = filteredOrders.slice(startIndex, endIndex);
  
      const response = {
        items: paginatedOrders.map(order => ({
          orderId: order.orderId,
          customerId: order.customerId,
          status: order.status,
          createdAt: order.createdAt,
          total: order.total,
          items: order.items.map(item => ({
            productId: item.productId,
            productName: item.productName,
            quantity: item.quantity,
            price: item.price
          })),
          shippingMethod: order.shippingMethod,
          trackingNumber: order.trackingNumber
        })),
        pagination: {
          total: filteredOrders.length,
          pages: Math.ceil(filteredOrders.length / limit),
          currentPage: page,
          limit
        }
      };
  
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(response)
      };
    } catch (error) {
      console.error('Search Orders Error:', error);
      return {
        statusCode: 400,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: 'Invalid search criteria' })
      };
    }
  }
}

const searchClass = new SearchOrderLambda();
export const handler = searchClass.handler.bind(searchClass);