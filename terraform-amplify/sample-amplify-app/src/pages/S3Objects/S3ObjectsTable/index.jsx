/* eslint-disable react/jsx-props-no-spreading */
/* eslint-disable no-console */
/* eslint-disable no-use-before-define */
/* eslint-disable react/prop-types */
/* eslint-disable import/no-cycle */
/* eslint-disable no-unused-vars */
/** **********************************************************************
                            DISCLAIMER

This is just a playground package. It does not comply with best practices
of using Cloudscape Design components. For production code, follow the
integration guidelines:

https://cloudscape.design/patterns/patterns/overview/
*********************************************************************** */

import React, { useState, useEffect } from 'react';
import { useCollection } from '@cloudscape-design/collection-hooks';
import {
  PropertyFilter,
  Pagination,
  Table,
} from '@cloudscape-design/components';

import { API, graphqlOperation } from 'aws-amplify';
import { listObjects, getObject } from '../../../graphql/queries';

import { getFilterCounterText } from '../../../common/resources/tableCounterStrings';
import { FullPageHeader, S3ObjectsTableEmptyState } from '..';
import {
  CustomAppLayout,
  Navigation,
  TableNoMatchState,
  Notifications,
} from '../../../common/common-components-config';
import { paginationLabels, transcriptSelectionLabels } from '../labels';
import {
  FILTERING_PROPERTIES,
  PROPERTY_FILTERING_I18N_CONSTANTS,
  DEFAULT_PREFERENCES,
  Preferences,
} from './table-property-filter-config';

import '../../../common/styles/base.scss';
import { useLocalStorage } from '../../../common/resources/localStorage';

import { useTCAJobs, useTCAJobsPropertyFiltering } from './hooks';

const TCAJobsTable = ({ updateTools, saveWidths, columnDefinitions }) => {
  // Below are variables declared to maintain the table's state.
  // Each declaration returns two values: the first value is the current state, and the second value is the function that updates it.
  // They use the general format: [x, setX] = useState(defaultX), where x is the attribute you want to keep track of.
  // For more info about state variables and hooks, see https://reactjs.org/docs/hooks-state.html.

  const [s3Objects, setS3Objects] = useState([]);
  // const [selectedTranscripts, setSelectedTranscripts] = useState([]);

  // const [distributions, setDistributions] = useState([]);
  const [preferences, setPreferences] = useLocalStorage(
    'React-TCAJobsTable-Preferences',
    DEFAULT_PREFERENCES
  );
  // const [preferences, setPreferences] = useState(DEFAULT_PREFERENCES);
  const [loading, setLoading] = useState(true);

  // a utility to handle operations on the data set (such as filtering, sorting and pagination)
  const {
    items,
    actions,
    filteredItemsCount,
    collectionProps,
    paginationProps,
    propertyFilterProps,
  } = useCollection(s3Objects, {
    propertyFiltering: {
      filteringProperties: FILTERING_PROPERTIES,
      empty: <S3ObjectsTableEmptyState resourceName="S3 Object" />,
      noMatch: (
        <TableNoMatchState
          onClearFilter={() => {
            actions.setPropertyFiltering({ tokens: [], operation: 'and' });
          }}
        />
      ),
    },
    pagination: { pageSize: preferences.pageSize },
    sorting: { defaultState: { sortingColumn: columnDefinitions[0] } },
    selection: {},
  });

  useEffect(() => {
    fetchS3Objects();
  }, []);

  const fetchS3Objects = async () => {
    try {
      const s3ObjectData = await API.graphql(
        graphqlOperation(listObjects, { limit: 10000 })
      );
      const s3ObjectsDataList = s3ObjectData.data.listObjects.items;
      console.log('S3 Object List', s3ObjectsDataList);
      setS3Objects(s3ObjectsDataList);
      setLoading(false);
    } catch (error) {
      console.log('error on fetching s3 objects', error);
    }
  };

  return (
    <Table
      {...collectionProps}
      items={items}
      columnDefinitions={columnDefinitions}
      visibleColumns={preferences.visibleContent}
      ariaLabels={transcriptSelectionLabels}
      selectionType="multi"
      variant="full-page"
      stickyHeader
      resizableColumns
      wrapLines={preferences.wrapLines}
      onColumnWidthsChange={saveWidths}
      header={
        <FullPageHeader
          selectedItems={collectionProps.selectedItems}
          totalItems={s3Objects}
          updateTools={updateTools}
          serverSide={false}
        />
      }
      loading={loading}
      loadingText="Loading S3 Objects..."
      filter={
        <PropertyFilter
          i18nStrings={PROPERTY_FILTERING_I18N_CONSTANTS}
          {...propertyFilterProps}
          countText={getFilterCounterText(filteredItemsCount)}
          expandToViewport
        />
      }
      pagination={
        <Pagination {...paginationProps} ariaLabels={paginationLabels} />
      }
      preferences={
        <Preferences
          preferences={preferences}
          setPreferences={setPreferences}
        />
      }
    />
  );
};

export default TCAJobsTable;
