package com.myorg;

import software.amazon.awscdk.App;

public final class EventbridgeScheduleSsmCdkJavaApp {
    public static void main(final String[] args) {
        App app = new App();

        new EventbridgeScheduleSsmCdkJavaStack(app, "EventbridgeScheduleSsmCdkJavaStack");

        app.synth();
    }
}
