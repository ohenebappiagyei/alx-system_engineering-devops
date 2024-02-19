#!/usr/bin/python3
"""
Retrieves an employee data
with his todo list
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    try:
        # Fetching employee details
        employee_response = requests.get(f"{base_url}/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetching employee's TODO list
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Counting completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        # Displaying employee TODO list progress
        print(
                f"Employee {employee_name} is done with tasks"
                f"({completed_tasks}/{total_tasks}):"
        )

        # Displaying completed tasks titles
        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
