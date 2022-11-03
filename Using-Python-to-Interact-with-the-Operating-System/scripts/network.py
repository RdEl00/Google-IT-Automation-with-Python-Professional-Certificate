#!/usr/bin/env python3
import requests
import socket

#check whether the local host is correctly configured
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

#check whether the computer can make successful calls to the internet
def check_connectivity():
    request = requests.get("http://www.google.com")
    return request.status_code == 200


