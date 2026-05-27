import unittest
import requests


class TestObjectApi(unittest.TestCase):
    def setUp(self) -> None:
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
        self.assertEqual(response.status_code, 200)
        self.object_id = response.json().get("id")

    def tearDown(self) -> None:
        requests.delete(f"http://objapi.course.qa-practice.com/object/{self.object_id}")
        print("done")

    def test_get_objects_by_id(self):
        response = requests.get(
            f"http://objapi.course.qa-practice.com/object/{self.object_id}"
        )
        self.assertEqual(response.status_code, 200)

    def test_update_objects(self):
        body = {
            "name": "Alina_PUT",
            "data": {
                "student": "Python automation course",
                "teacher": "Eugene_Okulik",
            },
        }
        headers = {"Content-Type": "application/json"}
        response = requests.put(
            f"http://objapi.course.qa-practice.com/object/{self.object_id}",
            json=body,
            headers=headers,
        )
        self.assertEqual(response.status_code, 200)


class TestObjectIndependentApi(unittest.TestCase):
    def test_get_objects(self):
        response = requests.get(f"http://objapi.course.qa-practice.com/object")
        self.assertEqual(response.status_code, 200)
        print(response.json())
