package org.myorg.example

import software.amazon.awscdk.RemovalPolicy
import software.amazon.awscdk.Stack
import software.amazon.awscdk.services.dynamodb.Attribute
import software.amazon.awscdk.services.dynamodb.AttributeType
import software.amazon.awscdk.services.dynamodb.Table
import software.amazon.awscdk.services.iot.actions.alpha.DynamoDBv2PutItemAction
import software.amazon.awscdk.services.iot.alpha.IotSql
import software.amazon.awscdk.services.iot.alpha.TopicRule
import software.constructs.Construct

class MyStack(scope: Construct, id: String) : Stack(scope, id) {
    private val myTable: Table = newTable()

    init {
        locationsReceivedRule(myTable)
    }

    private fun idKey() =
        Attribute.builder().name("id").type(AttributeType.STRING).build()

    private fun locationsReceivedRule(table: Table) {
        TopicRule.Builder.create(this, "TopicRule")
            .topicRuleName("exampleRule")
            .sql(IotSql.fromStringAsVer20160323("SELECT * FROM 'device/+/information'"))
            .actions(
                listOf(
                    DynamoDBv2PutItemAction(
                        table
                    )
                )
            ).build()
    }

    private fun newTable() = Table.Builder
        .create(this, "example-table")
        .tableName("example-table")
        .partitionKey(idKey())
        .removalPolicy(RemovalPolicy.DESTROY)
        .build()
}
