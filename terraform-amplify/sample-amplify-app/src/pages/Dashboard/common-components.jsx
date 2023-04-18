import React from 'react';
import {
  // Alert,
  // AppLayout,
  // Badge,
  // Box,
  // Button,
  // Flashbar,
  // Header,
  // Icon,
  Link,
  // SideNavigation,
  // SpaceBetween,
} from '@cloudscape-design/components';

// eslint-disable-next-line react/prop-types
export const CounterLink = ({ children }) => {
  return (
    // eslint-disable-next-line jsx-a11y/anchor-is-valid
    <Link variant="awsui-value-large" href="/s3-objects">
      {children}
    </Link>
  );
};
