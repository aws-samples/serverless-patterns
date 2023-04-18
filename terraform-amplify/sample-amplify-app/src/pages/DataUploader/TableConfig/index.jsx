// import React from 'react';
// import { Link, StatusIndicator } from '@cloudscape-design/components';

// ** Labels for the columns in the table **
// id - used for showing/hiding columns. Should match sortingField
// header - the label for the column
// cell - where you pass in the data fetched from the api. Format is item.JSON_LABEL
// minWidth - minimum width of the column
// sortingField - used for sorting the table when clicking on column name. Should match id
export const COLUMN_DEFINITIONS = [
  {
    id: 'name',
    header: 'Name',
    cell: (item) => item.name,
    minWidth: '180px',
    sortingField: 'name',
  },
  {
    id: 'type',
    cell: (item) => item.type,
    header: 'Type',
    minWidth: '160px',
    sortingField: 'type',
  },
  {
    id: 'size',
    header: 'Size',
    cell: (item) => item.size,
    minWidth: '100px',
    maxWidth: '200px',
    sortingField: ' size',
  },
];

// ** Selector options visible when clicking gear icon in table. Used to show/hide columns **
//  id - corresponding id defined in colum definitions above
// label - corresponding label defined in column definitions above
// editable - bool for if the toggle is selectable or not (greyed out when set to false)
export const CONTENT_SELECTOR_OPTIONS = [
  {
    label: 'Main emission properties',
    options: [
      { id: 'name', label: 'Name', editable: false },
      { id: 'type', label: 'Type', editable: true },
      { id: 'size', label: 'Size', editable: true },
    ],
  },
];

// ** Page selector options for how many rows to see on each page **
// value - how many rows
// label - label for the corresponding value
export const PAGE_SELECTOR_OPTIONS = [
  { value: 10, label: '10 Files' },
  { value: 30, label: '30 Files' },
  { value: 50, label: '50 Files' },
  { value: 100, label: '100 Files' },
];

// Custom options for how to view the table (cards or table)
export const CUSTOM_PREFERENCE_OPTIONS = [
  { value: 'table', label: 'Table' },
  { value: 'cards', label: 'Cards' },
];

// ** Default preferences for table **
// pageSize - how many rows on each page
// visibleContent - which rows are visible on component render (page load)
export const DEFAULT_PREFERENCES = {
  pageSize: 30,
  visibleContent: ['name', 'type', 'size'],
  wraplines: false,
  custom: CUSTOM_PREFERENCE_OPTIONS[0].value,
};
