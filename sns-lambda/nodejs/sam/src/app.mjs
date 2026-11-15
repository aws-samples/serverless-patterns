// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
export const handler = async (event, context) => {
    for (const record of event.Records) {
      await processMessageAsync(record);
    }
    console.info("done");
  };
  
  async function processMessageAsync(record) {
    try {
      const message = JSON.stringify(record.Sns.Message);
      console.log(`Processed message ${message}`);
      await Promise.resolve(1); //Placeholder for actual async work
    } catch (err) {
      console.error("An error occurred");
      throw err;
    }
  }
  
  