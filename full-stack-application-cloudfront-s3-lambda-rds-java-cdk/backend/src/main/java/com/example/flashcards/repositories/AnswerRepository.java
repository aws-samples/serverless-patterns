package com.example.flashcards.repositories;

import com.example.flashcards.model.entities.Answer;

import javax.sql.DataSource;
import java.sql.JDBCType;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import static com.example.flashcards.FlashcardsLambdaApplicationUtils.getStatementBuilder;

public class AnswerRepository {

    private final static String FIND_ANSWERS_FOR_QUESTIONS_SQL = """
            SELECT
            	*
            FROM
            	ANSWERS A
            WHERE
            	A.QUESTION_ID IN (%s)""";
    private final DataSource dataSource;

    public AnswerRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public List<Answer> findAnswersForQuestions(List<Long> questionIds) throws SQLException {
        try (
                var connection = dataSource.getConnection();
                var preparedStatement = getStatementBuilder(connection, FIND_ANSWERS_FOR_QUESTIONS_SQL, questionIds, JDBCType.BIGINT).getStatement();
                var resultSet = preparedStatement.executeQuery()
        ) {
            List<Answer> answers = new ArrayList<>();
            while (resultSet.next()) {
                answers.add(
                        Answer.builder()
                                .withId(resultSet.getLong("id"))
                                .withQuestionId(resultSet.getLong("question_id"))
                                .withAnswerText(resultSet.getString("answer_text"))
                                .withCorrect(resultSet.getBoolean("correct"))
                                .build()
                );
            }
            return answers;
        }

    }
}
