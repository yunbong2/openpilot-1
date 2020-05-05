import subprocess
import os
import time
from datetime import datetime

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))

import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.2

print ("Please select job what you want(number).")
print ("")
print ("1. OPBACKUP   - copy your openpilot directory to openpilot_(datetimestamp) and still remain openpilot dir")
print ("2. OPINSTALL  - install the openpilot directory. if exist OP direcoty, rename openpilot to openpilot_(datetimestamp")
print ("3. OPUPDATE   - run 'git pull' command to update OP latest")
print ("4. OPRESTORE  - restore openpilot with current OP directory referring timestamp")
print ("5. CHBRANCH   - branch change")
print ("6. SEEBRANCH  - confirm current branch")
print ("7. SEEFORK    - confirm current fork")
print ("z. EXIT)


char  = getch()

if (char == "1"):
    ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print (ct)

elif (char == "z"):
    process.kill()
    break

time.sleep(button_delay)