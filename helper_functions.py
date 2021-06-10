__author__ = "Generalbood"
""" This file contains helper methods for dealing with the 
league client api"""
import json
import os
import time
import base64

import requests

# fuck the ssl warning
import warnings
warnings.filterwarnings("ignore")

def get_credentials():
    """Retreive the current client credentials from the lock file"""
    # read from lockfile
    # replace this with your league install
    lockfile_location =  "/mnt/c/Riot Games/League of Legends/lockfile"
    with open(lockfile_location, "r") as lockfile:
        lockfile_array = lockfile.read().split(":")
        port = lockfile_array[2]
        token = lockfile_array[3]

    host = "127.0.0.1:{}".format(port)
    # encode the auth token
    token_bytes = "riot:{}".format(token).encode('ascii')
    token = base64.b64encode(token_bytes).decode('utf-8')
    return host, token


def call_endpoint(endpoint, method, *args, **kwargs):
    """Call the specified LCU endpoint via the given method , substituting in *args as needed"""
    host, token = get_credentials()
    formatted_endpoint = endpoint.format(*args)
   
    headers = {
        'Authorization': 'Basic {}'.format(token)
    }

    data = kwargs.get('data', None)
    full_url = "https://{}{}".format(host, formatted_endpoint)

    if data:
        if method == 'POST':
            res = requests.post(full_url, headers=headers, data=json.dumps(data), verify=False)
        elif method == 'PUT':
            res = requests.put(full_url, headers=headers, data=json.dumps(data), verify=False)
        elif method == 'PATCH':
            res = requests.patch(full_url, headers=headers, data=json.dumps(data), verify=False)
        elif method == 'GET':
            res = requests.get(full_url, headers=headers, data=json.dumps(data), verify=False)
    else:
        if method == 'GET':
            res = requests.get(full_url, headers=headers, verify=False)
        elif method == 'DELETE':
            res = requests.delete(full_url, headers=headers, verify=False)
        elif method == 'POST':
            res = requests.post(full_url, headers=headers, verify=False)
        elif method == 'PUT':
            res = requests.put(full_url, headers=headers, verify=False)
        elif method == 'PATCH':
            res = requests.patch(full_url, headers=headers, verify=False)
    try:
        return res.json()
    except ValueError:
        return res