#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

import random

import requests
from lxml import etree
from fake_useragent import UserAgent

from crawler.encrypt import gen_data

from config import PROXIES, USERNAME, PASSWORD


TIMEOUT = 5


def choice_proxy():
    if PROXIES:
        return random.choice(PROXIES + [''])
    return ''


def get_user_agent():
    ua = UserAgent()
    return ua.random


def fetch(url, retry=0, max_retries=3):
    s = requests.Session()
    # 设置代理
    proxies = {
        'http': choice_proxy()
    }
    # 设置agent和referer
    s.headers.update({'user-agent': get_user_agent(),
                      'referer': 'http://music.163.com/'})

    # 默认重试3次
    try:
        return s.get(url, timeout=TIMEOUT, proxies=proxies)
    except requests.exceptions.RequestException:
        if retry < max_retries:
            return fetch(url, retry=retry + 1)
        # 重新抛出异常
        raise


def post(url):
    headers = {
        'Cookie': 'appver=1.5.0.75771;',
        'Referer': 'http://music.163.com/'
    }

    return requests.post(url, headers=headers, data=gen_data(USERNAME, PASSWORD))


# 返回lxml解析后的xpath对象
def get_tree(url):
    r = fetch(url)
    return etree.HTML(r.text)
