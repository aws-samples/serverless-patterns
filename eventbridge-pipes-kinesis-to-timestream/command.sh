
DATE_TIME=$(date -u '+%Y-%m-%d %H:%M:%S.000')
DATA=$(echo "{\"dimension_1\": \"dimension1\", \"measure_1\": \"1.0\", \"time\": \"${DATE_TIME}\", \"version\": \"1\" }" | base64)
aws kinesis put-record --stream-name "$1" --data "$DATA" --partition-key "$RANDOM" --region "$2"