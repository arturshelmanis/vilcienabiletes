import imaplib
import email
import os

imap_url = 'mail.inbox.lv'
my_mail = imaplib.IMAP4_SSL(imap_url)
from user_login import *
my_mail.login(my_email, password_key)

my_mail.select("INBOX")

key = "FROM"
value = "info@mobilly.lv"
key1 = "SINCE"
value1 = ""
aaa, data = my_mail.search(None, key, value, '(SINCE "01-Sep-2023")')

list = data[0].split()

folder_name = "Mail_Attachments"
if not os.path.exists(folder_name):
    os.makedirs(folder_name, mode=0o777)

folder_path = os.path.abspath(folder_name)

count = 1
for i in list:
    typ, data = my_mail.fetch(i, '(RFC822)')
    mail=data[0][1]
    msg = email.message_from_string(mail.decode('utf-8'))
    # print('Subject:', msg['subject'])
    # print('From:', msg['from'])
    # print('Data:', msg['Date'])
    
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
                continue
        if part.get('Content-Disposition') is None:
                continue

        filename = "Bilete_" + str(count)
        if filename:
            filepath = os.path.join(folder_path,filename)
            with open(f"{filepath}.pdf", 'wb') as f:
                f.write(part.get_payload(decode=True))
        count += 1

my_mail.logout()