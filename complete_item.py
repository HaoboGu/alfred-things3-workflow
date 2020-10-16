#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2020.10.14"

import sys
import json
from common import get_things3_project_names_and_ids, get_things3_items


param_number = 2


def parse(raw_input):
    re = raw_input.split(" ")
    if len(re) < param_number:
        for i in range(0, param_number - len(re)):
            re.append("")
    return re[:param_number]


def process(params):
    title, project = params
    valid_project = []
    if project == "":
        for project_name, project_id in get_things3_project_names_and_ids():
            valid_project.append((project_name, project_id))
    else:
        for project_name, project_id in get_things3_project_names_and_ids():
            if project in project_name:
                valid_project.append((project_name, project_id))

    valid_items = []
    for item in get_things3_items(valid_project):
        name, id, p_id, p_name = item
        for valid_name, valid_id in valid_project:
            if p_id == "inbox" or p_id == valid_id:
                if name.find(title) != -1:
                    valid_items.append((name, id, p_id, p_name))
                    break

    url = "things:///update?"
    url += "auth-token=QYCFuQ22TpKmjRJ8bsunHg&"
    item_list = []
    for name, id, project_id, project_name in valid_items:
        item_list.append(build_item(name, id, project_id, project_name, url))

    result = {"items": item_list}
    result_json = json.dumps(result)
    return result_json


def build_item(name, id, project_id, project_name, url):
    item = {}
    item['title'] = "标记【" + name + "】为已完成"
    item['subtitle'] = "所属项目:" + project_name
    item['arg'] = url + "&id=" + id + "&completed=true"
    item['variables'] = {'project_id': project_id}
    icon = {'type': 'fileicon', 'path': '/Applications/Things3.app'}
    item['icon'] = icon
    return item


if __name__ == '__main__':
    sys_input = sys.argv
    if len(sys_input) == 2:
        params = parse(sys_input[1])
        sys.stdout.write(process(params))