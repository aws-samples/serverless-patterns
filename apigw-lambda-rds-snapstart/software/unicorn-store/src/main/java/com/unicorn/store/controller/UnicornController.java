package com.unicorn.store.controller;

import com.unicorn.store.model.Unicorn;
import com.unicorn.store.service.UnicornService;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Delete;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.PathVariable;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.annotation.Put;
import io.micronaut.http.annotation.Status;
import io.micronaut.http.uri.UriBuilder;

@Controller("/unicorns")
public class UnicornController {

    private final UnicornService unicornService;

    public UnicornController(UnicornService unicornService) {
        this.unicornService = unicornService;
    }

    @Post
    public HttpResponse<?> createUnicorn(@Body Unicorn unicorn) {
        Unicorn savedUnicorn = unicornService.createUnicorn(unicorn);
        return HttpResponse.created(UriBuilder.of("/unicorns").path(savedUnicorn.getId()).build());
    }

    @Put("/{unicornId}")
    public Unicorn updateUnicorn(@Body Unicorn unicorn, @PathVariable String unicornId) {
        return unicornService.updateUnicorn(unicorn, unicornId);
    }

    @Get("/{unicornId}")
    public Unicorn getUnicorn(@PathVariable String unicornId) {
        return unicornService.getUnicorn(unicornId);
    }

    @Delete("/{unicornId}")
    @Status(HttpStatus.NO_CONTENT)
    public void deleteUnicorn(@PathVariable String unicornId) {
        unicornService.deleteUnicorn(unicornId);
    }
}
