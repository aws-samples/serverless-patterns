const request = require('supertest');
const fc = require('fast-check');
const app = require('./app');

describe('Products API Property Tests', () => {
  
  // **Feature: products-api, Property 1: Valid JSON Response Format**
  // **Validates: Requirements 1.1, 6.2**
  test('Property 1: Valid JSON Response Format - For any valid GET request to the products endpoint, the response should be valid JSON containing a "products" array', () => {
    return fc.assert(
      fc.asyncProperty(fc.constant('/products'), async (endpoint) => {
        const response = await request(app).get(endpoint);
        
        // Response should be valid JSON
        expect(response.type).toBe('application/json');
        
        // Response body should contain products array
        expect(response.body).toHaveProperty('products');
        expect(Array.isArray(response.body.products)).toBe(true);
        
        // Each product should have required fields
        response.body.products.forEach(product => {
          expect(product).toHaveProperty('id');
          expect(product).toHaveProperty('name');
          expect(product).toHaveProperty('description');
          expect(product).toHaveProperty('price');
          expect(product).toHaveProperty('category');
        });
      }),
      { numRuns: 100 }
    );
  });

  // **Feature: products-api, Property 2: Successful Request Status Code**
  // **Validates: Requirements 1.2**
  test('Property 2: Successful Request Status Code - For any valid GET request to the products endpoint, the response should have HTTP status code 200', () => {
    return fc.assert(
      fc.asyncProperty(fc.constant('/products'), async (endpoint) => {
        const response = await request(app).get(endpoint);
        
        // Response should have status 200
        expect(response.status).toBe(200);
      }),
      { numRuns: 100 }
    );
  });

  // **Feature: products-api, Property 3: Required Response Headers**
  // **Validates: Requirements 1.3**
  test('Property 3: Required Response Headers - For any valid GET request, the response should include appropriate HTTP headers including Content-Type: application/json', () => {
    return fc.assert(
      fc.asyncProperty(fc.constant('/products'), async (endpoint) => {
        const response = await request(app).get(endpoint);
        
        // Response should have Content-Type header set to application/json
        expect(response.headers['content-type']).toMatch(/application\/json/);
        
        // Response should have other standard headers
        expect(response.headers).toHaveProperty('content-length');
      }),
      { numRuns: 100 }
    );
  });

  // **Feature: products-api, Property 4: Consistent Response Structure**
  // **Validates: Requirements 1.5**
  test('Property 4: Consistent Response Structure - For any valid request to the products endpoint, the response should maintain the same JSON structure regardless of the number of products returned', () => {
    return fc.assert(
      fc.asyncProperty(fc.constant('/products'), async (endpoint) => {
        const response = await request(app).get(endpoint);
        
        // Response should always have the same top-level structure
        expect(response.body).toHaveProperty('products');
        expect(Array.isArray(response.body.products)).toBe(true);
        
        // Response should not have any other top-level properties
        const expectedKeys = ['products'];
        const actualKeys = Object.keys(response.body);
        expect(actualKeys).toEqual(expectedKeys);
        
        // Each product in the array should have consistent structure
        response.body.products.forEach(product => {
          const productKeys = Object.keys(product).sort();
          const expectedProductKeys = ['id', 'name', 'description', 'price', 'category'].sort();
          expect(productKeys).toEqual(expectedProductKeys);
        });
      }),
      { numRuns: 100 }
    );
  });

  // **Feature: products-api, Property 5: Appropriate Status Codes**
  // **Validates: Requirements 6.4**
  test('Property 5: Appropriate Status Codes - For any request scenario (valid, invalid, error), the API should return the appropriate HTTP status code corresponding to the request outcome', () => {
    return fc.assert(
      fc.asyncProperty(
        fc.oneof(
          fc.constant({ method: 'GET', path: '/products', expectedStatus: 200 }),
          fc.constant({ method: 'GET', path: '/health', expectedStatus: 200 }),
          fc.constant({ method: 'POST', path: '/products', expectedStatus: 405 }),
          fc.constant({ method: 'PUT', path: '/products', expectedStatus: 405 }),
          fc.constant({ method: 'DELETE', path: '/products', expectedStatus: 405 }),
          fc.constant({ method: 'GET', path: '/nonexistent', expectedStatus: 404 }),
          fc.constant({ method: 'POST', path: '/nonexistent', expectedStatus: 404 })
        ),
        async (scenario) => {
          let response;
          
          switch (scenario.method) {
            case 'GET':
              response = await request(app).get(scenario.path);
              break;
            case 'POST':
              response = await request(app).post(scenario.path);
              break;
            case 'PUT':
              response = await request(app).put(scenario.path);
              break;
            case 'DELETE':
              response = await request(app).delete(scenario.path);
              break;
          }
          
          // Response should have the expected status code
          expect(response.status).toBe(scenario.expectedStatus);
        }
      ),
      { numRuns: 100 }
    );
  });

});