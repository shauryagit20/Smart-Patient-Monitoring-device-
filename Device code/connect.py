import pyodbc

def Connect():
    conn = pyodbc.connect('DRIVER={FreeTDS};Server=192.168.1.31;PORT=1433;DATABASE=Hospital1;UID=SA;PWD=Enter your password over here;TDS_Version=7.2;')
    
    return conn

print(Connect())