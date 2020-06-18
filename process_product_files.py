import os
import requests
import json


def process_product_files():
    """Parses text files containing product descriptions and saves the data to a json"""

    #source directory for the description files
    file_src = os.path.abspath(".\\supplier-data\\descriptions")

    #source directory for the corresponding product images
    img_src = os.path.abspath(".\\supplier-data\\images")

    #address to upload the product data
    upload_url = "<web_server_address>"

    #create an empty dictionary to use as a template for the item descriptions
    item_description = {"name": "", "weight": 0, "description": "", "image_name": ""}

    #create an empty list to hold all of the item description dictionaries
    all_descriptions = []


    for description in os.listdir(file_src):
        
        description_path = os.path.join(file_src, description)

        #split the file path up into the base file name and the extension
        description_base_name = description.split(".")[0]  
        
        with open(description_path, "r") as file:

            reader = file.readlines()
            converted_weight = int(reader[1].split()[0]) #split the weight filed on the space and convert to int

            #generate a new dictionary to hold the product data for each item in the source directory
            processed_dict = item_description.copy()

            #populate the new dictionary with the relevant info for each product. Each item has a corresponding image with the same file name, so set the image_name value to the basename of the file, plus the jpeg extension
            processed_dict.update(name= reader[0].strip(), weight=converted_weight, description=reader[2].strip(), 
            image_name=description_base_name + ".jpeg")

            #add the new dictionary to the list that holds all of the product descriptions
            all_descriptions.append(processed_dict)

            # upload each processed descriptoin to web server
            request = requests.post(upload_url, json=processed_dict)

    #create a new json file to hold the product data for future use
    with open(".\\supplier-data\\descriptions.json", "w") as json_file:

        #write all of the product data to json. indent=2 formats for better readability 
        json.dump(all_descriptions, json_file, indent=2)
            


process_product_files() 