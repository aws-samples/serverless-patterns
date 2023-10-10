# Put message onto the Source Kinesis Stream (one record with NEW_CUSTOMER and one with EXISTING_CUSTOMER)
aws kinesis put-records --stream-name kin-to-kin-source --records file://example-records.json