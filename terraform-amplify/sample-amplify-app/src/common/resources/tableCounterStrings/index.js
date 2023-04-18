/* eslint-disable default-param-last */
export const getHeaderCounterText = (items = [], selectedItems = []) => {
  return selectedItems && selectedItems.length > 0
    ? `(${selectedItems.length}/${items.length})`
    : `(${items.length})`;
};

export const getServerHeaderCounterText = (totalCount, selectedItems) => {
  return selectedItems && selectedItems.length > 0
    ? `(${selectedItems.length}/${totalCount}+)`
    : `(${totalCount}+)`;
};

export const getServerFilterCounterText = (
  items = [],
  pagesCount,
  pageSize
) => {
  const count =
    pagesCount > 1 ? `${pageSize * (pagesCount - 1)}+` : `${items.length}`;
  return count === '1' ? `1 match` : `${count} matches`;
};

export const getFilterCounterText = (count) =>
  `${count} ${count === 1 ? 'match' : 'matches'}`;
