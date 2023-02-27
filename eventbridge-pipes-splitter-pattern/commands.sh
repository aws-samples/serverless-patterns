aws dynamodb put-item \
--table-name=Orders-Table \
--item '{"id":{"S":"905fa520-4d4a-4850-97c5-1d429f8c23ba"},"userId":{"S":"b507de3e-d9d4-4e88-9e61-28416394777f"},"tickets":{"L":[{"M":{"id":{"S":"5c27a12d-f33f-4b64-8afe-844a8a297660"}}},{"M":{"id":{"S":"2208130e-4f78-48d4-b3e3-bf94912ae71d"}}},{"M":{"id":{"S":"0325bf78-a162-4486-adb1-218aadf41fdc"}}}]}}'
