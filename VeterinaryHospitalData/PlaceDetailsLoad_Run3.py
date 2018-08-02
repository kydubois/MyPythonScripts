import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
import pprint as pp

api_key = # add you Google Places API key here

serviceurl = "https://maps.googleapis.com/maps/api/place/details/json?"

conn = sqlite3.connect('HospitalDetails.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS hospital_dets (
    hospital TEXT,
    place_id TEXT,
    data TEXT
);
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
tots = 0
with open('HospitalData.csv') as fh:
    next(fh)
    for col in fh:
        ls = col.split(',')
        # print(ls)
        hospital = ls[1]
        hospital = hospital.strip()
        place_id = ls[0]
        place_id = place_id.strip()
        # print(hospital)
        # print(place_id)

        if count == 200:
            print('Retrieved', count, 'locations, restart the script to retrieve more')
            break

        cur.execute("SELECT data FROM hospital_dets WHERE place_id= ?;",
            (memoryview(place_id.encode()), ))

        try:
            data = cur.fetchone()[0]
            print("Found in database ",place_id)
            tots += 1
            continue
        except:
            pass

        parms = dict()
        parms["placeid"] = place_id
        parms["key"] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)

        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters', data[:30].replace('\n', ' '))
        count += 1
        tots += 1

        try:
            js = json.loads(data)
        except:
            print(data)
            continue

        if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
            print('==== Failure To Retrieve ====')
            print(data)
            break

        # pp.pprint(js)
        # print('')

        cur.execute('''INSERT INTO hospital_dets (hospital, place_id, data)
                VALUES ( ?, ?, ? );''', (memoryview(hospital.encode()), memoryview(place_id.encode()), memoryview(data.encode()) ) )
        conn.commit()

        if count % 10 == 0:
            print('')
            print('Compiling Data...')
            time.sleep(5)

print('There are a total of', tots, "Place Details in the database.  Run PlaceDetailsDump_Run4.py to write data from database into CSV file.")
cur.close()
