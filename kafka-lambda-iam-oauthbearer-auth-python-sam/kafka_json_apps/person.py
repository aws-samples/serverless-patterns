"""A simple person record populated with Faker-generated data and serialized to
JSON by the producer."""


def random_person(faker):
    """Build a person dict with random, realistic-looking values."""
    return {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "streetAddress": faker.street_address(),
        "apartmentNumber": faker.secondary_address(),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "zip": faker.zipcode(),
        "phoneNumber": faker.phone_number(),
        "email": faker.email(),
    }
