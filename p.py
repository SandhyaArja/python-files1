from email.message import EmailMessage #The email package is an email message management library
#From email module we are importing the email for It is the base class for the email object model.
#EmailMessage provides the core functionality for setting and querying header fields
from email.mime.text import MIMEText
import schedule

import ssl,smtplib,time
#SMTP client session object that can be used to send mail to any Internet machine with an SMTP
from pandas import *
#from the above line we are importing pandas module and  imports all objects from the pandas module

df = pandas.read_csv("mail.csv")
f=df["Name"].tolist()
g=df["Pdf"].tolist()
print(g)
receiver=df["Mail"].tolist()
file1=open("mail.html")
html_file=file1.read()
count=0
# count variable is for counting the given next name suppose we are having 3 names if we complete sending mail
# for 1name later we are count that we are having another name
for f in receiver:
    sender = 'arjasandhya@gmail.com'
    paswd = 'zwlcybviklzsvrac'
    subject = 'Insurance Mail'
    body =MIMEText(html_file, 'html')
    mail= EmailMessage()
    mail['From'] = sender
    mail['To'] = f
    mail['Subject'] = subject
    mail["Cc"]=f
    mail.set_content(body)
    file=g[count]
    with open(file, 'rb') as attachfile:
        file_data = attachfile.read()
        file_name = attachfile.name
        mail.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465,context= context) as mi:

        mi.login(sender,paswd)
        mi.sendmail(sender,f,mail.as_string())
        count+=1
    schedule.every().minutes.do(sendmail)
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)
        print(f'mail sent successfully to {f} please check your email inbox')