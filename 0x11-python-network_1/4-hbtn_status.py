#!/usr/bin/python3
""" fetches http://alx-intranet/hbtn.io/status
    using the requests library.
"""
import requests

if __name__ == "__main__":
    s = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(s.text)))
    print("\t- content: {}".format(s.text))

