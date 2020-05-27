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

print ("Please select job what you want(number)")
print ("")
print ("1. OPBACKUP   - copy your OP directory to openpilot_(timestamp) and back up the kegman.json file")
print ("2. OPINSTALL  - install OP. if exist OP direcoty, rename openpilot to openpilot_(timestamp")
print ("3. OPUPDATE   - run 'git pull' command to update OP latest")
print ("4. OPRESTORE  - replace OP with current OP bak directory referring timestamp")
print ("5. CHBRANCH   - branch change")
print ("6. SEEBRANCH  - confirm current branch")
print ("q. EXIT")


char  = getch()

if (char == "1"):
    ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print ("Copying openpilot to openpilot_(timestamp)...")
    os.system("cp -rp /data/openpilot /data/openpilot_" + ct)
    os.system("cp -f /data/kegman.json /data/kegman.json_" + ct)
    os.system("ls -altr /data")

elif (char == "2"):
    os.system("clear")
    print ("Select Branch you want to install(number)")
    print ("")
    print ("1. OPKR_0.7.3")
    print ("2. OPKR_0.7.4")
    print ("3. OPKR_0.7.5")
    print ("4. OPKR_0.7.3_BOLT")
    print ("5. OPKR_0.7.3_HKG_community")
    print ("q. EXIT")
    
    char2  = getch()

    if (char2 == "1"):    
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        os.system("mv /data/openpilot /data/openpilot_" + ct)
        os.system("cd /data; git clone https://github.com/openpilotkr/openpilot.git; cd openpilot; git checkout OPKR_0.7.3; reboot")
    elif (char2 == "2"):
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        os.system("mv /data/openpilot /data/openpilot_" + ct)
        os.system("cd /data; git clone https://github.com/openpilotkr/openpilot.git; cd openpilot; git checkout OPKR_0.7.4; reboot")
    elif (char2 == "3"):
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        os.system("mv /data/openpilot /data/openpilot_" + ct)
        os.system("cd /data; git clone https://github.com/openpilotkr/openpilot.git; cd openpilot; git checkout OPKR_0.7.5; reboot")
    elif (char2 == "4"):
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        os.system("mv /data/openpilot /data/openpilot_" + ct)
        os.system("cd /data; git clone https://github.com/openpilotkr/openpilot.git; cd openpilot; git checkout OPKR_0.7.3_BOLT; reboot")
    elif (char2 == "5"):
        ct = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        os.system("mv /data/openpilot /data/openpilot_" + ct)
        os.system("cd /data; git clone https://github.com/openpilotkr/openpilot.git; cd openpilot; git checkout OPKR_0.7.3_HKG_community; reboot")

elif (char == "3"):
    os.system("cd /data/openpilot; git pull")

elif (char == "4"):
    os.system("cd /data; rm -rf openpilot; curopdir=`ls -aldrt /data/openpilot_* | awk -F '/' '{print $3}' | tail -n 1`; mv $curopdir openpilot; reboot")

elif (char == "5"):
    os.system("clear")
    print ("Select Branch you want to change(number)")
    print ("")
    print ("1. OPKR_0.7.3")
    print ("2. OPKR_0.7.4")
    print ("3. OPKR_0.7.5")
    print ("4. OPKR_0.7.3_BOLT")
    print ("5. OPKR_0.7.3_HKG_community")
    print ("q. EXIT")

    char5  = getch()

    if (char5 == "1"):
        os.system("cd /data/openpiot; git pull")
        os.system("cd /data/openpilot; git checkout OPKR_0.7.3; reboot")
    elif (char5 == "2"):
        os.system("cd /data/openpiot; git pull")
        os.system("cd /data/openpilot; git checkout OPKR_0.7.4; reboot")
    elif (char5 == "3"):
        os.system("cd /data/openpiot; git pull")
        os.system("cd /data/openpilot; git checkout OPKR_0.7.5; reboot")
    elif (char5 == "4"):
        os.system("cd /data/openpiot; git pull")
        os.system("cd /data/openpilot; git checkout OPKR_0.7.3_BOLT; reboot")
    elif (char5 == "5"):
        os.system("cd /data/openpiot; git pull")
        os.system("cd /data/openpilot; git checkout OPKR_0.7.3_HKG_community; reboot")

elif (char == "6"):
    os.system("cd /data/openpilot; git branch")