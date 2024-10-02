import requests


class HttpMethods:
    @staticmethod
    def make_request(method, url, body=None, headers=None, cookies=None):
        if headers is None:
            headers = {"Content-Type": "application/json"}
        response = requests.request(method, url, json=body, headers=headers, cookies=cookies)
        return response

    @staticmethod
    def get(url, headers=None, cookies=None):
        return HttpMethods.make_request("GET", url, headers=headers, cookies=cookies)

    @staticmethod
    def post(url, body=None, headers=None, cookies=None):
        return HttpMethods.make_request("POST", url, body=body, headers=headers, cookies=cookies)

    @staticmethod
    def put(url, body=None, headers=None, cookies=None):
        return HttpMethods.make_request("PUT", url, body=body, headers=headers, cookies=cookies)

    @staticmethod
    def delete(url, body=None, headers=None, cookies=None):
        return HttpMethods.make_request("DELETE", url, body=body, headers=headers, cookies=cookies)
