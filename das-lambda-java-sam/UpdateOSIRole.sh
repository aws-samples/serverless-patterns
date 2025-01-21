# Adding Role to Backend Roles in OpenSearch Security to allow OpenSearch Pipeline to send data to OpenSearch
#!/bin/bash

curl -XPUT "$OPENSEARCH_DOMAIN_URL/_plugins/_security/api/rolesmapping/all_access" -H 'Content-Type: application/json' -H "Authorization: Basic $BASE64_USERNAME_PWD" -d'
{
    "backend_roles" : [ "'"${OSI_IAM_ROLE}"'" ],
    "users" : ["'"${OS_MASTER_USERNAME}"'"]

}
'