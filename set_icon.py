import sys

from helper_functions import call_endpoint

# roughly 65200 chars is the limit
def set_icon(icon_id=0):
	return call_endpoint("/lol-summoner/v1/current-summoner/icon/", "PUT", data={
		  "inventoryToken": "string",
		  "profileIconId": icon_id
		})

if __name__ == "__main__":
	if len(sys.argv) > 1:
		icon_id = sys.argv[1]
		print(set_icon(icon_id=icon_id))
