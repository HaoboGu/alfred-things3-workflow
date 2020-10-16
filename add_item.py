#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2020.10.14"

import sys
import datetime
import json

from common import get_things3_project_names


# 解析参数
def parse(param):
    re = param.split(" ")
    if len(re) < 3:
        for i in range(0, 3 - len(re)):
            re.append("")
    return re[:3]


def process(params):
    title, when, cost = params
    projects = get_things3_project_names()
    url = "things:///add?"
    cost = parse_cost(cost)
    if cost > 0:
        title += " : "
        title += ("🍅" * cost)
    url = url + "title=" + title
    when = parse_when(when)
    if when != "":
        url = url + "&when=" + when

    item_list = []
    for project_name in projects:
        item_list.append(build_item(project_name, title, when, cost, url))

    result = {"items": item_list}
    result_json = json.dumps(result)
    return result_json


# 构建候选Item
def build_item(project_name, title, when, cost, url):
    item = {}
    item['title'] = "添加到：" + project_name
    # item['subtitle'] = "标题：" + title + "，时间：" + when
    item['arg'] = url + "&list=" + project_name
    item['variables'] = {'project_name': project_name}
    icon = {'type': 'fileicon', 'path': '/Applications/Things3.app'}
    item['icon'] = icon
    return item


def parse_cost(cost):
    if not cost.isdigit() or int(cost) < 0:
        return 0
    else:
        return int(cost)


def parse_when(when):
    today = datetime.date.today()
    if when == "-1":
        return ""
    if when == "0":
        return today.__str__()
    if when.isdigit():
        when = today + datetime.timedelta(int(when))
        return when.__str__()
    else:
        return when
    return ""


if __name__ == '__main__':
    sys_input = sys.argv
    if len(sys_input) == 2:
        params = parse(sys_input[1])
        sys.stdout.write(process(params))
