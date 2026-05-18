import requests


def create_object():
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
    user_id = response.json().get("id")
    assert response.status_code == 200
    print(response.json())
    return user_id


def update_object_put(user_id):
    body = {
        "name": "Alina_PUT",
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{user_id}",
        json=body,
        headers=headers,
    )
    print(response.json())
    assert response.status_code == 200


def update_object_patch(user_id):
    body = {
        "data": {
            "student": "Python automation course",
            "teacher": "Eugene_Okulik_PATCH",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{user_id}",
        json=body,
        headers=headers,
    )
    print(response.json())
    assert response.status_code == 200


def clear(user_id):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{user_id}")
    print(response.text)
    assert response.status_code == 200
    assert response.text == f"Object with id {user_id} successfully deleted"


user_id = create_object()
update_object_put(user_id)
update_object_patch(user_id)
clear(user_id)
