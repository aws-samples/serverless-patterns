exports.handler = async (event) => {
    console.log('Received order:', event.orderId);
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    await sleep(2000); // Sleep for 2 seconds
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
