// A person record populated with Faker-generated data and serialized to JSON by
// the producer.
import { faker } from "@faker-js/faker";

export function randomPerson() {
  return {
    firstName: faker.person.firstName(),
    lastName: faker.person.lastName(),
    streetAddress: faker.location.streetAddress(),
    apartmentNumber: faker.location.secondaryAddress(),
    city: faker.location.city(),
    state: faker.location.state({ abbreviated: true }),
    zip: faker.location.zipCode(),
    phoneNumber: faker.phone.number(),
    email: faker.internet.email(),
  };
}
