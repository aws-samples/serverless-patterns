export const resourcesBreadcrumbs = [
  {
    text: 'Sample Amplify App',
    href: '/',
  },
  {
    text: 'S3 Objects',
    href: '/s3-objects',
  },
];

export const resourceDetailBreadcrumbs = [
  ...resourcesBreadcrumbs,
  {
    text: 'MyFavoriteTomato123456',
    href: '#',
  },
];

export const resourceManageTagsBreadcrumbs = [
  ...resourceDetailBreadcrumbs,
  {
    text: 'Manage tags',
    href: '#',
  },
];

export const resourceEditBreadcrumbs = [
  ...resourceDetailBreadcrumbs,
  {
    text: 'Edit',
    href: '#',
  },
];

export const resourceCreateBreadcrumbs = [
  ...resourcesBreadcrumbs,
  {
    text: 'Upload File',
    href: '#',
  },
];

export const readFromS3Breadcrumbs = [
  ...resourceDetailBreadcrumbs,
  {
    text: 'Run simulation',
    href: '#',
  },
];

export const writeToS3Breadcrumbs = [
  ...resourceDetailBreadcrumbs,
  {
    text: 'Create simulation',
    href: '#',
  },
];
