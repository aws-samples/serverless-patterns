## Handler
[AWS Lambda Handler](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html)

Handler: io.micronaut.function.aws.proxy.MicronautLambdaHandler

When deployed to Lambda, set as environment variables: 
```
DATASOURCES_DEFAULT_URL
DATASOURCES_DEFAULT_USERNAME
DATASOURCES_DEFAULT_PASSWORD
```

```
curl --location --request POST $(cat infrastructure/cdk/target/output.json | jq -r '.UnicornStoreApp.ApiEndpoint')'/unicorns' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "Something",
"age": "Older",
"type": "Animal",
"size": "Very big"
}' | jq
```

```
[36m13:03:42.093[0;39m [1;30m[main][0;39m [31mWARN [0;39m [35mcom.zaxxer.hikari.pool.PoolBase[0;39m - HikariPool-1 - Failed to validate connection org.postgresql.jdbc.PgConnection@4233e892 (This connection has been closed.). Possibly consider using a shorter maxLifetime value.
```

Without CRaC support
REPORT RequestId: bf46dfe0-3b2c-43e6-b9ab-b977302e2a8d	Duration: 333.03 ms	Billed Duration: 566 ms	Memory Size: 2048 MB	Max Memory Used: 154 MB	Restore Duration: 527.20 ms	Billed Restore Duration: 232 ms
Total 333 + 527 = 860ms

With CRaC support
REPORT RequestId: 0012e9ef-b0ce-4dbe-83d5-400c10b3036d	Duration: 280.43 ms	Billed Duration: 534 ms	Memory Size: 2048 MB	Max Memory Used: 157 MB	Restore Duration: 438.11 ms	Billed Restore Duration: 253 ms	
Total 280 + 438 = 718ms