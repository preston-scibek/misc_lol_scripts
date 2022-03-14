import json
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get('API_KEY')
puuid = os.environ.get('PUUID')
start = 0
count = 100

# why this stupid shit not have all data, ffs
match_list_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?start={}&count={}&api_key={}'
match_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}'

match_list = []

obey_rate_limit1s = 0
obey_rate_limit2m = 0

for i in range(10000):
	if obey_rate_limit2m >= 100:
		print('Sleeping for 120s')
		time.sleep(120)
		obey_rate_limit2m = 0

	if obey_rate_limit1s >= 20:
		print('Sleeping for 1s')
		time.sleep(1)
		obey_rate_limit1s = 0
	
	obey_rate_limit1s += 1
	obey_rate_limit2m += 1
	try:
		print('Calling api for {}:{}'.format(start, start + count))
		res = requests.get(match_list_url.format(puuid, start, count, api_key))

		print(res.text)
		if len(res.json()) > 0:
			match_list += res.json()
			start += count
		else:
			break
	except:
		print(res)
		print(res.text)
		print(i)
		raise

with open('match_ids.json', 'w') as jfile:
	json.dump(match_list, jfile, indent=4)

match_detail_list = []

for match in match_list:
	if obey_rate_limit2m >= 100:
		print('Sleeping for 120s')
		time.sleep(120)
		obey_rate_limit2m = 0

	if obey_rate_limit1s >= 20:
		print('Sleeping for 1s')
		time.sleep(1)
		obey_rate_limit1s = 0
	
	obey_rate_limit1s += 1
	obey_rate_limit2m += 1

	try:
		print('Calling api for {}'.format(match))
		res = requests.get(match_url.format(match))
		match_detail_list.append(res.json())
	except:
		print(res)
		print(res.text)
		print(match)
		raise

with open('match_detail.json', 'w') as jfile:
	json.dump(match_detail_list, jfile, indent=4)
