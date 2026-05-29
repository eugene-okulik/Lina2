from http import HTTPStatus
import allure


def test_create_object(post_create_object_endpoint):
    with allure.step("Create the object"):
        body = {
            "name": "Alina",
            "data": {
                "student": "Python automation course",
                "teacher": "Eugene_Okulik",
            },
        }
        post_create_object_endpoint.create_new_object(body)
        post_create_object_endpoint.check_response_name_is_correct("Alina")
        post_create_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
