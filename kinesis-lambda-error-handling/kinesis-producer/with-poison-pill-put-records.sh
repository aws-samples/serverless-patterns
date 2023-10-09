aws kinesis put-records \
    --stream-name DataActivityKinesisStream \
    --records file://kinesis-producer/test-records-with-poison-pill.json