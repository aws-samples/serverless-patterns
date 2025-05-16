import { APIGatewayProxyEvent } from 'aws-lambda';
import { getCustomerIdFromAuthInfo } from '../../lib/ordersCommonCode/customer';

describe('Customer Functions', () => {
  describe('getCustomerIdFromAuthInfo', () => {
    it('should extract customerId from JWT claims in requestContext', () => {
      const event = {
        requestContext: {
          authorizer: {
            jwt: {
              claims: {
                'cognito:username': 'CUST123',
              },
            },
          },
        },
      } as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('CUST123');
    });

    it('should extract customerId from Lambda authorizer claims', () => {
      const event = {
        requestContext: {
          authorizer: {
            claims: {
              'cognito:username': 'CUST456',
            },
          },
        },
      } as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('CUST456');
    });

    it('should use sub claim if cognito:username is not available', () => {
      const event = {
        requestContext: {
          authorizer: {
            jwt: {
              claims: {
                'sub': 'CUST789',
              },
            },
          },
        },
      } as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('CUST789');
    });

    it('should return a default test customer ID if no auth info is available', () => {
      const event = {
        requestContext: {},
      } as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('TEST-CUSTOMER');
    });

    it('should handle missing requestContext gracefully', () => {
      const event = {} as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('TEST-CUSTOMER');
    });

    it('should handle null authorizer gracefully', () => {
      const event = {
        requestContext: {
          authorizer: null,
        },
      } as unknown as APIGatewayProxyEvent;

      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('TEST-CUSTOMER');
    });

    it('should handle complex nested auth structures', () => {
      const event = {
        requestContext: {
          authorizer: {
            jwt: {
              claims: {
                'custom:customer_id': 'CUSTOM-CUST-123',
                'cognito:username': 'user@example.com',
                'sub': 'abc123',
              },
            },
          },
        },
      } as unknown as APIGatewayProxyEvent;

      // Should prioritize cognito:username over sub
      const result = getCustomerIdFromAuthInfo({ event });
      expect(result).toBe('user@example.com');
    });
  });
});