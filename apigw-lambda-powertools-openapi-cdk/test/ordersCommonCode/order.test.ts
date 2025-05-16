import {
  convertOrderToDdb,
  convertDdbToOrderItem,
  convertDdbToOrder,
  Order,
  DdbOrder,
  DdbOrderItem,
  OrderItem
} from '../../lib/ordersCommonCode/order';

describe('Order Conversion Functions', () => {
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
      },
      {
        productId: 'PROD456',
        productName: 'Example Corp Running Shorts',
        quantity: 2,
        price: 34.99,
        sku: 'EC-RS-BLU-M',
        variantId: 'SIZE-M-BLUE'
      }
    ],
    shippingAddress: {
      street: '123 Main Street',
      city: 'Anytown',
      state: 'WA',
      postalCode: '31415',
      country: 'USA',
      apartment: 'Unit 45'
    },
    billingAddress: {
      street: '123 Main Street',
      city: 'Anytown',
      state: 'WA',
      postalCode: '31415',
      country: 'USA',
      apartment: 'Unit 45'
    },
    paymentMethod: 'CREDIT_CARD',
    shippingMethod: 'EXPRESS',
    customerNotes: 'Please leave the package at the front desk if no one is home',
    giftWrapping: true,
    couponCode: 'SUMMER25',
    status: 'PENDING',
    createdAt: '2023-06-15T10:30:00Z'
  };

  describe('convertOrderToDdb', () => {
    it('should convert an Order to DynamoDB format correctly', () => {
      const result = convertOrderToDdb({ order: mockOrder });
      
      // Check the main order record
      expect(result.ddbOrder.p).toBe('ORDERS#CUST123');
      expect(result.ddbOrder.s).toBe('ORD-abc123');
      expect(result.ddbOrder.customerId).toBe('CUST123');
      expect(result.ddbOrder.status).toBe('PENDING');
      expect(result.ddbOrder.createdAt).toBe('2023-06-15T10:30:00Z');
      expect(result.ddbOrder.giftWrapping).toBe(true);
      expect(result.ddbOrder.couponCode).toBe('SUMMER25');
      
      // Check order items
      expect(result.ddbOrderItems.length).toBe(2);
      expect(result.ddbOrderItems[0].p).toBe('ORDERS#CUST123');
      expect(result.ddbOrderItems[0].s).toBe('ORD-abc123#ITEMS#PROD789');
      expect(result.ddbOrderItems[0].productName).toBe('AnyCompany Run');
      expect(result.ddbOrderItems[0].price).toBe(129.99);
      
      expect(result.ddbOrderItems[1].p).toBe('ORDERS#CUST123');
      expect(result.ddbOrderItems[1].s).toBe('ORD-abc123#ITEMS#PROD456');
      expect(result.ddbOrderItems[1].quantity).toBe(2);
    });

    it('should remove undefined properties from the result', () => {
      const orderWithUndefined = {
        ...mockOrder,
        discountAmount: undefined,
        items: [
          {
            ...mockOrder.items[0],
            sku: undefined
          }
        ]
      };

      const result = convertOrderToDdb({ order: orderWithUndefined });
      
      expect(result.ddbOrder).not.toHaveProperty('discountAmount');
      expect(result.ddbOrderItems[0]).not.toHaveProperty('sku');
    });

    it('should handle orders with minimum required fields', () => {
      const minimalOrder: Order = {
        customerId: 'CUST123',
        orderId: 'ORD-abc123',
        items: [
          {
            productId: 'PROD789',
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
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z'
      };

      const result = convertOrderToDdb({ order: minimalOrder });
      
      expect(result.ddbOrder.p).toBe('ORDERS#CUST123');
      expect(result.ddbOrder.s).toBe('ORD-abc123');
      expect(result.ddbOrderItems[0].s).toBe('ORD-abc123#ITEMS#PROD789');
      expect(result.ddbOrderItems[0]).not.toHaveProperty('productName');
      expect(result.ddbOrderItems[0]).not.toHaveProperty('sku');
      expect(result.ddbOrderItems[0]).not.toHaveProperty('variantId');
    });
  });

  describe('convertDdbToOrderItem', () => {
    it('should convert a DdbOrderItem to OrderItem correctly', () => {
      const ddbOrderItem: DdbOrderItem = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123#ITEMS#PROD789',
        productName: 'AnyCompany Run',
        quantity: 1,
        price: 129.99,
        sku: 'AC-AM24-BLK-42',
        variantId: 'SIZE-42-BLACK'
      };

      const result = convertDdbToOrderItem({ ddbOrderItem });
      
      expect(result.productId).toBe('PROD789');
      expect(result.productName).toBe('AnyCompany Run');
      expect(result.quantity).toBe(1);
      expect(result.price).toBe(129.99);
      expect(result.sku).toBe('AC-AM24-BLK-42');
      expect(result.variantId).toBe('SIZE-42-BLACK');
    });

    it('should handle DdbOrderItem with minimum required fields', () => {
      const minimalDdbOrderItem: DdbOrderItem = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123#ITEMS#PROD789',
        quantity: 1,
        price: 129.99
      };

      const result = convertDdbToOrderItem({ ddbOrderItem: minimalDdbOrderItem });
      
      expect(result.productId).toBe('PROD789');
      expect(result.quantity).toBe(1);
      expect(result.price).toBe(129.99);
      expect(result.productName).toBeUndefined();
      expect(result.sku).toBeUndefined();
      expect(result.variantId).toBeUndefined();
    });

    it('should handle complex product IDs with special characters', () => {
      const ddbOrderItem: DdbOrderItem = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123#ITEMS#PROD-789#SPECIAL',
        quantity: 1,
        price: 129.99
      };

      const result = convertDdbToOrderItem({ ddbOrderItem });
      
      // The productId should be everything after the first #ITEMS# in the sort key
      expect(result.productId).toBe('PROD-789#SPECIAL');
    });
  });

  describe('convertDdbToOrder', () => {
    it('should convert DynamoDB records to an Order correctly', () => {
      const ddbOrder: DdbOrder = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123',
        customerId: 'CUST123',
        shippingAddress: mockOrder.shippingAddress,
        billingAddress: mockOrder.billingAddress,
        paymentMethod: 'CREDIT_CARD',
        shippingMethod: 'EXPRESS',
        customerNotes: 'Please leave the package at the front desk if no one is home',
        giftWrapping: true,
        couponCode: 'SUMMER25',
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z'
      };

      const ddbOrderItems: DdbOrderItem[] = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          productName: 'AnyCompany Run',
          quantity: 1,
          price: 129.99,
          sku: 'AC-AM24-BLK-42',
          variantId: 'SIZE-42-BLACK'
        },
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD456',
          productName: 'Example Corp Running Shorts',
          quantity: 2,
          price: 34.99,
          sku: 'EC-RS-BLU-M',
          variantId: 'SIZE-M-BLUE'
        }
      ];

      const result = convertDdbToOrder({ ddbItem: ddbOrder, ddbOrderItems });
      
      expect(result.orderId).toBe('ORD-abc123');
      expect(result.customerId).toBe('CUST123');
      expect(result.status).toBe('PENDING');
      expect(result.createdAt).toBe('2023-06-15T10:30:00Z');
      expect(result.items.length).toBe(2);
      expect(result.items[0].productId).toBe('PROD789');
      expect(result.items[1].productId).toBe('PROD456');
      expect(result.shippingAddress).toEqual(mockOrder.shippingAddress);
      expect(result.billingAddress).toEqual(mockOrder.billingAddress);
    });

    it('should handle conversion with no order items', () => {
      const ddbOrder: DdbOrder = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123',
        customerId: 'CUST123',
        shippingAddress: mockOrder.shippingAddress,
        billingAddress: mockOrder.billingAddress,
        giftWrapping: false,
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z'
      };

      const result = convertDdbToOrder({ ddbItem: ddbOrder, ddbOrderItems: [] });
      
      expect(result.orderId).toBe('ORD-abc123');
      expect(result.customerId).toBe('CUST123');
      expect(result.items).toEqual([]);
    });

    it('should handle conversion with minimum required fields', () => {
      const minimalDdbOrder: DdbOrder = {
        p: 'ORDERS#CUST123',
        s: 'ORD-abc123',
        customerId: 'CUST123',
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
        status: 'PENDING',
        createdAt: '2023-06-15T10:30:00Z'
      };

      const minimalDdbOrderItems: DdbOrderItem[] = [
        {
          p: 'ORDERS#CUST123',
          s: 'ORD-abc123#ITEMS#PROD789',
          quantity: 1,
          price: 129.99
        }
      ];

      const result = convertDdbToOrder({ 
        ddbItem: minimalDdbOrder, 
        ddbOrderItems: minimalDdbOrderItems 
      });
      
      expect(result.orderId).toBe('ORD-abc123');
      expect(result.customerId).toBe('CUST123');
      expect(result.items.length).toBe(1);
      expect(result.items[0].productId).toBe('PROD789');
      expect(result.items[0].quantity).toBe(1);
      expect(result.items[0].price).toBe(129.99);
      expect(result.paymentMethod).toBeUndefined();
      expect(result.shippingMethod).toBeUndefined();
      expect(result.customerNotes).toBeUndefined();
    });
  });
});