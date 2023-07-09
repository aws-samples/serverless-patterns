package com.unicorn.store.data;

import com.unicorn.store.model.Unicorn;

import java.util.Optional;

public interface UnicornRepository {

    Unicorn save(Unicorn unicorn);

    Optional<Unicorn> findById(String unicornId);

    void deleteById(String unicornId);

    Unicorn update(Unicorn unicorn);

}
