package com.example.flashcards.model.dto;

import com.example.flashcards.model.entities.Category;
import lombok.Builder;

import java.util.List;

@Builder(setterPrefix = "with", builderClassName = "FindCategoriesResponseBuilder")
public record FindCategoriesResponse(List<Category> categories) {
}