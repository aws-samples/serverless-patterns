from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution
import random
import datetime
import boto3
import logging
import json
import os
import uuid

dynamodb = boto3.client('dynamodb')

# Get function names from environment variables
RESERVE_FLIGHT_FUNCTION = os.environ.get('RESERVE_FLIGHT_FUNCTION', 'saga-reserve-flight')
CANCEL_FLIGHT_FUNCTION = os.environ.get('CANCEL_FLIGHT_FUNCTION', 'saga-cancel-flight')
RESERVE_HOTEL_FUNCTION = os.environ.get('RESERVE_HOTEL_FUNCTION', 'saga-reserve-hotel')
CANCEL_HOTEL_FUNCTION = os.environ.get('CANCEL_HOTEL_FUNCTION', 'saga-cancel-hotel')
RESERVE_CAR_FUNCTION = os.environ.get('RESERVE_CAR_FUNCTION', 'saga-reserve-car')
CANCEL_CAR_FUNCTION = os.environ.get('CANCEL_CAR_FUNCTION', 'saga-cancel-car')


@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    """
    Saga orchestrator that coordinates distributed transactions across flight, hotel, and car services.
    Implements compensating transactions (cancellations) if any step fails.
    Uses direct context.invoke() calls instead of durable steps.
    """
    print(f"Saga workflow started at: {datetime.datetime.now()}")
    context.logger.info(f"Received event: {json.dumps(event)}")
    
    # Generate unique IDs for this saga transaction
    transaction_id = str(uuid.uuid4())
    booking_id = None
    reservation_id = None
    rental_id = None
    
    try:
        # Step 1: Reserve the flight
        context.logger.info("Step 1: Reserving flight...")
        flight_data = {
            "bookingId": str(uuid.uuid4()),
            "passengerName": event.get("passengerName", "John Doe"),
            "flightNumber": event.get("flightNumber", f"FL{uuid.uuid4().hex[:6].upper()}"),
            "departure": event.get("departure", "JFK"),
            "destination": event.get("destination", "LAX"),
            "price": event.get("flightPrice", 299.99),
            "failBookFlight": event.get("failBookFlight", False)  # Pass failure flag
        }
        
        flight_result = context.invoke(
            function_name=RESERVE_FLIGHT_FUNCTION,
            payload=flight_data,
            name="reserve_flight_invocation"
        )

        if flight_result is None:
            context.logger.error("Flight reservation returned None - invocation may have failed")
            raise Exception("Flight reservation returned None - invocation may have failed")
        
        # If it's a string, parse it first
        if isinstance(flight_result, str):
            flight_result = json.loads(flight_result)
        
        # Parse the Lambda response format
        if isinstance(flight_result, dict) and 'body' in flight_result:
            flight_body = json.loads(flight_result['body']) if isinstance(flight_result['body'], str) else flight_result['body']
            if flight_result.get('statusCode') != 200:
                raise Exception(f"Flight reservation failed: {flight_body.get('message')}")
            booking_id = flight_body.get('bookingId')
        elif isinstance(flight_result, dict):
            booking_id = flight_result.get('bookingId')
        else:
            raise Exception(f"Unexpected flight result format: {type(flight_result)}")
            
        context.logger.info(f"Flight reserved successfully: {booking_id}")
        
        # Step 2: Reserve hotel
        context.logger.info("Step 2: Reserving hotel...")
        hotel_data = {
            "reservationId": str(uuid.uuid4()),
            "guestName": event.get("guestName", "John Doe"),
            "hotelName": event.get("hotelName", "Grand Hotel"),
            "roomType": event.get("roomType", "Deluxe Suite"),
            "checkIn": event.get("checkIn", datetime.datetime.utcnow().date().isoformat()),
            "checkOut": event.get("checkOut", datetime.datetime.utcnow().date().isoformat()),
            "price": event.get("hotelPrice", 199.99),
            "failBookHotel": event.get("failBookHotel", False)  # Pass failure flag
        }
        
        hotel_result = context.invoke(
            function_name=RESERVE_HOTEL_FUNCTION,
            payload=hotel_data,
            name="reserve_hotel_invocation"
        )
        
        context.logger.info(f"Hotel result after invoke: {hotel_result}")
        
        if hotel_result is None:
            raise Exception("Hotel reservation returned None - invocation may have failed")
        
        # If it's a string, parse it first
        if isinstance(hotel_result, str):
            hotel_result = json.loads(hotel_result)
        
        # parse the Lambda response format
        if isinstance(hotel_result, dict) and 'body' in hotel_result:
            hotel_body = json.loads(hotel_result['body']) if isinstance(hotel_result['body'], str) else hotel_result['body']
            if hotel_result.get('statusCode') != 200:
                raise Exception(f"Hotel reservation failed: {hotel_body.get('message')}")
            reservation_id = hotel_body.get('reservationId')
        elif isinstance(hotel_result, dict):
            reservation_id = hotel_result.get('reservationId')
        else:
            raise Exception(f"Unexpected hotel result format: {type(hotel_result)}")
            
        context.logger.info(f"Hotel reserved successfully: {reservation_id}")
        
        # Step 3: Reserve car
        context.logger.info("Step 3: Reserving car...")
        car_data = {
            "rentalId": str(uuid.uuid4()),
            "driverName": event.get("driverName", "John Doe"),
            "carType": event.get("carType", "Sedan"),
            "pickupLocation": event.get("pickupLocation", "Airport"),
            "dropoffLocation": event.get("dropoffLocation", "Airport"),
            "pickupDate": event.get("pickupDate", datetime.datetime.utcnow().date().isoformat()),
            "dropoffDate": event.get("dropoffDate", datetime.datetime.utcnow().date().isoformat()),
            "price": event.get("carPrice", 89.99),
            "failBookCar": event.get("failBookCar", False)  # Pass failure flag
        }
        
        car_result = context.invoke(
            function_name=RESERVE_CAR_FUNCTION,
            payload=car_data,
            name="reserve_car_invocation"
        )
        
        context.logger.info(f"Car result after invoke: {car_result}")
        
        if car_result is None:
            raise Exception("Car reservation returned None - invocation may have failed")
        
        # If it's a string, parse it first
        if isinstance(car_result, str):
            car_result = json.loads(car_result)
        
        # Parse the Lambda response format
        if isinstance(car_result, dict) and 'body' in car_result:
            car_body = json.loads(car_result['body']) if isinstance(car_result['body'], str) else car_result['body']
            if car_result.get('statusCode') != 200:
                raise Exception(f"Car reservation failed: {car_body.get('message')}")
            rental_id = car_body.get('rentalId')
        elif isinstance(car_result, dict):
            rental_id = car_result.get('rentalId')
        else:
            raise Exception(f"Unexpected car result format: {type(car_result)}")
            
        context.logger.info(f"Car reserved successfully: {rental_id}")
        
        # All reservations successful
        context.logger.info("All reservations completed successfully!")
        
        return {
            "success": True,
            "transactionId": transaction_id,
            "message": "All travel arrangements completed successfully",
            "bookings": {
                "flight": booking_id,
                "hotel": reservation_id,
                "car": rental_id
            }
        }
        
    except Exception as e:
        # Saga compensation: rollback all successful reservations
        context.logger.error(f"Error in saga workflow: {str(e)}")
        context.logger.info("Starting compensation (rollback) process...")
        
        compensation_results = []
        
        # Cancel car if it was reserved
        if rental_id:
            try:
                context.logger.info(f"Compensating: Cancelling car rental {rental_id}")
                # Direct invoke call for cancellation
                cancel_car_result = context.invoke(
                    function_name=CANCEL_CAR_FUNCTION,
                    payload={"rentalId": rental_id},
                    name="cancel_car_invocation"
                )
                compensation_results.append({"car": "cancelled", "rentalId": rental_id})
            except Exception as cancel_error:
                context.logger.error(f"Failed to cancel car: {str(cancel_error)}")
                compensation_results.append({"car": "cancellation_failed", "error": str(cancel_error)})
        
        # Cancel hotel if it was reserved
        if reservation_id:
            try:
                context.logger.info(f"Compensating: Cancelling hotel reservation {reservation_id}")
                # Direct invoke call for cancellation
                cancel_hotel_result = context.invoke(
                    function_name=CANCEL_HOTEL_FUNCTION,
                    payload={"reservationId": reservation_id},
                    name="cancel_hotel_invocation"
                )
                compensation_results.append({"hotel": "cancelled", "reservationId": reservation_id})
            except Exception as cancel_error:
                context.logger.error(f"Failed to cancel hotel: {str(cancel_error)}")
                compensation_results.append({"hotel": "cancellation_failed", "error": str(cancel_error)})
        
        # Cancel flight if it was reserved
        if booking_id:
            try:
                context.logger.info(f"Compensating: Cancelling flight booking {booking_id}")
                # Direct invoke call for cancellation
                cancel_flight_result = context.invoke(
                    function_name=CANCEL_FLIGHT_FUNCTION,
                    payload={"bookingId": booking_id},
                    name="cancel_flight_invocation"
                )
                compensation_results.append({"flight": "cancelled", "bookingId": booking_id})
            except Exception as cancel_error:
                context.logger.error(f"Failed to cancel flight: {str(cancel_error)}")
                compensation_results.append({"flight": "cancellation_failed", "error": str(cancel_error)})
        
        context.logger.info("Compensation process completed")
        
        # Raise an exception with compensation details
        error_details = {
            "transactionId": transaction_id,
            "originalError": str(e),
            "compensations": compensation_results,
            "message": f"Transaction failed and rolled back: {str(e)}"
        }
        
        raise Exception(f"Saga transaction failed and compensated. Details: {json.dumps(error_details)}")
