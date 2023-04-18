/* eslint-disable no-console */
/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable react/prop-types */
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
import { Link, useNavigate, useParams } from 'react-router-dom';
// COMPONENT IMPORTS
import {
  BreadcrumbGroup,
  Button,
  AppLayout,
  Container,
  Header,
  HelpPanel,
  Icon,
  SpaceBetween,
  ContentLayout,
} from '@cloudscape-design/components';

// Amplify
import { API, graphqlOperation, Amplify, Auth, PubSub, Hub } from 'aws-amplify';

// Common
import {
  ExternalLinkItem,
  InfoLink,
  Navigation,
  TableHeader,
} from '../../common/common-components-config';
import Sidebar from '../../common/components/Sidebar';

// Page configuration components
import {
  PageHeader,
  SingleS3ObjectDetailsTableConfig,
  SingleS3ObjectTableConfig,
  // SingleS3ObjectTableConfig2,
} from './config';

// API functions
import { getObject } from '../../graphql/queries';

// Styles
import '../../common/styles/base.scss';

// Main component for page
const SingleS3ObjectPage = () => {
  const [toolsOpen, setToolsOpen] = useState(false);
  const { ObjectId } = useParams();
  const [singleS3Object, setSingleS3Object] = useState([]);

  // Fetch data for one bittle by 'DeviceId' specified in browser URL via useParams hook
  const fetchSingleS3Object = async () => {
    try {
      const singleS3ObjectData = await API.graphql(
        graphqlOperation(getObject, { ObjectId: `${ObjectId}` })
      );
      const singleS3ObjectDataList = singleS3ObjectData.data.getObject;
      console.log('Single S3 Object List', singleS3ObjectDataList);
      setSingleS3Object(singleS3ObjectDataList);
      // setLoading(false)
    } catch (error) {
      console.log('error on fetching single s3 object', error);
    }
  };

  // Subscribe to the specific topic relating to the current bittle on the page on page load
  useEffect(() => {
    fetchSingleS3Object();
    console.log(`${singleS3Object.ObjectId}`);
  }, []);

  return (
    <AppLayout
      navigation={<Sidebar activeHref="/s3-objects" />}
      // notifications={<Notifications successNotification={false} />}
      breadcrumbs={<Breadcrumbs singleS3Object={singleS3Object} />}
      content={
        <ContentLayout
          header={
            <PageHeader
              singleS3Object={singleS3Object}
              buttons={[{ text: 'S3 Objects', href: '/s3-objects' }]}
              // buttons={[{ text: 'Edit' }, { text: 'Delete' }]}
              // loadHelpPanelContent={this.loadHelpPanelContent.bind(this)}
            />
          }
        >
          <SpaceBetween size="l">
            <SingleS3ObjectDetailsTable
              singleS3Object={singleS3Object}
              isInProgress
            />
          </SpaceBetween>
        </ContentLayout>
      }
      contentType="table"
      tools={<ToolsContent />}
      toolsOpen={toolsOpen}
      onToolsChange={({ detail }) => setToolsOpen(detail.open)}
      stickyNotifications
    />
  );
};

export default SingleS3ObjectPage;

// Bittle Device Details Table - Configuration is in config.jsx
const SingleS3ObjectDetailsTable = ({
  singleS3Object,
  loadHelpPanelContent,
  isInProgress,
  setToolsOpen,
}) => {
  return (
    <Container
      header={
        <Header variant="h2">
          {/* Table Title */}
          Object Details
        </Header>
      }
    >
      <SingleS3ObjectDetailsTableConfig
        // Pass singleBittle data as prop
        singleS3Object={singleS3Object}
        isInProgress={isInProgress}
      />
      {/* <SingleS3ObjectTableConfig singleS3Object={singleS3Object} /> */}
      {/* Option 2 for commands layout */}
      {/* <BittleCommandsTableConfig2 /> */}
    </Container>
  );
};

export const Breadcrumbs = ({ singleS3Object }) => (
  <BreadcrumbGroup
    items={[
      {
        text: ' Sample Amplify App',
        href: '/dashboard',
      },
      {
        text: 'S3 Objects',
        href: '/s3-objects',
      },
      {
        text: `${singleS3Object.FileName}`,
        href: '#',
      },
    ]}
    expandAriaLabel="Show path"
    ariaLabel="Breadcrumbs"
  />
);

// Info pop out window seen when clicking 'info' or the i in a circle button on right side of page
export const ToolsContent = () => (
  <HelpPanel
    header={<h2>Device Details</h2>}
    footer={
      <>
        <h3>
          Learn more{' '}
          <span role="img" aria-label="Icon external Link">
            <Icon name="external" />
          </span>
        </h3>
        <ul>
          <li>
            <ExternalLinkItem
              href="https://ghgprotocol.org/Third-Party-Databases/IPCC-Emissions-Factor-Database"
              text="IPCC Emissions Factor Database"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/energy/"
              text="AWS Energy & Utilities"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://ghgprotocol.org/"
              text="GHG Protocol Guidance"
            />
          </li>
        </ul>
      </>
    }
  >
    <p>
      This page is a summary of your selected S3 Object and related information
      such as the Key, Region, File Size, Lifecycle Configuration, and more.
    </p>
  </HelpPanel>
);
