package com.aws.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.env.Environment;
import org.springframework.web.client.RestTemplate;

/**
 *
 * @author biswanath
 */
@SpringBootApplication
public class BookManagementApi {

    final Environment environment;

    BookManagementApi(Environment environment) {
        this.environment = environment;
    }

    public static void main(String[] args) {
        SpringApplication.run(BookManagementApi.class, args);
    }


    @Bean
    public SpringApplicationContext springApplicationContext() {
        return new SpringApplicationContext();
    }

    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }

}