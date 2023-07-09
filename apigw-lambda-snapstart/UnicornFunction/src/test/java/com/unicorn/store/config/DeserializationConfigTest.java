package com.unicorn.store.config;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;

@DisplayName("DeserializationConfig Unit Test")
class DeserializationConfigTest {

    private DeserializationConfig deserializationConfig;

    @BeforeEach
    void setup() {
        this.deserializationConfig = new DeserializationConfig();
    }

    @Test
    @DisplayName("ObjectMapper is configured correctly")
    void testObjectMapperConfiguration() {
        ObjectMapper objectMapper = deserializationConfig.objectMapper();
        assertNotNull(objectMapper);

    }

    @Test
    @DisplayName("ObjectMapper is configured to not fail on unknown properties")
    void testObjectMapperConfigurationFailOnUnknown() {
        ObjectMapper objectMapper = deserializationConfig.objectMapper();
        boolean failOnUnknownProperties = objectMapper.getDeserializationConfig()
                .hasDeserializationFeatures(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES.getMask());
        assertFalse(failOnUnknownProperties);
    }

}