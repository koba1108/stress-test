from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession

import re

class MetricsTaskSet(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        response = self.client.get("/login")

        username   = "nextlevel"
        password   = "nhRiBHQeM97G"
        save       = "0"
        csrf_token = response.cookies['csrfToken']

        m_token_fields = re.search("<input type=\"hidden\" name=\"_Token\[fields\]\" autocomplete=\"off\" value=\"([^\"]+)\"/>", response.text)
        token_fields   = m_token_fields.group(1) if m_token_fields != None else ""

        m_token_unlocked = re.search("<input type=\"hidden\" name=\"_Token\[unlocked\]\" autocomplete=\"off\" value=\"([^\"]+)\"/>", response.text)
        token_unlocked   = m_token_unlocked.group(1) if m_token_unlocked != None else ""

        payload = {
            "username":         username,
            "password":         password,
            "_csrfToken":       csrf_token,
            "save":             save,
            "_Token[fields]":   token_fields,
            "_Token[unlocked]": token_unlocked,
        }

        self.client.post("/login", data=payload)

    def logout(self):
        self.client.get("/logout")

    @task
    def index(self):
        self.client.get("/")

class MetricsLocust(HttpLocust):
    host = "http://asp.ykoba.work"
    #host = "http://marchant.ykoba.work"
    #host = "http://partner.ykoba.work"

    task_set = MetricsTaskSet
    min_wait = 500
    max_wait = 1000
