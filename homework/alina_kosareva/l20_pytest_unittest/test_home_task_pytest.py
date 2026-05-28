import requests
import pytest


@pytest.fixture(scope="session", autouse=True)
def main_text():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def text():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_object_id_without_delete():
    body = {
        "name": "Alina",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
    )
    assert response.status_code == 200
    return response.json().get("id")


@pytest.fixture()
def new_object_id():
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
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


@pytest.mark.critical
def test_get_objects_by_id(new_object_id):
    response = requests.get(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}"
    )
    assert response.status_code == 200


def test_update_put_objects(new_object_id):
    body = {
        "name": "Alina_PUT",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200


def test_update_patch_objects(new_object_id):
    body = {"name": "Alina_PATH"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200


@pytest.mark.medium
def test_get_objects():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200
    print(response.json())


@pytest.mark.parametrize(
    "name, student, teacher",
    [
        ("Alina", "Python automation course", "Eugene_Okulik"),
        ("Olga1", "automation course1", "Eugene_Okulik1"),
        ("Ivan^&*", "course^&*", "Eugene_Okulik@#$"),
    ],
)
def test_create_object(name, student, teacher):
    body = {
        "name": name,
        "data": {
            "student": student,
            "teacher": teacher,
        },
    }

    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["name"] == name
    assert response_json["data"]["student"] == student
    assert response_json["data"]["teacher"] == teacher


def test_delete_objects(new_object_id_without_delete):
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{new_object_id_without_delete}"
    )
    assert response.status_code == 200
