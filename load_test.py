from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/repo")

    @task
    def about(self):
        self.client.get("/developer")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = 'https://trendings.herokuapp.com'
    min_wait = 5000
    max_wait = 15000