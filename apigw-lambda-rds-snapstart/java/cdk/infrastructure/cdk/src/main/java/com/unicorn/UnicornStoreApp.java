package com.unicorn;

import software.amazon.awscdk.App;
import software.amazon.awscdk.StackProps;

public class UnicornStoreApp {

    public static void main(final String[] args) {
        App app = new App();

        var infrastructureStack = new InfrastructureStack(app, "UnicornStoreInfrastructure", StackProps.builder()
                .build());

        var unicornStoreStack= new UnicornStoreStack(app, "UnicornStoreApp", StackProps.builder()
                .build(), infrastructureStack);

        app.synth();
    }
}
