import React, { useState, useRef, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { makeRequest } from "../../utils/apigwRequest";

const ChatComponent: React.FC = () => {
  const [wsConnection, setWsConnection] = useState<WebSocket | null>(null);
  const [channelName, setChannelName] = useState('');
  const [userId, setUserId] = useState('');
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState<string[]>([]);
  const [connectionEvents, setConnectionEvents] = useState<string[]>([]);
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [subscriptionId, setSubscriptionId] = useState('');

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const connectionEventsEndRef = useRef<HTMLDivElement>(null);

  const wssUrl = `wss://${import.meta.env.VITE_EVENTS_API_REAL_TIME}/event/realtime`;
  const authorization = {
    host: import.meta.env.VITE_EVENTS_API_HTTP,
    "x-api-key": import.meta.env.VITE_API_KEY
  };

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  useEffect(() => {
    if (connectionEventsEndRef.current) {
      connectionEventsEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [connectionEvents]);

  function getBase64URLEncoded(authorization: any): string {
    return btoa(JSON.stringify(authorization))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=+$/, '');
  }

  function getSubprotocols(authorization: any): string[] {
    const header = getBase64URLEncoded(authorization);
    return ['aws-appsync-event-ws', `header-${header}`];
  }

  const initializeWebSocket = () => {
    const ws = new WebSocket(wssUrl, getSubprotocols(authorization));
  
    ws.onopen = () => {
      console.log('WebSocket Connected');
      ws.send(JSON.stringify({ type: 'connection_init' }));
    }
  
    ws.onclose = (event) => {
      console.log('WebSocket connection closed:', event.code, event.reason);
      setConnectionEvents(prev => [...prev, `WebSocket connection closed: ${event.code}, ${event.reason}`]);
    }
  
    ws.onerror = (error) => {
      console.log('WebSocket Error:', error);
      setConnectionEvents(prev => [...prev, `WebSocket Error: ${error}`]);
    }
  
    ws.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        if (message.type === 'connection_ack') {
          setConnectionEvents(prev => [...prev, 'connection_ack']);
        } else if (message.type === 'ka') {
          setConnectionEvents(prev => [...prev, 'ka']);
        } else if (message.type === 'subscribe_success' && message.id === subscriptionId) {
          setIsSubscribed(true);
          setConnectionEvents(prev => [...prev, 'subscribe_success']);
        } else if (message.type === 'unsubscribe_success' && message.id === subscriptionId) {
          setIsSubscribed(false);
          setConnectionEvents(prev => [...prev, 'unsubscribe_success']);
        } else if (message.type === 'unsubscribe_error' && message.id === subscriptionId) {
          setIsSubscribed(false);
          setConnectionEvents(prev => [...prev, 'unsubscribe_error']);
        } else if (message.type === 'data') {
          // Handle data events here
          console.log(message)
          setMessages(prev => [...prev, JSON.parse(message.event).data]);
        } else {
          console.log('Unhandled message type:', message.type, message);
        }
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    };
  
    setWsConnection(ws);
  };
  

  const subscribeToChannel = async () => {
    if (wsConnection && channelName) {
      const newSubscriptionId = uuidv4();
      setSubscriptionId(newSubscriptionId);

      wsConnection.send(JSON.stringify({
        type: 'subscribe',
        id: newSubscriptionId,
        channel: channelName,
        authorization
      }));

      try {
        await new Promise<void>((resolve, reject) => {
          const subscriptionTimeoutMs = 10000; // 10 seconds
          const subscriptionTimer = setTimeout(() => {
            reject(new Error('Subscription timeout'));
          }, subscriptionTimeoutMs);

          const messageHandler = (event: MessageEvent) => {
            const message = JSON.parse(event.data.toString());
            if (message.type === 'subscribe_success' && message.id === newSubscriptionId) {
              clearTimeout(subscriptionTimer);
              wsConnection.removeEventListener('message', messageHandler);
              resolve();
            }
          };

          wsConnection.addEventListener('message', messageHandler);
        });

        setIsSubscribed(true);
        setConnectionEvents(prev => [...prev, `subscribe - ${channelName}`]);
      } catch (error: any) {
        console.error('Subscription failed:', error);
        setMessages(prev => [...prev, `Subscription failed: ${error.message}`]);
      }
    }
  };

  const unsubscribe = () => {
    if (wsConnection && isSubscribed) {
      wsConnection.send(JSON.stringify({
        type: 'unsubscribe',
        id: subscriptionId
      }));
      setConnectionEvents(prev => [...prev, `unsubscribe - ${channelName}`]);
      setIsSubscribed(false)
    }
  };

  const closeWebSocket = () => {
    if (wsConnection) {
      wsConnection.close();
      setWsConnection(null);
      setIsSubscribed(false);
      setSubscriptionId('');
      setConnectionEvents(prev => [...prev, 'WebSocket connection closed']);
    }
  };

  const sendMessage = async () => {
    if (wsConnection && userId && prompt) {
      const res = makeRequest({
        url: import.meta.env.VITE_CHAT_API_URL || "",
        method: "POST",
        apiKey: import.meta.env.VITE_API_KEY
      }, {
        prompt: prompt,
        userId: userId
      });

      //console.log(res)

      setPrompt('');
    }
  };

  const clearMessages = () => {
    setMessages([]);
  };

  const clearConnectionEvents = () => {
    setConnectionEvents([]);
  };

  return (
    <div>
      <div>
        <button onClick={initializeWebSocket} disabled={!!wsConnection}>
          Initialize WebSocket
        </button>
      </div>
      <div>
        <input
          type="text"
          value={channelName}
          onChange={(e) => setChannelName(e.target.value)}
          placeholder={`${import.meta.env.VITE_CHANNEL}/*`}
          disabled={isSubscribed}
        />
        <button onClick={subscribeToChannel} disabled={!wsConnection || !channelName || isSubscribed}>
          Subscribe
        </button>
      </div>
      <div>
        <button onClick={unsubscribe} disabled={!isSubscribed}>
          Unsubscribe
        </button>
      </div>
      <div>
        <button onClick={closeWebSocket} disabled={!wsConnection}>
          Close WebSocket
        </button>
      </div>
      <div>
        <input
          type="text"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          placeholder="User ID"
        />
      </div>
      <div>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt"
        />
      </div>
      <div>
        <button onClick={sendMessage} disabled={!wsConnection || !userId || !prompt}>
          Send Message
        </button>
      </div>
      <div style={{ height: '200px', overflowY: 'auto', border: '1px solid black', marginTop: '10px' }}>
        {connectionEvents.map((event, index) => (
          <div key={index}>{event}</div>
        ))}
        <div ref={connectionEventsEndRef} />
      </div>
      <div style={{ height: '200px', overflowY: 'auto', border: '1px solid black', marginTop: '10px' }}>
        {messages.map((msg, index) => (
          <div key={index}>{msg}</div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div>
        <button onClick={clearMessages}>Clear Messages</button>
        <button onClick={clearConnectionEvents}>Clear Connection Events</button>
      </div>
    </div>
  );
};

export default ChatComponent;