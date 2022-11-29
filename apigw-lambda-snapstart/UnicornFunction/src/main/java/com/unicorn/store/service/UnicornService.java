package com.unicorn.store.service;

import com.unicorn.store.data.UnicornRepository;
import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.model.Unicorn;
import org.springframework.stereotype.Service;

@Service
public class UnicornService {
    private final UnicornRepository unicornRepository;

    public UnicornService(UnicornRepository unicornRepository) {
        this.unicornRepository = unicornRepository;
    }

    public Unicorn createUnicorn(Unicorn unicorn) {
        return unicornRepository.save(unicorn);
    }

    public Unicorn updateUnicorn(Unicorn unicorn, String unicornId) {
        unicorn.setId(unicornId);
        return unicornRepository.save(unicorn);
    }

    public Unicorn getUnicorn(String unicornId) {
        return unicornRepository.findById(unicornId).orElseThrow(ResourceNotFoundException::new);
    }

    public void deleteUnicorn(String unicornId) {
        Unicorn unicorn = unicornRepository.findById(unicornId).orElseThrow(ResourceNotFoundException::new);
        unicornRepository.delete(unicorn);
    }
}
