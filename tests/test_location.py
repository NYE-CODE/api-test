"""Create, Edit, Delete a new location"""
import pytest

from utils.api import ApiTest
from utils.checking import APIResponseValidator
from utils.factories import LocationFactory


def test_create_valid_location(location_data):
    response_post = ApiTest.create_place(location_data)
    APIResponseValidator.validate_status_code(response_post, 200)
    APIResponseValidator.validate_required_keys(response_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    APIResponseValidator.validate_key_value(response_post, 'status', 'OK')


@pytest.mark.parametrize("invalid_location_data, expected_error_field", [
    ('missing_accuracy', 'accuracy'),
    ('invalid_accuracy', 'accuracy'),
], indirect=["invalid_location_data"])
def test_create_invalid_location(invalid_location_data, expected_error_field):
    response_post = ApiTest.create_place(invalid_location_data)
    APIResponseValidator.validate_status_code(response_post, 500)


def test_get_exist_location():
    response_get = ApiTest.get_place("334189580e1b16cb5bd53334fa973829")
    APIResponseValidator.validate_status_code(response_get, 200)
    APIResponseValidator.validate_required_keys(response_get,
                                                ['location', 'accuracy', 'name', 'phone_number',
                                                 'address', 'types', 'website', 'language'])
    APIResponseValidator.validate_key_value(response_get, 'address',
                                            '29, side layout, cohen 09')


def test_get_invalid_location():
    response_get = ApiTest.get_place(123456)
    APIResponseValidator.validate_status_code(response_get, 404)


def test_edit_location():
    place_id = "d303b3b4a63e91596594a2ade47f3370"
    new_address = LocationFactory.build().get('address')

    update_data = {
        "place_id": place_id,
        "address": new_address,
        "key": "qaclick123"
    }

    update_response = ApiTest.update_place(place_id, update_data)
    APIResponseValidator.validate_status_code(update_response, 200)
    APIResponseValidator.validate_required_keys(update_response, ['msg'])
    APIResponseValidator.validate_key_value(update_response, 'msg',
                                            'Address successfully updated')
