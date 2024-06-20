

 amis = {
   amzn2      = data.aws_ami.amzn2.id
   # Add other AMIs you might need
 }


 # Example for selecting secrets based on region
 secrets = {
   "us-east-1" = "arn:aws:secretsmanager:us-east-1:123456789123:secret:a-passwords-x"
   "us-east-2" = "arn:aws:secretsmanager:us-east-2:123456789123:secret:b-passwords-y"
 }


 is_us_east_1 = var.region == "us-east-1" ? 1 : 0
}
