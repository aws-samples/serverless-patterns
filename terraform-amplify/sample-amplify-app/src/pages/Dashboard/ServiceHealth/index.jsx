import React from 'react';
import {
  Box,
  // HelpPanel,
  // Icon,
  Container,
  Header,
  StatusIndicator,
  ColumnLayout,
} from '@cloudscape-design/components';
// import { ExternalLinkItem, InfoLink } from '../../commons/common-components';

export const ServiceHealth = () => {
  return (
    <Box margin="xxl" padding={{ vertical: '', horizontal: 'l' }}>
      <Container
        header={
          <Header variant="h2">
            Service health - <em>new</em>
          </Header>
        }
      >
        <ColumnLayout columns="2">
          <div>
            <Box variant="awsui-key-label">Region</Box>
            <div>US East (N. Virginia)</div>
          </div>
          <div>
            <Box variant="awsui-key-label">Status</Box>
            <StatusIndicator type="success">
              Service is operating normally
            </StatusIndicator>
          </div>
        </ColumnLayout>
      </Container>
    </Box>
  );
};
