import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your@email.com"
SMTP_PASSWORD = "yourpassword"
FROM_EMAIL = "no-reply@cinema.com"

def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)

def send_confirmation_email(to_email: str, token: str):
    link = f"http://yourdomain.com/confirm-email?token={token}"
    subject = "Confirm your registration"
    body = f"Please click the link to confirm your registration: {link}"
    send_email(to_email, subject, body)

def send_password_reset_email(to_email: str, token: str):
    link = f"http://yourdomain.com/password-reset?token={token}"
    subject = "Password Reset Request"
    body = f"Click the link to reset your password: {link}"
    send_email(to_email, subject, body)