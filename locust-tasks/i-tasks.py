# -*- coding: utf-8 -*-
import os
from locust import HttpLocust, TaskSequence, task, seq_task


class MetricsTaskSet(TaskSequence):
    @seq_task(1)
    @task(5)
    def impression(self):
        self.client.get("/impression?q=c2l0ZV9pZD0xJmNvbnRlbnRfaWQ9MQ==")

    @seq_task(2)
    @task(3)
    def click(self):
        self.client.get("/click?q=Y29udGVudF9pZD0xJnNpdGVfaWQ9MQ%3D%3D")

    @seq_task(3)
    def conversion(self):
        self.client.get("/conversion?q=cHJvZ3JhbV9pZD0x")


class MetricsLocust(HttpLocust):
    host = os.getenv("LOCUST_TARGET_HOST", "http://i.sl-galop.xyz")
    task_set = MetricsTaskSet
    min_wait = 1000
    max_wait = 5000
