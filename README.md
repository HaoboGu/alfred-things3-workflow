# alfred-things3-workflow
Manage things3 using alfred workflow!

# Command design
This workflow aims to provide a convenient, easy-to-use and concise way to add/update/delete/complete things workitems using alfred considering using Pomodoro Technique. Things3 has already provided a shortcut for quickly add workitems, but I have to use my mouse to choose deadline, tag, project, etc. This is why I want to integrate things3 to alfred workflow.
## Add workitem

- What do I want to add when I use this command?
  a workitem with target project, title, deadline(in natural language), estimated tomato cost, etc.
- How does this command looks like?
  ```shell
  # Command
  th add title deadline 3
  # Example
  th add DoSomething! today 2
  th add DoAnotherthingTomorrow +1 3
  ``` 
- Where is the target project?
  I hope alfred can automatically give me all avaliable projects after I entered my workitem info. I donot want to input it by myself.
- TODO