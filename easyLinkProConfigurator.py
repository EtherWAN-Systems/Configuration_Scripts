#================================================================================
#This is Proprietary Information of the following:
#
# SOFTWARE: EasyLink Configurator ("Brian TWOter")
# Authors: Dylan Han & Brian Tutor & Liam McCabe
# ETHERWAN SYSTEMS INC
# ANAHEIM, CA
#
#Under no circumstances, without proper authorization of either company is this
#object to be released, copied, or reproduced in an environment outside the confines
#of EtherWAN Systems Inc.
#================================================================================


#=======================================================
#=======================================================
#==================[GlobalVariables]====================
#name = ""
#POnumber = ""
#shippingmethod = ""
link = "EtherWANPDFOFTHETHING.com"
shippingtype = ""
shippingspeed =  ""
shippingdate = ""
filename = ""
salt = "w4L2M1QR"
#=======================================================


#=======================================================
#=======================================================
#=====================[PACKAGES]========================
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
#=======================================================


#======================================================= 
def INTRO():
    print("====================================================")
    print("  ______ _   _            __          __     _   _  ")
    print(" |  ____| | | |           \ \        / /\   | \ | | ")
    print(" | |__  | |_| |__   ___ _ _\ \  /\  / /  \  |  \| | ")
    print(" |  __| | __| '_ \ / _ \ '__\ \/  \/ / /\ \ | . ` | ")
    print(" | |____| |_| | | |  __/ |   \  /\  / ____ \| |\  | ")
    print(" |______|\__|_| |_|\___|_|    \/  \/_/    \_\_| \_| ")
    print("          [EasyLink Configurator Software]          ")
    print("    Author(s): Brian Tutor, Dylan Han, Liam McCabe  ")
    print("                                                    ")
    print("====================================================")
#=======================================================
def searchFILES():
    if(os.path.exists('EasyLinkA.txt') and os.path.exists('EasyLinkB.txt')):
        print("Both files found!")
        return True
    else:
        print("Cannot locate both files. Please make sure 'EasyLinkA.txt' & 'EasyLinkB.txt' are in current directory.")
        return False
#=======================================================
def runPROGRAM():
    global SSID
    global SSIDA
    global SSIDB
    global SERIAL
    global SERIALP

    done = False
    while(not done):
        print("Please set a SSID name for the bridges: ")
        SSID = input()
        print("Is SSID: '" + SSID + "' correct?")
        checkConfirm = False
        while(not checkConfirm):
            answer = input("y or n [y]:")
            if(answer == "" or answer == "y"):
                SSIDA = SSID + "A.rsc"
                SSIDB = SSID + "B.rsc"
                SERIAL = SSID
                SERIALP = SSID + "etherwan"
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
    print("Trying")
    while(not checkRestart):
        restart = input("Would you configure another? y or n [y]:")
        if(restart == 'y' or restart == ""):
            checkRestart = True
            configure()
        elif(restart == "n"):
            checkRestart = True
            print("Goodbye")
        else:
            print("Please enter either y or n")
#=======================================================
def wordCHANGER():
    os.mkdir(SSID)
    f = open("EasyLinkA.txt")
    f1 = open(SSID + "/" + SSIDA, 'a')
    for x in f.readlines():
            f1.write(x)
    f.close()
    f1.close()

    g = open("EasyLinkB.txt")
    g1 = open(SSID + "/" + SSIDB, 'a')
    for y in g.readlines():
            g1.write(y)
    g.close()
    g1.close()
#=======================[SSID CHANGE]===================
    with open(SSID + "/" + SSIDA, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHID', SSID)
    with open(SSID + "/" + SSIDA, 'w') as file:
        file.write(filedata)

    with open(SSID + "/" + SSIDB, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHID', SSID)
    with open(SSID + "/" + SSIDB, 'w') as file:
        file.write(filedata)
#=======================================================

#=======================[WPA2 KEYGEN]===================

    md5 = hashlib.md5( (SSID+salt).encode('utf-8')) 
    md5hex = md5.hexdigest()
    buffer = md5hex[0:20]
    
    rand20key = buffer

    with open(SSID + "/" + SSIDA, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHKEY123', rand20key)
    with open(SSID + "/" + SSIDA, 'w') as file:
        file.write(filedata)

    with open(SSID + "/" + SSIDB, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHKEY123', rand20key)
    with open(SSID + "/" + SSIDB, 'w') as file:
        file.write(filedata)
#=======================================================

#=======================[ADD PASSWORD]==================
    md5A = hashlib.md5( (SSIDA+salt).encode('utf-8')) 
    md5B = hashlib.md5( (SSIDB+salt).encode('utf-8')) 
    hiddenSSID = hashlib.md5(bytes(SERIAL, 'UTF-8')).hexdigest()
    hiddenSSIDP = hashlib.md5(bytes(SERIALP, 'UTF-8')).hexdigest()

    md5Ahex = md5A.hexdigest()
    md5Bhex = md5B.hexdigest()

    abuffer = md5Ahex[0:7]
    bbuffer = md5Bhex[0:7]

    abuffer = abuffer + "A"
    bbuffer = bbuffer + "B"

    PWA = abuffer
    PWB = bbuffer

    with open(SSID + "/" + SSIDA, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHPWA', PWA)
    with open(SSID + "/" + SSIDA, 'w') as file:
        file.write(filedata)

    with open(SSID + "/" + SSIDB, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('ETHPWB', PWB)
    filedata = filedata.replace('HIDDENSSIDP', hiddenSSIDP)
    filedata = filedata.replace('HIDDENSSID', hiddenSSID)
    with open(SSID + "/" + SSIDB, 'w') as file:
        file.write(filedata)

#=======================================================

#======================[PRINT PW FILE]================== 
    SSIDPW = SSID + "/" + SSID + "PASSWORDS.txt"
    with open(SSIDPW, 'w') as file:
        texterA = SSIDA + " password is: " + PWA
        texterB = SSIDB + " password is: " + PWB
        texterHidden = "Hidden SSID: " + hiddenSSID
        texterHiddenP = "Hidden SSID Password: " + hiddenSSIDP
        texterWPA = "WPA2 password is: " + rand20key
        file.write(texterA)
        file.write("\n")
        file.write(texterB)
        file.write("\n")
        file.write(texterWPA)
        file.write("\n")
        file.write(texterHidden)
        file.write("\n")
        file.write(texterHiddenP)
        file.write("\n")
        
    print("\n")
    print("Output files successfully created!")
    print("Files stored in directory: " + SSID )
    print("Also, your passwords are stored in '" + SSIDPW + "'.")
    print("Your passwords are:")
    print(SSIDA + " password is: " + PWA)
    print(SSIDB + " password is: " + PWB)
    print("WPA2KEY password is: " + rand20key)
    print("Please store these passwords and do not lose them.")

def configure():
    if(searchFILES()):
        runPROGRAM()
    runAgain()

#=======================================================
#=======================================================
#=================[MAIN]================================
def main():
    INTRO()
    configure()
main()
#=======================================================
    
