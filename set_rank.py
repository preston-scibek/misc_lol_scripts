import sys

from helper_functions import call_endpoint

def set_rank(rank="CHALLENGER", division="IV"):
    get_res = call_endpoint("/lol-chat/v1/me", "GET")
    get_res['lol']['rankedLeagueTier'] = rank
    get_res['lol']['rankedLeagueDivision'] = division
    return call_endpoint("/lol-chat/v1/me", "PUT", data=get_res)


if __name__ == "__main__":
        rank = sys.argv[1] if len(sys.argv) > 1 else "CHALLENGER"
        division = sys.argv[2] if len(sys.argv) > 2 else "IV"
        set_rank(rank=rank, division=division)
