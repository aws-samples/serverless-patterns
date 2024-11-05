package com.example.flashcards.model.entities;

import lombok.Builder;

@Builder(setterPrefix = "with", builderClassName = "QuestionBuilder")
public record Question(Long id, Long categoryId, String questionText) {
}