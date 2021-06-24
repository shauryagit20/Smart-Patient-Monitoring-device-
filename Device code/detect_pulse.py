import serial
import time


def detect_pulse():
    pulse_detected =  False
    ser =  serial.Serial('/dev/ttyACM0',9600)
    print("Detecting pulse")
    ser.baudrate =  9600
    x =  ""
    while not pulse_detected:
        x = ser.readline()
        print(x)
        x  =  str(x)
        print(type(x))
        l =  x.split("\'")
        l_o =  l[1]
        l_o =  list(l_o)
        l_o.pop()
        l_o.pop()
        x =  "".join(l_o)
        print(f"Pulse rate:  {x}")
        x  =  float(x)
        if(x>35):
            print("Pulse_Detected")
            pulse_detected =  True
            return True
