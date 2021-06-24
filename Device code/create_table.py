import connect


def create_table(table_name):
    conn =  connect.Connect()
    cursor  =  conn.cursor()
    query =  "CREATE TABLE {} (Srno int IDENTITY(1,1), UID varchar(255), Pass varchar(255), Heart_Rate varchar(10) );".format(table_name)
    cursor.execute(query)
    conn.commit()
