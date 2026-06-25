"""
Durable Function Orchestrator for Travel Planning Conversation
Uses AWS Lambda Durable Functions for stateful, long-running workflows with human-in-the-loop
"""
import json
import os
import boto3
from typing import Dict, Any

from aws_durable_execution_sdk_python import durable_execution, DurableContext
from aws_durable_execution_sdk_python.config import WaitForCallbackConfig, Duration

from activities import post_to_slack
from agentcore_client import AgentCoreClient

dynamodb = boto3.resource('dynamodb')
callbacks_table = dynamodb.Table(os.environ['CALLBACKS_TABLE_NAME'])

agentcore_client = AgentCoreClient()


@durable_execution
def travel_planning_orchestrator(event: Dict[str, Any], context: DurableContext) -> Dict[str, Any]:
    """
    Main orchestrator function - runs as a Durable Function

    This demonstrates:
    1. State persistence across multiple invocations (automatic)
    2. Wait-for-callback pattern for user responses
    3. Automatic replay safety - steps execute only once
    4. Integration with external services (Slack, Bedrock)

    Args:
        event: Lambda event containing user_id, channel, execution_id
        context: Durable execution context

    Returns:
        Result dictionary with status and details
    """
    user_id = event['user_id']
    channel = event['channel']
    execution_id = event['execution_id']

    context.logger.info(f"Starting travel planning orchestration for user {user_id}")

    # Step 1: Ask for destination
    context.step(post_to_slack(
        channel=channel,
        text="📍 Where would you like to go? (e.g., Japan, Paris, New York)"
    ))

    # Wait for user response
    def request_destination(callback_id: str, ctx):
        ctx.logger.info(f"Callback ID for destination: {callback_id}")
        callbacks_table.put_item(Item={
            'user_id': user_id,
            'callback_id': callback_id,
            'step': 'destination',
        })

    destination = context.wait_for_callback(
        submitter=request_destination,
        name='wait-for-destination',
        config=WaitForCallbackConfig(timeout=Duration.from_hours(1))
    )

    context.logger.info(f"Received destination: {destination}")

    # Step 2: Ask for dates
    context.step(post_to_slack(
        channel=channel,
        text=f"Great choice! {destination} is beautiful. 📅 When are you planning to travel? (e.g., May 15-22, 2026)"
    ))

    def request_dates(callback_id: str, ctx):
        ctx.logger.info(f"Callback ID for dates: {callback_id}")
        callbacks_table.put_item(Item={
            'user_id': user_id,
            'callback_id': callback_id,
            'step': 'dates',
        })

    dates = context.wait_for_callback(
        submitter=request_dates,
        name='wait-for-dates',
        config=WaitForCallbackConfig(timeout=Duration.from_hours(1))
    )

    context.logger.info(f"Received dates: {dates}")

    # Step 3: Ask for budget
    context.step(post_to_slack(
        channel=channel,
        text="💰 What's your approximate budget for this trip? (e.g., $2000, $5000)"
    ))

    def request_budget(callback_id: str, ctx):
        ctx.logger.info(f"Callback ID for budget: {callback_id}")
        callbacks_table.put_item(Item={
            'user_id': user_id,
            'callback_id': callback_id,
            'step': 'budget',
        })

    budget = context.wait_for_callback(
        submitter=request_budget,
        name='wait-for-budget',
        config=WaitForCallbackConfig(timeout=Duration.from_hours(1))
    )

    context.logger.info(f"Received budget: {budget}")

    # Step 4: Ask for interests
    context.step(post_to_slack(
        channel=channel,
        text="🎯 What are you most interested in? (e.g., food, history, adventure, beaches, culture)"
    ))

    def request_interests(callback_id: str, ctx):
        ctx.logger.info(f"Callback ID for interests: {callback_id}")
        callbacks_table.put_item(Item={
            'user_id': user_id,
            'callback_id': callback_id,
            'step': 'interests',
        })

    interests = context.wait_for_callback(
        submitter=request_interests,
        name='wait-for-interests',
        config=WaitForCallbackConfig(timeout=Duration.from_hours(1))
    )

    context.logger.info(f"Received interests: {interests}")

    # Step 5: Notify user we're generating itinerary
    context.step(post_to_slack(
        channel=channel,
        text="✨ Generating your personalized itinerary... This may take a moment."
    ))

    # Step 6: Generate itinerary via AgentCore (async with callback)
    def invoke_agentcore(callback_id: str, ctx):
        ctx.logger.info(f"Invoking AgentCore with callback {callback_id[:20]}...")
        # AgentCore will process and send callback when done
        confirmation = agentcore_client.generate_itinerary(
            destination=destination,
            dates=dates,
            budget=budget,
            interests=interests,
            callback_id=callback_id
        )
        ctx.logger.info(f"AgentCore confirmed: {confirmation}")

    # Wait for AgentCore to send back the itinerary via callback
    itinerary_response = context.wait_for_callback(
        submitter=invoke_agentcore,
        name='wait-for-agentcore-itinerary',
        config=WaitForCallbackConfig(timeout=Duration.from_minutes(5))
    )

    # Parse the response from AgentCore
    if isinstance(itinerary_response, str):
        itinerary_data = json.loads(itinerary_response)
    else:
        itinerary_data = itinerary_response

    itinerary = itinerary_data.get('itinerary', str(itinerary_data))

    context.logger.info("Itinerary generated, posting to Slack")

    # Step 7: Post final itinerary
    context.step(post_to_slack(
        channel=channel,
        text=f"🎉 *Your Personalized Travel Itinerary*\n\n{itinerary}\n\n_Have an amazing trip!_"
    ))

    context.logger.info("Orchestration completed successfully")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'completed',
            'execution_id': execution_id,
            'destination': destination,
            'dates': dates
        })
    }


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler wrapper - entry point for AWS Lambda

    This handles both:
    1. New orchestration requests
    2. Callback responses from users

    Args:
        event: Lambda event
        context: Lambda context

    Returns:
        Response dictionary
    """
    # Check if this is a callback response
    if event.get('callback_id'):
        # This is a callback response - the SDK will automatically handle it
        # and resume the waiting orchestration
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Callback processed'})
        }

    # This is a new orchestration request
    return travel_planning_orchestrator(event, context)
