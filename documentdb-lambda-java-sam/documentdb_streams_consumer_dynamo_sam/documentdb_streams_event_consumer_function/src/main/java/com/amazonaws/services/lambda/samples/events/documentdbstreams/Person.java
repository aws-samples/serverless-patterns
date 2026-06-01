package com.amazonaws.services.lambda.samples.events.documentdbstreams;

import java.util.Objects;

import com.google.gson.Gson;


public class Person {
	
	String firstname;
	String lastname;
	String company;
	String street;
	String city;
	String county;
	String state;
	String zip;
	String homePhone;
	String cellPhone;
	String email;
	String website;
	public Person() {
		super();
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
		return "Person [firstname=" + firstname + ", lastname=" + lastname + ", company=" + company + ", street="
				+ street + ", city=" + city + ", county=" + county + ", state=" + state + ", zip=" + zip
				+ ", homePhone=" + homePhone + ", cellPhone=" + cellPhone + ", email=" + email + ", website=" + website
				+ "]";
	}
	
	public String toJson() {
		Gson gson = new Gson();
		return gson.toJson(this);
	}
	@Override
	public int hashCode() {
		return Objects.hash(cellPhone, city, company, county, email, firstname, homePhone, lastname, state, street,
				website, zip);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Person other = (Person) obj;
		return Objects.equals(cellPhone, other.cellPhone) && Objects.equals(city, other.city)
				&& Objects.equals(company, other.company) && Objects.equals(county, other.county)
				&& Objects.equals(email, other.email) && Objects.equals(firstname, other.firstname)
				&& Objects.equals(homePhone, other.homePhone) && Objects.equals(lastname, other.lastname)
				&& Objects.equals(state, other.state) && Objects.equals(street, other.street)
				&& Objects.equals(website, other.website) && Objects.equals(zip, other.zip);
	}
	
}
