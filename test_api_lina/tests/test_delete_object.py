from http import HTTPStatus


def test_delete_object(object_id, post_create_object_endpoint, delete_object_endpoint):
    post_create_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
    post_create_object_endpoint.check_response_name_is_correct("Alina")
    delete_object_endpoint.delete_object_by_id(
        object_id,
    )
    delete_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
