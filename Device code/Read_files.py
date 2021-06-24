import os


def getSSID():
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
    with open("SSID.txt","r") as f:
        ssid =  f.read()
    return ssid

def getPassword():
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
    with open("password.txt","r") as f:
        password =  f.read()
    return password

def getRoomNo():
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
    with open("room_no.txt","r") as f:
        room_no =  f.read()
    return room_no

