/* eslint-disable no-console */
/* eslint-disable react/prop-types */
import React from 'react';

import TopNavigationHeader from '../TopNavigationHeader';

const FetchUserDetails = ({ user }) => {
  // This function uses the prop 'user' that is passed from the parent 'App' component
  // The function takes this prop and passes the variable as a prop to all components listed in the return., assigns them to the variable 'amplifySignedInUser'

  console.log(`I am the child of App component`);
  console.log(user);

  return <TopNavigationHeader user={user} />;
};

export default FetchUserDetails;
