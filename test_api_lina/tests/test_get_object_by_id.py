from http import HTTPStatus


def test_get_object_by_id(
    object_id_with_delete, post_create_object_endpoint, get_object_endpoint
):
    post_create_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
    get_object_endpoint.get_object_by_id(
        object_id_with_delete,
    )
    get_object_endpoint.check_response_name_is_correct("Alina")
    get_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
