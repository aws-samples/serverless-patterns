## 🎒 Pre-requisites

- The [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) must be installed *and* configured with an AWS account on the deployment machine (see <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html> for instructions on how to do this on your preferred development platform). To make sure you have it available on your machine, try running the following command.
  ```sh
  aws --version
  ```
- This project requires [Node.js](http://nodejs.org/). See [How to Install Node.Js](https://nodejs.dev/en/learn/how-to-install-nodejs/) for installation instructions.
To make sure you have it available on your machine, try running the following command.
  ```sh
  node -v
  ```
- This project requires [NPM](http://nodejs.org/). See [Downloading and installing Node.Js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) for installation instructions.
To make sure you have it available on your machine, try running the following command.
  ```sh
  npm -v
  ```
- This project requires [Terraform](https://www.terraform.io/). See [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) for installation instructions. To make sure you have it available on your machine, try running the following command.

  ```sh
  terraform -v
  ```

For best experience we recommend installing using an [IAM Roles](https://aws.amazon.com/iam/features/manage-roles/) with adequate permissions to deploy the AWS services. It is also recommended to deploy this workshop into a development/test AWS account.

## 🚀 Setup

### 0/ Use git to clone this repository to your local environment

```sh
git clone #insert-http-or-ssh-for-this-repository
```

### 1/ Set up your AWS environment

- Configure your AWS credentials by running the command **`aws configure`**
- For more on setting up your AWS Credentials please see [Using an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html) (Recommended) OR [Named profiles for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)

### 2/ Prepare your Terraform environment

1. Navigate to **`terraform-deployment/main.tf`**
2. The `main.tf` file comes preloaded with a template for deployment. Simply modify the relevant values. You can also use one of the example templates in **`terraform-deployment/examples`** to set up your `main.tf` file. Please read the custom `sample-module` [module documentation](/terraform-deployment/modules/sample-qs/README.md) and the general [Terraform Documentation](/terraform-deployment/README.md) for more information.

**Example `main.tf`**:
```go
module "sample-qs" {
  // location of the module - can be local or git repo
  source = "./modules/sample-module"

  # - Cognito -
  # Admin Users to create
  sample_admin_cognito_users = {
    NarutoUzumaki : {
      username       = "admin"
      given_name     = "Default"
      family_name    = "Admin"
      email          = "novekm@amazon.com"
      email_verified = true // no touchy
    },
    SasukeUchiha : {
      username       = "kmayers"
      given_name     = "Kevon"
      family_name    = "Mayers"
      email          = "kevonmayers31@gmail.com"
      email_verified = true // no touchy
    }
  }
  # Standard Users to create
  sample_standard_cognito_users = {
    DefaultStandardUser : {
      username       = "default"
      given_name     = "Default"
      family_name    = "User"
      email          = "kevon_mayers@yahoo.com"
      email_verified = true // no touchy
    }
  }

}
```

#### **```sample-module``` Variables**

A full list of the module variables is in the [module documentation](/terraform-deployment/modules/sample-module/README.md). All variables have default values set based on the function of the workshop. These can be modified to customize your deployment. See [this document](./terraform-deployment/README.md) for more information.


**Amplify Web Application Note:** If you choose to deploy the Amplify Web Application make sure you review [web application documentation](/sample-amplify-app/documentation/README.md).

### 3/ Initialize Terraform and plan your infrastructure changes.
Before running these commands, ensure you are in the **`terraform-deployment`** directory.

- Make sure that you have assumed an AWS Profile or credentials through `aws configure` or some other means. [AWSP  - AWS Profile Switcher](https://github.com/johnnyopao/awsp) is an open source GitHub solution that you can look into if you wish.
- Get your AWS Account Number to verify you are in the correct AWS account. Run the command **`aws sts get-caller-identity`**


- Initialize Terraform.

```sh
terraform init
```

- Preview the changes that Terraform plans to make to your infrastructure.

```sh
terraform plan
```




### 4/ Deploy the application

-  **NOTE**: All resources deployed using the custom Terraform Module **`sample-module`** will have the tags **`IAC_PROVIDER = Terraform`** and **`AppName = sample-App`**. You can add additional tags in the module's relevant service `.tf` resource files if you wish ( `s3.tf`, `dynamodb.tf`, `iam.tf`, etc.). The Terraform `merge()` function will merge your additional tags with the default tags specified in the module's **`variables.tf`** file. Deployed resources will also start with the prefix **`tca`** for ease of visibility.

**Example:**
```go
  tags = merge(
    {
      "AppName" = var.app_name,
      "Naruto" = "Hokage",
      "Smitty Werbenjägermanjensen" = "#1"
    },
    var.tags,
  )
```

- 👨🏾‍💻 ✅ Apply (execute) the Terraform plan with the command **`terraform apply`**. Note, you will be prompted to accept the changes (Y/N) before the apply will take place.

- 😏 ⛔️ Advanced User: You can bypass these prompts by running the command **`terraform apply --auto-approve`** but this is only recommended if you have experience with Terraform. For those newer to Terraform, it is recommended to follow the prompts.

### 5/ Optional: Set up the Amplify Web Application

If you have chosen to deploy the optional Web Application by leaving the default value of **`create_sample_amplify_app = true`**, there are a few simple steps to get up and running with the web application.

For quick setup follow the instructions below.

#### Quick Setup

If you are reading this it is because you deployed the Sample Web Applicaiton by leaving the default value os `create_sample_amplify_app = true` in the `modules/sample-qs/variables.tf` file. Your application is already available via your `localhost`. The web application is leveraging [React](https://reactjs.org/), a javascript framework, and [ViteJS](https://vitejs.dev/) an alternative to CRA (`create-react-app`) that is quite popular and has a some substantial benefits.

1. To deploy the full Amplify Application with Amplify Hosting in AWS, you must connect your repository to the Amplify App. The workshop supports 3 ways to do this:
- **Mirror your GitLab repo to AWS CodeCommit**. Push events will trigger the Amplify App to build in AWS. You can specify which branches you wish to trigger the build, by default it will be the main branch. See [setting up GitLab to CodeCommit Mirroring](https://docs.gitlab.com/ee/user/project/repository/mirror/push.html) and the [Amplify App documentation](/sample-sample-amplify-app/documentation/README.md) for more information.
- **Use your GitHub Personal Access Token**. You can alternatively use a GitHub personal access token to give Amplify access to your GitHub repository. See the [Amplify App Documentation](/sample-sample-amplify-app//documentation/README.md) and [Setting up the Amplify GitHub App for AWS CloudFormation, CLI, and SDK deployments](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html) for more information
- **Use an existing AWS CodeCommit Repo**. You can also use an existing AWS CodeCommit repository and directly push to that to trigger the build. Just ensure that the Amplify App has access to your CodeCommit repo via the generated IAM Role. See the [Amplify App Documentation](/sample-amplify-app/documentation/README.md) for more information.

2. Push your code to the repo. This will trigger Amplify to start the build of your Amplify App following the buildspec defined at `/amplify.yml`

3. Visit the AWS Console and search for **AWS Amplify**
4. You should see one application running called **`sample-App`**. Wait for the build to complete, then click on the URL generated for you.
**(insert image)**

✅ Success! At this point, you should successfully have the Amplify app working.

For detailed instructions, see the [Amplify App Documentation](/sample-amplify-app/documentation/README.md).


## 🗑 How to Destroy
#### Deleting all resources

You can destroy **all** resources deployed by Terraform by running the command **`terraform destroy`**. Similar to the `apply` command, you can ignore the prompts by adding the `--auto-approve` flag to the command.
Ex:
```sh
terraform destroy --auto-approve
```
#### Deleting specific resources
 You can destroy individual resources two ways:
1. **`terraform apply` to Destroy** - Comment out (or delete) the resource in your configuration files and run the command **`terraform apply`**. This will check state file and compare it to the remaining defined resources in your configuration files and make the changes to make the two match (delete the resources that are commented out).
2. **`terraform destroy` to Destroy** - You can add the flag `--target` to your `terraform destroy` command to specify a specific target. You then would need to remove the code from your configuration file or the resources would be re-created the next time you apply your configuration.
Ex:
```sh
terraform destroy --target aws_s3_bucket.sample_quicksight_bucket
```

## Work with outputs

The Terraform module has a number of outputs that you can reference to integrate the deployment into your existing infrastructure, or expand what is deployed by the module. These outputs are defined in the `outputs.tf` file in **`/terraform-deployment/modules/sample-qs/outputs.tf`**. These outputs are being used to dynamically configure the Amplify Application without using the Amplify CLI. To learn more about how this is being done, visit the [Amplify App Documentation](/sample-sample-amplify-app//documentation/README.md). Take a look at [this document](https://www.terraform.io/language/values/outputs) to learn more about [Terraform outputs](https://www.terraform.io/language/values/outputs). For a list of all outputs, visit the [sample-qs module documentation](/terraform-deployment//modules/sample-qs/README.md).


## Extending this sample workshop

If you are looking to utilize existing features of this sample project while integrating your own features, modules, or applications, please feel free to fork this repo and download locally and make changes to fit your use case.


Helpful Commands
- **`terraform init`** - Initialize Terraform
- **`terraform plan`** - Plan Terraform deployment
- **`terraform apply`** - Apply the Terraform plan
- **`terraform apply --auto-approve`** - Apply the Terraform plan without prompts

Use one of the Examples in `./examples` and paste it in your `main.tf` to get started. If using the Amplify App, ensure you list at least one cognito user in `main.tf`
Ex:
```go
  # Admin Users to create
  sample_admin_cognito_users = {
    DefaultAdmin : {
      username       = "admin"
      given_name     = "Naruto"
      family_name    = "Uzumaki"
      email          = "naruto@hokage.com"
      email_verified = true
    },
    SasukeUchiha : {
      username       = "novekm"
      given_name     = "Sasuke"
      family_name    = "Uchiha"
      email          = "sasuke@uchiha.com"
      email_verified = true
    }
  }
  # Standard Users to create
  sample_standard_cognito_users = {
    DefaultStandardUser : {
      username       = "default"
      given_name     = "Default"
      family_name    = "User"
      email          = "example@example.com"
      email_verified = false
    }
  }
```

To help shorten commands, it's recommended to use aliases
Ex: **`tf plan`**, **`tf apply`** instead of the full word terraform
More info:
ZSH - https://linuxhint.com/configure-use-aliases-zsh/
Bash - https://linuxize.com/post/how-to-create-bash-aliases/
