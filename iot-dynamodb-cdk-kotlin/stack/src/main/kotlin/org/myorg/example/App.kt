package org.myorg.example

import software.amazon.awscdk.App

fun main() {
    val app = App()

    MyStack(app, "iot-dynamodb-example")
    app.synth()
}
