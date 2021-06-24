import connect

def Add_uid(table_name,UID,Pass):
    conn =  connect.Connect()
    cursor =  conn.cursor()
    cursor.execute("INSERT into {}(UID,Pass) values(?,?)".format(table_name),UID,Pass)
    conn.commit()
