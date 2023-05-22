#!/usr/bin/python3
"""Retrieves task information from a to-do list based on an employee's ID."""
import requests
import sys

import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        employee_name = employee_data['name']

        completed_tasks = [task['title'] for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos_data)

        print(f'Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):')
        print(f'{employee_name}: {number_of_done_tasks}/{total_number_of_tasks}')

        for task_title in completed_tasks:
            print(f'\t{task_title}')

    except requests.exceptions.HTTPError as e:
        print(f'An error occurred: {e}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

# Example usage
employee_id = 1
get_employee_todo_progress(employee_id)
