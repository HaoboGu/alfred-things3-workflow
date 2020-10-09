# coding=utf-8
import sys
import datetime


def parse(param):
    re = param.split(" ")
    if len(re) < 4:
        for i in range(0, 4 - len(re)):
            re.append("")
    return re[:4]


def build_things3_url(params):
    title, when, cost, project = params
    if project == "":
        # 默认Project名
        project = "代码补全"
    url = "things:///add?"
    cost = parse_cost(cost)
    if cost > 0:
        title += " : "
        title += ("🍅" * cost)
    url = url + "title=" + title
    when = parse_when(when)
    if when != "":
        url = url + "&when=" + when
    if project != "":
        url = url + "&list=" + project
    return url


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
    return ""


if __name__ == '__main__':
    sys_input = sys.argv
    if len(sys_input) == 2:
        params = parse(sys_input[1])
        sys.stdout.write(build_things3_url(params))
