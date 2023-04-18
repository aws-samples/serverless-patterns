/* eslint-disable no-console */
// This is for testing only it is recommended to store this
// information in a database in production - most likely associated
// with a specific user so their app preference can be stored.
import { useState } from 'react';

export const save = (key, value) =>
  localStorage.setItem(key, JSON.stringify(value));

export const load = (key) => {
  const value = localStorage.getItem(key);
  try {
    return value && JSON.parse(value);
  } catch (e) {
    console.warn(
      `⚠️ The ${key} value that is stored in localStorage is incorrect. Try to remove the value ${key} from localStorage and reload the page`
    );
    return undefined;
  }
};

export const useLocalStorage = (key, defaultValue) => {
  const [value, setValue] = useState(() => load(key) ?? defaultValue);

  function handleValueChange(newValue) {
    setValue(newValue);
    save(key, newValue);
  }
  return [value, handleValueChange];
};
