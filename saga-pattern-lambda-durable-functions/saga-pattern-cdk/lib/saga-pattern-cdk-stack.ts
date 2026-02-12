import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import { aws_dynamodb, aws_lambda, aws_logs, Duration, RemovalPolicy } from 'aws-cdk-lib';

export class SagaPatternCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Hotel reservations table
    const hotelTable = new aws_dynamodb.Table(this, 'HotelReservationsTable', {
      tableName: 'saga-hotel-reservations',
      partitionKey: { name: 'reservationId', type: aws_dynamodb.AttributeType.STRING },
      billingMode: aws_dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    // Flight bookings table
    const flightTable = new aws_dynamodb.Table(this, 'FlightBookingsTable', {
      tableName: 'saga-flight-bookings',
      partitionKey: { name: 'bookingId', type: aws_dynamodb.AttributeType.STRING },
      billingMode: aws_dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    // Car rentals table
    const carTable = new aws_dynamodb.Table(this, 'CarRentalsTable', {
      tableName: 'saga-car-rentals',
      partitionKey: { name: 'rentalId', type: aws_dynamodb.AttributeType.STRING },
      billingMode: aws_dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    // Flight Lambda functions
    const reserveFlightLogGroup = new aws_logs.LogGroup(this, 'ReserveFlightLogGroup', {
      logGroupName: '/aws/lambda/saga-reserve-flight',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const reserveFlight = new aws_lambda.Function(this, 'ReserveFlightFunction', {
      functionName: 'saga-reserve-flight',
      description: 'Creates a new flight booking reservation and stores it in DynamoDB as part of the saga transaction',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'reserve_flight.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/flight'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: reserveFlightLogGroup,
      environment: {
        TABLE_NAME: flightTable.tableName
      },
    });

    const cancelFlightLogGroup = new aws_logs.LogGroup(this, 'CancelFlightLogGroup', {
      logGroupName: '/aws/lambda/saga-cancel-flight',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const cancelFlight = new aws_lambda.Function(this, 'CancelFlightFunction', {
      functionName: 'saga-cancel-flight',
      description: 'Compensating transaction that cancels a flight booking when the saga needs to rollback',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'cancel_flight.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/flight'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: cancelFlightLogGroup,
      environment: {
        TABLE_NAME: flightTable.tableName
      },
    });

    // Hotel Lambda functions
    const reserveHotelLogGroup = new aws_logs.LogGroup(this, 'ReserveHotelLogGroup', {
      logGroupName: '/aws/lambda/saga-reserve-hotel',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const reserveHotel = new aws_lambda.Function(this, 'ReserveHotelFunction', {
      functionName: 'saga-reserve-hotel',
      description: 'Creates a new hotel room reservation and stores it in DynamoDB as part of the saga transaction',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'reserve_hotel.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/hotel'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: reserveHotelLogGroup,
      environment: {
        TABLE_NAME: hotelTable.tableName
      },
    });

    const cancelHotelLogGroup = new aws_logs.LogGroup(this, 'CancelHotelLogGroup', {
      logGroupName: '/aws/lambda/saga-cancel-hotel',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const cancelHotel = new aws_lambda.Function(this, 'CancelHotelFunction', {
      functionName: 'saga-cancel-hotel',
      description: 'Compensating transaction that cancels a hotel reservation when the saga needs to rollback',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'cancel_hotel.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/hotel'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: cancelHotelLogGroup,
      environment: {
        TABLE_NAME: hotelTable.tableName
      },
    });

    // Car Lambda functions
    const reserveCarLogGroup = new aws_logs.LogGroup(this, 'ReserveCarLogGroup', {
      logGroupName: '/aws/lambda/saga-reserve-car',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const reserveCar = new aws_lambda.Function(this, 'ReserveCarFunction', {
      functionName: 'saga-reserve-car',
      description: 'Creates a new car rental reservation and stores it in DynamoDB as part of the saga transaction',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'reserve_car.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/car'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: reserveCarLogGroup,
      environment: {
        TABLE_NAME: carTable.tableName
      },
    });

    const cancelCarLogGroup = new aws_logs.LogGroup(this, 'CancelCarLogGroup', {
      logGroupName: '/aws/lambda/saga-cancel-car',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const cancelCar = new aws_lambda.Function(this, 'CancelCarFunction', {
      functionName: 'saga-cancel-car',
      description: 'Compensating transaction that cancels a car rental reservation when the saga needs to rollback',
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      handler: 'cancel_car.lambda_handler',
      code: aws_lambda.Code.fromAsset('lambda/car'),
      tracing: aws_lambda.Tracing.ACTIVE,
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      timeout: Duration.minutes(1),
      logGroup: cancelCarLogGroup,
      environment: {
        TABLE_NAME: carTable.tableName
      },
    });

    // Saga orchestrator durable function
    const sagaDurableFunctionLogGroup = new aws_logs.LogGroup(this, 'SagaDurableFunctionLogGroup', {
      logGroupName: '/aws/lambda/saga-durable-function',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const sagaDependenciesLayer = new aws_lambda.LayerVersion(this, 'SagaDependenciesLayer', {
      code: aws_lambda.Code.fromAsset('lambda/saga-workflow/saga-layer.zip'),
      compatibleRuntimes: [aws_lambda.Runtime.PYTHON_3_14],
      description: 'Saga pattern dependencies (durable SDK, boto3, etc.)',
    });

    const sagaDurableFunction = new aws_lambda.Function(this, 'SagaDurableFunction', {
      runtime: aws_lambda.Runtime.PYTHON_3_14,
      tracing: aws_lambda.Tracing.ACTIVE,
      functionName: 'saga-durable-function',
      description: 'Orchestrates the saga pattern workflow by coordinating flight, hotel, and car reservations with automatic rollback on failure',
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      handler: 'index.lambda_handler',
      logGroup: sagaDurableFunctionLogGroup,
      layers: [sagaDependenciesLayer],
      durableConfig: {
        executionTimeout: Duration.hours(1),
        retentionPeriod: Duration.days(30)
      },
      code: aws_lambda.Code.fromAsset('lambda/saga-workflow'),
      environment: {
        HOTEL_TABLE_NAME: hotelTable.tableName,
        FLIGHT_TABLE_NAME: flightTable.tableName,
        CAR_TABLE_NAME: carTable.tableName,
        RESERVE_FLIGHT_FUNCTION: reserveFlight.functionName,
        CANCEL_FLIGHT_FUNCTION: cancelFlight.functionName,
        RESERVE_HOTEL_FUNCTION: reserveHotel.functionName,
        CANCEL_HOTEL_FUNCTION: cancelHotel.functionName,
        RESERVE_CAR_FUNCTION: reserveCar.functionName,
        CANCEL_CAR_FUNCTION: cancelCar.functionName,
      },
    });

    // Grant Lambda permissions to access DynamoDB tables
    hotelTable.grantReadWriteData(sagaDurableFunction);
    flightTable.grantReadWriteData(sagaDurableFunction);
    carTable.grantReadWriteData(sagaDurableFunction);

    // Grant individual Lambda functions access to their respective tables
    flightTable.grantReadWriteData(reserveFlight);
    flightTable.grantReadWriteData(cancelFlight);
    hotelTable.grantReadWriteData(reserveHotel);
    hotelTable.grantReadWriteData(cancelHotel);
    carTable.grantReadWriteData(reserveCar);
    carTable.grantReadWriteData(cancelCar);

    // Grant saga orchestrator permission to invoke service functions
    reserveFlight.grantInvoke(sagaDurableFunction);
    cancelFlight.grantInvoke(sagaDurableFunction);
    reserveHotel.grantInvoke(sagaDurableFunction);
    cancelHotel.grantInvoke(sagaDurableFunction);
    reserveCar.grantInvoke(sagaDurableFunction);
    cancelCar.grantInvoke(sagaDurableFunction);

    // Outputs
    new cdk.CfnOutput(this, 'SagaDurableFunctionArn', {
      value: sagaDurableFunction.functionArn,
      description: 'The ARN of the Saga durable function',
    });

    new cdk.CfnOutput(this, 'ReserveFlightFunctionArn', {
      value: reserveFlight.functionArn,
      description: 'Reserve flight function ARN',
    });

    new cdk.CfnOutput(this, 'CancelFlightFunctionArn', {
      value: cancelFlight.functionArn,
      description: 'Cancel flight function ARN',
    });

    new cdk.CfnOutput(this, 'ReserveHotelFunctionArn', {
      value: reserveHotel.functionArn,
      description: 'Reserve hotel function ARN',
    });

    new cdk.CfnOutput(this, 'CancelHotelFunctionArn', {
      value: cancelHotel.functionArn,
      description: 'Cancel hotel function ARN',
    });

    new cdk.CfnOutput(this, 'ReserveCarFunctionArn', {
      value: reserveCar.functionArn,
      description: 'Reserve car function ARN',
    });

    new cdk.CfnOutput(this, 'CancelCarFunctionArn', {
      value: cancelCar.functionArn,
      description: 'Cancel car function ARN',
    });

    new cdk.CfnOutput(this, 'HotelTableName', {
      value: hotelTable.tableName,
      description: 'Hotel reservations table name',
    });

    new cdk.CfnOutput(this, 'FlightTableName', {
      value: flightTable.tableName,
      description: 'Flight bookings table name',
    });

    new cdk.CfnOutput(this, 'CarTableName', {
      value: carTable.tableName,
      description: 'Car rentals table name',
    });
  }
}
