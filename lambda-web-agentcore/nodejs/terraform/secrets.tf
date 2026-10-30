# ---------------------------------------------------------------------------------------------
# Secrets for the web app's sign-in. Both are generated at deploy time and stored in
# AWS Secrets Manager. The web app reads them when an execution environment starts.
# ---------------------------------------------------------------------------------------------

# The login secret that the chat UI asks for. Read it with the command in the README.
resource "random_password" "login" {
  length  = 24
  special = false
}

resource "aws_secretsmanager_secret" "login" {
  name        = "${local.name}-login"
  description = "Login secret for the ${local.name} chat app."
  # Delete at once on destroy instead of after the default 30-day recovery window.
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "login" {
  secret_id     = aws_secretsmanager_secret.login.id
  secret_string = random_password.login.result
}

# The key that the web app uses to sign session tokens (HMAC-SHA256).
resource "random_password" "session_signing_key" {
  length  = 64
  special = false
}

resource "aws_secretsmanager_secret" "session_signing_key" {
  name                    = "${local.name}-session-signing-key"
  description             = "Session token signing key for the ${local.name} chat app."
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "session_signing_key" {
  secret_id     = aws_secretsmanager_secret.session_signing_key.id
  secret_string = random_password.session_signing_key.result
}
