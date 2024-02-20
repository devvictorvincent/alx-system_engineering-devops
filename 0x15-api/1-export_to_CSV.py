#!/usr/bin/python3
"""
this module gets user info from and api
and writes to a csv file in a specific
format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))

    user = user_response.json()

    username = user.get("username")
    data = {"userId": user_id}
    todos_data = requests.get(url + "todos", params=data)

    todos = todos_data.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        mywriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            mywriter.writerow(
                    [user_id, username, todo.get("completed"),
                        todo.get("title")])
