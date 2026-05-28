import locust
from locust import task, HttpUser, between


class Objects(HttpUser):
    wait_time = between(1, 3)
    object_id = None

    def on_start(self):
        response = self.client.post(
            "/object",
            json={
                "name": "Alina",
                "data": {
                    "student": "Python automation course",
                    "teacher": "Eugene_Okulik",
                },
            },
        )
        self.object_id = response.json().get("id")
        assert response.status_code == 200

    @task(5)
    def get_all_objects(self):
        response = self.client.get(
            "/object",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1

    @task(1)
    def update_object(self):
        response = self.client.put(
            f"/object/{self.object_id}",
            json={
                "name": "AlinaPut",
                "data": {
                    "student": "Python automation course",
                    "teacher": "Eugene_Okulik Put method",
                },
            },
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.json()["name"] == "AlinaPut"

    @task(7)
    def get_object_by_id(self):
        response = self.client.get(
            f"/object/{self.object_id}",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1

    def on_stop(self):
        response = self.client.delete(f"/object/{self.object_id}")
        assert response.status_code == 200
