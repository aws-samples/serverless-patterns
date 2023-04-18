/* eslint-disable react/prop-types */
/* eslint-disable react/jsx-no-useless-fragment */
import React from 'react';
import {
  Box,
  Container,
  Header,
  ColumnLayout,
} from '@cloudscape-design/components';
import { CounterLink } from '../common-components';

export const S3ObjectsOverview = ({ s3Objects, s3ObjectSizeSum }) => {
  return (
    <>
      <Box margin="xxl" padding={{ vertical: '', horizontal: 'l' }}>
        <Container
          className="custom-dashboard-container"
          header={
            <Header
              variant="h2"
              description="Viewing data from S3 Objects DynamoDB table."
            >
              S3 overview
            </Header>
          }
        >
          <ColumnLayout columns="4" variant="text-grid">
            <div>
              <Box variant="awsui-key-label">S3 Buckets</Box>
              <CounterLink>4</CounterLink>
            </div>
            <div>
              <Box variant="awsui-key-label">S3 Objects</Box>
              <CounterLink>{s3Objects.length}</CounterLink>
            </div>
            <div>
              <Box variant="awsui-key-label">Total Storage (GB)</Box>
              <CounterLink>{s3ObjectSizeSum}</CounterLink>
            </div>
            <div>
              <Box variant="awsui-key-label">Areas of Concern</Box>
              <CounterLink>0</CounterLink>
            </div>
          </ColumnLayout>
        </Container>
      </Box>
    </>
  );
};
