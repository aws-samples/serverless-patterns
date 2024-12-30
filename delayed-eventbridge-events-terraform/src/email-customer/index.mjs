export const handler = async (event) => {
  
    // Received EventBridge Scheduler schedule event
    console.log('Received event:', JSON.stringify(event, null, 2));
    
  
    /**
    * Example of a consumer for the UserCreated24HoursAgo event, if you wanted to email them you could put your email code here
    */
  
    console.log('Email the customer 24 hours ago after they were created.')
  };