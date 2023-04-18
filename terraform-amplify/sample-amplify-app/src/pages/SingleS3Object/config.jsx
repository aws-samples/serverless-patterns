/* eslint-disable camelcase */
/* eslint-disable no-console */
/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable no-use-before-define */
/* eslint-disable react/no-array-index-key */
/* eslint-disable react/prop-types */
/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
/** **********************************************************************
                            DISCLAIMER

This is just a playground package. It does not comply with best practices
of using Cloudscape Design components. For production code, follow the
integration guidelines:

https://cloudscape.design/patterns/patterns/overview/
*********************************************************************** */
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router';
import {
  Box,
  BreadcrumbGroup,
  Button,
  ButtonDropdown,
  ColumnLayout,
  Container,
  Header,
  Link,
  ProgressBar,
  StatusIndicator,
  SpaceBetween,
  Table,
} from '@cloudscape-design/components';
import { API, graphqlOperation, Amplify, Auth, PubSub, Hub } from 'aws-amplify';
import {
  TableEmptyState,
  InfoLink,
} from '../../common/common-components-config';

import { getObject } from '../../graphql/queries';

export const PageHeader = ({ buttons, singleS3Object }) => {
  return (
    <Header
      variant="h1"
      actions={
        <SpaceBetween direction="horizontal" size="xs">
          {buttons.map((button, key) =>
            !button.items ? (
              <Button
                href={button.href || ''}
                disabled={button.disabled || false}
                key={key}
              >
                {button.text}
              </Button>
            ) : (
              <ButtonDropdown items={button.items} key={key}>
                {button.text}
              </ButtonDropdown>
            )
          )}
        </SpaceBetween>
      }
    >
      {/* Reference 'singleS3Object' prop passed by SingleS3Object component in index.jsx */}
      {singleS3Object.FileName}
    </Header>
  );
};

// Content/formatting for the Bittle Device Details table
export const SingleS3ObjectDetailsTableConfig = ({
  isInProgress,
  singleS3Object,
}) => {
  const s3Data = singleS3Object;
  console.log(s3Data);

  return (
    <ColumnLayout columns={3} variant="text-grid">
      {/* ------------ FIRST COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          <Box variant="awsui-key-label">AWS Region</Box>
          <div>{singleS3Object.Region}</div>
        </div>
        {/* Second Item */}
        <div>
          <Box variant="awsui-key-label">Account Id</Box>
          <div>{singleS3Object.AccountId}</div>
        </div>
        {/* Third Item */}
        <div>
          <Box variant="awsui-key-label">Last Modified</Box>
          <div>{singleS3Object.CreatedAt}</div>
        </div>
        {/* Fourth Item */}
        <div>
          <Box variant="awsui-key-label">File Size</Box>
          <div>{singleS3Object.ObjectSize} Bytes</div>
        </div>
      </SpaceBetween>

      {/* ------------ SECOND COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          {/* TODO - Parse data for emissions_output with JSON.parse() */}
          <Box variant="awsui-key-label">S3 URI</Box>
          <div>{singleS3Object.FilePath}</div>
        </div>
        <div>
          {/* TODO - Parse data for emissions_output with JSON.parse() */}
          <Box variant="awsui-key-label">Object URL</Box>
          <div>
            <Link
              href={`https://${singleS3Object.CurrentBucket}.s3.amazonaws.com/
            ${singleS3Object.FileName}-${singleS3Object.ObjectId}`}
            >
              https://{singleS3Object.CurrentBucket}.s3.amazonaws.com/
              {singleS3Object.FileName}-{singleS3Object.ObjectId}
            </Link>
          </div>
        </div>

        {/* Second Item */}
        <div>
          <Box variant="awsui-key-label">Original Bucket</Box>
          <div>{singleS3Object.OriginalBucket}</div>
        </div>
      </SpaceBetween>

      {/* ------------ THIRD COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          <Box variant="awsui-key-label">Status</Box>
          {singleS3Object.ObjectSize ? (
            <StatusIndicator
              type={
                singleS3Object.ObjectSize === 'Disconnected'
                  ? 'error'
                  : 'success'
              }
            >
              Secured
              {/* {singleS3Object.ObjectSize} */}
            </StatusIndicator>
          ) : (
            <ProgressBar
              value={27}
              label="Status"
              // description={isInProgress ? 'Update in progress' : undefined}
              variant="key-value"
              resultText="Available"
              status={isInProgress ? 'in-progress' : 'success'}
            />
          )}
        </div>
        {/* Second Item */}
        <div>
          <Box variant="awsui-key-label">Version</Box>
          <div>{singleS3Object.Version}</div>
        </div>
        {/* Third Item */}
        <div>
          <Box variant="awsui-key-label">Source IP Address</Box>
          <div>{singleS3Object.SourceIPAddress}</div>
        </div>
        {/* Third Item */}
        <div>
          <Box variant="awsui-key-label">Lifecycle Config</Box>
          <div>{singleS3Object.LifecycleConfig}</div>
        </div>
      </SpaceBetween>
      {/* <div className="VideoStreamContainer">TODO - ADD KINESIS VIDEO HERE</div> */}
    </ColumnLayout>
  );
};
// OPTION 1 - Content/formatting for the Bittle Commands table
export const SingleS3ObjectTableConfig = ({ singleS3Object }) => {
  // const singleS3ObjectName = singleS3Object.ObjectId;
  console.log(
    'SingleS3ObjectTableConfig - Single S3 Object Name:'
    // , singleS3ObjectName
  );

  return (
    <ColumnLayout columns={3} variant="text-grid">
      {/* ------------ FIRST COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          <Box variant="awsui-key-label">Movements</Box>
          {/* <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kwkF' })
              }
            >
              Forward
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kwkL' })
              }
            >
              Forward L
            </Button>
            <Button
              onClick={() => {
                PubSub.publish(`Bittle1/sub`, { message: 'kwkR' });
                console.log('you clicked me');
              }}
            >
              Forward R
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kbkL' })
              }
            >
              Back L
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kbkR' })
              }
            >
              Back R
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kbk' })
              }
            >
              Back
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, {
                  message: 'kbalance',
                })
              }
              variant="primary"
            >
              Stop
            </Button>
            <Button
              onClick={
                () =>
                  PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'd' })
                // PubSub.publish(`Bittle2/sub`, { message: 'd' })
              }
              variant="primary"
            >
              Rest
            </Button>
          </div> */}
        </div>
      </SpaceBetween>

      {/* ------------ SECOND COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          {/* TODO - Parse data for emissions_output with JSON.parse() */}
          <Box variant="awsui-key-label">Mode</Box>
          {/* <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'g' })
              }
            >
              Gyro On/Off
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'c' })
              }
            >
              Calibration
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, {
                  message: 'kbalance',
                })
              }
            >
              Balanced
            </Button>
          </div> */}
        </div>
      </SpaceBetween>

      {/* ------------ THIRD COLUMN ------------ */}
      <SpaceBetween size="l">
        {/* First Item */}
        <div>
          {/* TODO - Parse data for emissions_output with JSON.parse() */}
          <Box variant="awsui-key-label">Actions</Box>
          {/* <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kwkF' })
              }
            >
              Walk
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'ksit' })
              }
            >
              Sit
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'khi' })
              }
            >
              Hello
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kpee' })
              }
            >
              Pee
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'ktrF' })
              }
            >
              Trot
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kck' })
              }
            >
              Check
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kvtF' })
              }
            >
              Stepping
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kpu' })
              }
            >
              Push Ups
            </Button>
          </div>
          <div>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kstr' })
              }
            >
              Stretch
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, {
                  message: 'kbuttUp',
                })
              }
            >
              Butt Up
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'krnF' })
              }
            >
              Run
            </Button>
            <Button
              onClick={() =>
                PubSub.publish(`${singleS3ObjectName}/sub`, { message: 'kcrF' })
              }
            >
              Crawl
            </Button>
          </div> */}
        </div>
      </SpaceBetween>

      {/* <div className="VideoStreamContainer">TODO - ADD KINESIS VIDEO HERE</div> */}
    </ColumnLayout>
  );
};

// May not need this

// export const EmptyTable = props => {
//   const resourceType = props.title || 'Tag';
//   const colDefs = props.columnDefinitions || TAGS_COLUMN_DEFINITIONS;
//   return (
//     <Table
//       empty={<TableEmptyState resourceName={resourceType} />}
//       columnDefinitions={colDefs}
//       items={[]}
//       header={
//         <Header
//           actions={
//             <SpaceBetween size="xs" direction="horizontal">
//               <Button disabled={true}>Edit</Button>
//               <Button disabled={true}>Delete</Button>
//               <Button>Create {resourceType.toLowerCase()}</Button>
//             </SpaceBetween>
//           }
//         >{`${resourceType}s`}</Header>
//       }
//     />
//   );
// };
