import email, smtplib, ssl, csv

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "arjasandhya@gmail.com"


with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    with open("mail.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for Mail in reader:

                # Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = from_address
                message["To"] = "arjanirmala777@gmail.com"
                message["Subject"] = "sending"
                filename = str(reader)

                # Add body to email
                message.attach(MIMEText(body, "plain"))

                with open(filename, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(part)

                    # Add header as key/value pair to attachment part
                    part.add_header(
                    "Content-Disposition",f"attachment; filename= {filename}",)

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

                # Use server to send email
                server.sendmail(from_address, Mail, text)