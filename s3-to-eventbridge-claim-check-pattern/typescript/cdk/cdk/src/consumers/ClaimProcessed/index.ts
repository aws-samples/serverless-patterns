/**
 * Lambda triggered when the claim has been processed
 */
export async function handler(event: any) {
  console.log('ClaimProcessed', JSON.stringify(event, null, 4));
}
