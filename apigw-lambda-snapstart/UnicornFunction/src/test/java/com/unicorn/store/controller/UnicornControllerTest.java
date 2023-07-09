package com.unicorn.store.controller;

import com.unicorn.store.exceptions.ResourceDeletionException;
import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.exceptions.ResourceRetrievalException;
import com.unicorn.store.exceptions.ResourceSaveException;
import com.unicorn.store.exceptions.ResourceUpdateException;
import com.unicorn.store.model.Unicorn;
import com.unicorn.store.service.UnicornService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(UnicornController.class)
@DisplayName("Unicorn Controller Web Layer Test")
class UnicornControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UnicornService unicornService;

    @Test
    @DisplayName("GET /unicorns/{unicornId} - 200")
    void testGetUnicornByIdSuccess() throws Exception {
        when(unicornService.retrieveUnicorn("123"))
                .thenReturn(createTestUnicorn());
        mockMvc.perform(get("/unicorns/123"))
                .andDo(print())
                .andExpect(status().isOk())
                .andExpect(content().json("""
                        {
                           "id": "123",
                           "name": "Something",
                           "age": "Older",
                           "size": "Very big",
                           "type": "Animal"
                        }
                        """, true));
    }

    @Test
    @DisplayName("GET /unicorns/{unicornId} - 404")
    void testGetUnicornByIdNotFound() throws Exception {
        when(unicornService.retrieveUnicorn("999"))
                .thenThrow(new ResourceNotFoundException("Unicorn with id 999 not found."));
        mockMvc.perform(get("/unicorns/999"))
                .andDo(print())
                .andExpect(status().isNotFound())
                .andExpect(content().json("""
                        {
                           "message": "Unicorn was not found in DynamoDB.",
                           "errors": [
                             "Requested Unicorn was not found."
                           ]
                         }
                        """, true));
    }

    @Test
    @DisplayName("GET /unicorns/{unicornId} - 500")
    void testGetUnicornByIdSomethingWentWrong() throws Exception {
        when(unicornService.retrieveUnicorn("999"))
                .thenThrow(new ResourceRetrievalException("Could not retrieve unicorn with id 999 from DynamoDB."));
        mockMvc.perform(get("/unicorns/999"))
                .andDo(print())
                .andExpect(status().isInternalServerError())
                .andExpect(content().json("""
                        {
                           "message": "Something went wrong while retrieving Unicorn.",
                           "errors": [
                             "Unicorn could not be retrieved."
                           ]
                         }
                        """, true));
    }

    @Test
    @DisplayName("POST /unicorns/ - 201")
    void testPostUnicornCreated() throws Exception {
        when(unicornService.createUnicorn(any()))
                .thenReturn(createTestUnicorn());
        mockMvc.perform(post("/unicorns").contentType(MediaType.APPLICATION_JSON).content("""
                        {
                        "name": "Something",
                        "age": "Older",
                        "size": "Very big",
                        "type": "Animal"
                        }
                        """))
                .andDo(print())
                .andExpect(status().isCreated())
                .andExpect(content().json("""
                        {
                           "id": "123",
                           "name": "Something",
                           "age": "Older",
                           "size": "Very big",
                           "type": "Animal"
                        }
                        """, true));
    }

    @Test
    @DisplayName("POST /unicorns/ - 500")
    void testPostUnicornSomethingWentWrong() throws Exception {
        when(unicornService.createUnicorn(any()))
                .thenThrow(new ResourceSaveException("Unicorn could not be saved to DynamoDB."));
        mockMvc.perform(post("/unicorns").contentType(MediaType.APPLICATION_JSON).content("""
                        {
                        "name": "Something",
                        "age": "Older",
                        "size": "Very big",
                        "type": "Animal"
                        }
                        """))
                .andDo(print())
                .andExpect(status().isInternalServerError())
                .andExpect(content().json("""
                        {
                           "message": "Something went wrong while saving Unicorn.",
                           "errors": [
                             "Unicorn could not be saved."
                           ]
                         }
                        """, true));
    }

    @Test
    @DisplayName("PUT /unicorns/{unicornId} - 200")
    void testPutUnicornSuccess() throws Exception {
        when(unicornService.updateUnicorn(eq("123"), any()))
                .thenReturn(createTestUnicorn());
        when(unicornService.createUnicorn(any()))
                .thenReturn(createTestUnicorn());
        mockMvc.perform(put("/unicorns/123").contentType(MediaType.APPLICATION_JSON).content("""
                        {
                        "name": "Something",
                        "age": "Older",
                        "size": "Very big",
                        "type": "Animal"
                        }
                        """))
                .andDo(print())
                .andExpect(status().isOk())
                .andExpect(content().json("""
                        {
                           "id": "123",
                           "name": "Something",
                           "age": "Older",
                           "size": "Very big",
                           "type": "Animal"
                        }
                        """, true));
    }

    @Test
    @DisplayName("PUT /unicorns/{unicornId} - 404")
    void testPutUnicornNotFound() throws Exception {
        when(unicornService.updateUnicorn(eq("999"), any()))
                .thenThrow(new ResourceNotFoundException("Unicorn with id 999 not found."));
        mockMvc.perform(put("/unicorns/999").contentType(MediaType.APPLICATION_JSON).content("""
                        {
                        "name": "Something",
                        "age": "Older",
                        "size": "Very big",
                        "type": "Animal"
                        }
                        """))
                .andDo(print())
                .andExpect(status().isNotFound())
                .andExpect(content().json("""
                        {
                           "message": "Unicorn was not found in DynamoDB.",
                           "errors": [
                             "Requested Unicorn was not found."
                           ]
                         }
                        """, true));
    }

    @Test
    @DisplayName("PUT /unicorns/{unicornId} - 500")
    void testPutUnicornSomethingWentWrong() throws Exception {
        when(unicornService.updateUnicorn(eq("999"), any()))
                .thenThrow(new ResourceUpdateException("Unicorn could not be updated in DynamoDB."));
        mockMvc.perform(put("/unicorns/999").contentType(MediaType.APPLICATION_JSON).content("""
                        {
                        "name": "Something",
                        "age": "Older",
                        "size": "Very big",
                        "type": "Animal"
                        }
                        """))
                .andDo(print())
                .andExpect(status().isInternalServerError())
                .andExpect(content().json("""
                        {
                           "message": "Something went wrong while updating Unicorn.",
                           "errors": [
                             "Unicorn could not be updated."
                           ]
                         }
                        """, true));
    }

    @Test
    @DisplayName("DELETE /unicorns/{unicornId} - 200")
    void testDeleteUnicornSuccess() throws Exception {
        mockMvc.perform(delete("/unicorns/123"))
                .andDo(print())
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("DELETE /unicorns/{unicornId} - 500")
    void testDeleteUnicornSomethingWentWrong() throws Exception {
        doThrow(new ResourceDeletionException("Could not delete unicorn with id 999 from DynamoDB."))
                .when(unicornService).deleteUnicorn("999");
        mockMvc.perform(delete("/unicorns/999"))
                .andDo(print())
                .andExpect(status().isInternalServerError())
                .andExpect(content().json("""
                        {
                           "message": "Something went wrong while deleting Unicorn.",
                           "errors": [
                             "Unicorn could not be deleted."
                           ]
                         }
                        """, true));
    }

    private Unicorn createTestUnicorn() {
        Unicorn unicorn = new Unicorn();
        unicorn.setId("123");
        unicorn.setName("Something");
        unicorn.setAge("Older");
        unicorn.setSize("Very big");
        unicorn.setType("Animal");
        return unicorn;
    }

}