# pure_python

Some of my projects developed during practicing skills in python coding language. Clone this repository for testing.

## Task organizer

[task_organizer](https://github.com/wszoltysek/pure_python/blob/master/task_organizer.py) - since I was an Event Project Manager for many years, I had to have a program to organize my "TODO".
Project uses "argparse" library and sqlite3 database, which is created automatically during first run. You can add, update, remove and list tasks with commands:

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

## File analyzer

[file_analyzer](https://github.com/wszoltysek/pure_python/blob/master/file_analyzer.py) - Program takes user *.txt file from an input and analyzes it content. 
Developed during OOP practice, context managers usage and working with files in python. To run, type command:
```
python3 file_analyzer.py
```
Then type your "file.txt" if it's in the same directory or "path-to-your/file.txt" if it's not.

## Web scrapers
I found them popular, so I developed a few ones. From newest:

1. [Blog Scraper](https://github.com/wszoltysek/pure_python/blob/master/blog_scraper.py) - Scrapes posts content from event blog by title, date, summary, link and save it to the csv file.
2. [TV Scraper](https://github.com/wszoltysek/pure_python/blob/master/tv_scraper.py) - Scrapes TV program of a specific station from teleman.pl page and save it to sqlite3 database.
3. [Filmweb Scraper](https://github.com/wszoltysek/pure_python/blob/master/filmweb_scraper.py) - Scrapes TOP25 movies from Filmweb ranking page and save it to the json file.

To run:
```
python3 blog_scraper.py
# OR
python3 tv_scraper.py
# OR
python3 filmweb_scraper.py
```

## Calculator
[calculator](https://github.com/wszoltysek/pure_python/blob/master/calculator.py) - Popular and simple, but I wanted to have my own. 
Program gives the user options to add, subtract, multiply and divide two numbers from an input. 
Feel free to check it - maybe you will find something interesing there.

## 
Apps messages are imported from own created module.
Unittests in progress.