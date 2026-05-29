import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class UpdateObjectPatch(BaseEndpoint):

    @allure.step("Update object via patch")
    def update_object_by_patch(self, object_id_with_delete, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id_with_delete}",
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
