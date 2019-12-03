from locust import HttpLocust, TaskSequence,seq_task


class ImoocIndex(TaskSequence):
    """
    the VUser' behavior
    """
    @seq_task(1)# 起動順番
    def imooc_index(self):
        print("1:imooc_index")
        self.client.get("/") # ホームへアクセス

    @seq_task(2)
    def imooc_couse(self):
        print("2:imooc_couse")
        self.client.get("course/list") # 従業


class studentUser(HttpLocust):
    task_set = ImoocIndex  # テストケースをテストグループへ追加
    min_wait = 1  # リクエストの最小待ち間隔
    max_wait = 5  # リクエストの待ち最大間隔
    host = 'https://www.imooc.com/'
