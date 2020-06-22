# pure_python

Some of my projects developed during practicing skills in python coding language.

## Task organizer

[task_organizer](https://github.com/wszoltysek/pure_python/blob/master/task_organizer.py) - since I was an Event Project Manager for many years, I had to have a program to organize my "TODO".
Project uses "argparse" library and sqlite3 database. You can add, update, remove and list tasks with commands:

To add task:
```
python3 task_organizer.py add --name "your task name" --deadline "your task deadline" --description "your task description"
```

To update task:
```
python3 task_organizer.py update --name "task new name" --deadline "task new deadline" --description "task new description" --hash "task hash"
```

To remove task:
```
python3 task_organizer.py remove --hash "task hash"
```

To list tasks:
```
python3 task_organizer.py list --all
# OR
python3 task_organizer.py list --today
```


Don't forget to write deadline in correct format (YYYY-MM-DD).
Task hash is created automatically during adding it.

Apps messages are imported from own created module.
Unittests in progress.