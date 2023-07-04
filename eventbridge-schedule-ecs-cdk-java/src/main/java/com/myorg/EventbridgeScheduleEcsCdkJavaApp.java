package com.myorg;

import software.amazon.awscdk.App;

public final class EventbridgeScheduleEcsCdkJavaApp {
    public static void main(final String[] args) {
        App app = new App();

        new EventbridgeScheduleEcsCdkJavaStack(app, "EventbridgeScheduleEcsCdkJavaStack");

        app.synth();
    }
}
