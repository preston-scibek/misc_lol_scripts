import time
from set_field import set_field

if __name__ == "__main__":
    while(True): # we brute forcing this shit
        res = set_field('availability', 'offline')
        print(f"availability is now {res['availability']}")
        time.sleep(5) # set offline every 5 seconds?
