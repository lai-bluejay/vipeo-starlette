#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/Users/charleslai/PycharmProjects/ivideo-flask.test.py was created on 2019/03/12.
file in :

Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""
import json
fpath = "assets/urls.txt"
uri_list = list()
with open(fpath) as fi:
    for url in fi:
        url = url.strip()
        uri_list.append(url)
bd = dict()
bd['list'] = list()
default_dict = {
    "name": "如发现不可解析的线路，请及时联系作者",
    "url": ""
}
bd['list'].append(default_dict)
for i, u in enumerate(uri_list):
    tmp = dict()
    tmp['name'] = '推荐线路{}'.format(i+1)
    tmp['url'] = u
    bd['list'].append(tmp)

with open('assets/lists.json', 'w+') as fo:
    json.dump(bd, fo, ensure_ascii=False)

with open('assets/lists.json', ) as fi:
    api = json.load(fi)
    print [(a['url'], a['name']) for a in api['list']]

