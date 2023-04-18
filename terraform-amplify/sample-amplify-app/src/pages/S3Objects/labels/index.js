export const appLayoutLabels = {
  navigation: 'Side navigation',
  navigationToggle: 'Open side navigation',
  navigationClose: 'Close side navigation',
  notifications: 'Notifications',
  tools: 'Help panel',
  toolsToggle: 'Open help panel',
  toolsClose: 'Close help panel',
};

export const paginationLabels = {
  nextPageLabel: 'Next page',
  previousPageLabel: 'Previous page',
  pageLabel: (pageNumber) => `Page ${pageNumber} of all pages`,
};

export const externalLinkProps = {
  external: true,
  externalIconAriaLabel: 'Opens in a new tab',
};

export const transcriptSelectionLabels = {
  itemSelectionLabel: (data, row) => `select ${row.id}`,
  allItemsSelectionLabel: () => 'select all',
  selectionGroupLabel: 'Distribution selection',
};

export const originsSelectionLabels = {
  itemSelectionLabel: (data, row) => `select ${row.name}`,
  allItemsSelectionLabel: () => 'select all',
  selectionGroupLabel: 'Origins selection',
};

export const behaviorsSelectionLabels = {
  itemSelectionLabel: (data, row) =>
    `select path ${row.pathPattern} from origin ${row.origin}`,
  allItemsSelectionLabel: () => 'select all',
  selectionGroupLabel: 'Behaviors selection',
};

export const logsSelectionLabels = {
  itemSelectionLabel: (data, row) => `select ${row.name}`,
  allItemsSelectionLabel: () => 'select all',
  selectionGroupLabel: 'Logs selection',
};

const headerLabel = (title, sorted, descending) => {
  return `${title}, ${
    sorted ? `sorted ${descending ? 'descending' : 'ascending'}` : 'not sorted'
  }.`;
};

export const addColumnSortLabels = (columns) =>
  columns.map((col) => ({
    ariaLabel:
      col.sortingField || col.sortingComparator
        ? (sortState) =>
            headerLabel(col.header, sortState.sorted, sortState.descending)
        : undefined,
    ...col,
  }));
