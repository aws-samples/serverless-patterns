plugins {
    kotlin("jvm") version "1.7.21"
    kotlin("plugin.serialization") version "1.5.20"
    id("com.github.johnrengelman.shadow") version "7.1.2"
}

group = "org.myorg"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.amazonaws:aws-lambda-java-events:3.11.0")
    implementation("com.amazonaws:aws-lambda-java-core:1.2.1")
    implementation("org.jetbrains.kotlin:kotlin-stdlib:1.8.0")
    implementation("org.apache.logging.log4j:log4j-to-slf4j:2.8.2")
    testImplementation(kotlin("test"))
}

tasks.shadowJar {
    archiveBaseName.set("serverless")
    archiveClassifier.set("")
    archiveVersion.set("")
}

tasks.getByName<Test>("test") {
    useJUnitPlatform()
}