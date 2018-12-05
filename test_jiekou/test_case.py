
##测试用例：
'''
import requests
import unittest
from ddt import ddt,file_data

@ddt class InterfaceTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://httpbin.org/post"

    def tearDown(self):
        print(self.result)

    @file_data("./data/test_data_dict.json")

'''

import requests
import unittest
from ddt import ddt, file_data


class InterfaceTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://httpbin.org/post"

    def tearDown(self):
        print(self.result)

    @file_data("./data/test_data_dict.json")
    def test_post_request(self, key, status_code):
        r = requests.post(self.url, data={"key": key})
        self.result = r.json()
        self.assertEqual(r.status_code, status_code)
