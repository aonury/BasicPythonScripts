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
    existing_path = ttc_path_document
elif (os.path.exists(ttc_path_onedrive)):
    print("Seems like you don't have AddOns folder in your Documents Folder. Let's try OneDrive.")
    existing_path = ttc_path_onedrive
else:
    print("Are you sure you have AddOns folder for Elder Scrolls Online?")
    time.sleep(3)
    
# Let's check if we can download and unzip file from url or not:
if (existing_path != ""):
    http_response = urlopen(zip_url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=existing_path)

else:
    print("You need to check the problems before running again.")
    time.sleep(3)
