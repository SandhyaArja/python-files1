from email.message import EmailMessage

import ssl ,smtplib,time

sender = 'arjasandhya@gmail.com'
paswd = 'nwufcqzazgufyxcx'
receiver =["Chinnarididla4555@gmail.com","raghusankarreddys08@gmail.com"]
#vijay995577@gmail.com","arjasandhya@gmail.com","athukuri@gmail.com","raghusankarreddys08@gmail.com","psailaja0101@gmail.com



subject = 'Going To Ice Cream'
body = 'Guys when we are going to have Fun'
mail= EmailMessage()        #it is an object to EmailMessage CLASS
mail['From'] = sender
mail['To'] = receiver
mail['Subject'] = subject
mail.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com' , 465,context= context) as mi:
    mi.login(sender,paswd)
    mi.sendmail(sender,receiver,mail.as_string())
    time.sleep(3)
    print(f'mail sent successfully to {receiver} please check your email inbox')
