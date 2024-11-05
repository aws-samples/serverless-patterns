package com.example.flashcards.services;

import com.example.flashcards.model.dto.FindFlashcardsRequest;
import com.example.flashcards.model.dto.FindFlashcardsResponse;
import com.example.flashcards.model.dto.Flashcard;
import com.example.flashcards.model.entities.Answer;
import com.example.flashcards.model.entities.Question;
import com.example.flashcards.repositories.AnswerRepository;
import com.example.flashcards.repositories.QuestionRepository;
import org.apache.commons.lang3.StringUtils;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.function.Predicate;

import static org.apache.commons.collections4.CollectionUtils.isEmpty;

public class FlashcardService {

    private final QuestionRepository questionRepository;
    private final AnswerRepository answerRepository;
    private final Predicate<Answer> correctAnswerPredicate = Answer::correct;

    public FlashcardService(QuestionRepository questionRepository, AnswerRepository answerRepository) {
        this.questionRepository = questionRepository;
        this.answerRepository = answerRepository;
    }

    public FindFlashcardsResponse findFlashcards(FindFlashcardsRequest request) throws SQLException {
        var categoryId = request.categoryId();
        var maxItems = request.maxItems();
        var questions = questionRepository.findRandomQuestions(categoryId, maxItems);
        var questionIds = Optional.ofNullable(questions)
                .map(List::stream)
                .map(
                        questionStream -> questionStream
                                .map(Question::id)
                                .collect(() -> new ArrayList<Long>(), List::add, List::addAll)
                )
                .orElseGet(ArrayList::new);
        var answers = answerRepository.findAnswersForQuestions(questionIds);
        var flashcards = Optional.ofNullable(questions)
                .map(
                        questionaList -> questionaList.stream()
                                .filter(Objects::nonNull)
                                .map(
                                        question -> Flashcard.builder()
                                                .withQuestion(question.questionText())
                                                .withCorrectAnswer(
                                                        answers.stream()
                                                                .filter(getAnswerPredicate(question, correctAnswerPredicate))
                                                                .map(Answer::answerText)
                                                                .findAny()
                                                                .orElse(null)
                                                )
                                                .withIncorrectAnswers(
                                                        answers.stream()
                                                                .filter(getAnswerPredicate(question, correctAnswerPredicate.negate()))
                                                                .map(Answer::answerText)
                                                                .collect(ArrayList::new, List::add, List::addAll)
                                                )
                                                .build()
                                )
                                .map(
                                        flashCard -> Optional.ofNullable(flashCard)
                                                .filter(card -> StringUtils.isNotBlank(card.question()))
                                                .filter(card -> StringUtils.isNotBlank(card.correctAnswer()))
                                                .filter(card -> !isEmpty(card.incorrectAnswers()))
                                                .filter(card -> card.incorrectAnswers().stream().noneMatch(StringUtils::isBlank))
                                                .filter(card -> card.incorrectAnswers().size() >= 2)
                                                .orElseThrow(() -> new RuntimeException("Invalid flash card found."))
                                )
                                .collect(() -> new ArrayList<Flashcard>(), List::add, List::addAll)
                ).orElseGet(ArrayList::new);
        return FindFlashcardsResponse.builder()
                .withFlashcards(flashcards)
                .build();
    }


    private static Predicate<Answer> getAnswerPredicate(Question question, Predicate<Answer> correctAnswerPredicate) {
        Predicate<Answer> validAnswerPredicate = (answer) -> Optional.ofNullable(answer)
                .map(Answer::questionId)
                .flatMap(
                        id -> Optional.ofNullable(question)
                                .map(Question::id)
                                .map(id::compareTo)
                                .filter(value -> value == 0)
                )
                .isPresent();
        return validAnswerPredicate.and(correctAnswerPredicate);
    }
}
