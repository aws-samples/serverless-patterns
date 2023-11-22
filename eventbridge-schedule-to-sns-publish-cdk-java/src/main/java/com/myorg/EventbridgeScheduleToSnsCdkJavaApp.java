package com.myorg;

import software.amazon.awscdk.App;

public final class EventbridgeScheduleToSnsCdkJavaApp {
    public static void main(final String[] args) {
        App app = new App();

        new EventbridgeScheduleToSnsCdkJavaStack(app, "EventbridgeScheduleToSnsCdkJavaStack");

        app.synth();
    }
}
