package com.myorg;

import software.amazon.awscdk.App;
import software.amazon.awscdk.StackProps;


public class MyServerlessApplicationApp {
    public static void main(final String[] args) {
        App app = new App();

        new MyServerlessApplicationStack(app, "MyServerlessApplicationStack", StackProps.builder()
                .build());

        app.synth();
    }
}

