import requests
import pytest
import allure


@allure.epic("Api Objects")
@allure.feature("Get object")
@allure.story("Get object by id")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical
@allure.title("Получение объектов по идентификатору")
def test_get_objects_by_id(new_object_id):
    response = requests.get(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}"
    )
    assert response.status_code == 200


@allure.epic("Api Objects")
@allure.feature("Update object")
@allure.story("Update object via put")
@allure.title("Изменение объекта с помощью метода put")
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


@allure.epic("Api Objects")
@allure.feature("Update object")
@allure.story("Update object via patch")
@allure.title("Изменение объекта с помощью метода patch")
def test_update_patch_objects(new_object_id):
    body = {"name": "Alina_PATH"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200


@allure.epic("Api Objects")
@allure.feature("Get object")
@allure.story("Get all objects")
@allure.title("Получение всех объектов")
@allure.severity(allure.severity_level.NORMAL)
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
@allure.epic("Api Objects")
@allure.feature("Create object")
@allure.story("Create objects via parametrize")
@allure.title("Cоздание объектов посредством параметризации")
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
