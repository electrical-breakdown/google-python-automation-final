import os
import requests
import json

file_src = os.path.abspath(".\\supplier-data\\descriptions")
img_src = os.path.abspath(".\\supplier-data\\images")

upload_url = "http://[linux-instance-external-IP]/fruits"

#file_list = os.listdir("C:\\Users\\Mike\\Documents\\Python\\reviews")
item_description = {"name": "", "weight": 0, "description": "", "image_name": ""}


for desc in os.listdir(file_src):

    desc_path = os.path.join(file_src, desc)
    desc_base_name = desc.split(".")[0]  
    
    with open(desc_path, "r") as file:

        reader = file.readlines()
        converted_weight = int(reader[1].strip("lbs")[0])
        description_text = ""

        # for line in reader[2:]:
        #     clean_line = line.strip()
        #     description_text += clean_line

        processed_dict = item_description.copy()
        processed_dict.update(name= reader[0].strip(), weight=converted_weight, description=reader[2].strip(), 
        image_name=desc_base_name + ".JPEG")

       # request = requests.post(upload_url, json=processed_dict)
        
        print(processed_dict)
        
      