package com.unicorn.store.controller;

import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.model.Unicorn;
import com.unicorn.store.service.UnicornService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import static org.springframework.http.HttpStatus.INTERNAL_SERVER_ERROR;
import static org.springframework.http.HttpStatus.NOT_FOUND;

@RestController
public class UnicornController {

    private final UnicornService unicornService;
    private static final Logger logger = LoggerFactory.getLogger(UnicornController.class);

    public UnicornController(UnicornService unicornService) {
        this.unicornService = unicornService;
    }

    @PostMapping("/unicorns")
    public ResponseEntity<Unicorn> createUnicorn(@RequestBody Unicorn unicorn) {
        try {
            var savedUnicorn = unicornService.createUnicorn(unicorn);
            return ResponseEntity.ok(savedUnicorn);
        } catch (Exception e) {
            String errorMsg = "Error creating unicorn";
            logger.error(errorMsg, e);
            throw new ResponseStatusException(INTERNAL_SERVER_ERROR, errorMsg, e);
        }
    }

    @PutMapping("/unicorns/{unicornId}")
    public ResponseEntity<Unicorn> updateUnicorn(@RequestBody Unicorn unicorn, @PathVariable String unicornId) {
        try {
            var savedUnicorn = unicornService.updateUnicorn(unicorn, unicornId);
            return ResponseEntity.ok(savedUnicorn);
        } catch (Exception e) {
            String errorMsg = "Error updating unicorn";
            logger.error(errorMsg, e);
            throw new ResponseStatusException(INTERNAL_SERVER_ERROR, errorMsg, e);
        }
    }

    @GetMapping("/unicorns/{unicornId}")
    public ResponseEntity<Unicorn> getUnicorn(@PathVariable String unicornId) {
        try {
            var unicorn = unicornService.getUnicorn(unicornId);
            return ResponseEntity.ok(unicorn);
        } catch (ResourceNotFoundException e) {
            String errorMsg = "Unicorn not found";
            logger.error(errorMsg, e);
            throw new ResponseStatusException(NOT_FOUND, errorMsg, e);
        }
    }

    @DeleteMapping("/unicorns/{unicornId}")
    public ResponseEntity<String> deleteUnicorn(@PathVariable String unicornId) {
        try {
            unicornService.deleteUnicorn(unicornId);
            return ResponseEntity.ok().build();
        } catch (ResourceNotFoundException e) {
            String errorMsg = "Unicorn not found";
            logger.error(errorMsg, e);
            throw new ResponseStatusException(NOT_FOUND, errorMsg, e);
        }
    }
}
