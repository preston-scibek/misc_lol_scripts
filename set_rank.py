import sys

from helper_functions import call_endpoint

def set_rank(rank="CHALLENGER"):
	
	get_res = call_endpoint("/lol-chat/v1/me", "GET")
	get_res['lol']['rankedLeagueTier'] = rank
	return call_endpoint("/lol-chat/v1/me", "PUT", data=get_res)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		rank = sys.argv[1]
		set_rank(rank=message)
	set_rank()