exports.handler = async (event) => {
    console.log('Received order:', event.orderId);
    
    // Simple enrichment
    return {
        statusCode: 200,
        orderId: event.orderId,
        enrichedData: {
            customerId: 'CUST-' + Math.floor(Math.random() * 10000),
            timestamp: new Date().toISOString()
        }
    };
};
