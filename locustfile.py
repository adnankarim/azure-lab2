from locust import HttpUser, task, constant

class NumericalIntegrationUser(HttpUser):
    wait_time = constant(1)  # seconds between requests

    @task
    def get_integration_results(self):
        # Adjust the lower/upper as needed
        self.client.get("/numericalintegralservice/0/3.14159")
