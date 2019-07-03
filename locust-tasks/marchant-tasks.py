# -*- coding: utf-8 -*-
import os
import re
import logging
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    csrf_token = ""
    cake_php = ""

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        response = self.client.get("/login")

        username = os.getenv("LOGIN_USER_NAME", "nextlevel")
        password = os.getenv("LOGIN_PASSWORD", "nhRiBHQeM97G")
        save = "0"

        self.csrf_token = response.cookies.get('csrfToken')
        self.cake_php = response.cookies.get('CAKEPHP')

        f_token_fields = "<input type=\"hidden\" name=\"_Token\[fields\]\" autocomplete=\"off\" value=\"([^\"]+)\"/>"
        m_token_fields = re.search(f_token_fields, response.text)
        token_fields = ""
        if m_token_fields is not None:
            token_fields = m_token_fields.group(1)

        f_token_unlocked = "<input type=\"hidden\" name=\"_Token\[unlocked\]\" autocomplete=\"off\" value=\"([^\"]+)\"/>"
        m_token_unlocked = re.search(f_token_unlocked, response.text)
        token_unlocked = ""
        if m_token_unlocked is not None:
            token_unlocked = m_token_unlocked.group(1)

        payload = {
            "username": username,
            "password": password,
            "_csrfToken": self.csrf_token,
            "save": save,
            "_Token[fields]": token_fields,
            "_Token[unlocked]": token_unlocked,
        }
        logging.info("payload %s", payload)

        self.client.post("/login", data=payload)

    def logout(self):
        self.client.get("/logout")

    @task(3)
    def dashboard(self):
        self.client.get("/")

    @task
    def programs(self):
        self.client.get("/programs")

    @task
    def programs_search(self):
        self.client.get("/programs?name=メニュー左上の案件を探すからのパターン")

    @task
    def program_detail(self):
        self.client.get("/programs/view/1")

    @task
    def conversion(self):
        self.client.get("/conversions")

    @task
    def daily_reports(self):
        self.client.get("/daily-reports")

    @task
    def daily_reports_program(self):
        self.client.get("/daily-reports/program")

    @task
    def daily_reports_site(self):
        self.client.get("/daily-reports/site")

    @task
    def daily_reports_device(self):
        self.client.get("/daily-reports/device")

    @task
    def monthly_reports(self):
        self.client.get("/monthly-reports")

    @task
    def invoices(self):
        self.client.get("/invoices")

    @task
    def notices(self):
        self.client.get("/notices")

    @task
    def notice_detail(self):
        self.client.get("/notices/view/1")

    @task
    def profile(self):
        self.client.get("/clients/edit/1")


class MetricsLocust(HttpLocust):
    host = os.getenv("LOCUST_TARGET_HOST", "http://marchant.sl-galop.xyz")

    task_set = MetricsTaskSet
    min_wait = 3000
    max_wait = 10000
