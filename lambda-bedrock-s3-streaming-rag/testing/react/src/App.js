import "./styles.css";
import React, { useState } from "react";
import { fetchEventSource } from "@microsoft/fetch-event-source";
import { SignatureV4 } from "@smithy/signature-v4";
import { Sha256 } from "@aws-crypto/sha256-js";

export default function App() {
  const [searchQuery, setSearchQuery] = useState();
  const [chat, setChat] = useState([]);

  const streamData = async () => {

    const credentials = {
      accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
      secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
      sessionToken: process.env.REACT_APP_AWS_SESSION_TOKEN,
    };
    setChat([]);
    const sigv4 = new SignatureV4({
      service: "lambda",
      region: process.env.REACT_APP_AWS_REGION,
      credentials,
      sha256: Sha256
    });

    const apiUrl = new URL(process.env.REACT_APP_LAMBDA_ENDPOINT_URL);

    const query = document.getElementById("searchQuery").value;
    setSearchQuery(query);
    let body = JSON.stringify({
      query: query,
      // Can use any Bedrock available models
      model: "anthropic.claude-instant-v1",
      // This is required for the @microsoft/fetch-event-source library to understand the streaming response
      streamingFormat: "fetch-event-source"
    });
    let signed = await sigv4.sign({
      body,
      method: "POST",
      hostname: apiUrl.hostname,
      path: apiUrl.pathname.toString(),
      protocol: apiUrl.protocol,
      headers: {
        "Content-Type": "application/json",
        host: apiUrl.hostname
      }
    });

    await fetchEventSource(apiUrl.origin, {
      method: signed.method,
      headers: signed.headers,
      body,
      onopen(res) {
        if (res.ok && res.status === 200) {
          console.log("Connection made ", res);
        } else if (
          res.status >= 400 &&
          res.status < 500 &&
          res.status !== 429
        ) {
          console.log("Client-side error ", res);
        }
      },
      onmessage(event) {
        setChat((data) => [...data, event.data]);
        // Important to set the data this way, otherwise old data may be overwritten if the stream is too fast
      },
      onclose() {
        console.log("Connection closed by the server");
      },
      onerror(err) {
        console.log("There was an error from server", err);
      }
    });
  };

  return (
    <div>
      <div>
        <span className="label">Ask a question: </span>
        <input id="searchQuery"></input>
        <br></br>
        <button onClick={() => streamData()}>Submit Question</button>
      </div>
      <div>
        <p>
          <b>Question:</b> {searchQuery}
          <br></br>
          <br></br>
          <b>Response:</b> {chat.join("")}
        </p>
      </div>
    </div>
  );
}
