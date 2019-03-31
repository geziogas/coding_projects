import json
import requests
import re
from time import sleep
from datetime import datetime
import os

# Best library for parsing websites
from bs4 import BeautifulSoup


url = "https://rowermevo.pl/locations.js"

def getUrlData(url):
    r = requests.get(url)
    source = r.text
    # Returnes a list of all json found
    obj = re.findall(r"var NEXTBIKE_PLACES_DB = '(.*?)'", source)
    return obj

len(obj)

# You can try to save it on a file by iterating the list with the returned JSON strings

# Checks if the output folder exists. If not, it creates it
if not os.path.exists("extracted"):
    os.makedirs("extracted")
    
# Running forever and stores the json in a new file every 5 secods
count = 0
while count < 20:
    obj = getUrlData(url)
    datastore = json.loads(obj[0])
    f_time = int(time.time())
    f= open("extracted/extr.{}.json".format(f_time),"w")
    #print(f_time)
    f.write(json.dumps(datastore, sort_keys = True, indent=4))
    f.close()
    #print(json.dumps(datastore, sort_keys = True, indent=4))
    time.sleep(5) #repeat every 5 seconds
    count+=1