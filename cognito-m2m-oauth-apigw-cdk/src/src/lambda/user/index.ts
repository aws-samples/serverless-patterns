export const handler = async (event: any) => {
  console.log("event", event);
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: "Permission granted you can access this resource",
    }),
  };
};

export default handler;
