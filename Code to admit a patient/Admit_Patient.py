import patient_Data
import no_of_rows
import add_details

def database_connect(x):
    print(x.uniqueid)


def getInput():
    room_available = False
    x = patient_Data.Patient()
    database_name = "Hospital1"
    name = input("Enter the name of the patient : ")
    age = input("Enter the patients age: ")
    disease = input("Enter the reason of hospitalization: ")
    while not room_available:
        room_no = input("Enter the room number: ")
        room_available = True

    contact_no = input("Enter the contact no: ")
    mail_id = input("Enter the mail id: ")

    row_no = no_of_rows.no_of_rows(database_name) + 1
    unique_id = name + str(row_no)

    print(unique_id)
    x.__int__(name, age, disease, room_no, contact_no, mail_id, unique_id,database_name)
    add_details.Add_details(x)


getInput()
