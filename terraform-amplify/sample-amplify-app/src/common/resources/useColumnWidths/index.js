import { useMemo } from 'react';
import {
  addToColumnDefinitions,
  mapWithColumnDefinitionIds,
} from '../columnDefinitionsHelper';
import { useLocalStorage } from '../localStorage';

export function useColumnWidths(storageKey, columnDefinitions) {
  const [widths, saveWidths] = useLocalStorage(storageKey);

  function handleWidthChange(event) {
    saveWidths(
      mapWithColumnDefinitionIds(
        columnDefinitions,
        'width',
        event.detail.widths
      )
    );
  }
  const memoDefinitions = useMemo(() => {
    return addToColumnDefinitions(columnDefinitions, 'width', widths);
  }, [widths, columnDefinitions]);

  return [memoDefinitions, handleWidthChange];
}
