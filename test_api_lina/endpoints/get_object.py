import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetObjectById(BaseEndpoint):

    @allure.step("Get object by id")
    def get_object_by_id(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f"{self.url}/{object_id}",
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
