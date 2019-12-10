# from locust import HttpLocust, TaskSet, task, TaskSequence, seq_task
# from random import random
#
#
# class Imooc(TaskSequence):
#     """
#     the VUser behavior
#     """
#     first_url = ""
#
#     # ホームページにアクセス
#     @seq_task(1)
#     def imooc_index(self):
#         self.client.get("/")
#

import requests


res = requests.get("https://bell-face.local/", verify=False)
print(res.text)