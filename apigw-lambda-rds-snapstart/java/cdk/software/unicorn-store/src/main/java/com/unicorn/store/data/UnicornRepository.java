package com.unicorn.store.data;

import com.unicorn.store.model.Unicorn;
import io.micronaut.data.jdbc.annotation.JdbcRepository;
import io.micronaut.data.model.query.builder.sql.Dialect;
import io.micronaut.data.repository.CrudRepository;

@JdbcRepository(dialect = Dialect.POSTGRES)
public interface UnicornRepository extends CrudRepository<Unicorn, String > {
}
