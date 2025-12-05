package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

import com.google.gson.annotations.SerializedName;

public class FullDocument {
   	private String _id;
   	@SerializedName("Firstname")
	private String firstname;
   	@SerializedName("Lastname")
    private String lastname;
   	@SerializedName("Street")
    private String street;
   	@SerializedName("City")
    private String city;
   	@SerializedName("County")
    private String county;
   	@SerializedName("State")
    private String state;
   	@SerializedName("Zip")
    private String zip;
   	@SerializedName("HomePhone")
    private String homePhone;
   	@SerializedName("CellPhone")
    private String cellPhone;
   	@SerializedName("Email")
    private String email;
   	@SerializedName("Company")
    private String company;
   	@SerializedName("Website")
    private String website;
	/**
	 * 
	 */
	public FullDocument() {
		super();
	}
	/**
	 * @param _id
	 * @param firstname
	 * @param lastname
	 * @param street
	 * @param city
	 * @param county
	 * @param state
	 * @param zip
	 * @param homePhone
	 * @param cellPhone
	 * @param email
	 * @param company
	 * @param website
	 */
	public FullDocument(String _id, String firstname, String lastname, String street, String city, String county,
			String state, String zip, String homePhone, String cellPhone, String email, String company,
			String website) {
		super();
		this._id = _id;
		this.firstname = firstname;
		this.lastname = lastname;
		this.street = street;
		this.city = city;
		this.county = county;
		this.state = state;
		this.zip = zip;
		this.homePhone = homePhone;
		this.cellPhone = cellPhone;
		this.email = email;
		this.company = company;
		this.website = website;
	}
	/**
	 * @return the _id
	 */
	public String get_id() {
		return _id;
	}
	/**
	 * @param _id the _id to set
	 */
	public void set_id(String _id) {
		this._id = _id;
	}
	/**
	 * @return the firstname
	 */
	public String getFirstname() {
		return firstname;
	}
	/**
	 * @param firstname the firstname to set
	 */
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
	/**
	 * @return the lastname
	 */
	public String getLastname() {
		return lastname;
	}
	/**
	 * @param lastname the lastname to set
	 */
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	/**
	 * @return the street
	 */
	public String getStreet() {
		return street;
	}
	/**
	 * @param street the street to set
	 */
	public void setStreet(String street) {
		this.street = street;
	}
	/**
	 * @return the city
	 */
	public String getCity() {
		return city;
	}
	/**
	 * @param city the city to set
	 */
	public void setCity(String city) {
		this.city = city;
	}
	/**
	 * @return the county
	 */
	public String getCounty() {
		return county;
	}
	/**
	 * @param county the county to set
	 */
	public void setCounty(String county) {
		this.county = county;
	}
	/**
	 * @return the state
	 */
	public String getState() {
		return state;
	}
	/**
	 * @param state the state to set
	 */
	public void setState(String state) {
		this.state = state;
	}
	/**
	 * @return the zip
	 */
	public String getZip() {
		return zip;
	}
	/**
	 * @param zip the zip to set
	 */
	public void setZip(String zip) {
		this.zip = zip;
	}
	/**
	 * @return the homePhone
	 */
	public String getHomePhone() {
		return homePhone;
	}
	/**
	 * @param homePhone the homePhone to set
	 */
	public void setHomePhone(String homePhone) {
		this.homePhone = homePhone;
	}
	/**
	 * @return the cellPhone
	 */
	public String getCellPhone() {
		return cellPhone;
	}
	/**
	 * @param cellPhone the cellPhone to set
	 */
	public void setCellPhone(String cellPhone) {
		this.cellPhone = cellPhone;
	}
	/**
	 * @return the email
	 */
	public String getEmail() {
		return email;
	}
	/**
	 * @param email the email to set
	 */
	public void setEmail(String email) {
		this.email = email;
	}
	/**
	 * @return the company
	 */
	public String getCompany() {
		return company;
	}
	/**
	 * @param company the company to set
	 */
	public void setCompany(String company) {
		this.company = company;
	}
	/**
	 * @return the website
	 */
	public String getWebsite() {
		return website;
	}
	/**
	 * @param website the website to set
	 */
	public void setWebsite(String website) {
		this.website = website;
	}
	@Override
	public int hashCode() {
		return Objects.hash(_id, cellPhone, city, company, county, email, firstname, homePhone, lastname, state, street,
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
		FullDocument other = (FullDocument) obj;
		return Objects.equals(_id, other._id) && Objects.equals(cellPhone, other.cellPhone)
				&& Objects.equals(city, other.city) && Objects.equals(company, other.company)
				&& Objects.equals(county, other.county) && Objects.equals(email, other.email)
				&& Objects.equals(firstname, other.firstname) && Objects.equals(homePhone, other.homePhone)
				&& Objects.equals(lastname, other.lastname) && Objects.equals(state, other.state)
				&& Objects.equals(street, other.street) && Objects.equals(website, other.website)
				&& Objects.equals(zip, other.zip);
	}
	@Override
	public String toString() {
		return "FullDocument [_id=" + _id + ", firstname=" + firstname + ", lastname=" + lastname + ", street=" + street
				+ ", city=" + city + ", county=" + county + ", state=" + state + ", zip=" + zip + ", homePhone="
				+ homePhone + ", cellPhone=" + cellPhone + ", email=" + email + ", company=" + company + ", website="
				+ website + "]";
	}
    
}
