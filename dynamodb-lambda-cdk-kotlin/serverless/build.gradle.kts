import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    kotlin("jvm") version "2.4.20"
    kotlin("plugin.serialization") version "2.4.20"
    id("com.gradleup.shadow") version "9.6.1"
}

group = "org.myorg"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.amazonaws:aws-lambda-java-events:3.16.1")
    implementation("com.amazonaws:aws-lambda-java-core:1.4.0")
    implementation("org.jetbrains.kotlin:kotlin-stdlib:2.4.20")
    implementation("org.apache.logging.log4j:log4j-to-slf4j:2.8.2")
    testImplementation(kotlin("test"))
}

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_21)
    }
}

tasks.shadowJar {
    archiveBaseName.set("serverless")
    archiveClassifier.set("")
    archiveVersion.set("")
}

tasks.getByName<Test>("test") {
    useJUnitPlatform()
}
