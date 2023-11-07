# Create an IAM policy
resource "aws_iam_policy" "ct_iam_policy" {
  name = "ct-iam-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sso:DescribeAccountAssignmentCreationStatus",
          "sso:CreateAccountAssignment",
          "organizations:CloseAccount",
          "organizations:MoveAccount"
        ]
        Resource = "*"
      }
    ]
  })
}

# Create an IAM role
resource "aws_iam_role" "ct_cross_account_role" {
  name = "AFTCrossAccountRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          "AWS" : "arn:aws:iam::XXXXXXXXXXX:root"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Attach the IAM policy to the IAM role
resource "aws_iam_policy_attachment" "ct_role_policy_attachment" {
  name       = "ct-role-policy"
  policy_arn = aws_iam_policy.ct_iam_policy.arn
  roles      = [aws_iam_role.ct_cross_account_role.name]
}