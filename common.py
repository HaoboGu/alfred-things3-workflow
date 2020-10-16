#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2020.10.16"

import subprocess


# 使用AppleScript获取Things3的Project列表
def get_things3_project_names():
    script = """
    tell application "Things3"
    set prStr to ""
    repeat with pr in projects
        set prStr to prStr & name of pr & "|"
    end repeat
    return prStr
    end tell
    """
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script)
    projects = stdout.rstrip("|\n").split("|")
    projects.insert(0, 'inbox')
    return projects


# 使用AppleScript获取Things3的Project列表（带id）
def get_things3_project_names_and_ids():
    script = """
    tell application "Things3"
    set prStr to ""
    repeat with pr in projects
        set prStr to prStr & name of pr & "|" & id of pr & "||"
    end repeat
    return prStr
    end tell
    """
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script)
    result = stdout.rstrip("||\n").split("||")
    projects = []
    for p in result:
        name, id = p.split("|")
        projects.append((name, id))
    return projects


def get_things3_items(project_list):
    items = []
    base_script = ('tell application "Things3"\n'
                   '	set prStr to ""\n'
                   '	script V\n'
                   '		property ToDoList : missing value\n'
                   '     property ProjectId : missing value\n'
                   '	end script\n'
                   '	set V\'s ToDoList to to dos of {list_name}\n'
                   '    set V\'s ProjectId to id of {list_name}\n'
                   '	repeat with toDo in V\'s ToDoList\n'
                   '		if status of toDo = open then\n'
                   '			set prStr to prStr & name of toDo & "|" & id of toDo & "||"\n'
                   '		end if\n'
                   '	end repeat\n'
                   '	return prStr\n'
                   'end tell\n'
                   '    ')
    # Get items in projects
    for project_name, project_id in project_list:
        script = base_script.format(list_name='project \"' + project_name + '\"')
        p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
        stdout, stderr = p.communicate(script)
        items_with_project_id = stdout.rstrip("||\n").split("||")
        for item in items_with_project_id:
            if item == "":
                continue
            name, item_id = item.split("|")
            items.append((name, item_id, project_id, project_name))

    # Get items in Inbox list
    script = ('tell application "Things3"\n'
              '	set prStr to ""\n'
              '	script V\n'
              '		property ToDoList : missing value\n'
              '     property ProjectId : missing value\n'
              '	end script\n'
              '	set V\'s ToDoList to to dos of list "Inbox"\n'
              ' set V\'s ProjectId to id of list "Inbox"\n'
              '	repeat with toDo in V\'s ToDoList\n'
              '		if status of toDo = open then\n'
              '			set prStr to prStr & name of toDo & "|" & id of toDo & "||"\n'
              '		end if\n'
              '	end repeat\n'
              '	return prStr\n'
              'end tell\n'
              '    ')
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script)
    items_with_project_id = stdout.rstrip("||\n").split("||")
    for item in items_with_project_id:
        if item == "":
            continue
        name, item_id = item.split("|")
        items.append((name, item_id, "inbox", "inbox"))
    return items


if __name__ == '__main__':
    import time
    time_start = time.time()
    print(get_things3_items([("代码补全", "project_id")]))
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
