#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    # User Response
    user_res = requests.get(user_uri).json()

    # Name of the employee
    name = user_res.get('name')

    # User TODO Response
    todo_res = requests.get(todo_uri).json()

    # Total number of tasks, the sum of completed and non-completed tasks
    total = len(todo_res)

    # Number of non-completed tasks
    non_completed = sum([elem['completed'] is False for elem in todo_res])

    # Number of completed tasks
    completed = total - non_completed

    # Formatting the expected output
    output_str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(output_str.format(emp_name=name, completed=completed, total=total))

    # Printing completed tasks
    for elem in todo_res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))

    # Exporting data in CSV format
    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for elem in todo_res:
            csv_writer.writerow([emp_id, name, elem['completed'], elem['title']])

    print(f"Data exported to {csv_filename}")

