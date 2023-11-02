// This lambda is used to unwrap events with messages which have nested payloads that were already stringified.
exports.handler = async (event) => {
    console.log("event before enrichment: " + JSON.stringify(event));

    return event.map((e) => {
        var body = e.body;
        body.Message = JSON.parse(body.Message);
        console.log("message after enrichment: " + JSON.stringify(body));
        return body;
    });
}