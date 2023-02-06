package com.unicorn.store.service;

import jakarta.inject.Singleton;

import java.util.UUID;

@Singleton
public class UUIDIdGenerator implements IdGenerator {
    @Override
    public String generate() {
        return UUID.randomUUID().toString();
    }
}
