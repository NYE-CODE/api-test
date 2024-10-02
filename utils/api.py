from utils.http_methods import HttpMethods

"""Methods for testing the API"""

API_BASE_URL = 'https://rahulshettyacademy.com'  # Base URL for API
API_KEY_PARAM = '?key=qaclick123'  # Parameter for the API requests


class ApiTest:
    @staticmethod
    def create_place(data):
        post_url = f'{API_BASE_URL}/maps/api/place/add/json{API_KEY_PARAM}'
        response_post = HttpMethods.post(post_url, data)
        return response_post

    @staticmethod
    def get_place(place_id):
        get_url = f'{API_BASE_URL}/maps/api/place/get/json{API_KEY_PARAM}&place_id={place_id}'
        response_get = HttpMethods.get(get_url)
        return response_get

    @staticmethod
    def update_place(place_id, data):
        put_url = f'{API_BASE_URL}/maps/api/place/update/json{API_KEY_PARAM}&place_id={place_id}'
        response_put = HttpMethods.put(put_url, data)
        return response_put
