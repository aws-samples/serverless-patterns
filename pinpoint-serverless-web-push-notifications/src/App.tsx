import React, {useEffect, useState} from 'react';
import logo from './Amazon_icon.svg';
import './App.css';
import {Amplify, Analytics, Auth, Notifications} from 'aws-amplify';
import awsExports from './aws-exports';
import { withAuthenticator, Button, Heading } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { initializeApp } from "firebase/app";
import { getMessaging, getToken, onMessage } from 'firebase/messaging';
import axios from "axios";
Amplify.configure(awsExports);

const firebaseConfig = {
  apiKey: "",
  authDomain: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: ""
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const updateToken = async (token: string) => {
  const user = await Auth.currentAuthenticatedUser()
  await axios.post(process.env.REACT_APP_API_URL + '/updateToken', {
    id: user.attributes.sub,
    token: token
  })
}

function App() {
  const [title, setTitle] = useState('')
  const [body, setBody] = useState('')

  const messaging = getMessaging(app)

  onMessage(messaging, (payload) => {
    if(payload.data){
      setTitle(payload.data['pinpoint.notification.title'])
      setBody(payload.data['pinpoint.notification.body'])
    }
  })
  const requestPermissions = async () => {
    const permissions = await Notification.requestPermission();
    if (permissions === 'granted') {
      const token = await getToken(messaging, {
        vapidKey: process.env.REACT_APP_FIREBASE_VAPID_KEY
      })
      await Analytics.updateEndpoint({
        address: token,
        channelType: 'GCM'
      })
      await updateToken(token)
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {title}
        </p>
        <p>
          {body}
        </p>
        <button
          onClick={requestPermissions}
        >
          Enable Notifications
        </button>
      </header>
    </div>
  );
}

export default withAuthenticator(App);
