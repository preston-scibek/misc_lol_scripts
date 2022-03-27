import sys

from helper_functions import call_endpoint


if __name__ == "__main__":
        endpoint = sys.argv[1] if len(sys.argv) > 1 else "/liveclientdata/allgamedata"
        method = sys.argv[2] if len(sys.argv) > 2 else "GET"
        data = sys.argv[2] if len(sys.argv) > 3 else {}
        res = call_endpoint(endpoint, method, data=data)
        print(res)
