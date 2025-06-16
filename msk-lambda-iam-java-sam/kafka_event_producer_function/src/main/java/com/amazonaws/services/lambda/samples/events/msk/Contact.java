package com.amazonaws.services.lambda.samples.events.msk;

/**
 * POJO class representing a Contact based on the AVRO schema defined in Glue Schema Registry
 */
public class Contact {
    private String firstname;
    private String lastname;
    private String company;
    private String street;
    private String city;
    private String county;
    private String state;
    private String zip;
    private String homePhone;
    private String cellPhone;
    private String email;
    private String website;

    public Contact() {
    }

    public Contact(String firstname, String lastname, String company, String street, String city, String county,
                  String state, String zip, String homePhone, String cellPhone, String email, String website) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.company = company;
        this.street = street;
        this.city = city;
        this.county = county;
        this.state = state;
        this.zip = zip;
        this.homePhone = homePhone;
        this.cellPhone = cellPhone;
        this.email = email;
        this.website = website;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getCounty() {
        return county;
    }

    public void setCounty(String county) {
        this.county = county;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }

    public String getHomePhone() {
        return homePhone;
    }

    public void setHomePhone(String homePhone) {
        this.homePhone = homePhone;
    }

    public String getCellPhone() {
        return cellPhone;
    }

    public void setCellPhone(String cellPhone) {
        this.cellPhone = cellPhone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    @Override
    public String toString() {
        return "Contact{" +
                "firstname='" + firstname + '\'' +
                ", lastname='" + lastname + '\'' +
                ", company='" + company + '\'' +
                ", street='" + street + '\'' +
                ", city='" + city + '\'' +
                ", county='" + county + '\'' +
                ", state='" + state + '\'' +
                ", zip='" + zip + '\'' +
                ", homePhone='" + homePhone + '\'' +
                ", cellPhone='" + cellPhone + '\'' +
                ", email='" + email + '\'' +
                ", website='" + website + '\'' +
                '}';
    }
}
