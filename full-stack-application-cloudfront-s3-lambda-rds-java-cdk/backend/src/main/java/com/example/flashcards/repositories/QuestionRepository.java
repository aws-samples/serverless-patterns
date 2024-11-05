package com.example.flashcards.repositories;

import com.example.flashcards.model.entities.Question;

import javax.sql.DataSource;
import java.sql.JDBCType;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import static com.example.flashcards.FlashcardsLambdaApplicationUtils.getStatementBuilder;

public class QuestionRepository {

    private final static String FIND_RANDOM_QUESTIONS_SQL = """
            SELECT
            	*
            FROM
            	QUESTIONS Q
            WHERE
            	Q.CATEGORY_ID = ?
            ORDER BY
            	RANDOM() LIMIT ?""";
    private final DataSource dataSource;

    public QuestionRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public List<Question> findRandomQuestions(Long categoryId, Integer limit) throws SQLException {
        try (
                var connection = dataSource.getConnection();
                var preparedStatement = getStatementBuilder(connection, FIND_RANDOM_QUESTIONS_SQL)
                        .setParameter(1, categoryId, JDBCType.BIGINT)
                        .setParameter(2, limit, JDBCType.INTEGER)
                        .getStatement();
                var resultSet = preparedStatement.executeQuery()
        ) {
            List<Question> questions = new ArrayList<>();
            while (resultSet.next()) {
                questions.add(
                        Question.builder()
                                .withId(resultSet.getLong("id"))
                                .withCategoryId(resultSet.getLong("category_id"))
                                .withQuestionText(resultSet.getString("question_text"))
                                .build()
                );
            }
            return questions;
        }
    }
}
