import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.7.21"
    application
    kotlin("plugin.serialization") version "1.5.20"
    id("com.github.johnrengelman.shadow") version "7.1.2"
}

group = "org.myorg"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    val cdkVersion = "2.56.0"
    implementation("software.amazon.awscdk:aws-cdk-lib:${cdkVersion}")
    implementation("software.constructs:constructs:${cdkVersion}")
    testImplementation(kotlin("test"))}



tasks.test {
    useJUnitPlatform()
}

tasks.withType<KotlinCompile> {
    kotlinOptions.jvmTarget = "1.8"
}

application {
    mainClass.set("org.myorg.example.AppKt")
}

