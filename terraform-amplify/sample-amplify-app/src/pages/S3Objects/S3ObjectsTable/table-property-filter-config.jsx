/* eslint-disable no-sequences */
/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable react/prop-types */
import React from 'react';
import {
  CollectionPreferences,
  // StatusIndicator,
  Link,
} from '@cloudscape-design/components';
import { addColumnSortLabels } from '../labels';

export const COLUMN_DEFINITIONS = addColumnSortLabels([
  {
    id: 'FileName',
    header: 'File Name',
    // cell: (item) => <Link>{item.ObjectId}</Link>,
    cell: (item) => (
      <Link href={`/s3-objects/${item.ObjectId}`}>{item.FileName}</Link>
    ),
    minWidth: 200,
    sortingField: 'FileName',
  },
  {
    id: 'ObjectId',
    header: 'Object Id',
    // cell: (item) => <Link>{item.ObjectId}</Link>,
    cell: (item) => item.ObjectId,
    minWidth: 200,
    sortingField: 'ObjectId',
  },
  {
    id: 'AccountId',
    cell: (item) => item.AccountId,
    header: 'Account ID',
    minWidth: 120,
    maxWidth: 200,
    sortingField: 'AccountId',
  },
  {
    id: 'CurrentBucket',
    header: 'Current Bucket',
    cell: (item) => item.CurrentBucket,
    minWidth: 160,
    maxWidth: 200,
    sortingField: ' CurrentBucket',
  },
  {
    id: 'DetailType',
    header: 'Detail Type',
    cell: (item) => item.DetailType,
    minWidth: 100,
    maxWidth: 100,
    sortingField: 'DetailType',
  },

  {
    id: 'LifecycleConfig',
    header: 'Lifecycle Config',
    cell: (item) => item.LifecycleConfig,
    minWidth: 100,
    sortingField: 'LifecycleConfig',
  },
  {
    id: 'ObjectSize',
    header: 'Object Size (Bytes)',
    cell: (item) => item.ObjectSize,
    minWidth: 100,
    sortingField: 'ObjectSize',
  },
  {
    id: 'OriginalBucket',
    header: 'Original Bucket',
    cell: (item) => item.OriginalBucket,
    minWidth: 100,
    sortingField: 'OriginalBucket',
  },
  {
    id: 'Region',
    header: 'Region',
    cell: (item) => item.Region,
    minWidth: 100,
    sortingField: 'Region',
  },
  {
    id: 'SourceIPAddress',
    header: 'Source IP Address',
    cell: (item) => item.SourceIPAddress,
    minWidth: 100,
    sortingField: 'SourceIPAddress',
  },
  {
    id: 'CreatedAt',
    header: 'Created At',
    cell: (item) => item.CreatedAt,
    minWidth: 100,
    sortingField: 'CreatedAt',
  },
  // {
  //   id: 'CompletedAt',
  //   header: 'Completed At',
  //   cell: (item) => item.CompletedAt,
  //   minWidth: 100,
  //   sortingField: 'CompletedAt',
  // },
  {
    id: 'FilePath',
    header: 'File Path',
    cell: (item) => item.FilePath,
    minWidth: 100,
    sortingField: 'FilePath',
  },
  // {
  //   id: 'SampleRate',
  //   header: 'Sample Rate',
  //   cell: (item) => item.SampleRate,
  //   minWidth: 100,
  //   sortingField: 'SampleRate',
  // },
  // {
  //   id: 'MediaFormat',
  //   header: 'Media Format',
  //   cell: (item) => item.MediaFormat,
  //   minWidth: 100,
  //   sortingField: 'MediaFormat',
  // },
  // This eventually could be used for error handling
  // Could maybe have State of 'Verified', 'Unverified', 'Failed', etc. to give more info
  // {
  //   id: 'JobStatus',
  //   header: 'Job Status',
  //   //  cell: item => item.JobStatus,
  //   cell: (item) => (
  //     item.JobStatus,
  //     (
  //       <StatusIndicator type={item.state === 'Disabled' ? 'error' : 'success'}>
  //         {' '}
  //         {item.state}
  //         {item.JobStatus}
  //       </StatusIndicator>
  //     )
  //   ),
  //   minWidth: 100,
  //   sortingField: 'JobStatus',
  // },
]);

export const PAGE_SIZE_OPTIONS = [
  { value: 10, label: '10 Objects' },
  { value: 30, label: '30 Objects' },
  { value: 50, label: '50 Objects' },
];

export const FILTERING_PROPERTIES = [
  {
    propertyLabel: 'File Name',
    key: 'FileName',
    groupValuesLabel: 'File Name values',
    operators: [':', '!:', '=', '!='],
  },
  {
    propertyLabel: 'Object Id',
    key: 'ObjectId',
    groupValuesLabel: 'Object Id values',
    operators: [':', '!:', '=', '!='],
  },
  {
    propertyLabel: 'Account ID',
    key: 'AccountId',
    groupValuesLabel: 'Account ID values',
    operators: [':', '!:', '=', '!='],
  },
  {
    propertyLabel: 'DetailType',
    key: 'DetailType',
    groupValuesLabel: 'DetailType values',
    operators: [':', '!:', '=', '!='],
  },
  // {
  //   propertyLabel: 'Job Status',
  //   key: 'JobStatus',
  //   groupValuesLabel: 'Job Status values',
  //   operators: [':', '!:', '=', '!='],
  // },
  {
    propertyLabel: 'Source IP Address',
    key: 'SourceIPAddress',
    groupValuesLabel: 'Source IP Address values',
    operators: [':', '!:', '=', '!='],
  },
  // {
  //   propertyLabel: 'Media Format',
  //   key: 'MediaFormat',
  //   groupValuesLabel: 'Media Format values',
  //   operators: [':', '!:', '=', '!='],
  // },
  // {
  //   propertyLabel: 'Sample Rate',
  //   key: 'SampleRate',
  //   groupValuesLabel: 'Sample Rate values',
  //   operators: [':', '!:', '=', '!='],
  // },
];

export const PROPERTY_FILTERING_I18N_CONSTANTS = {
  filteringAriaLabel: 'your choice',
  dismissAriaLabel: 'Dismiss',

  filteringPlaceholder: 'Search',
  groupValuesText: 'Values',
  groupPropertiesText: 'Properties',
  operatorsText: 'Operators',

  operationAndText: 'and',
  operationOrText: 'or',

  operatorLessText: 'Less than',
  operatorLessOrEqualText: 'Less than or equal',
  operatorGreaterText: 'Greater than',
  operatorGreaterOrEqualText: 'Greater than or equal',
  operatorContainsText: 'Contains',
  operatorDoesNotContainText: 'Does not contain',
  operatorEqualsText: 'Equals',
  operatorDoesNotEqualText: 'Does not equal',

  editTokenHeader: 'Edit filter',
  propertyText: 'Property',
  operatorText: 'Operator',
  valueText: 'Value',
  cancelActionText: 'Cancel',
  applyActionText: 'Apply',
  allPropertiesLabel: 'All properties',

  tokenLimitShowMore: 'Show more',
  tokenLimitShowFewer: 'Show fewer',
  clearFiltersText: 'Clear filters',
  removeTokenButtonAriaLabel: () => 'Remove token',
  enteredTextLabel: (text) => `Use: "${text}"`,
};
export const CUSTOM_PREFERENCE_OPTIONS = [
  { value: 'table', label: 'Table' },
  { value: 'cards', label: 'Cards' },
];
export const DEFAULT_PREFERENCES = {
  pageSize: 30,
  visibleContent: [
    'FileName',
    'ObjectId',
    'AccountId',
    'CurrentBucket',
    'DetailType',
    'LifecycleConfig',
    'ObjectSize',
    'CreatedAt',
    'CompletedAt',
    'FilePath',
    'JobStatus',
    'OriginalBucket',
    'Region',
    'SourceIPAddress',
    'SampleRate',
    'MediaFormat',
  ],
  wraplines: false,
  custom: CUSTOM_PREFERENCE_OPTIONS[0].value,
};

export const VISIBLE_CONTENT_OPTIONS = [
  {
    label: 'Main S3 Object properties',
    options: [
      { id: 'FileName', label: 'File Name', editable: false },
      { id: 'ObjectId', label: 'Object Id', editable: true },
      { id: 'AccountId', label: 'Account ID', editable: true },
      { id: 'CurrentBucket', label: 'Current Bucket', editable: true },
      { id: 'DetailType', label: 'DetailType', editable: true },
      { id: 'LifecycleConfig', label: 'Lifecycle Config', editable: true },
      {
        id: 'ObjectSize',
        label: 'Object Size',
        editable: true,
      },
      { id: 'CreatedAt', label: 'Created At', editable: true },
      // { id: 'UpdatedAt', label: 'Updated At', editable: true },
      // { id: 'FilePath', label: 'File Path', editable: true },
      // { id: 'JobStatus', label: 'Job Status', editable: false },
      { id: 'OriginalBucket', label: 'Original Bucket', editable: true },
      { id: 'Region', label: 'Region', editable: true },
      { id: 'SourceIPAddress', label: 'SourceIPAddress', editable: true },
      // { id: 'MediaFormat', label: 'Media Format', editable: true },
      // { id: 'SampleRate', label: 'Sample Rate', editable: true },
    ],
  },
];
export const Preferences = ({
  preferences,
  setPreferences,
  disabled,
  pageSizeOptions = PAGE_SIZE_OPTIONS,
  visibleContentOptions = VISIBLE_CONTENT_OPTIONS,
}) => (
  <CollectionPreferences
    title="Preferences"
    confirmLabel="Confirm"
    cancelLabel="Cancel"
    disabled={disabled}
    preferences={preferences}
    onConfirm={({ detail }) => setPreferences(detail)}
    pageSizePreference={{
      title: 'Page size',
      options: pageSizeOptions,
    }}
    wrapLinesPreference={{
      label: 'Wrap lines',
      description: 'Check to see all the text and wrap the lines',
    }}
    visibleContentPreference={{
      title: 'Select visible columns',
      options: visibleContentOptions,
    }}
  />
);
