
from PIL import Image
import os

#set the source and destination folders, as well as the attributes we want for the file conversoin

img_src = os.path.abspath(".\\supplier-data\\images")
img_dest = ".\\supplier-data\\images"
dest_size = 600,400
dest_format = "jpeg"


for image in os.listdir(img_src):
    img_path = os.path.join(img_src, image)
  
    with open(img_path, "rb") as file:
        print(file)
        
        im = Image.open(file)
        im.convert("RGB")
        im.resize((dest_size)).save(dest + image, format=dest_format)