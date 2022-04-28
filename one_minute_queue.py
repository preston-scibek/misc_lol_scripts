__author__ = "Generalbood"
""" This file restarts your queue after one minute in 
an attempt to minimze offroling/autofilling"""

import time

from helper_functions import call_endpoint

def one_minute_queue():
    """this function restarts your queue after one minute has elaspsed"""
    while(call_endpoint("/lol-champ-select/v1/session", "GET")['httpStatus'] == 404):
        # start queue
        print('starting queue')
        call_endpoint("/lol-lobby/v2/lobby/matchmaking/search", "POST")
        time.sleep(58)
        # stop queue
        call_endpoint("/lol-lobby/v2/lobby/matchmaking/search", "DELETE")
        print('stoping queue')

if __name__ == "__main__":
    one_minute_queue()
