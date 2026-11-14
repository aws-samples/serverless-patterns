# Change to source directory
cd src

# Config file path
CONFIG_FILE=config.txt  

# If config file exists, read values from it
if [ -f "$CONFIG_FILE" ]; then

  echo "Reading config file..."

  # Read values 
  source $CONFIG_FILE

  # Set variables from config
  IMAGE_NAME=$image_name
  REPO_NAME=$repo_name
  AWS_ACCOUNT=$aws_account
  AWS_REGION=$aws_region

else

  # Prompt for inputs
  read -p "Enter image name: " IMAGE_NAME
  read -p "Enter repository name: " REPO_NAME  
  read -p "Enter AWS account ID: " AWS_ACCOUNT
  read -p "Enter AWS Region: " AWS_REGION

  # Save inputs to config file
  echo "Saving config..."
  echo "image_name=$IMAGE_NAME" > $CONFIG_FILE
  echo "repo_name=$REPO_NAME" >> $CONFIG_FILE
  echo "aws_account=$AWS_ACCOUNT" >> $CONFIG_FILE
  echo "aws_region=$AWS_REGION" >> $CONFIG_FILE

fi


# Build Docker image
docker build -t $IMAGE_NAME .

# Check if repository exists
REPO_EXISTS=$(aws ecr describe-repositories --repository-names $REPO_NAME --region $AWS_REGION 2>&1 | grep -c RepositoryNotFoundException)

# Create ECR repository if it doesn't exist
if [ $REPO_EXISTS -eq 1 ]; then
  aws ecr create-repository --repository-name $REPO_NAME --region $AWS_REGION
fi

# Tag image 
docker tag $IMAGE_NAME $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest

# Login to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com

# Push image to ECR
docker push $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest 

# Print image ID
IMAGE_ID=$(aws ecr describe-images --repository-name $REPO_NAME --image-ids imageTag=latest --region $AWS_REGION --query 'imageDetails[].imageId' --output text)

echo "Pushed image URI: $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest"

# Got back to project root folder
cd ..