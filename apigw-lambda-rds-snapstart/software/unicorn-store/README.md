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

