# alfred-things3-workflow
Manage things3 using alfred workflow!

# Command design
This workflow aims to provide a convenient, easy-to-use and concise way to add/update/delete/complete things workitems using alfred considering using Pomodoro Technique. Things3 has already provided a shortcut for quickly add workitems, but I have to use my mouse to choose deadline, tag, project, etc. This is why I want to integrate things3 to alfred workflow.

## Add workitems
- Command
  ```shell
  # Command
  thadd title deadline cost
  # Example
  thadd DoSomething! today 2
  thadd DoAnotherthingTomorrow +1 3
  ```
  
- Where is the target project?
  Valid target projects can be loaded automatically, just choose your target project.

- Usage example

  ![thadd](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2020-10-29-133231.gif)

## Complete workitems
- Command
  ```shell
  # Command
  thc title (project) 
  # Example
  thc myWorkitem target_project
  thc it
  ```
  
- How to filter the workitem?
  This command provides two ways to filter the workitem: title and project(optional). Both parameters accepts fuzzy query, which means you don't need to remember the full name of target project and full title of workitem.
  
- Usage example

  ![thc](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2020-10-29-133209.gif)