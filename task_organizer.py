import argparse
import sqlite3
import uuid
import datetime as dt
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='parser')

list_parser = subparsers.add_parser('list')
list_parser.add_argument('--all', help='All tasks', action='store_true')
list_parser.add_argument('--today', help='Tasks with today deadline', action='store_true')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('--name', help='Name of the task', required=True)
add_parser.add_argument('--deadline', help='Deadline for the task', required=True)
add_parser.add_argument('--description', help='Description of the task', required=True)

remove_parser = subparsers.add_parser('remove')
remove_parser.add_argument('--hash', help='Task hash', required=True)

update_parser = subparsers.add_parser('update')
update_parser.add_argument('--name', help='Name of the task', required=True)
update_parser.add_argument('--deadline', help='Deadline for the task', required=True)
update_parser.add_argument('--description', help='Description of the task', required=True)
update_parser.add_argument('--hash', help='Task hash', required=True)

args = parser.parse_args()

if args.parser is None:
    print('########################################')
    print('Enter command and data like in examples:')
    print('')
    print('add --name "TASK NAME" --deadline "TASK DEADLINE" --description "TASK DESCRIPTION"')
    print('update --name "TASK NEW NAME" --deadline "TASK NEW DEADLINE" '
          '--description "TASK NEW DESCRIPTION" --hash "TASK HASH"')
    print('remove --hash "TASK HASH"')
    print('list --all or list --today')
    print('########################################')
    sys.exit(0)

conn = sqlite3.connect('tasks.sqlite')
cursor = conn.cursor()


def get_datetime(datetime_string):
    try:
        return dt.datetime.strptime(datetime_string, '%Y-%m-%d').date()
    except ValueError:
        sys.exit('Incorrect data format, should be YYYY-MM-DD')


if args.parser == 'add':
    name = str(args.name)
    description = str(args.description)
    task_hash = str(uuid.uuid4())
    deadline = get_datetime(args.deadline)

    cursor.execute("INSERT INTO task VALUES (?, ?, ?, ?)", (name, deadline, description, task_hash))
    conn.commit()

elif args.parser == 'update':
    name = str(args.name)
    description = str(args.description)
    deadline = get_datetime(args.deadline)
    task_hash = str(args.hash)

    conn.execute(
        "UPDATE task SET name=?, deadline=?, description=? WHERE hash=?",
        (name, deadline, description, task_hash)
    )
    conn.commit()

elif args.parser == 'remove':
    task_hash = str(args.hash)

    result = conn.execute("DELETE FROM task WHERE hash=?", [task_hash])
    conn.commit()

    if result.rowcount == 0:
        sys.exit("Insert correct hash.")

elif args.parser == 'list':
    if args.all:
        tasks = conn.execute('SELECT * FROM task')
    elif args.today:
        tasks = conn.execute('SELECT * FROM task WHERE deadline = ?', [dt.datetime.now().date().strftime('%Y-%m-%d')])
    else:
        sys.exit('Insert correct command.')

    for row in tasks:
        if tasks is not None:
            print(f"Name: {row[0]} | Deadline: {row[1]} | Description: {row[2]} | Hash: {row[3]}")
        else:
            print("There are no tasks.")
else:
    print('Invalid command!')