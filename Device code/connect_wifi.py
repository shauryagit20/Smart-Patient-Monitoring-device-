import Read_files
import os
import time
def connect():
    file_path ="/etc/wpa_supplicant/wpa_supplicant.conf"
    os.system("sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf")

    with open(file_path,"r") as f:
        l =  f.readlines()
    print(l)
    l = ['ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n', 'update_config=1\n', 'country=IN\n', '\n', 'network={\n', '\tssid="Rajkiran"\n', '\tpsk="7276500229"\n', '\tkey_mgmt=WPA-PSK\n', '}\n']
    x =  Read_files.getSSID()
    y =  Read_files.getPassword()

    st =  f"\tssid=\"{x}\"\n"
    password  =  f"\tpsk=\"{y}\"\n"

    print(l[0])
    
    print(st)
    l[5] =  st
    l[6] = password
    print(l)
    with open(file_path,'w') as f:
        context = ""
        f.write(context)
    with open(file_path,"a") as f:
        l =  f.writelines(l)

    os.system("wpa_cli -i wlan0 reconfigure")
    time.sleep(45)
