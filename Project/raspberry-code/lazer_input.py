import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

def getInput(timer_start,offset=1,time_til_next_item=5):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN)


    zeros_counted = 0
    curr_sec = 0
    while zeros_counted < offset and time.clock() - timer_start < time_til_next_item:
        countdown = time.clock() - timer_start
        if countdown > curr_sec:
            print("Insert item in {} seconds".format(round(time_til_next_item - time.clock() + timer_start)))
            curr_sec += 1

        # nothing in bin
        if not GPIO.input(11):
            zeros_counted += 1

    time.sleep(0.5)
    # something went in the bin
    if zeros_counted == 0:
        return False
    else:
        return True

if __name__=="__main__":
    getInput()
