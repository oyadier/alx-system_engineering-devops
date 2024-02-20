#!/usr/bin/python3
"""Export Json to CSV"""
from requests import get
from sys import argv


def json_to_csv(user_id):
    usr_name = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    task_usr = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    response = get(usr_name)
    name = response.json().get('username')

    """Getting Users task"""
    content = get(task_usr)
    tasks = content.json()

    """Converting it to CSV"""
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, name, task.get('completed'),
                               task.get('title')))


if __name__ == '__main__':
    json_to_csv(argv[1])
