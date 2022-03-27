import sys

from helper_functions import call_endpoint

def set_field(field, value):
    get_res = call_endpoint("/lol-chat/v1/me", "GET")
    if "." in field:
        keylist = field.split(".")
        temp = get_res
        for key in keylist[0:-1]:
            temp = temp[key]
        temp[keylist[-1]] = value
        
        #get_res[field.split][field.split(".")[1]] = value
    else:
        get_res[field] = value
    return call_endpoint("/lol-chat/v1/me", "PUT", data=get_res)


if __name__ == "__main__":
        field = sys.argv[1] if len(sys.argv) > 1 else "statusMessage"
        value = sys.argv[2] if len(sys.argv) > 2 else "set via cli"
        res = set_field(field, value)
        print(res)
