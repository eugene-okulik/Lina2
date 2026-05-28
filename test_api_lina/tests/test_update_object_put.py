from http import HTTPStatus


def test_update_object_put(
    object_id_with_delete, post_create_object_endpoint, put_update_object_endpoint
):
    updated_body = {
        "name": "AlinaPut",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    post_create_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
    put_update_object_endpoint.update_object_by_put(
        object_id_with_delete,
        updated_body,
    )
    put_update_object_endpoint.check_response_name_is_correct("AlinaPut")
    put_update_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
