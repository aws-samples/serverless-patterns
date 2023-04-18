/* eslint-disable import/no-extraneous-dependencies */
import { useMemo } from 'react';
import { v4 as uuid4 } from 'uuid';

export const useId = () => useMemo(() => uuid4(), []);
