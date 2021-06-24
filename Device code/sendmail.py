import smtplib
def send_mail(email_id,unique_id,password,name):
    message =  f"Hey there the unique id for {name} is {unique_id} and the password is {password}"
    server = smtplib.SMTP_SSL("smtp.gmail.com","medical@123")
    print(f"Email id : {email_id}")
    server.login("Enter your mail id over here","Enter your password over here")
    server.sendmail("Enter your mail id over here",email_id,message)
    server.quit()
