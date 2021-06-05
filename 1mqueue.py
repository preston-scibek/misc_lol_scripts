__author__ = "Generalbood"
""" This file restarts your queue after one minute in 
an attempt to minimze offroling/autofilling"""
import json
import os
import time
import base64

def one_minute_queue():
    """this function restarts your queue after one minute has elaspsed"""
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

    # Generate the curl strings
    champ_select_check = "curl -X GET --header 'Accept: application/json' " +\
        "--header 'Authorization: Basic {}' 'https://{}/lol-champ-select/v1/session' -k"
    champ_select_check = champ_select_check.format(token, host)

    start_queue_curl = "curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' " + \
        "--header 'Authorization: Basic {}' " + \
        "'https://{}/lol-lobby/v2/lobby/matchmaking/search' -k"
    start_queue_curl = start_queue_curl.format(token, host)

    stop_queue_curl = "curl -X DELETE --header 'Content-Type: application/json' --header 'Accept: application/json' " + \
        "--header 'Authorization: Basic {}' " + \
        "'https://{}/lol-lobby/v2/lobby/matchmaking/search' -k"
    stop_queue_curl = stop_queue_curl.format(token, host)

    # execute the core loop
    # lol this key doesn't exist but who cares cuz at this point the program should stop anyways
    while(json.loads(os.popen(champ_select_check).read())['httpStatus'] == 404):
            # start queue
            os.system(start_queue_curl)
            time.sleep(58)
            # stop queue
            os.system(stop_queue_curl)


if __name__ == "__main__":
    one_minute_queue()
