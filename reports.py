from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime


def generate_report(filename, title, reports):

    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    #empty_line = Spacer(1, 20)
    
    report_body = []

    for item in reports:
        item_name = item["name"]
        item_weight = item["weight"]
        report_body.append(["name: {} \nweight: {}".format(item_name, item_weight)])
        report_body.append("\n")

   
    report_table = Table(data=report_body, hAlign="LEFT")
    report.build([report_title, report_table])

    print(report_table)

#generate_report("C:\\Users\\Mike\\Desktop\\processed.pdf", "title", all_reports)





