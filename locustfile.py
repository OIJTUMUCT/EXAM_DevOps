from locust import FastHttpUser, task, between


class IrisUser(FastHttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def healthcheck(self):
        self.client.get("/healthcheck", name="healthcheck", timeout=10)

    @task(1)
    def predict(self):
        payload = {
            "samples": [
                {
                    "sepal_length_cm": 5.1,
                    "sepal_width_cm": 3.5,
                    "petal_length_cm": 1.4,
                    "petal_width_cm": 0.2,
                },
                {
                    "sepal_length_cm": 6.2,
                    "sepal_width_cm": 2.8,
                    "petal_length_cm": 4.8,
                    "petal_width_cm": 1.8,
                },
            ]
        }
        self.client.post("/predict", json=payload, name="predict", timeout=10)