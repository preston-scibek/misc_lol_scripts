__author__ = "Generalbood"

import json
import os
import time

# Get Token From developer.riotgames.com
token = "notLeakingMyToken"
# IDK if host changes with each launch, might need rift explorer to find it. https://github.com/Pupix/rift-explorer
host = "'https://127.0.0.1:44563"
while(json.loads(os.popen("curl -X GET --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-champ-select/v1/session' -k".format(token, host)).read())['httpStatus'] == 404):
        # launch
        os.system("curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-lobby/v2/lobby/matchmaking/search' -k".format(token, host))
        time.sleep(58)
        # kill
        os.system("curl -X DELETE --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-lobby/v2/lobby/matchmaking/search' -k".format(token, host))

