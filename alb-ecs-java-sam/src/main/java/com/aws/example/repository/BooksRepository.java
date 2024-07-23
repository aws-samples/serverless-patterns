package com.aws.example.repository;

import org.springframework.data.repository.CrudRepository;

import com.aws.example.entity.BookEntity;

/**
 *
 * @author biswanath
 */
public interface BooksRepository extends CrudRepository<BookEntity, Long>{
    BookEntity findBypageCount(int pageCount);
    BookEntity findByBookId(String bookId);
}