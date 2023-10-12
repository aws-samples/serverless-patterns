// This lambda is used to unwrap events with messages which have nested payloads that were already stringified.
exports.handler = async (event) => {
    console.log("event before enrichment: " + JSON.stringify(event));

    return event.map((e) => {
        const message = JSON.parse(e.body.Message);
        message.payload = JSON.parse(message.payload);;
        message.payload.alreadyStringifiedContent = JSON.parse(message.payload.alreadyStringifiedContent);;
        console.log("message after enrichment: " + JSON.stringify(message));
        return message;
    });
}