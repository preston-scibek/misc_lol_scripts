import time
from set_field import set_field

if __name__ == "__main__":
    while(True): # we brute forcing this shit
        set_field('availability', 'offline')
        time.sleep(5) # set offline every 5 seconds?
