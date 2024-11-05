package com.example.flashcards;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Getter;
import software.amazon.awssdk.utils.StringUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.SQLType;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;
import java.util.function.Supplier;
import java.util.stream.Collectors;

public class FlashcardsLambdaApplicationUtils {

    @Getter
    public static class StatementBuilder {
        private final PreparedStatement statement;

        public StatementBuilder(Connection connection, String sql) throws SQLException {
            this.statement = connection.prepareStatement(sql);
        }

        public <T> StatementBuilder(Connection connection, String sql, List<T> parameters, SQLType parameterSqlType) throws SQLException {
            this.statement = connection.prepareStatement(
                    String.format(
                            sql,
                            parameters.stream()
                                    .map(v -> "?")
                                    .collect(Collectors.joining(", "))
                    )
            );
            for (int parameterIndex = 0; parameterIndex < parameters.size(); parameterIndex++) {
                setParameter(parameterIndex + 1, parameters.get(parameterIndex), parameterSqlType);
            }
        }

        public <T> StatementBuilder setParameter(int parameterIndex, T parameter, SQLType parameterSqlType) throws SQLException {
            statement.setObject(parameterIndex, parameter, parameterSqlType.getVendorTypeNumber(), 0);
            return this;
        }

    }

    public static String writeValue(Object object) {
        try {
            return getObjectMapperSupplier().get().writeValueAsString(object);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    public static <T> T readValue(String jsonString, Class<T> type) {
        try {
            return getObjectMapperSupplier().get().readValue(jsonString, type);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    public static JsonNode readTree(String jsonString) {
        try {
            return getObjectMapperSupplier().get().readTree(jsonString);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    public static String readEnvironmentVariable(String variableName) {
        return Optional.ofNullable(variableName)
                .map(System::getenv)
                .filter(StringUtils::isNotBlank)
                .orElseThrow(() -> new NoSuchElementException("Environment variable [" + variableName + "] not found."));
    }

    public static Supplier<ObjectMapper> getObjectMapperSupplier() {
        return ObjectMapper::new;
    }

    public static StatementBuilder getStatementBuilder(Connection connection, String sql) throws SQLException {
        return new StatementBuilder(connection, sql);
    }

    public static <T> StatementBuilder getStatementBuilder(Connection connection, String sql, List<T> parameters, SQLType sqlType) throws SQLException {
        return new StatementBuilder(connection, sql, parameters, sqlType);
    }
}
