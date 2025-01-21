# Creating script for re-starting OSI Pipeline
#!/bin/bash
aws osis stop-pipeline --pipeline-name das-osi-pipeline --no-cli-pager 
            
max_attempts=25 
attempt_num=1 
success=false 
while [ $success = false ] && [ $attempt_num -le \$max_attempts ]; do 
    echo "Getting Status of OSI Pipeline" 
                
    PIPELINE_STATUS=$(aws osis get-pipeline --pipeline-name das-osi-pipeline | jq -r '.Pipeline.Status')
               
    # Check the exit code of the command 
    if [ $PIPELINE_STATUS == "STOPPED" ]; then 
        echo "PIPELINE_STATUS=$PIPELINE_STATUS" 
        echo "PIPELINE is stopped"
        success=true 
    else 
        echo "PIPELINE_STATUS=$PIPELINE_STATUS" 
        echo "PIPELINE is being stopped. Sleeping for 1 minute and trying again..." 
        sleep 60
        ((attempt_num++))
    fi
done
echo "Pipeline has stopped. Now will attempt to restart it." 
            
aws osis start-pipeline --pipeline-name das-osi-pipeline --no-cli-pager" 

max_attempts=25 
attempt_num=1 
success=false
while [ $success = false ] && [ $attempt_num -le $max_attempts ]; do 
    echo "Getting Status of OSI Pipeline" 
                
    PIPELINE_STATUS=$(aws osis get-pipeline --pipeline-name das-osi-pipeline | jq -r '.Pipeline.Status') 
               
    # Check the exit code of the command" 
    if [ $PIPELINE_STATUS == "ACTIVE" ]; then 
        echo "PIPELINE_STATUS=\$PIPELINE_STATUS" 
        echo "PIPELINE is started" 
        success=true 
    else 
        echo "PIPELINE_STATUS=\$PIPELINE_STATUS" 
        echo "PIPELINE is being started. Sleeping for 1 minute and trying again..." 
        sleep 60 
        ((attempt_num++)) 
    fi
done
echo "Pipeline has restarted."