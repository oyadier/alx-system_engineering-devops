#!/usr/bin/python3
"""calling content of ID"""

from requests import get
import sys


if __name__ == '__main__':
    '''main function'''
    """
        Getting the user name
    """
    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    content = get(url)
    name = content.json().get('name')

    """
        Getting the todos of a particuler user by Id
    """
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    content = get(url)
    user_todo = content.json()
    task_done = 0
    dones = []
    for todo in user_todo:
        if todo.get('completed'):
            task_done += 1
            dones.append(todo)

    print("Employee {} is done with task({}/{}):"
          .format(name, task_done, len(user_todo)))
    for task in dones:
        print("\t {}".format(task.get('title')))
