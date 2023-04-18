/* eslint-disable import/prefer-default-export */
import { useState } from 'react';
import { useId } from '../useId';
import { useDisclaimerFlashbarItem } from '../disclaimerFlashbarItem';

export function useNotifications(successNotification) {
  const successId = useId();
  const [successDismissed, dismissSuccess] = useState(false);
  const [disclaimerDismissed, dismissDisclaimer] = useState(false);

  const disclaimerItem = useDisclaimerFlashbarItem(() =>
    dismissDisclaimer(true)
  );

  const notifications = [];

  if (disclaimerItem && !disclaimerDismissed) {
    notifications.push(disclaimerItem);
  }

  if (successNotification && !successDismissed) {
    notifications.push({
      type: 'success',
      content: 'Resource created successfully',
      dismissLabel: 'Dismiss message',
      dismissible: true,
      onDismiss: () => dismissSuccess(true),
      id: successId,
    });
  }

  return notifications;
}
