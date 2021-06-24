import os
import gpiozero
import RPi.GPIO as gpio
import time

def isConnected():
    try:
        res  = os.system("ping -c 1 google.com")
        print(res)
        if(res == 0):
            return True
        else:
            return False
    except:
        return  False
    
def isConnected_aftercheck():
    green_led =  16
    red_led =  26
    gpio.setmode(gpio.BCM)
    gpio.setup(red_led,gpio.OUT)
    gpio.setup(green_led,gpio.OUT)
    try:
        res =  os.system("ping -c 1 google.com")
        return True
    except:
        return False