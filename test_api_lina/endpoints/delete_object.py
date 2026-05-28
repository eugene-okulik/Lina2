import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    @allure.step("Delete object by id")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(
            f"{self.url}/{object_id}",
        )
        return self.response
