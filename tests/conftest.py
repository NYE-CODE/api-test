import pytest
from utils.factories import LocationFactory


@pytest.fixture
def location_data():
    return LocationFactory.build()


@pytest.fixture
def invalid_location_data(request):
    trait = request.param
    invalid_data = LocationFactory.build(**{trait: True})
    return invalid_data


