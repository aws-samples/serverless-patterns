package com.example.flashcards;

import software.amazon.awscdk.App;
import software.amazon.awscdk.StackProps;

public class FlashcardsInfraApp {
    public static void main(final String[] args) {
        var app = new App();
        var stackProps = StackProps.builder()
                .build();
        new FlashCardsInfraStack(app, "FlashcardsInfraStack", stackProps);
        app.synth();
    }
}