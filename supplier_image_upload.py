import requests
import os

upload_url = "http://localhost/upload"
img_src = os.path.abspath(".\\supplier-data\\images")


def upload_product_images():

    """Uploads images in the specified directory to the web server"""

    for img in os.listdir(img_src):

        img_ext = img.split(".")[1]
        img_path = os.path.join(img_src, img)

        #open and upload jpegs only
        if img_ext in ("JPEG", "jpeg", "jpg"):


            with open(img_path, "rb") as file:
                r = requests.post(upload_url, files={"file": file})


upload_product_images()