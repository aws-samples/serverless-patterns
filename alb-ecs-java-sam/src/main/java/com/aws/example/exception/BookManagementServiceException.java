package com.aws.example.exception;

/**
 *
 * @author biswanath
 */
public class BookManagementServiceException extends RuntimeException {
    
    public BookManagementServiceException(){}
    
    public BookManagementServiceException(String message)
    {
        super(message);
    }
    
}