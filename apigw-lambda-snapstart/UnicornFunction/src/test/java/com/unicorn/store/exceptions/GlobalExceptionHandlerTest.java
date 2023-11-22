package com.unicorn.store.exceptions;

import com.unicorn.store.model.ErrorResponse;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayName("GlobalExceptionHandler Unit Test")
class GlobalExceptionHandlerTest {

    private GlobalExceptionHandler globalExceptionHandler;

    @BeforeEach
    void setup() {
        this.globalExceptionHandler = new GlobalExceptionHandler();
    }

    @Test
    @DisplayName("ResourceSaveException - 500 Response Code")
    void testResourceSaveException() {
        ResponseEntity<ErrorResponse> errorResponseResponseEntity = globalExceptionHandler.resourceSaveException();
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, errorResponseResponseEntity.getStatusCode());
        assertEquals("Something went wrong while saving Unicorn.", errorResponseResponseEntity.getBody().message());
    }

    @Test
    @DisplayName("ResourceNotFoundException - 404 Response Code")
    void testResourceNotFoundException() {
        ResponseEntity<ErrorResponse> errorResponseResponseEntity = globalExceptionHandler.resourceNotFoundException();
        assertEquals(HttpStatus.NOT_FOUND, errorResponseResponseEntity.getStatusCode());
        assertEquals("Unicorn was not found in DynamoDB.", errorResponseResponseEntity.getBody().message());
    }

    @Test
    @DisplayName("ResourceDeletionException - 500 Response Code")
    void testResourceDeletionException() {
        ResponseEntity<ErrorResponse> errorResponseResponseEntity = globalExceptionHandler.resourceDeletionException();
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, errorResponseResponseEntity.getStatusCode());
        assertEquals("Something went wrong while deleting Unicorn.", errorResponseResponseEntity.getBody().message());
    }

    @Test
    @DisplayName("ResourceRetrievalException - 500 Response Code")
    void testResourceRetrievalException() {
        ResponseEntity<ErrorResponse> errorResponseResponseEntity = globalExceptionHandler.resourceRetrievalException();
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, errorResponseResponseEntity.getStatusCode());
        assertEquals("Something went wrong while retrieving Unicorn.", errorResponseResponseEntity.getBody().message());
    }

    @Test
    @DisplayName("ResourceUpdateException - 500 Response Code")
    void testResourceUpdateException() {
        ResponseEntity<ErrorResponse> errorResponseResponseEntity = globalExceptionHandler.resourceUpdateException();
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, errorResponseResponseEntity.getStatusCode());
        assertEquals("Something went wrong while updating Unicorn.", errorResponseResponseEntity.getBody().message());
    }

}