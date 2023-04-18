/* eslint-disable no-unused-vars */
import React from 'react';
import {
  AppLayout,
  SideNavigation,
  Container,
  Header,
  HelpPanel,
  Grid,
  Box,
  TextContent,
  SpaceBetween,
} from '@cloudscape-design/components';

const HelpTools = () => {
  return (
    <HelpPanel header={<h2>Help panel</h2>}>
      <p>
        For issues with the app, please submit a{' '}
        <a
          target="_blank"
          rel="noopener noreferrer"
          href="https://github.com/novekm/amplify-with-terraform/issues/new"
        >
          GitHub issue
        </a>
        .{' '}
      </p>
    </HelpPanel>
  );
};

export default HelpTools;
