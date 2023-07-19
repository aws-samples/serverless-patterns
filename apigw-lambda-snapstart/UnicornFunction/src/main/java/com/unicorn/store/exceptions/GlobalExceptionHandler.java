package com.unicorn.store.exceptions;

import com.unicorn.store.model.ErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.Collections;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceSaveException.class)
    public ResponseEntity<ErrorResponse> resourceSaveException() {
        ErrorResponse errorResponse = new ErrorResponse(
                "Something went wrong while saving Unicorn.",
                Collections.singletonList("Unicorn could not be saved.")
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(errorResponse);
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> resourceNotFoundException() {
        ErrorResponse errorResponse = new ErrorResponse(
                "Unicorn was not found in DynamoDB.",
                Collections.singletonList("Requested Unicorn was not found.")
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(errorResponse);
    }

    @ExceptionHandler(ResourceDeletionException.class)
    public ResponseEntity<ErrorResponse> resourceDeletionException() {
        ErrorResponse errorResponse = new ErrorResponse(
                "Something went wrong while deleting Unicorn.",
                Collections.singletonList("Unicorn could not be deleted.")
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(errorResponse);
    }

    @ExceptionHandler(ResourceRetrievalException.class)
    public ResponseEntity<ErrorResponse> resourceRetrievalException() {
        ErrorResponse errorResponse = new ErrorResponse(
                "Something went wrong while retrieving Unicorn.",
                Collections.singletonList("Unicorn could not be retrieved.")
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(errorResponse);
    }

    @ExceptionHandler(ResourceUpdateException.class)
    public ResponseEntity<ErrorResponse> resourceUpdateException() {
        ErrorResponse errorResponse = new ErrorResponse(
                "Something went wrong while updating Unicorn.",
                Collections.singletonList("Unicorn could not be updated.")
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(errorResponse);
    }

}
