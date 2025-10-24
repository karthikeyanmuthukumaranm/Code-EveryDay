import smtplib
from email.mime.text import MIMEText

def send_email_notification(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "karthideva093@gmail.com" 
    sender_password = "wlsr fvzz beoc rxwm"


    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    send_email_notification(
        subject="Test Alert Notification",
        body="This is a test email notification sent via SMTP.",
        to_email="mkarthikn25@gmail.com"  
    )