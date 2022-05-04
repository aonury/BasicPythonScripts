import os
import os.path
import time
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

# TTC path where all price tables are in now. 
ttc_path_onedrive = os.path.join(os.path.expanduser("~"),"OneDrive","Documents","Elder Scrolls Online","live","AddOns","TamrielTradeCentre")
ttc_path_document = os.path.join(os.path.expanduser("~"),"Documents","Elder Scrolls Online","live","AddOns","TamrielTradeCentre")

# This path will be used for TTC path depend on which exists
existing_path = ""

# Defining URL which we will download zip file:
zip_url = "https://eu.tamrieltradecentre.com/download/PriceTable"

if (os.path.exists(ttc_path_document)):
    print("Your AddOns folder is in your Documents folder! Setting path to: ", ttc_path_document)
    existing_path = ttc_path_document

elif (os.path.exists(ttc_path_onedrive)):
    print("Your AddOns folder is in your Onedrive folder! Setting path to:", ttc_path_onedrive)
    existing_path = ttc_path_onedrive
else:
    print("Are you sure you have AddOns folder for Elder Scrolls Online?")
    time.sleep(3)
    
# Let's check if we can download and unzip file from url or not:
if (existing_path != ""):
    http_response = urlopen(zip_url)
    print("Files are downloaded. Let's extract them")
    time.sleep(3)

    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=existing_path)
    print("Your files are extracted to TTC folder. You can check 'Date Modified' to ensure")
    time.sleep(3)

else:
    print("You need to solve the problems before running again.")
    time.sleep(3)
