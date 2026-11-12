package com.amazonaws.samples.kafka.oauth;

import net.datafaker.Faker;

/**
 * A simple person record populated with Faker-generated data and serialized to
 * JSON by the producer.
 */
public class Person {
    private String firstName;
    private String lastName;
    private String streetAddress;
    private String apartmentNumber;
    private String city;
    private String state;
    private String zip;
    private String phoneNumber;
    private String email;

    public Person() {
    }

    /**
     * Build a Person with random, realistic-looking values.
     */
    public static Person random(Faker faker) {
        Person p = new Person();
        p.firstName = faker.name().firstName();
        p.lastName = faker.name().lastName();
        p.streetAddress = faker.address().streetAddress();
        p.apartmentNumber = faker.address().secondaryAddress();
        p.city = faker.address().city();
        p.state = faker.address().stateAbbr();
        p.zip = faker.address().zipCode();
        p.phoneNumber = faker.phoneNumber().phoneNumber();
        p.email = faker.internet().emailAddress();
        return p;
    }

    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public String getStreetAddress() { return streetAddress; }
    public String getApartmentNumber() { return apartmentNumber; }
    public String getCity() { return city; }
    public String getState() { return state; }
    public String getZip() { return zip; }
    public String getPhoneNumber() { return phoneNumber; }
    public String getEmail() { return email; }
}
