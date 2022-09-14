from email.message import EmailMessage
import ssl ,smtplib
from pandas import *
df = pandas.read_csv("mail.csv")
f=df["Name"].tolist()
receiver=df["Mail"].tolist()
for f in receiver:
    sender = 'arjasandhya@gmail.com'
    paswd = 'zwlcybviklzsvrac'
    subject = 'Going To Ice Cream'
    body = 'Guys when we are going to have Fun'
    mail= EmailMessage()        #it is an object to EmailMessage CLASS
    mail['From'] = sender
    mail['To'] = f
    mail['Subject'] = subject
    mail.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465,context= context) as mi:
        mi.login(sender,paswd)
        mi.sendmail(sender,f,mail.as_string())
        print(f'mail sent successfully to {f} please check your email inbox')



