import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetAllObjects(BaseEndpoint):

    @allure.step("Get all objects")
    def get_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=self.url,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
