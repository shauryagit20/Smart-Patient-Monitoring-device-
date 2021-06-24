import getDetailsfromarduino 
import isConnectedtotheInternet
import gpiozero
import RPi.GPIO as gpio
import os
from signal import pause
import connect_wifi
import time
import detect_pulse
import getDetailsPaitent
import genrate_password
import download_details
import sendmail
import create_table
import insert_UID_Pass
import connect
import upload_data

def main():
    green_led =  16
    red_led =  26
    x =  ""
    
    try:
        with open("Error_file.txt","a") as f:
            x = f.read()
    except:
        print("File does not exists")
               
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(green_led,gpio.OUT)
    gpio.setup(red_led,gpio.OUT)
    gpio.output(green_led,gpio.LOW)
    if(len(x)==0):
        print("Red Led on")
        gpio.output(red_led,gpio.HIGH)
        time.sleep(5)
        print("Red Led off")
        gpio.output(red_led,gpio.LOW)
        time.sleep(5)
        print("Green Led on")
        gpio.output(green_led,gpio.HIGH)
        time.sleep(5)
        print("Green Led off")
        gpio.output(green_led,gpio.LOW)
        time.sleep(5)

    print(isConnectedtotheInternet.isConnected())
    
    if(isConnectedtotheInternet.isConnected()):
        print(isConnectedtotheInternet.isConnected())
        gpio.output(red_led, gpio.LOW)
        gpio.output(green_led, gpio.HIGH)
        print("Gping to stage2")
        main_stage2()
       
    else:
        gpio.output(red_led,  True)
        no_of_files = os.listdir(r"/home/pi/PycharmProjects/IOT_Project/Details")
        if(len(no_of_files) >= 3 and len(x)==0):
            print("Files found")
            connect_wifi.connect()
            gotConnected = isConnectedtotheInternet.isConnected_aftercheck()
            
            if(gotConnected):
                gpio.output(green_led,gpio.HIGH)
                gpio.output(red_led, gpio.LOW)
                print("Hurray")
                main_stage2()
            
            else:
                with open("Error_file.txt","a") as f:
                    print("Error")
                    f.write("Error")
                    main()
        else:
            gpio.output(red_led,gpio.HIGH)
            getDetailsfromarduino.getdetails()
            connect_wifi.connect()
            gotConnected = isConnectedtotheInternet.isConnected_aftercheck()
            
            if(gotConnected):
                gpio.output(green_led,gpio.HIGH)
                gpio.output(red_led, gpio.LOW)
                print("Woaaaah")
                try:
                    os.remove("Error_file")
                    main_stage2()
                except:
                    print("File not found")
                    main_stage2()
                main_stage2()
                
            else:
                with open("Error_file.txt","a") as f:
                    f.write("Error")
                    main()
def main_stage2():
     print("In main stage 2")
     pulse_detected =  detect_pulse.detect_pulse()
     lis_of_files_in_details =  os.listdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
     if(pulse_detected ==  True):
         patient_found =  getDetailsPaitent.CheckPulse()
         if (patient_found):
             conn =  connect.Connect()
             if(len(lis_of_files_in_details)<8):
                 getDetailsPaitent.getDetails()
                 unique_id =  download_details.getUniqueId()
                 print("Patient found")
                 passwd = genrate_password.genrate_password()
                 os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
                 with open("passwd","a") as f:
                     f.write(passwd)
                 os.chdir(r"/home/pi/PycharmProjects/IOT_Project/")
                 mail_id =  download_details.getMailId()
                 name =  download_details.getName()
                 pwd = passwd
                 sendmail.send_mail(mail_id,unique_id,pwd,name)
                 create_table.create_table(unique_id)
                 insert_UID_Pass.Add_uid(unique_id,unique_id,pwd)
                 
                 while True:
                     upload_data.update(conn,unique_id)
                     time.sleep(45)   
             else:
                 unique_id =  download_details.getUniqueId()
                 
                 while True:
                   upload_data.update(conn,unique_id)
                   time.sleep(45)
                 
         else:
            print("False Detection")
            main_stage2()
            

main()