#!/usr/bin/python3
from datetime import datetime
from time import sleep
import os

class morningLight:
    def __init__(self):
        self.time = datetime.now

    def getTime(self):
        self.time = datetime.now()
        return datetime.now().hour, datetime.now().minute, datetime.now().second

    def checkTime(self, h, m, s):
        if h == 16:
            print("Pwm: %i" % ((m*100)/60))
        else:
            print("Pwm: 0")

def main():
    print("Created object timer")
    timer = morningLight()
    while True:
        hour, minute, second = timer.getTime()
        print("\n\n\n\n\n\nhour:%i \tminute:%i\tsecond:%i \n---------------------------------" % (hour, minute, second))
        timer.checkTime(hour,minute,second)
        sleep(1)


main()
