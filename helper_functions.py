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

# WARNING
# IF YOU ARE ON WSL2
# THIS CODE WILL NOT WORK
# AS THERE IS NO WAY TO ACCESS THE RIOT LOCAL API
# VIA WSL2
# EVEN IF YOU USE get_windows_host AND ALLOW THE PORT IN FIREWALL
# RIOTS API IS STILL LOOKING ON LOCALHOST
# https://stackoverflow.com/questions/64763147/access-a-localhost-running-in-windows-from-inside-wsl2
# HOWEVER POWERSHELL WORKS FINE
def in_wsl():
    from platform import uname
    return 'microsoft-standard' in uname().release

def get_windows_host():
    import subprocess
    cmd = "grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'"
    cmd = "echo $(hostname).local"
    process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return str(process.stdout.decode('utf-8').strip())


def get_credentials():
    """Retreive the current client credentials from the lock file"""
    # read from lockfile
    # replace this with your league install
    
    
    lockfile_location =  "/mnt/e/Riot Games/League of Legends/lockfile" if in_wsl() else 'E:\Riot Games\League of Legends\lockfile'
    
    with open(lockfile_location, "r") as lockfile:
        lockfile_array = lockfile.read().split(":")
        port = lockfile_array[2]
        token = lockfile_array[3]

    host = f"{get_windows_host() if in_wsl() else '127.0.0.1'}:{port}"
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
    print(f"calling {full_url}")
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
        print(res.json())
        return res.json()
    except ValueError:
        print(res.text)
        return res
