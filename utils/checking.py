"""Utility for validating API responses."""
import json
import requests


class APIResponseValidator():
    """Validates the status code of API response"""

    @staticmethod
    def validate_status_code(response: requests.Response, expected_status_code):
        assert response.status_code == expected_status_code, 'Actual status code does not match with the expected'
        print(f'\nStatus code is correct: {response.status_code}')

    """Validates the presence of required keys in the JSON response"""

    @staticmethod
    def validate_required_keys(response: requests.Response, expected_keys):
        response_keys = json.loads(response.text)
        assert list(response_keys) == expected_keys, 'Response is missing some expected keys'
        print(f'All required keys are present in the response {list(response_keys)}')

    @staticmethod
    def validate_key_value(response: requests.Response, key, expected_value):
        response_json = response.json()
        actual_value = response_json.get(key)
        print(actual_value)
        assert actual_value == expected_value, 'Actual value does not match with the expected'
        print(f'Value of "{key}" is correct: {actual_value}')

    """Confirms the presence of a specific word in the value of a key in the JSON response"""

    @staticmethod
    def confirm_word_in_value(response: requests.Response, key, word):
        response_json = response.json()
        actual_value = response_json.get(key)
        assert word in actual_value, f'Word "{word}" not found in value of key "{key}"'
        print(f'Key "{key}" contains the word "{word}" in its value')

    @staticmethod
    def validate_error_message(response: requests.Response, expected_error_field):
        response_json = response.json()
        actual_error_message = response_json.get('error_message', '')
        assert expected_error_field in actual_error_message, \
            f"Expected error related to '{expected_error_field}', but got '{actual_error_message}'"
        print(f"Error message is correct: {actual_error_message}")




