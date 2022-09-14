import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
send="arjasandhya@gmail.com"
passd="zwlcybviklzsvrac"
sub="sending"
with open ("mail.csv",'r') as csvfile:
    reader=csv.reader(csvfile)

    for val in reader:
        text="hello"+val[0]+"send"
        print(text)
        email_send=val[1]
        #print(email_send)
        msg=MIMEMultipart()
        msg["From"]=send
        msg["To"]=email_send
        msg["Subject"]="sub"
        msg.attach(MIMEText(text,"plain"))
        smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login(send,passd)
        smtp.sendmail(send,email_send,text)
        smtp.quit()
#contacts = ['arjasandhya@gmail.com']

#msg = EmailMessage()
#msg['Subject'] = 'Check out Bronx as a puppy!'
#msg['From'] = EMAIL_ADDRESS
#msg['To'] = 'arjasandhya@gmail.com'

#msg.set_content('This is a plain text email')

#msg.add_alternative("""\
#<!DOCTYPE html>
#<html>
   # <body>
       # <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    #</body>
#</html>
#""", subtype='html')


#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #smtp.login(send,passd)
   # smtp.send_message(msg)
#Footer
