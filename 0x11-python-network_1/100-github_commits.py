#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repository)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print("Request Error:", err)
        sys.exit(1)

    commits = response.json()[:10]

    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit', {}).get('author', {}).get('name')
        print("{}: {}".format(sha, author_name))
