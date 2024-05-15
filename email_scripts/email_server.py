import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

def send_email(subject, message, to_email):
    # Get email credentials from environment variables
    from_email = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message content
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# Email parameters
subject = "Hello World"
message = "This is a test email. Hello, World!"
to_email = "lloyduogbonna@gmail.com"

# Send email
send_email(subject, message, to_email)