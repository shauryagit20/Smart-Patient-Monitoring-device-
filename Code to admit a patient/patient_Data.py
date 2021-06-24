class Patient:
    name = ""
    age = ""
    mailid = ""
    contactno = 1
    roomno = 0
    uniqueid = 0
    disease = ""
    databasename = ""
    def __int__(self, name, age, disease, roomno, contactno, mailid, uniqueid, databasename):
        self.name = name
        self.age = age
        self.disease = disease
        self.roomno = roomno
        self.contactno = contactno
        self.mailid = mailid
        self.uniqueid = uniqueid
        self.databasename = databasename



