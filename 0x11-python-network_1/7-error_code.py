#!/usr/bin/python3
""" Sends a request to a given URL and display the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    s = requests.get(url)
    if s.status_code >= 400:
        print("Error code: {}".format(s.status_code))
    else:
        print(s.text)

