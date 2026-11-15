package com.unicorn.broker.exceptions;

public class InvalidStockException extends RuntimeException{
    public InvalidStockException(String errorMessage) {
        super(errorMessage);
    }
}
