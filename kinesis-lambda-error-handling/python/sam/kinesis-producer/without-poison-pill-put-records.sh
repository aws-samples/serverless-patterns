aws kinesis put-records \
    --stream-name DataActivityKinesisStream \
    --records file://kinesis-producer/test-records-without-poison-pill.json