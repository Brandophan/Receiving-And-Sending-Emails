#to send emails with python, we need to manually go through the steps of connecting to an email server,
#confirming connection, setting a protocol, logging on, and sending the message
#wil be going over this process with a Gmail account 
import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
# or port number 465
#need to run an  E H L O method command that greets the server and establishes the connection


print(smtp_object.ehlo())
print(smtp_object.starttls())
#password = input('What is your password: ')
#better way of getting a password
import getpass
#password = getpass.getpass('Password please: ')

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
print(smtp_object.login(email,password))
from_address = email 
to_address = email
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = "Subject: "+ subject + "\n" + message
print(smtp_object.sendmail(from_address,to_address,msg))
print(smtp_object.quit())