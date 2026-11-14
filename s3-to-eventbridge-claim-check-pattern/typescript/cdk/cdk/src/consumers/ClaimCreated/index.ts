/**
 * Lambda triggered when the claim has been created
 */
export async function handler(event: any) {
  console.log('ClaimCreated', JSON.stringify(event, null, 4));
}
