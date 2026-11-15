package com.myorg;

import software.amazon.awscdk.App;

public final class CdkFirehoseLambdaS3JavaApp {
    public static void main(final String[] args) {
        App app = new App();

        new CdkFirehoseLambdaS3JavaStack(app, "CdkFirehoseLambdaS3JavaStack");

        app.synth();
    }
}
