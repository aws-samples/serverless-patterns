#!/bin/bash

# 📞 SEND CALLBACK TO DURABLE FUNCTION

set -e

# 📝 DECLARE VARIABLES
REGION="us-east-2"

echo "📞 Send Callback to Durable Function"
echo "===================================="
echo ""

# 🔍 PROMPT FOR CALLBACK ID
read -p "Enter Callback ID: " CALLBACK_ID

if [ -z "$CALLBACK_ID" ]; then
  echo "❌ Error: Callback ID cannot be empty"
  exit 1
fi

echo ""
echo "📋 Callback Details:"
echo "   Callback ID: $CALLBACK_ID"
echo "   Region: $REGION"
echo ""

# 🎯 PROMPT FOR SUCCESS OR FAILURE
echo "Select callback type:"
echo "  1) Approve"
echo "  2) Reject"
read -p "Enter choice (1 or 2): " CALLBACK_TYPE

case $CALLBACK_TYPE in
  1)
    echo ""
    echo "✅ Sending APPROVE/SUCCESS callback..."
    
    RESULT_PAYLOAD='{"status":"approved","message":"Transaction approved by user"}'
    
    # SEND SUCCESS CALLBACK
    aws lambda send-durable-execution-callback-success \
      --callback-id "$CALLBACK_ID" \
      --result "$RESULT_PAYLOAD" \
      --region $REGION 
    
    echo "✅ Success callback sent!"
    echo "📋 Result: $RESULT_PAYLOAD"
    ;;
    
  2)
    echo ""
    echo "❌ Sending REJECT/FAILURE callback..."
    
    ERROR_TYPE="UserRejection"
    ERROR_MESSAGE="Transaction rejected by user"

    # BUILD ERROR OBJECT
    ERROR_OBJECT=$(cat <<EOF
{
  "ErrorType": "$ERROR_TYPE",
  "ErrorMessage": "$ERROR_MESSAGE"
}
EOF
)
    
    # SEND FAILURE CALLBACK
    aws lambda send-durable-execution-callback-failure \
      --callback-id "$CALLBACK_ID" \
      --error "$ERROR_OBJECT" \
      --region $REGION 
    
    echo "✅ Failure callback sent!"
    echo "📋 Error Type: $ERROR_TYPE"
    echo "📋 Error Message: $ERROR_MESSAGE"
    ;;
    
  *)
    echo "❌ Invalid choice. Please enter 1 or 2."
    exit 1
    ;;
esac

echo ""
echo "✅ Callback operation complete!"
