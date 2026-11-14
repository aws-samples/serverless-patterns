# Create a directory for the layer
mkdir -p lambda-layer/python

# Navigate to the python directory
cd lambda-layer/python

# Create a requirements.txt file
echo "boto3" > requirements.txt
echo "botocore" >> requirements.txt

# Install the requirements
pip install -r requirements.txt -t .

# Go back to the lambda-layer directory
cd ..

# Zip the contents
zip -r boto3-bedrock-layer.zip python/

# Move back to the main project directory
cd ..

zip lambda_function.zip bedrock_integration.py