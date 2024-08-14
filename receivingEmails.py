import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
#grab password and email 
import getpass
email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')
print(M.login(email,password))
print(M.list())

M.select('inbox')

#now search the inbox 
typ, data = M.search(None,'SUBJECT "NEW TEST PYTHON"')
print(typ)
email_id = data[0]
#we are now fetching the email id
result,email_data = M.fetch(email_id,'(RFC822)')
#print(email_data)
#this is the raw email itself
raw_email = email_data[0][1]
#we are going to need to decode it with utf-8
raw_email_string = raw_email.decode('utf-8')
import email 
#now we can use the email library to parse the string and can grab the actual message 
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk(): 
    if part.get_content_type() =='text/plain': 
        #or can look for text/html and is usally for a link
        body = part.get_payload(decode = True)
        print(body)

