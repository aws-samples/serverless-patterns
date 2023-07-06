export function validatePromiseResponses(responses: PromiseSettledResult<any>[]) {
  const errors = responses.filter(
    (response: PromiseSettledResult<any>) => response.status === 'rejected' && response.reason.name !== 'ResourceConflictException'
  );
  if (errors.length === 0) {
    return;
  }
  const errorsMessages = errors.map((error) => {
    if (error.status === 'rejected') {
      return error?.reason.name;
    }
  });
  throw new Error(errorsMessages.join(','));
}
