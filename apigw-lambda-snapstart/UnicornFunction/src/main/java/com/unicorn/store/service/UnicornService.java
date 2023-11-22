package com.unicorn.store.service;

import com.unicorn.store.data.UnicornRepository;
import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.model.Unicorn;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class UnicornService {

    private final UnicornRepository unicornRepository;

    public UnicornService(UnicornRepository unicornRepository) {
        this.unicornRepository = unicornRepository;
    }

    public Unicorn createUnicorn(Unicorn unicorn) {
        String unicornId = UUID.randomUUID().toString();
        unicorn.setId(unicornId);
        return unicornRepository.save(unicorn);
    }

    public Unicorn retrieveUnicorn(String unicornId) {
        return unicornRepository.findById(unicornId)
                .orElseThrow(() -> new ResourceNotFoundException(String.format("Unicorn with id %s not found", unicornId)));
    }

    public Unicorn updateUnicorn(String unicornId, Unicorn unicorn) {
        unicorn.setId(unicornId);
        return unicornRepository.update(unicorn);
    }

    public void deleteUnicorn(String unicornId) {
        unicornRepository.deleteById(unicornId);
    }
}
