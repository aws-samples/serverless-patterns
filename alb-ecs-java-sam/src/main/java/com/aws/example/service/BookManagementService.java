package com.aws.example.service;

import com.aws.example.dto.BookDto;

import java.util.List;

/**
 *
 * @author biswanath
 */
public interface BookManagementService{

    public List<BookDto> getBooks();
    public BookDto createBook(BookDto userDto);
    public BookDto getBookByBookId(String userId);
    public void deleteBook(String userId);
    
}