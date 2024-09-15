import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD

def send_email_notification(email, location, alert_type):
    try:
        subject = f"Weather Alert: {alert_type.capitalize()} in {location}"
        body = f"There is a {alert_type} alert in {location}. Stay safe!"
        
        # Email message setup
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USERNAME
        msg['To'] = email

        # Connect to the SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, email, msg.as_string())
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False