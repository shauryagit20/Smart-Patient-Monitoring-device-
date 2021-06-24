import Read_files
import connect
import os

def getDetails():
    conn =  connect.Connect()
    cursor =  conn.cursor()
    room_no =  Read_files.getRoomNo()
    room_no =  int(room_no)
    cursor.execute("Select * from Patient_info where roomno = ?",room_no)
    patient_details =  cursor.fetchone()
    print(patient_details)
    create_file("name",patient_details[1])
    create_file("age",patient_details[2])
    create_file("disease",patient_details[3])
    create_file("phone_no",patient_details[4])
    create_file("mail_id",patient_details[5])
    create_file("room_no",patient_details[6])
    create_file("unique_id",patient_details[7])

def CheckPulse():
    room_no =  Read_files.getRoomNo()
    room_no =  int(room_no)
    conn =  connect.Connect()
    cursor =  conn.cursor()
    cursor.execute("Select roomno from Patient_info")
    list_of_rows = cursor.fetchall()
    print(list_of_rows)
    for ele in list_of_rows:
        room_db =  ele[0]
        if room_db ==  room_no:
            return True
    return False
def create_file(filename,detail):
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/patient_details")
    with open(filename,"a") as f:
        f.write(str(detail))
    os.chdir(r"/home/pi/PycharmProjects/IOT_Project/")
