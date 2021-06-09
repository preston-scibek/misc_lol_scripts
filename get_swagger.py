import json

from helper_functions import call_endpoint


# powershell command to launch client with swagger enabled
#  &"C:\Riot Games\League of Legends\LeagueClient.exe" "--system-yaml-override=C:\Dev\misc_lol_scripts\system.yaml"
# can use this to get the results
# https://editor.swagger.io/

get_res = call_endpoint("/swagger/v2/swagger.json", "GET")
# write the output to a file
with open('swagger_res.json', "w+") as swagger_file:
	json.dump(get_res, swagger_file, indent=4)