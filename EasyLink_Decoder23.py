import os
import os.path
import time
import fileinput
import shutil
import random
import string
#import graphics
import hashlib
import binascii

salt = "w4L2M1QR"

def INTRO():
    print("====================================================")
    print("  ______ _   _            __          __     _   _  ")
    print(" |  ____| | | |           \ \        / /\   | \ | | ")
    print(" | |__  | |_| |__   ___ _ _\ \  /\  / /  \  |  \| | ")
    print(" |  __| | __| '_ \ / _ \ '__\ \/  \/ / /\ \ | . ` | ")
    print(" | |____| |_| | | |  __/ |   \  /\  / ____ \| |\  | ")
    print(" |______|\__|_| |_|\___|_|    \/  \/_/    \_\_| \_| ")
    print("            [EasyLink Decoder Software]             ")
    print("    Author(s): Brian Tutor, Dylan Han, Liam McCabe  ")
    print("                                                    ")
    print("====================================================")

def runPROGRAM():
    global SSID
    global SSIDA
    global SSIDB
    done = False
    while(not done):
        print("Please Enter the serial number for the bridges: ")
        SSID = input()
        print("Is Serial Number: '" + SSID + "' correct?")
        checkConfirm = False
        while(not checkConfirm):
            answer = input("y or n [y]:")
            if(answer == "" or answer == "y"):
                SSIDA = SSID + "A.rsc"
                SSIDB = SSID + "B.rsc"
                wordCHANGER()
                done = True
                break
            elif(answer == "n"):
                checkConfirm = True
            else:
                print("Please enter either y or n")

#=======================================================
def runAgain():
    checkRestart = False
    while(not checkRestart):
        restart = input("Would you display another? y or n [y]:")
        if(restart == 'y' or restart == ""):
            checkRestart = True
            runPROGRAM()
        elif(restart == "n"):
            checkRestart = True
            print("Goodbye")
        else:
            print("Please enter either y or n")
#=======================================================
def wordCHANGER():
#=======================[WPA2 KEYGEN]===================

    md5 = hashlib.md5( (SSID+salt).encode('utf-8')) 
    md5hex = md5.hexdigest()
    buffer = md5hex[0:20]
    
    rand20key = buffer

#=======================[ADD PASSWORD]==================
    md5A = hashlib.md5( (SSIDA+salt).encode('utf-8')) 
    md5B = hashlib.md5( (SSIDB+salt).encode('utf-8')) 

    md5Ahex = md5A.hexdigest()
    md5Bhex = md5B.hexdigest()

    abuffer = md5Ahex[0:7]
    bbuffer = md5Bhex[0:7]

    abuffer = abuffer + "A"
    bbuffer = bbuffer + "B"

    PWA = abuffer
    PWB = bbuffer

#======================[PRINT PW FILE]================== 
    print("\n" + SSIDA + " password is: " + PWA)
    print(SSIDB + " password is: " + PWB)
    print("WPA2KEY password is: " + rand20key + "\n")
    runAgain()

def main():
    INTRO()
    runPROGRAM()
main()