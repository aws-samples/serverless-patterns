package org.myorg.example

import software.amazon.awscdk.App

fun main() {
    val app = App()

    MyStack(app, "dyamodbstream-lambda-example")
    app.synth()
}
