exports.handler = async (event) => {
  console.log('Event received:', JSON.stringify(event, null, 2));

  try {
    const action = event.action;
    const value = event.value;

    // Simple business logic simulation
    switch (action) {
      case 'process':
        if (!value || value < 0) {
          throw new Error('Invalid value: must be a positive number');
        }
        return {
          statusCode: 200,
          body: JSON.stringify({
            message: 'Processing successful',
            result: value * 2,
            action: action
          })
        };

      case 'validate':
        if (typeof value !== 'string' || value.length === 0) {
          throw new Error('Invalid value: must be a non-empty string');
        }
        return {
          statusCode: 200,
          body: JSON.stringify({
            message: 'Validation successful',
            result: value.toUpperCase(),
            action: action
          })
        };

      case 'calculate':
        if (!Array.isArray(value) || value.length === 0) {
          throw new Error('Invalid value: must be a non-empty array');
        }
        const sum = value.reduce((acc, curr) => acc + curr, 0);
        return {
          statusCode: 200,
          body: JSON.stringify({
            message: 'Calculation successful',
            result: sum,
            action: action
          })
        };

      default:
        throw new Error(`Unknown action: ${action}`);
    }
  } catch (error) {
    console.error('Error processing request:', error);
    // Lambda will automatically send this to the failed-event destination
    throw error;
  }
};
