from factory import Factory, LazyAttribute, Trait
from faker import Faker
import random

fake = Faker()


class LocationFactory(Factory):
    class Meta:
        model = dict

    location = LazyAttribute(lambda x: {
        "lat": float(fake.latitude()),
        "lng": float(fake.longitude())
    })
    accuracy = LazyAttribute(lambda x: fake.random_int(min=10, max=100))
    name = LazyAttribute(lambda x: fake.company())
    phone_number = LazyAttribute(lambda x: fake.phone_number())
    address = LazyAttribute(lambda x: fake.address())
    types = LazyAttribute(lambda x: random.sample(
        ["shoe park", "shop", "restaurant", "hotel", "cafe"], k=2))
    website = LazyAttribute(lambda x: fake.url())
    language = LazyAttribute(lambda x: fake.language_code())

    class Params:
        missing_accuracy = Trait(
            accuracy=None
        )
        invalid_accuracy = Trait(
            accuracy="invalid"
        )


