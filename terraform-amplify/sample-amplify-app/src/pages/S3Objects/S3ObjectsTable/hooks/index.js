/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable no-shadow */
import { useEffect, useState, useRef } from 'react';

export function useTCAJobs(params = {}) {
  const { pageSize, currentPageIndex: clientPageIndex } =
    params.pagination || {};
  const { sortingDescending, sortingColumn } = params.sorting || {};
  const { filteringText, filteringTokens, filteringOperation } =
    params.filtering || {};
  const [loading, setLoading] = useState(false);
  const [items, setItems] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [currentPageIndex, setCurrentPageIndex] = useState(clientPageIndex);
  const [pagesCount, setPagesCount] = useState(0);

  useEffect(() => {
    setCurrentPageIndex(clientPageIndex);
  }, [clientPageIndex]);

  useEffect(() => {
    setLoading(true);
    // eslint-disable-next-line no-shadow
    const params = {
      filteringText,
      filteringTokens,
      filteringOperation,
      pageSize,
      currentPageIndex,
      sortingDescending,
      ...(sortingColumn
        ? {
            sortingColumn: sortingColumn.sortingField,
          }
        : {}),
    };
    const callback = ({ items, pagesCount, currentPageIndex }) => {
      setLoading(false);
      setItems(items);
      setPagesCount(pagesCount);
      setCurrentPageIndex(currentPageIndex);
      if (totalCount === 0) {
        setTotalCount(
          pagesCount > 1 ? pageSize * (pagesCount - 1) : items.length
        );
      }
    };
    window.AwsUiFakeServer.fetchTCAJobs(params, callback);
  }, [
    pageSize,
    sortingDescending,
    sortingColumn,
    currentPageIndex,
    filteringText,
    filteringTokens,
    filteringOperation,
  ]);

  return {
    items,
    loading,
    totalCount,
    pagesCount,
    currentPageIndex,
  };
}

const asyncFetchFilteringOptions = (params) => {
  return new Promise((resolve, reject) => {
    try {
      window.AwsUiFakeServer.fetchTCAJobFilteringOptions(
        params,
        ({ filteringOptions, filteringProperties }) => {
          resolve({ filteringOptions, filteringProperties });
        }
      );
    } catch (e) {
      reject(e);
    }
  });
};

export function useTCAJobsPropertyFiltering(defaultFilteringProperties) {
  const request = useRef({ filteringText: '' });
  const [filteringOptions, setFilteringOptions] = useState([]);
  const [filteringProperties, setFilteringProperties] = useState(
    defaultFilteringProperties
  );
  const [status, setStatus] = useState('pending');
  const fetchData = async (filteringText, filteringProperty) => {
    try {
      const { filteringOptions, filteringProperties } =
        await asyncFetchFilteringOptions({
          filteringText,
          filteringPropertyKey: filteringProperty
            ? filteringProperty.propertyKey
            : undefined,
        });
      if (
        !request.current ||
        request.current.filteringText !== filteringText ||
        request.current.filteringProperty !== filteringProperty
      ) {
        // there is another request in progress, discard the result of this one
        return;
      }
      setFilteringOptions(filteringOptions);
      setFilteringProperties(filteringProperties);
      setStatus('finished');
    } catch (error) {
      setStatus('error');
    }
  };

  const handleLoadItems = ({
    detail: { filteringProperty, filteringText, firstPage },
  }) => {
    setStatus('loading');
    if (firstPage) {
      setFilteringOptions([]);
    }
    request.current = {
      filteringProperty,
      filteringText,
    };
    fetchData(filteringText, filteringProperty);
  };

  useEffect(() => {
    fetchData('');
  }, []);

  return {
    status,
    filteringOptions,
    filteringProperties,
    handleLoadItems,
  };
}
