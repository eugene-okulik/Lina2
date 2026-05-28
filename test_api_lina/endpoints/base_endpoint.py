import allure


class BaseEndpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step("Check response status code")
    def check_response_status_is_correct(self, expected_status):
        assert self.response.status_code == expected_status

    @allure.step("Check that name is the same as sent")
    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name
