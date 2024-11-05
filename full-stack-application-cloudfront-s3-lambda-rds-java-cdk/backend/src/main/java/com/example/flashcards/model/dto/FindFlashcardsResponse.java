package com.example.flashcards.model.dto;

import lombok.Builder;

import java.util.List;

@Builder(setterPrefix = "with", builderClassName = "FindFlashcardsResponseBuilder")
public record FindFlashcardsResponse(List<Flashcard> flashcards) {
}
