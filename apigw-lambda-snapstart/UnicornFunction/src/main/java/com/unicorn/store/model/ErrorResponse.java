package com.unicorn.store.model;

import java.util.List;

public record ErrorResponse(
        String message,
        List<String> errors
) {
}
