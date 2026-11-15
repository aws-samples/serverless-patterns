a=0
# -lt is less than operator

#Iterate the loop until a less than 10
while [ $a -lt 24 ]
do
	# Print the values
	aws kinesis put-record --stream-name LambdaPackagingStack-KinesisToLambdaPatternKinesisStreamFA60BE3F-ODRbhifDN9wS   \
      --data '{"user_id":"user1", "score": 100}' \
      --partition-key $a
	echo $a
	
	# increment the value
	a=`expr $a + 1`
done
