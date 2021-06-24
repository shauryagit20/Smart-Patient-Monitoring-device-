import pyodbc


def connection(hospital_name):
    conn = pyodbc.connect(f'DRIVER=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1;'
                          'Server=192.168.1.31;'
                          f'Database={hospital_name};'
                          'UID=SA;'
                          'PWD=Enter the password over here'
                          )
    return conn


hospital_name = "Hospital1"
conn = connection(hospital_name)
cursor =  conn.cursor()

print(cursor)
