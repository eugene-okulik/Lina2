import allure
import pytest
import requests


@pytest.fixture()
def new_object_id():
    with allure.step("Create the object"):
        body = {
            "name": "Alina",
            "data": {
                "student": "Python automation course",
                "teacher": "Eugene_Okulik",
            },
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "http://objapi.course.qa-practice.com/object", json=body, headers=headers
        )
        object_id = response.json().get("id")
        assert response.status_code == 200
        yield object_id
    with allure.step("Delete created object"):
        requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


@pytest.fixture(scope="session", autouse=True)
def main_text():
    with allure.step("The test session is started"):
        print("Start testing")
        yield
    with allure.step("The test session has ended"):
        print("Testing completed")


@pytest.fixture(autouse=True)
def text():
    with allure.step("The test is started"):
        print("before test")
        yield
    with allure.step("The test has ended"):
        print("after test")
