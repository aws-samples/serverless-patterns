/* eslint-disable react/no-unescaped-entities */
/** **********************************************************************
                            DISCLAIMER

This is just a playground package. It does not comply with best practices
of using Cloudscape Design components. For production code, follow the
integration guidelines:

https://cloudscape.design/patterns/patterns/overview/
*********************************************************************** */

import React from 'react';

import {
  AppLayout,
  Container,
  Header,
  HelpPanel,
  Grid,
  Box,
  TextContent,
  SpaceBetween,
  Icon,
} from '@cloudscape-design/components';
import Sidebar from '../../common/components/Sidebar';

import { ExternalLinkItem } from '../../common/common-components-config';

import '../../common/styles/intro.scss';
import '../../common/styles/servicehomepage.scss';

// Import images
import awsLogo from '../../public/images/AWS_logo_RGB_REV.png';
import iacBasicArch from '../../../../resources/architecture/IAC_SAMPLE_ARCH.png';
import iacAdvancedArch from '../../../../resources/architecture/IAC_ADVANCED_ARCH.png';

const GettingStarted = () => {
  return (
    <AppLayout
      navigation={<Sidebar activeHref="#/" />}
      // navigation={<Sidebar activeHref="#/" items={navItems}/>}
      content={<Content />}
      tools={<ToolsContent />}
      headerSelector="#h"
      disableContentPaddings
      // toolsHide={true}
    />
  );
};

export default GettingStarted;

const Content = () => {
  return (
    <div>
      <TextContent>
        <div>
          <Grid className="custom-home__header" disableGutters>
            <Box margin="xxl" padding={{ vertical: 'xl', horizontal: 'l' }}>
              <Box margin={{ bottom: 's' }} />
              <img
                src={awsLogo}
                alt=""
                style={{ maxWidth: '20%', paddingRight: '2em' }}
              />
              <div className="custom-home__header-title">
                <Box fontSize="display-l" fontWeight="bold" color="inherit">
                  AWS Amplify
                </Box>
                <Box
                  fontSize="display-l"
                  padding={{ bottom: 's' }}
                  fontWeight="light"
                  color="inherit"
                >
                  Automated Deployment of AWS Amplify Apps with IaC.
                </Box>
                <Box fontWeight="light">
                  <span className="custom-home__header-sub-title">
                    This project serves as an example of how you can automate
                    deployment of AWS Amplify Applications with IaC
                    (Infrastructure as Code).
                    {/* Click <Link to={{ pathname: "/about-carbonlake"}}  target="_blank">here</Link> to learn more. */}
                    <br />
                    <br />
                    Click{' '}
                    <a
                      target="_blank"
                      rel="noopener noreferrer"
                      href="https://aws.amazon.com/amplify/"
                    >
                      here
                    </a>{' '}
                    to learn more.
                    {/* TODO - Replace this link with blog post link */}
                  </span>
                </Box>
              </div>
            </Box>
          </Grid>
        </div>

        {/* Start 'This project is buit' section */}
        <Box margin="xxl" padding="l">
          <SpaceBetween size="l">
            <div>
              <h1>Getting Started</h1>
              <Container>
                <div>
                  <p>
                    This project is built with the React framework and AWS
                    Amplify, leveraging public{' '}
                    <a
                      target="_blank"
                      rel="noopener noreferrer"
                      href="https://cloudscape.design/"
                    >
                      Cloudscape Design Components
                    </a>
                    .
                    <br />
                    <br />
                    This project provides the following:
                  </p>
                  <li>Secure Data Storage</li>
                  <li>Authentication, Authorization, and Auditing</li>
                  <li>Sample Amplify Application</li>
                  <li>Sample GraphQL API</li>
                  <p>
                    Data is ingested through the Landing Bucket, and can be
                    ingested from any service within or connected to the AWS
                    cloud.
                    <br />
                  </p>
                </div>
              </Container>
            </div>
            <div>
              <h1>Architecture</h1>
              <Container header={<Header>Basic Architecture</Header>}>
                {/* Make this flex later. maxWidth is not mobile responsive */}
                <div>
                  <img
                    src={iacBasicArch}
                    alt=""
                    style={{ maxWidth: '100%', paddingRight: '2em' }}
                  />
                </div>
                <div>{/* <p>This is the basic architecture.</p> */}</div>
              </Container>
              <Container header={<Header>Detailed Architecture</Header>}>
                <div>
                  <img
                    src={iacAdvancedArch}
                    alt=""
                    style={{ maxWidth: '100%', paddingRight: '2em' }}
                  />
                </div>
                <div>{/* <p>This is the detailed architecture.</p> */}</div>
              </Container>
            </div>
          </SpaceBetween>
        </Box>
      </TextContent>
    </div>
  );
};

export const ToolsContent = () => (
  <HelpPanel
    header={<h2>Sample Amplify App</h2>}
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
              href="https://aws.amazon.com/energy/"
              text="AWS Energy & Utilities"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/amplify/"
              text="AWS Amplify"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/s3/"
              text="Amazon S3"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/step-functions/"
              text="AWS Step Functions"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://www.terraform.io/"
              text="Terraform"
            />
          </li>
          <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/cdk/"
              text="AWS CDK (Cloud Development Kit)"
            />
          </li>
        </ul>
      </>
      /* <li>
            <ExternalLinkItem
              href="https://aws.amazon.com/energy/"
              text="TBD - Amazon TCAQS Blog Post"
            />
          </li> */
    }
  >
    <p>
      This sample app is meant to serve as an example of an application you can
      build with AWS Amplify, while leveraging Infrastructure as Code. It is
      built leveraging the AWS Amplify Libraries for JavaScript. For more
      information, see
      <a
        target="_blank"
        rel="noopener noreferrer"
        href="https://docs.amplify.aws/lib/q/platform/js/"
      >
        {' '}
        AWS Amplify Libraries for JavaScript
      </a>
    </p>
  </HelpPanel>
);
