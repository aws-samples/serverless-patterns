
DATE_TIME=$(date -u '+%Y-%m-%d %H:%M:%S.000')
DATA="{\"dimension_1\": \"dimension1\", \"measure_1\": \"1.0\", \"time\": \"${DATE_TIME}\", \"version\": \"1\" }"
aws sqs send-message --queue-url "$1" --message-body "$DATA" --region "$2"