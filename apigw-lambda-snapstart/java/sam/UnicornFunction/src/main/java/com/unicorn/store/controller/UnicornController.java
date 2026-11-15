// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.unicorn.store.controller;

import com.unicorn.store.model.Unicorn;
import com.unicorn.store.service.UnicornService;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/unicorns")
public class UnicornController {

    private static final Logger logger = LogManager.getLogger();

    private final UnicornService unicornService;

    public UnicornController(UnicornService unicornService) {
        this.unicornService = unicornService;
    }

    @GetMapping("/{unicornId}")
    public Unicorn retrieveUnicorn(@PathVariable String unicornId) {
        logger.debug("Received request to get unicorn with id {}", unicornId);
        return unicornService.retrieveUnicorn(unicornId);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Unicorn createUnicorn(@RequestBody Unicorn unicorn) {
        logger.debug("Received request to create a unicorn {}", unicorn);
        return unicornService.createUnicorn(unicorn);
    }

    @PutMapping("/{unicornId}")
    public Unicorn updateUnicorn(@PathVariable String unicornId, @RequestBody Unicorn unicorn) {
        logger.debug("Received request to update unicorn with id {} to {}", unicorn, unicornId);
        return unicornService.updateUnicorn(unicornId, unicorn);
    }

    @DeleteMapping("/{unicornId}")
    public void deleteUnicorn(@PathVariable String unicornId) {
        logger.debug("Received request to delete unicorn with id {}", unicornId);
        unicornService.deleteUnicorn(unicornId);
    }
}
