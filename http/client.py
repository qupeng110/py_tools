#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import requests

def https_post(a, b, retry = 0):
    '''

    :param data: json格式字符串的参数
    :return: 获取的返回json字符串信息
    '''

    args = {'a_id': a, 'b_id': b}
    try:
        rsp = requests.get("https://127.0.0.1:5000/", params=args, verify=False, timeout=60)
    except:
        if retry < 1:
            sys.stderr.write("https requests failed! ")
            sys.exit(-1)

        https_post(a, b, retry - 1)

    return rsp.json()
