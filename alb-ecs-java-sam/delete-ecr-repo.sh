# Config file path
CONFIG_FILE=config.txt  

# If config file exists, read values from it
if [ -f "$CONFIG_FILE" ]; then

  echo "Reading config file..."

  # Read values 
  source $CONFIG_FILE

  # Set variables from config
  REPO_NAME=$repo_name
  AWS_REGION=$aws_region

else

  # Prompt for inputs
  read -p "Enter repository name: " REPO_NAME
  read -p "Enter AWS Region: " AWS_REGION  

fi

# Check if repository exists
REPO_EXISTS=$(aws ecr describe-repositories --repository-names $REPO_NAME --region $AWS_REGION 2>&1 | grep -c RepositoryNotFoundException)

# Delete the ECR repository if exists
if [ $REPO_EXISTS -eq 1 ]; then
  echo "Repository $REPO_NAME does not exist"
else
  aws ecr delete-repository --repository-name $REPO_NAME --force --region $AWS_REGION
  echo "ECR reposity $REPO_NAME has been deleted"
fi