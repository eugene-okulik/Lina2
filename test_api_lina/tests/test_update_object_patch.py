from http import HTTPStatus


def test_update_object_patch(
    object_id_with_delete, post_create_object_endpoint, patch_update_object_endpoint
):
    updated_body = {
        "name": "AlinaPatch",
    }
    post_create_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
    patch_update_object_endpoint.update_object_by_patch(
        object_id_with_delete,
        updated_body,
    )
    patch_update_object_endpoint.check_response_name_is_correct("AlinaPatch")
    patch_update_object_endpoint.check_response_status_is_correct(HTTPStatus.OK)
