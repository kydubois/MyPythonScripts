import json
import urllib.request, urllib.parse, urllib.error
import requests
import ssl
import sqlite3
import time
import sys
import codecs
import csv
import pprint as pp
import re

tagname = input('input tag name: ')

insightlyurl = 'https://api.insight.ly/v2.2/Organisations/Search?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

db = sqlite3.connect(tagname + '_Orgs.sqlite')  # Make sure to update to new SQL database
cur = db.cursor()

# Create a new database table
cur.execute('''
CREATE TABLE IF NOT EXISTS Orgs (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    hospital TEXT,
    hospital_ID TEXT,
    data TEXT
);
''')

count = 0
while True:


    parms = dict()
    parms['tag'] = tagname
    parms['skip'] = count
    parms['top'] = 500
    parms['count_total'] = 'true'

    url = insightlyurl + urllib.parse.urlencode(parms)

    print(url)
    
    un = # put your username here
    pw = # put ypur password here

    uh = requests.get(url, auth = (un,pw))

    try:
        status = uh.status_code
        print("Status Code:", status)
        if status != 200:
            print("==== Successful Response Failed ====")
            break
    except:
        print("==== Failure to Retrieve Status ====")
        continue

    dumps = uh.headers
    dumps_total = int(dumps["X-Total-Count"])

    # js = json.loads(uh.text)
    # print(js)

    data = uh.json()  # this is a list
    # print(type(data))

cur.close()
fhand.close()
