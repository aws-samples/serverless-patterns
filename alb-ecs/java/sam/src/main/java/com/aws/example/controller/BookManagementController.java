package com.aws.example.controller;

import java.io.IOException;
import java.lang.reflect.Type;
import java.net.InetAddress;
import java.net.URI;
import java.net.UnknownHostException;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;
import java.util.List;

import org.modelmapper.ModelMapper;
import org.modelmapper.TypeToken;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aws.example.dto.BookDto;
import com.aws.example.model.BookRequest;
import com.aws.example.model.BookResponse;
import com.aws.example.service.BookManagementService;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import jakarta.validation.Valid;

import java.net.http.HttpRequest;

/**
 *
 * @author biswanath
 */
@RestController
@RequestMapping("/books")
public class BookManagementController {


    final BookManagementService bookManagementService;

    final Environment environment;

    @Value("${server.port}")
    private String port;

    @Value("${ecs.container.metadata.uri}")
    private String metadataUri;

    private final Logger log = LoggerFactory.getLogger(this.getClass());

    BookManagementController(Environment environment, BookManagementService bookManagementService) {
        this.environment = environment;
        this.bookManagementService = bookManagementService;
    }

    @PostMapping
    public ResponseEntity<BookResponse> createBook(@Valid @RequestBody BookRequest requestModel) {
        ModelMapper modelMapper = new ModelMapper();
        BookDto bookDto = modelMapper.map(requestModel, BookDto.class);

        BookDto createdBookDetails = bookManagementService.createBook(bookDto);
        log.info("From BookDto.getBookId" + createdBookDetails.getBookId());
        BookResponse returnValue = modelMapper.map(createdBookDetails, BookResponse.class);
        log.info("Book created with id: " + returnValue.getBookId());

        return ResponseEntity.status(HttpStatus.CREATED).body(returnValue);
    }


    @GetMapping("/{bookId}")
    public ResponseEntity<BookResponse> getBook(@PathVariable("bookId") String bookId) {

        BookDto bookDto = bookManagementService.getBookByBookId(bookId);

        BookResponse returnValue = new ModelMapper().map(bookDto, BookResponse.class);

        return ResponseEntity.status(HttpStatus.OK).body(returnValue);
    }



    @GetMapping()
    public ResponseEntity<List<BookResponse>> getBooks() {

        List<BookDto> bookDtoList = bookManagementService.getBooks();

        Type listType = new TypeToken<List<BookResponse>>() {
        }.getType();

        List<BookResponse> returnValue = new ModelMapper().map(bookDtoList, listType);
        log.info("Total books in database table: " + returnValue.size());

        return ResponseEntity.status(HttpStatus.OK).body(returnValue);
    }

    
    @DeleteMapping("/{bookId}")
    public ResponseEntity deleteBook(@PathVariable("bookId") String bookId) {

        bookManagementService.deleteBook(bookId);

        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }	



    @GetMapping("/ip")
    public String getIp() {
        String returnValue;

        try {
            InetAddress ipAddr = InetAddress.getLocalHost();
            returnValue = ipAddr.getHostAddress();
        } catch (UnknownHostException ex) {
            returnValue = ex.getLocalizedMessage();
        }

        return returnValue;
    }

    @GetMapping("/container-ip")
    public String getContainerPrivateIp() {
        String privateIp;
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                                        .uri(URI.create(metadataUri))
                                        .build();

        HttpResponse<String> response;
        try {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JsonNode json = new ObjectMapper().readTree(response.body());

            privateIp = json.get("Networks")
                                .get(0)
                                .get("IPv4Addresses")
                                .get(0)
                                .textValue();
        
        } catch (IOException e) {
            privateIp = e.getLocalizedMessage();
            e.printStackTrace();
        } catch (InterruptedException e) {
            privateIp = e.getLocalizedMessage();
            e.printStackTrace();
        }

        return privateIp;
    }

}