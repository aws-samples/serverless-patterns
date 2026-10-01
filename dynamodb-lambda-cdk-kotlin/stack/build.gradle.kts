import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    kotlin("jvm") version "2.4.20"
    application
    kotlin("plugin.serialization") version "2.4.20"
    id("com.gradleup.shadow") version "9.6.1"
}

group = "org.myorg"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("software.amazon.awscdk:aws-cdk-lib:2.272.0")
    implementation("software.constructs:constructs:10.8.1")
    testImplementation(kotlin("test"))
}

tasks.test {
    useJUnitPlatform()
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

application {
    mainClass.set("org.myorg.example.AppKt")
}
