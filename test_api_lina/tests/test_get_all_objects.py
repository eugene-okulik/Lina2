from http import HTTPStatus


def test_get_all_objects(get_all_objects_endpoint):
    get_all_objects_endpoint.get_objects()
    get_all_objects_endpoint.check_response_status_is_correct(HTTPStatus.OK)
