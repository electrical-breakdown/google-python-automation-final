import reports
import os
import datetime
import emails

#define report parameters

json_path = os.path.abspath(".\\supplier-data\\descriptions.json")
pdf_save_location = "C:\\Users\\Mike\\Desktop\\processed.pdf"
date = datetime.datetime.now()
month = date.strftime("%B")
title = f"Processed Update on {month} {str(date.day)}, {str(date.year)}"


#define email parameters

sender = "example@example.com"
recipient = "example@example.com"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."


# call the functions needed to create the report and then prepare and send the email
if __name__ == "__main__":

    reports.generate_report(pdf_save_location, title, json_path)
    prepared_email = emails.generate_email(sender, recipient, subject, body, pdf_save_location)
    emails.send_email(prepared_email)