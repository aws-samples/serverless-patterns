package com.aws.example.service;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import org.modelmapper.ModelMapper;
import org.modelmapper.TypeToken;
import org.modelmapper.convention.MatchingStrategies;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.env.Environment;


import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;


import com.aws.example.dto.BookDto;
import com.aws.example.entity.BookEntity;
import com.aws.example.exception.BookManagementServiceException;
import com.aws.example.repository.BooksRepository;

/**
 *
 * @author biswanath
 */
@Service
public class BookManagementServiceImpl implements BookManagementService {

	BooksRepository booksRepository;
	RestTemplate restTemplate;
	Environment environment;
	Logger logger = LoggerFactory.getLogger(this.getClass());


	public BookManagementServiceImpl(BooksRepository booksRepository,
			RestTemplate restTemplate, Environment environment) {
		this.booksRepository = booksRepository;
		this.restTemplate = restTemplate;
		this.environment = environment;
	}

	@Override
	public BookDto createBook(BookDto bookDto) {

		ModelMapper modelMapper = new ModelMapper();
		modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);

		BookEntity bookEntity = modelMapper.map(bookDto, BookEntity.class);

		bookEntity.setBookId(UUID.randomUUID().toString());

		try {
			BookEntity storedBookDetails = booksRepository.save(bookEntity);
			return modelMapper.map(storedBookDetails, BookDto.class);
		} catch (Exception e) {
			throw new BookManagementServiceException("Unable to save the book. Please check the input parameters.");
		}

	}


	@Override
	public void deleteBook(String bookId) {


		BookEntity bookEntity = booksRepository.findByBookId(bookId);

		if (bookEntity == null)
			throw new BookManagementServiceException("Book not found");

		booksRepository.delete(bookEntity);

	}

	@Override
	public BookDto getBookByBookId(String bookId) throws BookManagementServiceException {
		BookEntity bookEntity = booksRepository.findByBookId(bookId);
		if (bookEntity == null)
			throw new BookManagementServiceException(environment.getProperty("books.exceptions.book-not-found"));

		return new ModelMapper().map(bookEntity, BookDto.class);
	}

	@Override
	public List<BookDto> getBooks() {
		List<BookEntity> bookEntities = (List<BookEntity>) booksRepository.findAll();

		if (bookEntities == null || bookEntities.isEmpty())
			return new ArrayList<>();

		Type listType = new TypeToken<List<BookDto>>() {
		}.getType();

		List<BookDto> returnValue = new ModelMapper().map(bookEntities, listType);

		return returnValue;
	}
}
