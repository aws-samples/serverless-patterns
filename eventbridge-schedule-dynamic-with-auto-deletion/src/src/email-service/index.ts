interface EmailScheduledEvent {
  userId: string
  context: '24hr' | '1wk' | '1month'
}

export async function handler(event: EmailScheduledEvent) {
  // Replace this code with email service integration code.
  console.log(`User ${event.userId} signed up ${event.context} ago. Send an email`)
}
