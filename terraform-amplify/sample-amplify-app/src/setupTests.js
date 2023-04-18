/* eslint-disable import/no-extraneous-dependencies */
// The line above allows extraneous dependencies. These should be allowed
// for test files, but not files related to app functionality.
import matchers from '@testing-library/jest-dom/matchers';
import { expect } from 'vitest';

expect.extend(matchers);
