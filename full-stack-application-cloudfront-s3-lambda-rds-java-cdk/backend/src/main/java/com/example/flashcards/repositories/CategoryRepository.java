package com.example.flashcards.repositories;

import com.example.flashcards.model.entities.Category;

import javax.sql.DataSource;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class CategoryRepository {

    private final static String FIND_ALL_CATEGORIES_ORDERED_BY_NAME_ASC_SQL = """
            SELECT
            	*
            FROM
            	CATEGORIES C
            ORDER BY
            	C.NAME ASC""";
    private final DataSource dataSource;

    public CategoryRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public List<Category> findAllCategoriesOrderedByNameAsc() throws SQLException {
        try (
                var connection = dataSource.getConnection();
                var preparedStatement = connection.prepareStatement(FIND_ALL_CATEGORIES_ORDERED_BY_NAME_ASC_SQL);
                var resultSet = preparedStatement.executeQuery()
        ) {
            List<Category> categories = new ArrayList<>();
            while (resultSet.next()) {
                categories.add(
                        Category.builder()
                                .withId(resultSet.getLong("id"))
                                .withName(resultSet.getString("name"))
                                .build()
                );
            }
            return categories;
        }
    }
}
