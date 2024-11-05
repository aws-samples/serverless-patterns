package com.example.flashcards.services;

import com.example.flashcards.model.dto.FindCategoriesResponse;
import com.example.flashcards.repositories.CategoryRepository;

import java.sql.SQLException;

public class CategoryService {

    private final CategoryRepository categoryRepository;

    public CategoryService(CategoryRepository categoryRepository) {
        this.categoryRepository = categoryRepository;
    }

    public FindCategoriesResponse findCategories() throws SQLException {
        return FindCategoriesResponse.builder()
                .withCategories(categoryRepository.findAllCategoriesOrderedByNameAsc())
                .build();
    }

}
