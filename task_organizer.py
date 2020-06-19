import argparse
import sqlite3
import uuid
import datetime as dt
import sys
from apps_messages.organizer_msgs import task_intro

parser = argparse.ArgumentParser()
parser.add_argument('function', nargs='?', choices=['add', 'list', 'update', 'remove'])
args, sub_args = parser.parse_known_args()

conn = sqlite3.connect('tasks.sqlite')
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS task
             (name text NOT NULL,
             deadline date NOT NULL,
             description text NOT NULL,
             hash varchar(36) NOT NULL
             );''')


def get_datetime(datetime_string):
    try:
        return dt.datetime.strptime(datetime_string, '%Y-%m-%d').date()
    except ValueError:
        sys.exit('Incorrect data format. Should be YYYY-MM-DD.')


if args.function is None:
    print(task_intro)
    sys.exit()

elif args.function == 'add':
    parser.add_argument('--name', help='Name of the task', required=True)
    parser.add_argument('--deadline', help='Deadline for the task', required=True)
    parser.add_argument('--description', help='Description of the task', required=True)
    args = parser.parse_args(sub_args)


    def add_task(**kwargs):
        name = kwargs['name']
        deadline = kwargs['deadline']
        description = kwargs['description']
        task_hash = str(uuid.uuid4())

        cursor.execute('INSERT INTO task VALUES (?, ?, ?, ?)', (name, deadline, description, task_hash))
        conn.commit()
        print('Task added successfully.')


    add_task(name=str(args.name), description=str(args.description), deadline=get_datetime(args.deadline))

elif args.function == 'update':
    parser.add_argument('--name', help='Name of the task', required=True)
    parser.add_argument('--deadline', help='Deadline for the task', required=True)
    parser.add_argument('--description', help='Description of the task', required=True)
    parser.add_argument('--hash', help='Task hash', required=True)
    args = parser.parse_args(sub_args)


    def update_task(**kwargs):
        name = kwargs['name']
        deadline = kwargs['deadline']
        description = kwargs['description']
        task_hash = kwargs['task_hash']

        conn.execute(
            'UPDATE task SET name=?, deadline=?, description=? WHERE hash=?',
            (name, deadline, description, task_hash)
        )
        conn.commit()
        print('Task updated successfully.')


    update_task(
        name=str(args.name),
        description=str(args.description),
        deadline=get_datetime(args.deadline),
        task_hash=str(args.hash)
    )

elif args.function == 'remove':
    parser.add_argument('--hash', help='Task hash', required=True)
    args = parser.parse_args(sub_args)


    def remove_task(**kwargs):
        task_hash = kwargs['task_hash']

        result = conn.execute('DELETE FROM task WHERE hash=?', [task_hash])
        conn.commit()

        if result.rowcount == 0:
            sys.exit('Insert correct hash.')
        else:
            print('Task removed successfully.')


    remove_task(task_hash=str(args.hash))

elif args.function == 'list':
    parser.add_argument('--all', help='All tasks', action='store_true')
    parser.add_argument('--today', help='Tasks with today deadline', action='store_true')
    args = parser.parse_args(sub_args)


    def list_task(**kwargs):

        if kwargs['all']:
            tasks = conn.execute('SELECT * FROM task')
        elif kwargs['today']:
            tasks = conn.execute('SELECT * FROM task WHERE deadline = ?',
                                 [dt.datetime.now().date().strftime('%Y-%m-%d')])
        else:
            sys.exit('Insert correct command.')

        for row in tasks:
            if tasks is not None:
                print(f'Name: {row[0]} | Deadline: {row[1]} | Description: {row[2]} | Hash: {row[3]}')
            else:
                print('There are no tasks.')


    list_task(all=args.all, today=args.today)
