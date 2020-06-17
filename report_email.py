import reports
import os
import datetime
import emails

file_src = os.path.abspath(".\\supplier-data\\descriptions")
report_contents = {"name": "", "weight": 0, "description": ""}
#attachment = "C:\\Users\\Mike\\Desktop\\processed.pdf"
date = datetime.datetime.now()
month = date.strftime("%B")
title = "Processed Update on {} {}, {}".format(month, str(date.day), str(date.year))
all_reports = []


for desc in os.listdir(file_src):

    desc_path = os.path.join(file_src, desc)
    desc_base_name = desc.split(".")[0]  
    
    with open(desc_path, "r") as file:

        reader = file.readlines()
        converted_weight = reader[1].strip()

        processed_report = report_contents.copy()
        processed_report.update(name= reader[0].strip(), weight=converted_weight, description=reader[2].strip())

        all_reports.append(processed_report)



#define email parameters

sender = "mmcgovern5@gmail.com"
recipient = "mmcgovern5@gmail.com"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachment = "C:\\Users\\Mike\\Desktop\\processed.pdf"

if __name__ == "__main__":
    reports.generate_report(attachment, title, all_reports)
    prepared_email = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(prepared_email)