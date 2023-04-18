/* eslint-disable react/jsx-props-no-spreading */
/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable react/destructuring-assignment */
/* eslint-disable react/prop-types */
import React from 'react';
import {
  Alert,
  AppLayout,
  Badge,
  Box,
  Button,
  Flashbar,
  Header,
  Icon,
  Link,
  SideNavigation,
  SpaceBetween,
} from '@cloudscape-design/components';
import { appLayoutLabels, externalLinkProps } from './resources/labels';
// eslint-disable-next-line prettier/prettier
import { getHeaderCounterText, getServerHeaderCounterText } from './resources/tableCounterStrings';
import { useNotifications } from './resources/useNotifications';
import TopNavigationHeader from './components/TopNavigationHeader';

export const navHeader = { text: 'Amazon TCA', href: '/' };
export const navItems = [
  // {
  //   type: 'section',
  //   text: 'Getting Started',
  //   items: [
  //     { type: 'link', text: 'TCA 101', href: '/sample-101' },
  //     { type: 'link', text: 'Setup Guide', href: '/setup-guide' },
  //     { type: 'link', text: 'Case Studies', href: '/case-studies' },
  //   ],
  // },
  // {
  //   type: 'section',
  //   text: 'Admin',
  //   expanded: true,
  //   items: [
  //     { type: 'link', text: 'Users', href: 'https://us-east-1.console.aws.amazon.com/cognito/v2/home?region=us-east-1', external: true},
  //     { type: 'link', text: 'Groups', href: 'https://us-east-1.console.aws.amazon.com/cognito/v2/home?region=us-east-1',  external: true },
  //     { type: 'link', text: 'Edit App', href: 'https://us-east-1.console.aws.amazon.com/amplify/home?region=us-east-1',  external: true },
  //   ]
  // },
  // {
  //   type: 'section',
  //   text: 'Data Explorer',
  //   expanded: true,
  //   items: [
  //     { type: 'link', text: 'Data Uploader', href: '/data-uploader' },
  //     { type: 'link', text: 'CLM Uploader', href: '/custom-language-model-uploader' },
  //     { type: 'link', text: 'CV Uploader', href: '/custom-vocabulary-uploader' },
  //     { type: 'link', text: 'TCA Jobs', href: '/sample-jobs' },
  //     // { type: 'link', text: 'Decarb Intelligence', href: '/decarb-intelligence' },
  //     // { type: 'link', text: 'Visualizations', href: '/visualizations' },
  //   ]
  // },
  // {
  //   type: 'section',
  //   text: 'Private content',
  //   items: [
  //     { type: 'link', text: 'How-to guide', href: '#/howto' },
  //     { type: 'link', text: 'Origin access identity', href: '#/origin' },
  //   ],
  // },
];

export const ec2NavHeader = { text: 'Service', href: '#/' };
export const ec2NavItems = [
  { type: 'link', text: 'Instances', href: '#/instances' },
  { type: 'link', text: 'Instance types', href: '#/instance-types' },
  { type: 'link', text: 'Launch templates', href: '#/launch-templates' },
  { type: 'link', text: 'Spot requests', href: '#/spot-requests' },
  { type: 'link', text: 'Saving plans', href: '#/saving-plans' },
  { type: 'link', text: 'Reserved instances', href: '#/reserved-instances' },
  { type: 'divider' },
  {
    type: 'link',
    text: (
      <>
        Notifications <Badge color="red">23</Badge>
      </>
    ),
    href: '#/notifications',
  },
  {
    type: 'link',
    text: (
      <>
        Documentation <Icon name="external" />
      </>
    ),
    href: '#/documentation',
  },
];

export const InfoLink = ({ id, onFollow, ariaLabel }) => (
  <Link variant="info" id={id} onFollow={onFollow} ariaLabel={ariaLabel}>
    Info
  </Link>
);

// a special case of external link, to be used within a link group, where all of them are external
// and we do not repeat the icon
export const ExternalLinkItem = ({ href, text }) => (
  <Link
    href={href}
    ariaLabel={`${text} ${externalLinkProps.externalIconAriaLabel}`}
    target="_blank"
  >
    {text}
  </Link>
);

export const TableNoMatchState = (props) => (
  <Box margin={{ vertical: 'xs' }} textAlign="center" color="inherit">
    <SpaceBetween size="xxs">
      <div>
        <b>No matches</b>
        <Box variant="p" color="inherit">
          We cannot find a match.
        </Box>
      </div>
      <Button onClick={props.onClearFilter}>Clear filter</Button>
    </SpaceBetween>
  </Box>
);

export const TableEmptyState = ({ resourceName }) => (
  <Box margin={{ vertical: 'xs' }} textAlign="center" color="inherit">
    <SpaceBetween size="xxs">
      <div>
        <b>No {resourceName.toLowerCase()}s</b>
        <Box variant="p" color="inherit">
          No {resourceName.toLowerCase()}s associated with this resource.
        </Box>
      </div>
      <Button>Create {resourceName.toLowerCase()}</Button>
    </SpaceBetween>
  </Box>
);

function getCounter(props) {
  if (props.counter) {
    return props.counter;
  }
  if (!props.totalItems) {
    return null;
  }
  if (props.serverSide) {
    return getServerHeaderCounterText(props.totalItems, props.selectedItems);
  }
  return getHeaderCounterText(props.totalItems, props.selectedItems);
}

export const TableHeader = (props) => {
  return (
    <Header
      variant={props.variant}
      counter={getCounter(props)}
      info={
        props.updateTools && (
          <InfoLink
            onFollow={props.updateTools}
            ariaLabel={`Information about ${props.title}.`}
          />
        )
      }
      description={props.description}
      actions={props.actionButtons}
    >
      {props.title}
    </Header>
  );
};

const defaultOnFollowHandler = (ev) => {
  // keep the locked href for our demo pages
  ev.preventDefault();
};

export function Navigation({
  activeHref,
  header = navHeader,
  items = navItems,
  onFollowHandler = defaultOnFollowHandler,
}) {
  return (
    <SideNavigation
      items={items}
      header={header}
      activeHref={activeHref}
      onFollow={onFollowHandler}
    />
  );
}

export function Notifications({ successNotification }) {
  const notifications = useNotifications(successNotification);
  return <Flashbar items={notifications} />;
}

export function DevSameOriginWarning() {
  const { hostname, protocol } = document.location;
  const amazonSubdomain =
    /.amazon.com$/.test(hostname) || /.a2z.com$/.test(hostname);
  const sameOrigin = protocol === 'https:' && amazonSubdomain;

  if (!sameOrigin) {
    return (
      <Alert
        header="You need to host this page in compliance with same-origin policy"
        type="error"
      >
        <span>
          The dashboard will not work properly unless the page is hosted:
          <ul>
            <li>over https</li>
            <li>on amazon.com or a2z.com subdomains</li>
          </ul>
          Use startHttps script{' '}
          <Box variant="code">sudo npm run startHttps</Box> from examples
          package to achieve this
        </span>
      </Alert>
    );
  }
  return null;
}

export function CustomAppLayout(props) {
  return (
    <>
      <TopNavigationHeader />
      <AppLayout
        {...props}
        ariaLabels={appLayoutLabels}
        onNavigationChange={(event) => {
          if (props.onNavigationChange) {
            props.onNavigationChange(event);
          }
        }}
        onToolsChange={(event) => {
          if (props.onToolsChange) {
            props.onToolsChange(event);
          }
        }}
      />
    </>
  );
}

export const CounterLink = ({ children }) => {
  return (
    <Link variant="awsui-value-large" href="#">
      {children}
    </Link>
  );
};
