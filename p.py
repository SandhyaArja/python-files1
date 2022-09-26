from email.message import EmailMessage
from email.mime.text import MIMEText
import ssl,smtplib,time
from pandas import *
df = pandas.read_csv("mail.csv")
person=df["Name"].tolist()
g=df["Pdf"].tolist()
receiver=df["Mail"].tolist()
file1=open("mail.html")
html_file=file1.read()
count=0
for person in receiver:
    sender = 'XXXXXXXX'
    paswd = 'XXXXXXXXX'
    subject = 'Insurance Mail'
    body =MIMEText(html_file, 'html')
    mail= EmailMessage()
    mail['From'] = sender
    mail['To'] = person
    mail['Subject'] = subject
    mail["Cc"]=person
    mail.set_content(body)
    file=g[count]
    with open(file, 'rb') as attachfile:
        file_data = attachfile.read()
        file_name = attachfile.name
        mail.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465,context= context) as mi:
        mi.login(sender,paswd)
        mi.sendmail(sender,person,mail.as_string())
        count+=1
        time.sleep(10)
        print(f'mail sent successfully to {person} please check your email inbox')