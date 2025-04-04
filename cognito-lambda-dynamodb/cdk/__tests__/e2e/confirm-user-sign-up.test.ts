import * as given from "../steps/given";
import * as then from "../steps/then";
import * as when from "../steps/when";

describe("When a user Signs up ", () => {
  it("Users profile should be saved in DynamoDB", async () => {
    const { password, given_name, family_name, email } = given.a_random_user();
    console.log("name: ", given_name, family_name);
    const userSub = await when.a_user_signs_up(
      password,
      email,
      given_name,
      family_name
    );

    console.log("user: ", userSub);
    const ddbUser = await then.user_exists_in_UsersTable(userSub);

    console.log("ddbUser: ", ddbUser);

    expect(ddbUser.UserID).toMatch(userSub);
  });
});
