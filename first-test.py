from locust import HttpLocust, TaskSet, task


# テストを定義する
class ImoocIndex(TaskSet):
    '''
    the VUser' behavior
    '''
    @task
    def imooc_index(self):
        self.client.get('/')# ホームページ


class WebsiteUser(HttpLocust):
    task_set = ImoocIndex # テストケースをテストグループへ追加
    min_wait = 1 # リクエストの最小待ち間隔
    max_wait = 5 # リクエストの待ち最大間隔
    host = 'https://www.imooc.com/'
