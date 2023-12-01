#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_info = response.json()
        print(user_info.get('id'))
    except ValueError:
        print(None)
