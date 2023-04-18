import React from 'react';
import { useId } from '../useId';

export function useDisclaimerFlashbarItem(onDismiss) {
  const id = useId();

  return {
    type: 'info',
    dismissible: true,
    dismissLabel: 'Dismiss message',
    onDismiss: () => onDismiss(id),
    content: (
      <>
        This demo is an example of Cloudscape Design System patterns and
        components, and may not reflect the current patterns and components of
        AWS services. Created by Kevon Mayers.
      </>
    ),
    id,
  };
}
