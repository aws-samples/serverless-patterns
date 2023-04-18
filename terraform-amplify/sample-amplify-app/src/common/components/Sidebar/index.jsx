import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { SideNavigation, Badge } from '@cloudscape-design/components';

const Sidebar = () => {
  const navigate = useNavigate();
  const location = useLocation();
  // const [activeHref, setActiveHref] = useState('/');
  return (
    <SideNavigation
      // TODO - Make active link work for navigation
      // activeHref={activeHref}
      activeHref={location.pathname}
      header={{ text: 'Sample Amplify App', href: '/' }}
      onFollow={(event) => {
        if (!event.detail.external) {
          event.preventDefault();
          // setActiveHref(event.detail.href);
          navigate(event.detail.href);
        }
      }}
      items={[
        // { type: "link", text: "Dashboard", href: "/" },
        // {
        //   type: 'section',
        //   text: 'Main',
        //   expanded: true,
        //   items: [
        //     { type: 'link', text: 'Dashboard', href: '/dashboard' },
        //     // { type: 'link', text: 'Setup Guide', href: '/setup-guide' },
        //     // { type: 'link', text: 'Case Studies', href: '/case-studies' },
        //   ],
        // },
        {
          type: 'section',
          text: 'Getting Started',
          expanded: true,
          items: [
            { type: 'link', text: 'Getting Started', href: '/getting-started' },
            // { type: 'link', text: 'Setup Guide', href: '/setup-guide' },
            // { type: 'link', text: 'Case Studies', href: '/case-studies' },
          ],
        },
        {
          type: 'link',
          text: 'Dashboard',
          href: '/dashboard',
        },
        {
          type: 'section',
          text: 'Admin',
          expanded: true,
          items: [
            {
              type: 'link',
              text: 'Users',
              href: 'https://us-east-1.console.aws.amazon.com/cognito/v2/home?region=us-east-1',
              external: true,
            },
            {
              type: 'link',
              text: 'Groups',
              href: 'https://us-east-1.console.aws.amazon.com/cognito/v2/home?region=us-east-1',
              external: true,
            },
            {
              type: 'link',
              text: 'Edit App',
              href: 'https://us-east-1.console.aws.amazon.com/amplify/home?region=us-east-1',
              external: true,
            },
          ],
        },
        {
          type: 'section',
          text: 'Data Explorer',
          expanded: true,
          items: [
            { type: 'link', text: 'S3 Objects', href: '/s3-objects' },
            { type: 'link', text: 'Data Uploader', href: '/data-uploader' },
            // {
            //   type: 'link',
            //   text: 'CLM Uploader',
            //   href: '/custom-language-model-uploader',
            // },
            // {
            //   type: 'link',
            //   text: 'CV Uploader',
            //   href: '/custom-vocabulary-uploader',
            // },
          ],
        },
        // Example of notifications in sidebar, uncomment this if not needed
        {
          type: 'link',
          text: 'Notifications',
          href: '#/notifications',
          info: <Badge color="red">8</Badge>,
        },
        {
          type: 'link',
          text: 'Documentation',
          // TODO - Link to public GitHub repo Amplify App Documentation
          // href: "https://example.com",
          external: true,
        },
      ]}
    />
  );
};

export default Sidebar;
