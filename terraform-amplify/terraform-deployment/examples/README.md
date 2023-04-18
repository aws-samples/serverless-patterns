# Terraform Examples Documentation
There are several examples you can leverage to get started with deployment. Most parameters are optional as there are defaults set based on the intended use of the workshop.
### Instructions
1. Navigate to the directory for one of the examples
2. Copy the content of the the related **`main.tf`** file and paste into YOUR **`main.tf`** file.
3. Modify the variables as desired, referencing the [sample-qs module documentation](/terraform-deployment//modules/sample-qs/README.md).
4. Ensure you have assumed an AWS profile and are in **`terraform-deployment`** directory. Check that you have assumed the correct profile by running the command **`aws sts get-caller-identity`**
5. Initialize Terraform **`terraform init`**
6. Plan Terraform deployment **`terraform plan`**
7. Apply Terraform plan **`terraform apply`**
8. ✅ 🎉 Your infrastructure should be successfully deployed into your AWS account.
