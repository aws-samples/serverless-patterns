export const resourcesBreadcrumbs = [
  {
    text: 'Service',
    href: '#',
  },
  {
    text: 'Distributions',
    href: '#',
  },
];

export const resourceDetailBreadcrumbs = [
  ...resourcesBreadcrumbs,
  {
    text: 'SLCCSMWOHOFUY0',
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
    text: 'Create distribution',
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
