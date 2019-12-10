from locust import HttpLocust, TaskSet, task


class BellFaceLogin(TaskSet):
    """
    loginページテスト
    """
    @task
    def bell_face(self):
        self.client.get('staff/login', verify=False)


class WebsiteUser(HttpLocust):
    task_set = BellFaceLogin # テストケースをテストグループへ追加
    min_wait = 1 # リクエストの最小待ち間隔
    max_wait = 5 # リクエストの待ち最大間隔
    host = 'https://user.bell-face.local/'