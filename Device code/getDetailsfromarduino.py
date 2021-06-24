import RPi.GPIO as gpio
import serial
import time
import os
def getdetails():
    green_led=  16
    red_led =  26
    gpio.setwarnings(False)
    ser = serial.Serial('/dev/ttyACM1',9600)
    print("execute")
    input_string = ""
    ser.baudrate = 9600
    ssid = ""
    password = "" 
    gpio.output(green_led,gpio.HIGH)
    gpio.output(red_led,gpio.LOW)
    while(len(input_string) == 0):
        gpio.output(green_led,gpio.LOW)
        gpio.output(red_led,gpio.HIGH)
        input_string =  ser.readline();
    if(len(input_string)>0):
        
        gpio.output(green_led,gpio.HIGH)
        gpio.output(red_led,gpio.LOW)
    while(len(ssid) == 0):
        gpio.output(green_led,gpio.LOW)
        gpio.output(red_led,gpio.HIGH)
        ssid =  ser.readline();
    while(len(password) == 0):
        gpio.output(green_led,gpio.LOW)
        gpio.output(red_led,gpio.HIGH)
        password =  ser.readline();
    print(ssid)
    print(password)
    print(input_string)

    ssid =  preprocess(str(ssid))
    password =  preprocess(str(password))
    room_no =  preprocess(str(input_string))

    print(f"SSID : {ssid}")
    print(f"password : {password}")
    print(f"room_no :  {room_no}")

    delete_file("password")
    delete_file("room_no")
    delete_file("SSID")
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
    create_file("password",password)
    create_file("room_no", room_no)
    create_file("SSID",ssid)
    
def preprocess(var):
        chara =  '\''
        print(chara)
        o =  var.split(chara)
        list_o =  list(o[1])
        list_o.pop(-1)
        list_o.pop(-1)
        list_o.pop(-1)
        list_o.pop(-1)
        for index in range(len(list_o)):
            list_o[index]  =  str(list_o[index])
        return_s =  "".join(list_o)
        return return_s
def delete_file(filename):
    try:
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
        os.remove(filename)
    except:
        print("File doess not exist")
def create_file(category,data):
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
    filename =  category +  ".txt"
    with open(filename, "w") as f:
        f.write(data)
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project")    
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
