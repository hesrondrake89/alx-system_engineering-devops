#!/usr/bin/python3
"""Retrieves task information from a to-do list based on an employee's ID."""
import requests
import sys

if name == "main":
url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(sys.argv[1])).json()
todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

completed = [t.get("title") for t in todos if t.get("completed") is True]
print("Tasks completed by employee {} ({}/{}):".format(
    user.get("name"), len(completed), len(todos)))
[print("\t {}".format(c)) for c in completed]
