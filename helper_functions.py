__author__ = "Generalbood"
""" This file contains helper methods for dealing with the 
league client api"""
import json
import os
import time
import base64

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


def call_endpoint(endpoint, method, *args):
    """Call the specified LCU endpoint via the given method , substituting in *args as needed"""
    host, token = get_credentials()
    formatted_endpoint = endpoint.format(*args)
    curl_command = "curl -X {} --header 'Accept: application/json' " +\
        "--header 'Authorization: Basic {}' 'https://{}{}' -k"
    curl_command = curl_command.format(method, token, host, formatted_endpoint)
    res_str = os.popen(curl_command).read()
    if res_str:
        return json.loads(res_str)
    return {"response": res_str}
