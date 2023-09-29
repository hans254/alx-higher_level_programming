#!/usr/bin/python3
""" takes URL and Email as arguments. sends a POST request to the
    passed URL with the email as parameter. and finally displays the
    body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    w = requests.post(url, data=email)
    print(w.text)

