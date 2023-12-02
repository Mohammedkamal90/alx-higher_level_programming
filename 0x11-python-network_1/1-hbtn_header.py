#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('https://alx-intranet.hbtn.io/status')
        print(x_request_id)
        print("\t- type: {}".format(type(x_request_id)))
        print("\t- content: {}".format(x_request_id))
        print("\t- utf8 content: {}".format(x_request_id.decode("utf-8")))
