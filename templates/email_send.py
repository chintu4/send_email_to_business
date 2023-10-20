import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, subject, message):
    # Set up the SMTP server
    smtp_server = "your-smtp-server.com"
    port = 587  # Replace with the appropriate port
    username = "your-email@example.com"
    password = "your-password"

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# Usage
email = "recipient@example.com"
subject = "Your Subject"
message = "Your email content here"
send_email(email, subject, message)
