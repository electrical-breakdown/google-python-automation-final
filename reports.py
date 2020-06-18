from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import json



def generate_report(filename, title, reports):
    """Generates a pdf report containing a summary of data from a product descriptions file"""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    
    #create empty list to hold table data for the pdf
    report_body = []
    

    #open the json file containing product data

    with open(reports, "r") as json_file:

        #load data from json
        json_dict = json.load(json_file)

        #iterate through the prodcut descriptoins in the json data and extract just the values for name and weight 
        for item in json_dict:
            item_name = item["name"]
            item_weight = item["weight"]

            #append a list conating the name and weight to create a two dimensional array that can be converted to a table
            report_body.append([f"name: {item_name} \nweight: {item_weight}"])
            report_body.append("\n")

    #convert report_body to a table
    report_table = Table(data=report_body, hAlign="LEFT")

    # build the pdf
    report.build([report_title, report_table])

   





