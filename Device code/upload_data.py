import os
import connect
import serial

def update(conn,table_name):
    ser  =  serial.Serial("/dev/ttyACM0",9600)
    ser.baudrate =  9600
    h_r = 0
    while h_r == 0:
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
        h_r  =  float(x)
    h_r =  str(h_r)
    print(h_r)
    cursor =  conn.cursor()
    cursor.execute("INSERT into {}(Heart_Rate) values(?)".format(table_name),h_r)
    conn.commit()
