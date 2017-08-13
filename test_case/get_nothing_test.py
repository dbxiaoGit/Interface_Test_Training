#!/usr/bin/env python

"""
@author:     巧吧软件测试
@desc:无请求参数
"""

import requests
import json
import unittest
from public import base

class GetNothingTest(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_1(self):
        '''校验状态码是否为200'''
        r = requests.get(self.url)

        status_code  = r.status_code
        self.assertEqual(status_code,200)

    def test_2(self):
        '''校验headers里的Connection值'''
        r = requests.get(self.url)
        resp = r.json()
        connect = resp['headers']['Connection']
        self.assertEqual(connect, 'close')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
        # print(r.url)#获取URL
        # print(r.status_code,r.reason) #获取状态码,获取状态码的原因
        # print(r.headers)#响应头

        # print(type(r.text))
        # print(r.content) #byte,图片、文件，
        # print(type(r.content))
        # print(r.request.headers) #请求头
        # print(r.request.url)
        # print(r.request.method)
        # print(type(response))
        # print(response['headers']['Connection'])
        # print(eval(r.text)['headers']['Connection'])
