##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Device for Robot(Server)

#Packages
from RN42 import RN42
from time import sleep
import RPi.GPIO as GPIO
import sys
import time

#Libraries
#--import Settings

def main():
    #""" Main Class """
    # Setting & Connect
    ras = RN42("ras", "B8:27:EB:B9:40:6E", 1)
    ras.connectBluetooth(ras.bdAddr,ras.port)

    print("Entering main loop now")

    while 1:
        try:
            ras.sock.send("Hello World")
            print("data send")
            time.sleep(1)
        except KeyboardInterrupt:
            ras.disconnect(ras.sock)

if __name__ == '__main__':
    main()

#---END---