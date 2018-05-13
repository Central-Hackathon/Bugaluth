from ethereum_utils import BlockchainManager
import subprocess
import re
import lazer_input as li
import time

# start a new BlockchainManager
bcManager = BlockchainManager()

time_til_next_item = 5 # seconds

proc = subprocess.Popen(['zbarcam','--nodisplay','/dev/video0'], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    line = line.decode('utf-8').strip()
    r = re.match('QR-Code:(.*)', line)
#   print(line)
    print(r.group(1))

    begin = time.clock() # begin timer
    number_of_items = 0
    item = True
    while item:
        item = li.getInput(begin,100)
        print(item)
        if item:
            number_of_items += 1
            begin = time.clock()

    print("Congrats you just recycled {} items".format(number_of_items))
    bcManager.reward(r.group(1), number_of_items)
