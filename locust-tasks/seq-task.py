from locust import HttpLocust, TaskSequence, task, seq_task
from locust.clients import HttpSession

class MetricsTaskSet(TaskSequence):
    @seq_task(1)
    @task(10)
    def impression(self):
        self.client.get("/impression?q=c2l0ZV9pZD0xJmNvbnRlbnRfaWQ9MQ==")

    @seq_task(2)
    def click(self):
        self.client.get("/click?q=Y29udGVudF9pZD0xJnNpdGVfaWQ9MQ%3D%3D")

    @seq_task(3)
    def conversion(self):
        self.client.get("/conversion?q=cHJvZ3JhbV9pZD0x")

class MetricsLocust(HttpLocust):
    host = "http://i.ykoba.work"
    task_set = MetricsTaskSet
    min_wait = 500
    max_wait = 1000
