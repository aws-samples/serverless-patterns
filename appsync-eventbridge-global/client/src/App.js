import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "@popperjs/core";
import "bootstrap";
import ScrollToBottom from "react-scroll-to-bottom";
import logo from "./logo.svg";
import "./App.css";
import Amplify, { API, graphqlOperation } from "aws-amplify";
import * as subscriptions from "./graphql/subscriptions"; //codegen generated code
import * as mutations from "./graphql/mutations"; //codegen generated code

//AppSync endpoint settings
const myAppConfig = {
  aws_appsync_graphqlEndpoint:
    "https://xxxxxxxxxxxxxx.appsync-api.us-west-2.amazonaws.com/graphql",
  aws_appsync_region: "us-west-2",
  aws_appsync_authenticationType: "API_KEY",
  aws_appsync_apiKey: "da2-xxxxxxxxxxxxxxxxxx",
};

Amplify.configure(myAppConfig);

function App() {
  const [channel, setChannel] = useState("");
  const [channelName, setChannelName] = useState("");
  const [message, setMessage] = useState("");
  const [received, setReceived] = useState([]);
  const [display, setDisplay] = useState(false);
  let messages = [];

  //Publish data to subscribed clients
  async function handleSubmit(evt) {
    evt.preventDefault();
    evt.stopPropagation();
    const publish = await API.graphql(
      graphqlOperation(mutations.publish, { name: channel, message: message })
    );
    setChannelName(channel);
    setChannel("");
    setMessage("");
    setDisplay(true);
  }

  useEffect(() => {
    //Subscribe via WebSockets
    const subscription = API.graphql(
      graphqlOperation(subscriptions.subscribe, { name: channelName })
    ).subscribe({
      next: ({ provider, value }) => {
        setReceived((prevArray) => [
          ...prevArray,
          {
            name: value.data.subscribe.name,
            message: value.data.subscribe.message
          },
        ]);
      },
      error: (error) => console.warn(error),
    });
    return () => subscription.unsubscribe();
  }, [channelName]);

  if (received) {
    //messages.push(received);
    messages = [].concat(received).map((msg, i) => (
      <div>
        <div>
          <div className="w-25 p-3 d-inline-block badge bg-secondary p-0 rounded p-2">
            <span>{msg.name}</span>
          </div>
          <div className="w-75 p-2 d-inline-block alert alert-secondary">
            <span>{msg.message}</span>
          </div>
        </div>
      </div>
    ));
  }

  //Display pushed data on browser
  return (
    <div className="App bg-secondary">
      <br />
      <h4 className="text-white fs-1 bg-dark p-2">Global PubSub App</h4>
      <br />
      <div className="container-md border shadow p-3 mb-5 bg-body rounded-3">
        <img src={logo} className="App-logo" alt="logo" />
        <form>
          <div className="input-group mb-3">
            <button
              className="btn btn-outline-light btn-dark dropdown-toggle"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Channel
            </button>
            <ul className="dropdown-menu">
              <li>
                <p
                  className="dropdown-item"
                  onClick={(e) => setChannel("cars")}
                >
                  cars
                </p>
              </li>
              <li>
                <p
                  className="dropdown-item"
                  onClick={(e) => setChannel("robots")}
                >
                  robots
                </p>
              </li>
              <li>
                <p
                  className="dropdown-item"
                  onClick={(e) => setChannel("tech")}
                >
                  tech
                </p>
              </li>
              <li>
                <p
                  className="dropdown-item"
                  onClick={(e) => setChannel("music")}
                >
                  music
                </p>
              </li>
              <li>
                <p
                  className="dropdown-item"
                  onClick={(e) => setChannel("media")}
                >
                  media
                </p>
              </li>
            </ul>
            <input
              type="text"
              className="form-control"
              value={channel}
              aria-label="Channel"
              onChange={(e) => setChannel(e.target.value)}
            />
          </div>
          <div className="input-group mb-3">
            <input
              type="text"
              className="form-control"
              placeholder="Message"
              aria-label="Message"
              aria-describedby="button-addon2"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />
            <button
              onClick={handleSubmit}
              className="btn btn-outline-light btn-dark"
              type="button"
              id="button-addon2"
            >
              Send
            </button>
          </div>
        </form>
      </div>
      {display ? (
        <div className="container-md border shadow p-3 mb-5 bg-body rounded-3">
          <p className="badge fs-3 bg-dark p-0 rounded p-2">Message Board</p>
          <div className="bg-light p-0 rounded p-2">
            <span>{messages}</span>
          </div>
        </div>
      ) : null}
      <br />
    </div>
  );
}

export default App;