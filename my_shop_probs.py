import json

from helper_functions import call_endpoint

def my_shop_i_think():
    my_id_res = call_endpoint("/lol-chat/v1/me", "GET")
    my_id = my_id_res['summonerId']
    res = call_endpoint("/lol-tastes/v1/skins-model", "GET")

    res['modelData']['payload'] = sorted(res['modelData']['payload'], key=lambda champ: champ['prob'], reverse=True)

    print(json.dumps(res, indent=4))

    count = 0
    top_champs = []
    for champ in res['modelData']['payload']:
    	top_champs.append(champ)
    	count += 1
    	if count >= 10:
    		break

    print("Your top champs are:")
    for champ in top_champs:
        try:
            print("{} at {}%".format(champ['championName'], champ['prob'] * 100))
        except KeyError:
            res = call_endpoint(f"/lol-champions/v1/inventories/{my_id}/champions/{champ['championId']}", "GET")
            print(f"{res['alias']} at {champ['prob'] * 100}%")
    return res


if __name__ == "__main__":
    my_shop_i_think()
