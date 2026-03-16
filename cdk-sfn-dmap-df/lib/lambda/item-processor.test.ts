import { LocalDurableTestRunner, OperationStatus, OperationType } from '@aws/durable-execution-sdk-js-testing';
import { handler } from './item-processor';

describe('Product Catalog Item Processor', () => {
    beforeAll(() => LocalDurableTestRunner.setupTestEnvironment({ skipTime: true }));
    afterAll(() => LocalDurableTestRunner.teardownTestEnvironment());

    it('should validate, wait, and update a product item', async () => {
        const runner = new LocalDurableTestRunner({
            handlerFunction: handler,
        });

        const execution = await runner.run({
            payload: {
                itemId: 'PROD-001',
                productName: 'Wireless Mouse',
                category: 'electronics',
                price: 29.99,
            },
        });

        // Verify invocations (initial + replay after wait)
        expect(execution.getInvocations().length).toBe(2);

        // Verify final result
        const result = execution.getResult() as any;
        expect(result.itemId).toBe('PROD-001');
        expect(result.productName).toBe('Wireless Mouse');
        expect(result.category).toBe('electronics');
        expect(result.price).toBe(29.99);
        expect(result.priceTier).toBe('standard');
        expect(result.status).toBe('completed');
        expect(result.validatedAt).toBeDefined();
        expect(result.processedAt).toBeDefined();

        // Verify 3 operations were executed
        expect(execution.getOperations()).toHaveLength(3);

        // Verify validate step
        const validateStep = runner.getOperation('validate-item');
        expect(validateStep.getType()).toBe(OperationType.STEP);
        expect(validateStep.getStatus()).toBe(OperationStatus.SUCCEEDED);

        // Verify wait operation
        const waitOp = runner.getOperation('rate-limit-delay');
        expect(waitOp.getType()).toBe(OperationType.WAIT);
        expect(waitOp.getStatus()).toBe(OperationStatus.SUCCEEDED);

        // Verify update step
        const updateStep = runner.getOperation('update-catalog');
        expect(updateStep.getType()).toBe(OperationType.STEP);
        expect(updateStep.getStatus()).toBe(OperationStatus.SUCCEEDED);
    });

    it('should assign budget tier for low-price items', async () => {
        const runner = new LocalDurableTestRunner({
            handlerFunction: handler,
        });

        const execution = await runner.run({
            payload: {
                itemId: 'PROD-050',
                productName: 'Cotton Socks',
                category: 'clothing',
                price: 9.99,
            },
        });

        const result = execution.getResult() as any;
        expect(result.priceTier).toBe('budget');
        expect(result.status).toBe('completed');
    });

    it('should assign premium tier for high-price items', async () => {
        const runner = new LocalDurableTestRunner({
            handlerFunction: handler,
        });

        const execution = await runner.run({
            payload: {
                itemId: 'PROD-025',
                productName: '4K Monitor',
                category: 'electronics',
                price: 499.99,
            },
        });

        const result = execution.getResult() as any;
        expect(result.priceTier).toBe('premium');
        expect(result.status).toBe('completed');
    });
});
