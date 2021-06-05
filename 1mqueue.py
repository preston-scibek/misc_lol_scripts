__author__ = "Generalbood"

import json
import os
import time
import subprocess
import re
import base64
import sys

# Get Token From developer.riotgames.com
#token = "cmlvdDpfMkZENGp1N3psTVNUajc3d1QzLVNB"
# Host changes with each launch, need rift explorer to find it. https://github.com/Pupix/rift-explorer
#host = "https://127.0.0.1:48878"

if 'win' in sys.platform:
    process = os.popen(" wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline").read()
    output = process
else:
    if sys.version[0] == '3':
        process = subprocess.run("wmic.exe PROCESS WHERE name=\\'LeagueClientUx.exe\\' GET commandline", shell=True, stdout=subprocess.PIPE)
        output = str(process.stdout)
        #print(output)
    else:
        process = os.popen("wmic.exe PROCESS WHERE name=\\'LeagueClientUx.exe\\' GET commandline").read()
        #print(process)
        output = process

    lockfile_location =  "/mnt/c/Riot Games/League of Legends/lockfile"
    good_str = ""
    with open(lockfile_location, "r") as lockfile:
        good_str = lockfile.read()
    good_array = good_str.split(":")
    port = good_array[2]
    token = good_array[3]
#port = re.findall("--app-port=(\d+)", str(output))
#if not len(port):
#        print("Is the client running?")
#        exit()
#port = port[0]
host = "127.0.0.1:{}".format(port)

#token = re.findall("--remoting-auth-token=([A-Za-z0-9\-_]*)", str(output))[0]


#print("TOKEN PRE ENCODE: {}".format(token))
token_bytes = "riot:{}".format(token).encode('ascii')
token = base64.b64encode(token_bytes).decode('utf-8')
#print("HOST: {}\nTOKEN: {}".format(host, token))


#print("The curl command is curl -X GET --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-champ-select/v1/session' -k".format(token, host))
# x = os.popen("curl -X GET --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-champ-select/v1/session' -k".format(token, host)).read()
# print("result of curl is '{}'".format(x))

print("curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-lobby/v2/lobby/matchmaking/search' -k".format(token, host))


start_command = "curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' " + \
    "--header 'Authorization: Basic cmlvdDpEejNJaVFOb0RDNXROVVZDWkJ5ZVpn' " + \
    "'https://127.0.0.1:32254/lol-lobby/v2/lobby/matchmaking/search' -k"
start_command2 = start_command = "curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' " + \
    "--header 'Authorization: Basic cmlvdDpEejNJaVFOb0RDNXROVVZDWkJ5ZVpn' " + \
    "'https://127.0.0.1:32254/lol-lobby/v2/lobby/matchmaking/search' -k"
os.system(start_command)

while(json.loads(os.popen("curl -X GET --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-champ-select/v1/session' -k".format(token, host)).read())['httpStatus'] == 404):
        # launch
        #print("starting queue")
        os.system("curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-lobby/v2/lobby/matchmaking/search' -k".format(token, host))
        time.sleep(58)
        # kill
        os.system("curl -X DELETE --header 'Accept: application/json' --header 'Authorization: Basic {}' '{}/lol-lobby/v2/lobby/matchmaking/search' -k".format(token, host))
 
