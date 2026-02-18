const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

exports.handler = withDurableExecution(async (event, context) => {
  console.log('=== Saga Orchestrator Started ===');
  console.log('Input:', JSON.stringify(event));

  const { tripId, userId, simulateFailure } = event;
  const completedSteps = [];

  try {
    // Step 1: Reserve Flight
    const flight = await context.step('reserveFlight', async () => {
      console.log('Reserving flight...');
      if (simulateFailure === 'flight') {
        throw new Error('Flight reservation failed - no availability');
      }
      const reservationId = `FL-${Date.now()}`;
      console.log(`Flight reserved: ${reservationId}`);
      return { reservationId, from: 'SFO', to: 'NYC', date: '2026-03-15', status: 'CONFIRMED' };
    });
    completedSteps.push({ service: 'flight', data: flight });

    // Step 2: Reserve Hotel
    const hotel = await context.step('reserveHotel', async () => {
      console.log('Reserving hotel...');
      if (simulateFailure === 'hotel') {
        throw new Error('Hotel reservation failed - no rooms available');
      }
      const reservationId = `HT-${Date.now()}`;
      console.log(`Hotel reserved: ${reservationId}`);
      return { reservationId, name: 'Grand Hotel NYC', checkIn: '2026-03-15', checkOut: '2026-03-18', status: 'CONFIRMED' };
    }, { retry: { maxAttempts: 1 } });
    completedSteps.push({ service: 'hotel', data: hotel });

    // Step 3: Reserve Car
    const car = await context.step('reserveCar', async () => {
      console.log('Reserving car...');
      if (simulateFailure === 'car') {
        throw new Error('Car reservation failed - no vehicles available');
      }
      const reservationId = `CR-${Date.now()}`;
      console.log(`Car reserved: ${reservationId}`);
      return { reservationId, type: 'SUV', pickupDate: '2026-03-15', returnDate: '2026-03-18', status: 'CONFIRMED' };
    }, { retry: { maxAttempts: 1 } });
    completedSteps.push({ service: 'car', data: car });

    console.log('=== All Reservations Completed Successfully ===');
    return {
      status: 'SUCCESS',
      message: 'Trip booked successfully',
      tripId,
      userId,
      reservations: { flight, hotel, car }
    };

  } catch (error) {
    console.error('=== Saga Failed - Initiating Compensating Transactions ===');
    console.error('Error:', error.message);

    // Execute compensating transactions in REVERSE order
    for (let i = completedSteps.length - 1; i >= 0; i--) {
      const step = completedSteps[i];
      await context.step(`cancel_${step.service}`, async () => {
        console.log(`Cancelling ${step.service}: ${step.data.reservationId}`);
        // Simulate cancellation logic
        return { reservationId: step.data.reservationId, status: 'CANCELLED' };
      });
    }

    console.log('=== All Compensating Transactions Completed ===');
    return {
      status: 'FAILED',
      message: 'Trip booking failed, all reservations rolled back',
      tripId,
      userId,
      error: error.message,
      compensatedServices: completedSteps.map(s => s.service)
    };
  }
});
