import allure
import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_all_objects import GetAllObjects
from endpoints.get_object import GetObjectById
from endpoints.update_patch_object import UpdateObjectPatch
from endpoints.update_put_object import UpdateObjectPut


@pytest.fixture
def post_create_object_endpoint():
    return CreateObject()


@pytest.fixture
def put_update_object_endpoint():
    return UpdateObjectPut()


@pytest.fixture
def patch_update_object_endpoint():
    return UpdateObjectPatch()


@pytest.fixture
def get_all_objects_endpoint():
    return GetAllObjects()


@pytest.fixture
def get_object_endpoint():
    return GetObjectById()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(post_create_object_endpoint):
    body = {
        "name": "Alina",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    with allure.step("Create object"):
        post_create_object_endpoint.create_new_object(body)
    return post_create_object_endpoint.object_id


@pytest.fixture()
def object_id_with_delete(post_create_object_endpoint, delete_object_endpoint):
    body = {
        "name": "Alina",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    with allure.step("Create object"):
        post_create_object_endpoint.create_new_object(body)
    yield post_create_object_endpoint.object_id
    with allure.step("Delete object"):
        delete_object_endpoint.delete_object_by_id(
            post_create_object_endpoint.object_id
        )
