/**
 * Webhook validator function that validates incoming webhook payloads
 * Called by the durable webhook processor function
 */
exports.handler = async (event, context) => {
    const { payload, executionToken } = event;
    
    console.log(`Validating webhook for execution: ${executionToken}`);
    
    try {
        // Basic validation rules - customize based on your webhook requirements
        const validationErrors = [];
        
        // Check if payload exists
        if (!payload || typeof payload !== 'object') {
            validationErrors.push('Payload is required and must be an object');
        } else {
            // Check required fields - customize these based on your webhook schema
            if (!payload.type) {
                validationErrors.push('Payload must include a "type" field');
            }
            
            // Validate webhook signature/auth if needed
            // if (!payload.signature) {
            //     validationErrors.push('Webhook signature is required');
            // }
            
            // Add custom validation logic here
            if (payload.type && !['order', 'payment', 'user', 'system'].includes(payload.type)) {
                validationErrors.push('Invalid webhook type. Must be one of: order, payment, user, system');
            }
            
            // Validate payload structure based on type
            if (payload.type === 'order' && !payload.orderId) {
                validationErrors.push('Order webhooks must include orderId');
            }
            
            if (payload.type === 'payment' && !payload.transactionId) {
                validationErrors.push('Payment webhooks must include transactionId');
            }
        }
        
        const isValid = validationErrors.length === 0;
        
        return {
            isValid: isValid,
            executionToken: executionToken,
            errors: validationErrors,
            validatedAt: new Date().toISOString(),
            payloadType: payload?.type || 'unknown'
        };
        
    } catch (error) {
        console.error(`Error validating webhook ${executionToken}:`, error.message);
        return {
            isValid: false,
            executionToken: executionToken,
            errors: [`Validation error: ${error.message}`],
            error: error.message
        };
    }
};
