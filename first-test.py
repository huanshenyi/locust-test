from locust import HttpLocust, TaskSet, task


# TestCase
class ImoocIndex(TaskSet):
    '''
    the VUser' behavior
    '''
    @task
    def imooc_index(self):
        self.client.get('/')# ホームページ


class WebsiteUser(HttpLocust):
    task_set = ImoocIndex #将测试用例加入到测试任务套件中
    min_wait = 1 # 每个请求间最小等待时间 リクエストの最小待ち間隔
    max_wait = 5 # 每个请求间最大等待时间
    host = 'https://www.imooc.com/'