import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from typing import List, Optional

class MailManager:
    """Manages email actions, specifically sending attachments via Gmail."""

    def __init__(self, sender_email: str, app_password: str) -> None:
        """
        Initializes the MailManager with Gmail credentials.
        
        Args:
            sender_email: Your Gmail address.
            app_password: Your Gmail App Password (not your regular password).
        """
        self.sender_email = sender_email
        self.app_password = app_password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email_with_zip(
        self, 
        receiver_email: str, 
        subject: str, 
        body: str, 
        zip_file_path: str
    ) -> bool:
        """
        Sends an email with a zip file attachment.
        
        Example:
            mailer.send_email_with_zip(
                "target@gmail.com", 
                "Project Data", 
                "Please find the zipped data attached.", 
                "downloaded_files/data.zip"
            )
        """
        if not os.path.exists(zip_file_path):
            print(f"Error: Zip file not found at {zip_file_path}")
            return False

        # Create the message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            # Open the zip file in binary mode
            with open(zip_file_path, "rb") as attachment:
                part = MIMEBase("application", "zip")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            filename = os.path.basename(zip_file_path)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            print(f"Connecting to Gmail SMTP to send {filename}...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.app_password)
                server.sendmail(self.sender_email, receiver_email, text)
            
            print(f"Email sent successfully to {receiver_email}!")
            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
