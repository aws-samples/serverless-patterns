package com.unicorn.store.service;

import com.unicorn.store.data.UnicornRepository;
import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.model.Unicorn;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Captor;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class UnicornServiceTest {

    @Mock
    private UnicornRepository unicornRepository;

    @Captor
    private ArgumentCaptor<Unicorn> unicornArgumentCaptor;

    private UnicornService unicornService;

    @BeforeEach
    void setup() {
        this.unicornService = new UnicornService(unicornRepository);
    }

    @Test
    @DisplayName("Create Unicorn saves Unicorn to Repository")
    void testCreateUnicorn() {
        when(unicornRepository.save(any())).thenReturn(createTestUnicornWithId());
        Unicorn savedUnicorn = unicornService.createUnicorn(createTestUnicorn());
        verify(unicornRepository, times(1)).save(unicornArgumentCaptor.capture());
        assertEquals(savedUnicorn.getName(), unicornArgumentCaptor.getValue().getName());
        assertEquals(savedUnicorn.getAge(), unicornArgumentCaptor.getValue().getAge());
        assertEquals(savedUnicorn.getSize(), unicornArgumentCaptor.getValue().getSize());
        assertEquals(savedUnicorn.getType(), unicornArgumentCaptor.getValue().getType());
    }

    @Test
    @DisplayName("Retrieve Unicorn retrieves Unicorn from Repository if found")
    void testRetrieveUnicornFound() {
        when(unicornRepository.findById("123")).thenReturn(Optional.of(createTestUnicornWithId()));
        Unicorn retrievedUnicorn = unicornService.retrieveUnicorn("123");
        verify(unicornRepository, times(1)).findById("123");
        assertEquals("123", retrievedUnicorn.getId());
        assertEquals("Something", retrievedUnicorn.getName());
        assertEquals("Older", retrievedUnicorn.getAge());
        assertEquals("Very big", retrievedUnicorn.getSize());
        assertEquals("Animal", retrievedUnicorn.getType());
    }

    @Test
    @DisplayName("Retrieve Unicorn throws ResourceNotFoundException when Unicorn not found in Repository")
    void testRetrieveUnicornNotFound() {
        when(unicornRepository.findById("123")).thenReturn(Optional.empty());
        ResourceNotFoundException resourceNotFoundException = assertThrows(ResourceNotFoundException.class,
                () -> unicornService.retrieveUnicorn("123"));
        verify(unicornRepository, times(1)).findById("123");
        assertEquals("Unicorn with id 123 not found", resourceNotFoundException.getMessage());
    }

    @Test
    @DisplayName("Update Unicorn updates Unicorn in Repository")
    void testUpdateUnicorn() {
        when(unicornRepository.update(any())).thenReturn(createTestUnicornWithId());
        Unicorn updatedUnicorn = unicornService.updateUnicorn("123", createTestUnicorn());
        verify(unicornRepository, times(1)).update(unicornArgumentCaptor.capture());
        assertEquals("123", updatedUnicorn.getId());
        assertEquals("Something", updatedUnicorn.getName());
        assertEquals("Older", updatedUnicorn.getAge());
        assertEquals("Very big", updatedUnicorn.getSize());
        assertEquals("Animal", updatedUnicorn.getType());
        assertEquals("123", unicornArgumentCaptor.getValue().getId());
    }

    @Test
    @DisplayName("Delete Unicorn deletes Unicorn from Repository")
    void testDeleteUnicorn() {
        unicornService.deleteUnicorn("123");
        verify(unicornRepository, times(1)).deleteById("123");
    }

    private Unicorn createTestUnicorn() {
        Unicorn unicorn = new Unicorn();
        unicorn.setName("Something");
        unicorn.setAge("Older");
        unicorn.setSize("Very big");
        unicorn.setType("Animal");
        return unicorn;
    }

    private Unicorn createTestUnicornWithId() {
        Unicorn unicorn = createTestUnicorn();
        unicorn.setId("123");
        return unicorn;
    }

}