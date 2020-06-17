
from PIL import Image
import os

#set the source and destination folders, as well as the attributes we want for the file conversoin

img_src = os.path.abspath(".\\supplier-data\\images")
img_dest = os.path.abspath(".\\supplier-data\\images")
dest_size = 600,400
dest_format = "jpeg"


for img in os.listdir(img_src):
    
    img_path = os.path.join(img_src, img)
    img_base_name = img.split(".")[0]  
    
    with open(img_path, "rb") as file:
        
        im = Image.open(file)
        im.convert("RGB")
        im.resize((dest_size)).im.save(os.path.join(img_dest, img_base_name) + ".JPEG", format=dest_format)