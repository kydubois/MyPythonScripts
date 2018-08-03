import json
import urllib.request, urllib.parse, urllib.error
import requests
import ssl
import sqlite3
import csv

insightlyurl = 'https://api.insight.ly/v2.2/Tags?'

un = # add username here
pw = # add password here

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

db = sqlite3.connect('insightlyTAGS.sqlite')  # Make sure to update to new SQL database
cur = db.cursor()

# Create a new database called Tags with two columns, Id and Info
cur.execute('''
CREATE TABLE IF NOT EXISTS Tags (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    info TEXT
);
''')

count = 0
while True:
    skip = input('This script returns a maximum of 500 records at a time. What record would you like to start at? ')
    if len(skip) == '':
        break

    try:
        data = cur.fetchone()[0]
        continue
    except:
        pass

    parms = dict()
    parms['record_type'] = 'organisations'
    parms['skip'] = skip
    parms['top'] = 500
    parms['count_total'] = 'True'

    url = insightlyurl + urllib.parse.urlencode(parms)

    print(url)

    uh = requests.get(url, auth = (un,pw))

    dumps = uh.headers
    print(dumps)
    print('')


    data = uh.json()
    # print(data)
    # print('')

    for item in data:
        print(item)
        print('')
        # Insert json data into 'info' in Tags table
        cur.execute('''INSERT INTO Tags (info)
                VALUES ( ? );''', (str(item), ) )
        count += 1

    db.commit()
    print(count, "Records written to database.  Run again and indicate the next start point.")
