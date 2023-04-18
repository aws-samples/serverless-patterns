<!-- TODO - Update screenshots that say TCA, add GitHub instructions -->
# Sample Amplify App Documentation
### Created by [Kevon Mayers](https://www.linkedin.com/in/kevonmayers)
![image info](/resources/app-screenshots/sample_amplify_app_dashboard.png)
## Introduction
This sample app is used to serve as a demonstration for what you can do with the sample project's core features. This code is meant to be used purely for development/demo purpose. For production workloads it is ***highly*** recommended that you do your own extensive internal testing before using.

This package sets up a React development environment that has access to all [Cloudscape](https://cloudscape.design/) React components. It comes with a sample application using Cloudscape to give a demo of what your own Amplify Application using this sample project could look like. See [Getting started with Cloudscape](https://cloudscape.design/get-started/guides/introduction/).

## React + ViteJS

This is a modern React Web Application leveraging [Cloudscape Design Components](https://cloudscape.design). [ViteJS](https://vitejs.dev/) an alternative to CRA (`create-react-app`) that is quite popular and has some substantial benefits.

## Installation

Follow the [DEPLOYMENT.md](/DEPLOYMENT.md) guide to deploy your infrastructure with Terraform.

## Getting started

* **Prereqs:**
    * [Node.js installed](http://nodejs.org): if you don't already have it, you run **`brew install node`** (on Mac) to download Node (Homebrew needs to be installed for this to work). For other operating systems, check relevant installation instructions. Run **`node -v `** to check your version.
    * [NPM installed](https://www.npmjs.com/) - Run **`npm -v`** to check your version.
    * [Terraform deployed](/DEPLOYMENT.md)
    * [IAM User or Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with necessary permissions created (role is recommended)
    * [AWS Amplify CLI installed](https://google.com)
        * Run `npm install -g @aws-amplify/cli`
        * Run  `amplify --version` to verify installed version

* **Helpful commands (NPM):**
    * **`npm install`** - downloads app dependencies
    * **`npm run dev`** — Runs the application on your `localhost`
    * **`npm run build`** — builds a minified project for production
    * **`npm run preview`** — builds a minified project for production and runs locally
    * **`npm run test`** — runs tests that you define in your test files
* **Helpful commands (AWS Amplify):**
    * **`amplify init`** - initialized a new Amplify project. Must run this from the root directory of the frontend app. *Only necessary when using the Amplify CLI to launch resource (beyond the scope of this workshop).*

    * **`amplify pull`** -  operates similar to a git pull, fetching upstream backend environment definition changes from the cloud* and update the local environment to match that definition. *Only necessary when using the Amplify CLI to launch resource (beyond the scope of this workshop).*

    * **`amplify console`** - launches the browser directing you to your cloud project in the AWS Amplify Console. *Only necessary when using the Amplify CLI to launch resource (beyond the scope of this workshop).*

* **Learn:**
    * source files are fully auto-generated and served by HTTP server.  Write your code in `src/` dir.
    * Place static files in `public/` or `src/assets` and import them. Learn more about [importing static assets in ViteJS here](https://vitejs.dev/guide/assets.html).
    * [Configuring Vite](https://vitejs.dev/config/).



## Setup Guide

**Security Notice:**
It is important to note that up to **9 IAM roles** and **1 IAM user** are created by Terraform. These roles in addition to the Cognito User Pool Groups determine what permissions your users can perform. You can add additional roles, user pool groups, and users to the groups either via the AWS Management Console, or with Terraform (or another IaC provider). During testing/development it can be fine to launch resources in the console, however for production workloads it is ***HIGHLY*** recommended to manage your resources via IaC (Infrastructure as Code).

#### IAM Roles
- `sample_amplify_codecommit` (conditional)
- `sample_appsync_dynamodb_restricted_access`
- `sample_cognito_admin_group_restricted_access`
- `sample_cognito_authrole_restricted_access`
- `sample_cognito_standard_group_restricted_access`
- `sample_cognito_unauthrole_restricted_access`
- `sample_eventbridge_invoke_custom_sample_event_bus_restricted_access`
- `sample_eventbridge_invoke_sfn_state_machine_restricted_access`
- `sample_step_functions_master_restricted_acces`s
#### IAM Users
- `sample_gitlab_mirroring` (conditional)
#### Cognito User Pool Groups
- `Admin`
- `Standard-Users`

When users are added to the above groups, they have the respective permissions granted through the IAM roles (**`sample_cognito_admin_group_restricted_access`** or **`sample_cognito_standard_group_restricted_access`**). The standard permissions are restricted to what is necessary. However you can view/modify the IAM policies in **`/terraform-deployment/modules/sample-qs/iam.tf`**.

***HINT***: Most resources launched by the using Terraform module will start with **`sample`**. When searching for resources deployed by Terraform for the workshop, resources should begin with **`sample`** or include **`sample`** in the resource name.

**Example:**
```sh
sample_landing_bucket
```

### Local Development

1. Ensure that the Terraform configuration for the workshop has been deployed
2. In deploying, you should have been sent an email with a **TOTP** (Time-based One Time Password) to your provided email addresses specified in **`main.tf`**. You'll need this to authenticate into the web application and AppSync GraphQL API.

**Example:**
```hcl
 sample_admin_cognito_users = {
    DefaultAdmin : {
      username       = "admin"
      given_name     = "Yusuke"
      family_name    = "Urameshi"
      email          = "yusuke@spiritgun.com" // this
      email_verified = true
    },
    KevonMayers : {
      username       = "novekm"
      given_name     = "Kazuma"
      family_name    = "Kuwabara"
      email          = "iheartyukina@yyh.com" // this
      email_verified = true
    }
  }
  # Standard Users to create
  sample_standard_cognito_users = {
    DefaultStandardUser : {
      username       = "default"
      given_name     = "Default"
      family_name    = "User"
      email          = "example@example.com" // this
      email_verified = false
    }
  }

```

3. Ensure you are in the **`/sample-sample-amplify-app/`** directory and run the command **`npm install`** to install all dependencies.
4. Once dependencies are installed, run the command **`npm run dev`** to run the development server on your `localhost`. The Terraform module is configured to write the outputs of Terraform to a .env file (**`/terraform-deployment/modules/sample-qs/.env`**). This file is referenced in the custom Amplify configuration file at **`/sample-sample-amplify-app/src/config/amplify-config.js`**.

Note: A similar process takes place for the hosted Amplify App. In the Terraform configuration, the necessary environmental variables are passed directly to Amplify. Then during the build phase, those values are read from Amplify and a .env file is created within the docker instance during the build phase. This is then used by vite to render things correctly.

```yaml
    build:
      commands:
        - echo "🛠️ Setting up your environmental variables..."
        - echo "VITE_REGION=$sample_REGION" >> .env
        - echo "VITE_API_ID=$sample_GRAPHQL_API_ID" >> .env
        - echo "VITE_GRAPHQL_URL=$sample_GRAPHQL_ENDPOINT" >> .env
        - echo "VITE_IDENTITY_POOL_ID=$sample_IDENTITY_POOL_ID" >> .env
        - echo "VITE_USER_POOL_ID=$sample_USER_POOL_ID" >> .env
        - echo "VITE_APP_CLIENT_ID=$sample_APP_CLIENT_ID" >> .env
        - echo "VITE_IOT_ENDPOINT=$sample_IOT_ENDPOINT" >> .env
        - echo "Printing environmental variables to the console to ensure they are correct"
        - cat .env
        - npm run build
        - echo "✅ Success!"
```
You can learn more about Vite Env Vars/Modes here: https://vitejs.dev/guide/env-and-mode.html

**IMPORTANT:**

In **`main.jsx`** we are using the **`Amplify.configure()`** method to configure the Amplify App with the values in the configuration file. This is what enables us to configure the Amplify application without the use of the Amplify CLI. These values will be automatically updated if needed when you run another **`terraform apply`**. This enables you to perform local development.

The values in **`.env`** are also stored in [AWS Systems Manager Parameter store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), and are also being passed into the amplify web application as [Environment Variables](https://docs.aws.amazon.com/amplify/latest/userguide/environment-variables.html) for ease of access when building for production. The `.env` file is in the `.gitignore` so it will not be saved to the repo. If working within a team of developers to extend this sample application, you can simply remove this from the `.gitignore` so all team members can access the same file. However, as a best practice it is it is recommended to use the necessary values either from Systems Manager Parameter store, or with environment variables.

You also may want to separate your backend and frontend into different repositories, in which case you would need to use the values in SSM parameter store, or through the environment variables passed into Amplify.

5. Upon running **`npm run dev`** the dev server should be started and you should be able to access the Amazon Cognito login page on **`http://localhost:5173/`**. Enter your provided email address and paste in the TOTP that was sent to the email address.
![image info](/resources/app-screenshots/sample_amplify_app_cognito_sign_in.png)
6. You will then be prompted to change your password
![image info](/resources/app-screenshots/sample_amplify_app_cognito_change_password_blank.png)
7. Set a new password that conforms to the password policy
![image info](/resources/app-screenshots/sample_amplify_app_change_password.png)
8. Upon clicking **`Change Password`** you should be signed in and redirected to the sample Amplify App Dashboard Page.
![image info](/resources/app-screenshots/sample_amplify_app_dashboard.png)
9. To test the pipeline, head to the **``Data Uploader``** page
![image info](/resources/app-screenshots/sample_amplify_app_data_uploader_page.png)
10. Select **`Add File`** to browse your device, and use one of the provided sample media files in `/resources/sample-media`. You'll see the file loaded to the upload window with the file name, type, and size.

**REMINDER:** Uploaded files cannot have spaces in the filename.
![image info](/resources/app-screenshots/sample_amplify_app_data_uploader_page_file_upload.png)
11. Click **`Upload`** upload the file. You should see a blue progress bar appear, and then a green success alert upon successful file upload.
![image info](/resources/app-screenshots/sample_amplify_app_data_uploader_page_progress_bar.png)
![image info](/resources/app-screenshots/sample_amplify_app_data_uploader_page_file_upload_success.png)
This is because you are signed in as a user in the `Admin` Cognito User Pool group. The role attached to that group allows for S3 upload. If you are not signed in as a user in the admin group, by default you will get an access denied error.
![image info](/resources/app-screenshots/sample_amplify_app_data_uploader_page_file_upload_failure.png)
11. Once the upload of the media file is successful, you can click the **`View S3 Objects`** button, or **`S3 Objects`** in the sidebar to navigate to the S3 Objects page.
![image info](/resources/app-screenshots/sample_amplify_app_s3_object_page_empty.png)
12. The S3 Objects page is performing an async request leveraging the **AppSync GraphQL API** and a GraphQL resolver. The resolver points to the DynamoDB data source which is the **`sample_output`** DynamoDB table. It can take some time for the pipeline to run. The table will be empty until the metadata is written to DynamoDB. To check the progress, visit your Step Function in the AWS Console. You should see one state machine running.
![image info](./images/aws_console_search_for_sfn.png)
13. Click on the hyperlink for the name of your state machine `sample-state-machine` to navigate to a details page for the state machine. You should see one execution and the status should also be `Running`.
14. Click on the hyperlink for the name of the execution to go to a details page for the execution.
Within a few minutes, the Step Function Workflow should complete successfully.
15. Head to the DynamoDB console and click `Explore Items` for the `sample_output` table. You should see the Amazon Transcribe Call Analytics metadata in your table.
![image info](./images/dynamodb_console_search.png)
![image info](./images/dynamodb_dashboard.png)
![image info](./images/dynamodb_items.png)

16. Head back to the Amplify Application and refresh the `S3 Objects` page. You should see the same data in the table. This is being fetched directly through the AppSync GraphQL API.
![image info](/resources/app-screenshots/sample_amplify_app_s3_objects_page_1_item.png)
17. ✅ You have successfully uploaded a file, tested the pipeline, and fetch the data though the GraphQL API! 🎉

**IMPORTANT:** If your S3 Objects table remains displaying **`Loading S3 Objects...`** with a spinner, it is most likely because you do not have access to the API.
![image info](/resources/app-screenshots/sample_amplify_app_s3_objects_page_loading.png)

Currently the API actions are restricted to the **`Admin`** and **`Standard`** Cognito User Pool Groups. This is noted by the line **` @aws_auth(cognito_groups: ["Admin", "Standard"])`** in the GraphQL schema.

**Schema:**
```hcl
type Object  @aws_auth(cognito_groups: ["Admin", "Standard"])  {
  ObjectId: String!
  Version: String
  DetailType: String
  Source: String
  FileName: String
  FilePath: String
  AccountId: String
  CreatedAt: String
  Region: String
  CurrentBucket: String
  OriginalBucket: String
  ObjectSize: Int
  SourceIPAddress: String
  LifecycleConfig: String
```
If the user you are signed in as is not in either of the provided user pool groups, you will not be able to use the API and will receive an 'unauthorized' error.


 Access to the API can be modified by editing the GraphQL schema to fit your needs. You could remove the `@aws_auth` line completely and **all** users logged into your cognito user pool would be able to access the API, or you could add additional groups as necessary by adding another string in the array.

 **Example:**
  `@aws_auth(cognito_groups: ["Admin", "Standard", "Managers", "Auditors"])`

If you have any questions or run into issues with deployment, feel free to leave a comment or submit a GitHub issue.

🚀 **Next Steps** - Connect your repository to set up Amplify Hosting for the Web App.
### Amplify Hosting
To set up Amplify hosting for the web application, you must connect a repository to the Amplify App. This workshop currently supports three ways to do this:
1. **Mirror your GitLab repo to AWS CodeCommit**. Push events will trigger the Amplify App to build in AWS. You can specify which branches you wish to trigger the build, by default it will be the main branch. See [setting up GitLab to CodeCommit Mirroring](https://docs.gitlab.com/ee/user/project/repository/mirror/push.html) for more information. Read on for instructions here.
2. **Use your GitHub Personal Access Token**. You can alternatively use a GitHub personal access token to give Amplify access to your GitHub repository. See [Setting up the Amplify GitHub App for AWS CloudFormation, CLI, and SDK deployments](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html) for more information. Read on for instructions here.
3. **Use an existing AWS CodeCommit Repo**. You can also use an existing AWS CodeCommit repository and directly push to that to trigger the build. Just ensure that the Amplify App has access to your CodeCommit repo via the generated IAM Role. Read on for instructions here.


### Option 1: Mirror your GitLab repo to AWS CodeCommit
This method will mirror your GitLab repository to AWS CodeCommit. When you push to your GitLab repo, it will be mirrored to CodeCommit with a delay of 1 minute if you select **`Only mirror protected branches`**.

**Prerequisites:**
- IAM User with repository mirroring permissions (created for you by using the `sample-qs` Terraform Module if you set `sample_enable_gitlab_mirroring = true` in your `main.tf` file. The default value is false. )

1. If you did not set `sample_enable_gitlab_mirroring` to `= true` in your `main.tf` when first deploying do so now, and run `terraform apply` again.
2. Navigate to the IAM console and navigate to the created IAM User **`sample_gitlab_mirroring`**
![image info](./images/iam_console_search.png)
![image info](./images/iam_dashboard.png)
![image info](./images/iam_users.png)
3. Click on `Security Credentials` then scroll down to the section that says `HTTPS Git credentials for AWS CodeCommit` and click **`Generate credentials`**
![image info](./images/iam_user_https_codecommit.png)
4. A popup will appear with your generated username and password. Click Download credentials to save these, when you close the popup these credentials will no longer be viewable. If you need to regenerate credentials, select the credentials that were created in the same `HTTPS Git credentials for AWS CodeCommit` section, delete them and then click `Generate credentials` again. For ease of access, keep this popup open until you copy the needed values into GitLab.
![image info](./images/iam_user_generate_https_codecommit_creds.png)
5. In a new tab, navigate to the CodeCommit dashboard. A CodeCommit repository was deployed for you by default unless you set `create_sample_codecommit_repo` to `= false`. You would only set this to false if you have an existing CodeCommit repo in the same AWS Account that you want to use, or if you are going to use a GitHub repo.
![image info](./images/codecommit_console_search.png)
![image info](./images/codecommit_dashboard.png)
6. Select the radial button next to the `sample_codecommit_repo` and click the `Clone URL` button. A dropdown will appear. Select `Clone HTTPS` (**NOT** Clone HTTPS(GRC)). This will copy your HTTPS repo clone URL to your clipboard. You'll need this to set up GitLab mirroring. You should receive a success message upon clicking.
![image info](./images/codecommit_clone_https.png)
![image info](./images/codecommit_copy_https_clone_url.png)
7. In a new tab, navigate to your GitLab repository that you wish to clone. This is most likely the same repo that you cloned the sample project to.
8. On the left sidebar, select **Settings > Repository**, and then click to expand **Mirroring repositories**.
9. Fill in the **Git repository URL** field with this format:
**`https://<your_aws_git_username>@git-codecommit.<aws-region>.amazonaws.com/v1/repos/<your_codecommit_repo>`**
Replace `<your_aws_git_username>` with the **AWS HTTPS Git user name** that you generated earlier (hopefully you kept the tab open and/or downloaded the credential file like recommended 😊). Replace `<aws-region>` and `<your_codecommit_repo` with the relevant values.
10. For **Mirror direction**, select **Push**.
11. For **Authentication method**, select **Password**. Fill in the **Password** box with the password for the IAM Git clone password created earlier in the IAM console.
12. Leave the option **Only mirror protected branches** for CodeCommit. It pushes more frequently (every one minute instead of every five.)
13. Select **Mirror repository**. You should see the mirrored repository appear:
**`https://*****:*****@git-codecommit.<aws-region>.amazonaws.com/v1/repos/<your_codecommit_repo>`**
14. To test mirroring by forcing a push, select **Update now** (the half-circle arrows). If **Last successful update** shows a date, you have configured mirroring correctly. If it isn't working correctly, a red `error` tag appears and shows the error message as hover text.
15. Navigate to the AWS Amplify console and click on the **`sample-App`** You should see the app in the `Provision` phase.
![image info](/sample-amplify-app/documentation/images/aws_amplify_console_search.png)
![image info](/sample-amplify-app/documentation/images/aws_amplify_tca_app.png)
![image info](/sample-amplify-app/documentation/images/aws_amplify_tca_app_provision.png)
16. After a few minutes, all the phases (`Build`, `Deploy`, `Verify`) should turn to green check marks.
![image info](/sample-amplify-app/documentation/images/aws_amplify_tca_app_successful_deploy.png)

17. Click on the hyperlink for your amplify app and it should open in a new tab.
18. Sign in with your credentials and you should be logged into the application.
19. If this was your first time signing into the application, you need to use the **TOTP** (Time-based One Time Password) sent to your provided email address. You'll be prompted to change your password, then will be able to sign in.
20. ✅ You should successfully have been signed in to your web application, and it is now running in the AWS Cloud! 🎉
![image info](/resources/app-screenshots/sample_amplify_app_dashboard.png)

**Note:** A dev branch was also set up for you. You can disable this if you wish, but it is recommended to use different environments (prod, dev, staging, test, etc.)

**Troubleshooting:** If your build fails, check your Amplify configuration file at `/sample-sample-amplify-app/src/config/amplify-config.js` and your Amplify buildspec file at `/amplify.yml`. Ensure your buildspec file is pointing at the correct directory. If you change the location of the sample amplify application, you will need to modify your buildspec file accordingly.

- AWS S3 Upload Customization: https://docs.amplify.aws/lib/storage/upload/q/platform/js/
