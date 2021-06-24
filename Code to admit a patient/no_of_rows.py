import Connect


def no_of_rows(databse_name):
    sr_no = 0
    conn = Connect.connection(databse_name)
    cursor = conn.cursor()
    cursor.execute("Select * from Patient_info")
    rows = cursor.fetchall()
    sr_no = len(rows)
    return sr_no
