/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React, { useState } from 'react';
import { TopNavigation } from '@cloudscape-design/components';

// Amplify
import { Auth } from 'aws-amplify';
// Company logo. Upload your own logo and point to it to change this in the TopNavigation.
import logo from '../../../public/images/AWS_logo_RGB_REV.png';

// Styles
import '../../styles/top-navigation.scss';

const TopNavigationHeader = ({ user }) => {
  // Function to sign user out
  async function signOut() {
    try {
      await Auth.signOut();
    } catch (error) {
      console.log('error signing out: ', error);
    }
  }
  return (
    <div id="h">
      <TopNavigation
        identity={{
          href: '/',
          // Your Company Name
          title: `Sample Amplify App`,
          logo: {
            src: logo,
            alt: 'Service',
          },
        }}
        utilities={[
          {
            type: 'button',
            text: 'AWS',
            href: 'https://aws.amazon.com/',
            external: true,
            externalIconAriaLabel: ' (opens in a new tab)',
          },
          {
            type: 'button',
            iconName: 'notification',
            title: 'Notifications',
            ariaLabel: 'Notifications (unread)',
            badge: true,
            disableUtilityCollapse: false,
          },
          {
            type: 'menu-dropdown',
            iconName: 'settings',
            ariaLabel: 'Settings',
            title: 'Settings',
            items: [
              {
                id: 'settings-org',
                text: 'Organizational settings',
              },
              {
                id: 'settings-project',
                text: 'Project settings',
              },
            ],
          },
          {
            type: 'menu-dropdown',
            text: `${user.attributes.given_name} ${user.attributes.family_name}`,
            description: `${user.attributes.email}`,
            iconName: 'user-profile',
            items: [
              { id: 'profile', text: 'Profile' },
              // Use me once a user profile page is created
              // { id: "profile", text: "Profile", href : '/user-profile'},
              { id: 'preferences', text: 'Preferences' },
              { id: 'security', text: 'Security' },
              {
                id: 'support-group',
                text: 'Support',
                items: [
                  {
                    id: 'documentation',
                    text: 'Documentation',
                    // TODO - Replace this with link to our GitHub docs
                    href: 'https://github.com/novekm/amplify-with-terraform/',
                    external: true,
                    externalIconAriaLabel: ' (opens in new tab)',
                  },
                  { id: 'support', text: 'Support' },
                  {
                    id: 'feedback',
                    text: 'Feedback',
                    // TODO - Replace this with link to our GitHub feedback mechanism
                    href: 'https://github.com/novekm/amplify-with-terraform/issues/newe',
                    external: true,
                    externalIconAriaLabel: ' (opens in new tab)',
                  },
                ],
              },
              // eslint-disable-next-line jsx-a11y/click-events-have-key-events, jsx-a11y/no-static-element-interactions
              { id: 'signout', text: <span onClick={signOut}>Sign out </span> },
            ],
          },
        ]}
        i18nStrings={{
          // searchIconAriaLabel: "Search",
          // searchDismissIconAriaLabel: "Close search",
          overflowMenuTriggerText: 'More',
          // overflowMenuTitleText: "All",
          // overflowMenuBackIconAriaLabel: "Back",
          // overflowMenuDismissIconAriaLabel: "Close menu"
        }}
      />
    </div>
  );
};

export default TopNavigationHeader;
