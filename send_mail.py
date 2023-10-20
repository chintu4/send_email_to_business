import os
import smtplib
import ssl
from email.message import EmailMessage
import config




def sendMail(email_receiver,subject,body):
   #load from config file
    email_sender=config.details['emailSender']
    
   #load from config file
    email_password =config.details['emailPassword']

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
   