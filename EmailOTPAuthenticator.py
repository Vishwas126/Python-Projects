import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
otp=random.randint(1111,9999)

smtp_server="smtp.gmail.com"
smtp_port=587
mailusername="ammavishwas786@gmail.com"
mailpassword="qkxt meth mqjl jjnl"

from_email="ammavishwas786@gmail.com"
to_email=input("Enter Your Email Address: ")
subject= "OTP for validatio"
body=f"OTP for validation is {otp}"

msg = MIMEMultipart()
msg["From"]=from_email
msg["To"]=to_email
msg["sunject"]=subject
msg.attach(MIMEText(body,"plain"))

server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)
server.quit()

validate=int(input("Enter OTP for validation: "))
if validate == otp:
    print("Login Successfull")
else:
    print("Login Unsuccessfull")
