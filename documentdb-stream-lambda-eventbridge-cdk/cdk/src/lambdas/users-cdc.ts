import { PutEventsCommand } from '@aws-sdk/client-eventbridge'
import { eventBridgeClient } from '../clients/eventbridge'
import { DocumentDBStreamEvent } from '../types/documentdb-stream-event'

const usersCdc = async (
  event: DocumentDBStreamEvent
): Promise<void> => {
  console.log(JSON.stringify(event, null, 2))
  const { events } = event
  const eventBridgeEvents = events.map(event => ({
    EventBusName: process.env.DEFAULT_EVENT_BUS! || 'default',
    Detail: JSON.stringify({
      documentKey: event.event.documentKey,
      fullDocument: event.event.fullDocument || {},
      updateDescription: event.event.updateDescription || {}
    }),
    DetailType: event.event.fullDocument?.template || 'delete_device',
    Source: 'Users_CDC'
  }))
  const response = await eventBridgeClient.send(
    new PutEventsCommand({
      Entries: eventBridgeEvents
    })
  )
  console.log('EventBridge Response', response)
}

export const main = usersCdc
