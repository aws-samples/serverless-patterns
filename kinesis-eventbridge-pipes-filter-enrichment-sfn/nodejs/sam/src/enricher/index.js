exports.handler = async (event) => {
  return event.map(message => {
    const data = JSON.parse(Buffer.from(message.data, 'base64').toString())
    return {
      ...data,
      enrichedKey: "I have been enriched"
    }
  })
}

