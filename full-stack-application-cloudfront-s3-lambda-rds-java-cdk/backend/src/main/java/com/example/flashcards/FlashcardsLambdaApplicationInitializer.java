package com.example.flashcards;

import com.example.flashcards.repositories.AnswerRepository;
import com.example.flashcards.repositories.CategoryRepository;
import com.example.flashcards.repositories.QuestionRepository;
import com.example.flashcards.services.CategoryService;
import com.example.flashcards.services.FlashcardService;
import com.example.flashcards.services.SecretsManagerService;
import liquibase.*;
import liquibase.database.DatabaseFactory;
import liquibase.database.jvm.JdbcConnection;
import liquibase.resource.ClassLoaderResourceAccessor;
import liquibase.ui.LoggerUIService;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.postgresql.ds.PGSimpleDataSource;
import org.slf4j.bridge.SLF4JBridgeHandler;

import javax.sql.DataSource;
import java.util.Map;

import static com.example.flashcards.FlashcardsLambdaApplicationUtils.readEnvironmentVariable;

@Getter
@Slf4j
public class FlashcardsLambdaApplicationInitializer {

    static {
        configLogging();
    }

    private final DataSource dataSource;
    private final CategoryRepository categoryRepository;
    private final QuestionRepository questionRepository;
    private final AnswerRepository answerRepository;
    private final CategoryService categoryService;
    private final FlashcardService flashcardService;

    private static void configLogging() {
        try {
            // Switch Liquibase logging to the logback implementation that will also be used by the application.
            // Changing the logging level for any component can be done from the logback.xml file.
            SLF4JBridgeHandler.removeHandlersForRootLogger();
            SLF4JBridgeHandler.install();
            // This is to prevent some Liquibase unwanted logging.
            Scope.enter(Map.of(Scope.Attr.ui.name(), new LoggerUIService()));
            log.info("Logging configured successfully.");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // constructor used for testing
    public FlashcardsLambdaApplicationInitializer(DataSource dataSource) {
        this.dataSource = dataSource;
        this.categoryRepository = new CategoryRepository(dataSource);
        this.questionRepository = new QuestionRepository(dataSource);
        this.answerRepository = new AnswerRepository(dataSource);
        this.categoryService = new CategoryService(categoryRepository);
        this.flashcardService = new FlashcardService(questionRepository, answerRepository);
        this.runLiquibase();
    }

    public FlashcardsLambdaApplicationInitializer() {
        this.dataSource = createDataSource();
        this.categoryRepository = new CategoryRepository(dataSource);
        this.questionRepository = new QuestionRepository(dataSource);
        this.answerRepository = new AnswerRepository(dataSource);
        this.categoryService = new CategoryService(categoryRepository);
        this.flashcardService = new FlashcardService(questionRepository, answerRepository);
        this.runLiquibase();
    }

    private DataSource createDataSource() {
        var secretsManagerService = new SecretsManagerService();
        var dbEndpoint = readEnvironmentVariable("DB_ENDPOINT");
        var dbName = readEnvironmentVariable("DB_NAME");
        var dbPort = readEnvironmentVariable("DB_PORT");
        var awsRegion = readEnvironmentVariable("AWS_REGION");
        var dbCredentialsSecretName = readEnvironmentVariable("DB_CREDENTIALS_SECRET_NAME");
        var dbUser = readEnvironmentVariable("DB_USER");
        var dbPassword = secretsManagerService.readPasswordFromSecret(awsRegion, dbCredentialsSecretName);
        var datasource = new PGSimpleDataSource();
        datasource.setUrl("jdbc:postgresql://" + dbEndpoint + ":" + dbPort + "/" + dbName);
        datasource.setUser(dbUser);
        datasource.setPassword(dbPassword);
        return datasource;
    }

    private void runLiquibase() {
        try (
                var connection = new JdbcConnection(dataSource.getConnection());
                var database = DatabaseFactory.getInstance().findCorrectDatabaseImplementation(connection)
        ) {
            var liquibase = new Liquibase("liquibaseChangeLog.xml", new ClassLoaderResourceAccessor(), database);
            // This is to disable the Liquibase update summary so it will not show up and pollute the logs.
            liquibase.setShowSummary(UpdateSummaryEnum.OFF);
            liquibase.update(new Contexts(), new LabelExpression());
            log.info("Liquibase update executed successfully.");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
