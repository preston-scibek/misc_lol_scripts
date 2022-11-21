import requests
api_key = ""
s = "aZ4dUkCl7W0Grr7cgNFEaI2P3sn6ETwkYnNlH5VKqv9iYZmijlEBVoEN6iJi9U4nsK47x-VwpJweZg"
url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/aZ4dUkCl7W0Grr7cgNFEaI2P3sn6ETwkYnNlH5VKqv9iYZmijlEBVoEN6iJi9U4nsK47x-VwpJweZg/ids?start=0&count=20&api_key={api_key}"

match_ids = requests.get(url).json()
busted = 0
for match_id in match_ids:
    busted += 1
    url2 = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    match = requests.get(url2).json()
    team1 = []
    team2 = []
    seen_champs = {}
    sstr = None
    for participant in match['info']['participants']:
        if seen_champs.get(participant['championName']) and participant['teamId'] == seen_champs[participant['championName']]:
            sstr = f"{participant['puuid'][0:5]} has duplicated their allied {participant['championName']}"
        else:
            seen_champs[participant['championName']] = participant['teamId']
        if participant['teamId'] == 100:
            team1.append(participant['puuid'])
        else:
            team2.append(participant['puuid'])
    if len(team1) == 6:
        if s in team1:
            print(f'team1 has 6 members for {match_id} and the offending user is on the team')
        else:
            print(team1)
            print(f'team1 has 6 members for {match_id} and the offending user is not on the team')
    elif len(team2) == 6:
        if s in team2:
            print(f'team2 has 6 members for {match_id} and the offending user is on the team')
        else:
            print(f'team2 has 6 members for {match_id} and the offending user is not on the team')
    else:
        print(f"the match for {match_id} is 5v5")
        busted -= 1
    if sstr:
        print(sstr)

print(f"{busted} matches were 6v4 out of {len(match_ids)}")
