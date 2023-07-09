type AppSyncEvent = {
  info: {
    fieldName: string;
  };
  arguments: {
    input: {
      username: string;
      email: string;
      profilePicUrl: string;
    };
  };
};

exports.handler = async (event: AppSyncEvent) => {
  console.log(JSON.stringify(event));
  return {
    id: "324987234",
    ...event.arguments.input,
  };
};
