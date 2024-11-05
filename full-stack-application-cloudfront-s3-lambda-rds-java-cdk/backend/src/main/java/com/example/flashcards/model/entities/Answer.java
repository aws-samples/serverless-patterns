package com.example.flashcards.model.entities;

import lombok.Builder;

@Builder(setterPrefix = "with", builderClassName = "AnswerBuilder")
public record Answer(Long id, Long questionId, String answerText, Boolean correct) {
}