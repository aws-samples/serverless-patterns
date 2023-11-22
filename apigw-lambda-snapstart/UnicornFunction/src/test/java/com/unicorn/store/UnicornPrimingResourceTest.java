package com.unicorn.store;

import com.unicorn.store.controller.UnicornController;
import org.crac.Resource;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

@ExtendWith(MockitoExtension.class)
@DisplayName("UnicornPrimingResource Unit Test")
class UnicornPrimingResourceTest {

    private UnicornPrimingResource unicornPrimingResource;

    @Mock
    private UnicornController unicornController;

    @BeforeEach
    void setup() {
        this.unicornPrimingResource = new UnicornPrimingResource(unicornController);
    }

    @Test
    @DisplayName("UnicornPrimingResourceTest is a CRAC Resource")
    void testIsACracResource() {
        assertInstanceOf(Resource.class, unicornPrimingResource);
    }

    @Test
    @DisplayName("UnicornPrimingResourceTest JIT Compiles code paths before checkpoint")
    void testJitCompilationPreCheckpoint() {
        unicornPrimingResource.beforeCheckpoint(null);
        verify(unicornController, times(1)).retrieveUnicorn(any());
    }

    @Test
    @DisplayName("Before Checkpoint Hook does not throw exception")
    void testBeforeCheckpointNoException() {
        doThrow(new RuntimeException("Some exception"))
                .when(unicornController).retrieveUnicorn(any());
        assertDoesNotThrow(() -> unicornPrimingResource.beforeCheckpoint(null));
    }

}