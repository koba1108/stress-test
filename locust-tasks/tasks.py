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

        self.client.post("/login", data=payload, cookies=self.locust.client.cookies.get_dict())

    def logout(self):
        self.client.get("/logout")

    @task(3)
    def dashboard(self):
        self.client.get("/", cookies=self.locust.client.cookies.get_dict())

    @task
    def histories(self):
        self.client.get("/histories", cookies=self.locust.client.cookies.get_dict())

    @task
    def programs(self):
        self.client.get("/programs", cookies=self.locust.client.cookies.get_dict())

    @task
    def programs_search(self):
        self.client.get("/programs?name=メニュー左上の案件を探すからのパターン", cookies=self.locust.client.cookies.get_dict())

    @task
    def programs_add(self):
        self.client.get("/programs/add", cookies=self.locust.client.cookies.get_dict())

    @task
    def alliances(self):
        self.client.get("/alliances", cookies=self.locust.client.cookies.get_dict())

    @task
    def conversion(self):
        self.client.get("/conversions", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports(self):
        self.client.get("/daily-reports", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports_program(self):
        self.client.get("/daily-reports/program", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports_site(self):
        self.client.get("/daily-reports/site", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports_device(self):
        self.client.get("/daily-reports/device", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports_partner(self):
        self.client.get("/daily-reports/partner", cookies=self.locust.client.cookies.get_dict())

    @task
    def daily_reports_client(self):
        self.client.get("/daily-reports/client", cookies=self.locust.client.cookies.get_dict())

    @task
    def monthly_reports(self):
        self.client.get("/monthly-reports", cookies=self.locust.client.cookies.get_dict())

    @task
    def payments(self):
        self.client.get("/payments", cookies=self.locust.client.cookies.get_dict())

    @task
    def invoices(self):
        self.client.get("/invoices", cookies=self.locust.client.cookies.get_dict())

    @task
    def invoices_detail(self):
        self.client.get("/invoices/view/1", cookies=self.locust.client.cookies.get_dict())

    @task
    def notices(self):
        self.client.get("/notices", cookies=self.locust.client.cookies.get_dict())

    @task
    def notices_add(self):
        self.client.get("/notices/add", cookies=self.locust.client.cookies.get_dict())

    @task
    def contact(self):
        self.client.get("/contact", cookies=self.locust.client.cookies.get_dict())

    @task
    def profile(self):
        self.client.get("/asps/edit/1", cookies=self.locust.client.cookies.get_dict())


class MetricsLocust(HttpLocust):
    # host = "http://asp.sl-galop.xyy"
    # host = "http://marchant.ykoba.work"
    # host = "http://partner.ykoba.work"
    host = os.getenv("LOCUST_TARGET_HOST", default="http://asp.sl-galop.xyz")

    task_set = MetricsTaskSet
    min_wait = 3000
    max_wait = 15000
