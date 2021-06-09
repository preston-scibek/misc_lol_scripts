import sys

from helper_functions import call_endpoint

# roughly 65200 chars is the limit
def set_status(status_message=""):
	return call_endpoint("/lol-chat/v1/me", "PUT", data={"statusMessage": status_message})

if __name__ == "__main__":
	if len(sys.argv) > 1:
		message = sys.argv[1]
		set_status(status_message=message)
