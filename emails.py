from email.message import EmailMessage
import mimetypes
import os
import smtplib
import getpass



def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Creates an email with an attachment"""

    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"]= subject
    message.set_content(body)

    if attachment_path != None:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        
        with open(attachment_path, "rb") as attachment:
            message.add_attachment(attachment.read(), 
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=attachment_filename
            )

    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP("localhost")
    #mail_server = smtplib.SMTP_SSL("64.233.184.108")
    #mail_pass = getpass.getpass("Password? ")
    #mail_server.login("mmcgovern5@gmail.com", mail_pass)
    mail_server.send_message(message)
    mail_server.quit()



