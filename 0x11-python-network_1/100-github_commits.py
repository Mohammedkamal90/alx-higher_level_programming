#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Error: Unable to fetch commits")
