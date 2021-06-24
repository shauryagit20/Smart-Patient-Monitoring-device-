import Connect


def Add_details(x):
    conn = Connect.connection(x.databasename)
    cursor = conn.cursor()

    cursor.execute("insert into Patient_info(Name,Age,Disease,Contactno,Mailid,Roomno,Uniqueid ) values (?, ?, ?, ?, ?, "
                   "?, ?)", x.name,x.age,x.disease,x.contactno,x.mailid,x.roomno,
                   x.uniqueid)
    conn.commit()
