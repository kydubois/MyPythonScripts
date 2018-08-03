import urllib.request, urllib.parse, urllib.error
import requests
import sqlite3
import json
import time
import ssl
import sys
import pprint as pp
import csv
import re

tagname = input('input tage name: ' )

insightlyurl = 'https://api.insight.ly/v2.2/Contacts/Search?'

un = # put username here
pw = # put password here

conn = sqlite3.connect(tagname + '_EmailList.sqlite')
cur = conn.cursor()

# cur.execute('''
# DROP TABLE IF EXISTS Contacts;
# ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Contacts (
    hospital TEXT,
    hospital_ID TEXT,
    first TEXT,
    last TEXT,
    role TEXT,
    email TEXT,
    data TEXT
);
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Openning a new CSV file so we can write in it
fhand = open(tagname + '_EmailList.csv', 'w', newline='')
csvfhand = csv.writer(fhand)
# We create headers for our new CSV file
csvfhand.writerow(['Hospital','Hospital ID','Contact First Name','Contact Last Name','Contact Role','Contact Email'])

count = 0
with open(tagname + "_OrgsList.csv") as fh:
    next(fh)
    for line in fh:
        hosp = line.strip()
        print(hosp)
        # ls = line.split(',')
        # hosp_email = ls[1]
        # hosp_email2 = ls[2]
        # hospid = ls[2]
        # hospname = ls[3]

        # hosp = hospital.strip()

        cur.execute("SELECT * FROM Contacts WHERE hospital= ?",
            (hosp, ))

        try:
            data = cur.fetchone()[0]
            if data is not None:
                print("Found in database ",hosp)
                continue
        except:
            pass

        parms = dict()
        parms['organisation'] = hosp
        parms['brief'] = 'false'
        # parms['skip'] = count
        parms['top'] = 500
        parms['count_total'] = 'true'

        url = insightlyurl + urllib.parse.urlencode(parms, safe='()', quote_via=urllib.parse.quote)
        uh = requests.get(url, auth = (un,pw))
        print('Retrieving', url)

        try:
            status = uh.status_code
            # print("Status Code:", status)
            if status != 200:
                print("==== Successful Response Failed ====")
                print('')
                break
        except:
            print("==== Failure to Retrieve Status ====")
            print('')
            continue

        dumps = uh.headers
        dumps_total = int(dumps["X-Total-Count"])

        js = uh.json()

        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

        for r in js:
            # pp.pprint(r)
            # print('')
            first = r["FIRST_NAME"]
            last = r["LAST_NAME"]
            hospID = r["DEFAULT_LINKED_ORGANISATION"]
            try:
                emaillist = list()
                for ro in r["CONTACTINFOS"]:
                    if EMAIL_REGEX.match(ro["DETAIL"]):  # search for email, skip phone numbers
                        email = ro["DETAIL"]
                        emaillist.append(email)
                        # print(email)
                for rl in r["LINKS"]:
                    role = rl["ROLE"]
                pass
            except:
                continue

            print(hosp)
            print(hospID)
            print(first)
            print(last)
            print(role)
            print(emaillist)
            print('')
            count = count + 1

            cur.execute('''INSERT INTO Contacts (hospital, hospital_ID, first, last, role, email, data)
                    VALUES ( ?, ?, ?, ?, ?, ?, ? )''', (str(hosp), str(hospID), str(first), str(last), str(role), str(email), str(r)) )
            conn.commit()

            csvfhand.writerow([hosp,hospID,first,last,role,emaillist])

        if count % 10 == 0 :
            print('Pausing for a bit...')
            time.sleep(5)

        print('')
        print(count, "Records written to database.")
        print(dumps_total, 'total Records available.')
        print('')

cur.close()
# fhand.close()
