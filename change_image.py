
from PIL import Image
import os


def process_images():

    """Converts a set of images according to the given parameters and saves them in the same folder as new files"""

    #set the source and destination folders, as well as the attributes we want for the file conversoin

    img_src = os.path.abspath(".\\supplier-data\\images")
    img_dest = os.path.abspath(".\\supplier-data\\images")
    dest_size = 600,400
    dest_format = "jpeg"


    for img in os.listdir(img_src):

        img_path = os.path.join(img_src, img)
        img_base_name = img.split(".")[0]  
        
        #open each image in the source directory
        with open(img_path, "rb") as file:
            
            #create the image object and apply the specfied conversions
            im = Image.open(file)
            im.convert("RGB")
            im.resize((dest_size)).im.save(os.path.join(img_dest, img_base_name) + ".jpeg", format=dest_format)


process_images()