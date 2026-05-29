import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    object_id = None

    @allure.step("Create new object")
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=self.url,
            headers=headers,
            json=body,
        )
        self.json = self.response.json()
        self.object_id = self.json["id"]
        return self.response
