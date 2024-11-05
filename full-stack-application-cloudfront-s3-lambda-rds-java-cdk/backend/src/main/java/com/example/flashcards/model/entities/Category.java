package com.example.flashcards.model.entities;

import lombok.Builder;

@Builder(setterPrefix = "with", builderClassName = "CategoryBuilder")
public record Category(Long Id, String name) {
}