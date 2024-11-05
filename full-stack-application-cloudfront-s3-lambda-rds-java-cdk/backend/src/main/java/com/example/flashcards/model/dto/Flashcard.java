package com.example.flashcards.model.dto;

import lombok.Builder;

import java.util.List;

@Builder(setterPrefix = "with", builderClassName = "FlashcardBuilder")
public record Flashcard(String question, String correctAnswer, List<String> incorrectAnswers) {
}
