import os


os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
def getUniqueId():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "unique_id"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getAge():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "age"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getName():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "name"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getPassword():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "passwd"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getPhoneNo():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename =  "phone_no"
        x =  read_file(phone_no)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getRoomNo():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename =  "room_no"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getDisease():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "disease"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
def getMailId():
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
        filename = "mail_id"
        x =  read_file(filename)
        os.chdir(r"/home/pi/PycharmProjects/IOT_Project")
        return x
        
        
def read_file(filename):
    with open(filename,"r") as f:
        x = f.readline()
    x  =  str(x)
    return x

