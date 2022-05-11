# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:10:13 2021

@author: Jayesh Jethy
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


myfile = open("info.txt",'r')
username = myfile.readline()
password = myfile.readline()
senderadd = myfile.readline()

body = 'Time Table is attached below'
msg = MIMEMultipart()
msg['Subject'] = 'Python Project'
msg['From'] = username
msg['To'] = senderadd
msg.attach(MIMEText(body, 'plain'))

pdfb = open('Time Table.pdf','rb')
payload = MIMEBase('application', 'octate-stream', Name='Time Table.pdf')
payload.set_payload((pdfb).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition', 'attachment', filename='Time Table.pdf')
msg.attach(payload)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username,password)
server.sendmail(username, senderadd, msg.as_string())
print('Mail sent')
