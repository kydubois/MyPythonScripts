import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = # Insert you googple API key here

serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

db = sqlite3.connect('HospitalData.sqlite')  # Make sure to update to new SQL database
cur = db.cursor()

# Create a new database called Table with two columns, Address and Geodata
cur.execute('''
CREATE TABLE IF NOT EXISTS hospital (zip_code TEXT, data TEXT);''')
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT);''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("zips.csv")  # Make sure to update to new CSV or TXT file
count = 0
for line in fh:
    if count == 200 :  # Retrieves 50 items at a time
        print('Retrieved', count, 'locations, restart to retrieve more')
        break

    zip_code = line.strip()
    print('')
    cur.execute("SELECT data FROM hospital WHERE zip_code= ?;",
        (memoryview(zip_code.encode()), ))

    # Check to see if address is already in Datebase and skip if it is present
    try:
        data = cur.fetchone()[0]
        print("Found in database ",zip_code)
        continue
    except:
        pass

    # Create URL address using a dictionary that contains serviceurl, address, and api_key
    parms = dict()
    parms['query'] = zip_code
    parms['type'] = 'veterinary_care'
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    # Connect to our created URL
    print('Retrieving', url)
    #  We open the URL, which can either be a string or a Request object
    uh = urllib.request.urlopen(url, context=ctx)
    # We decode the returned bytestring
    data = uh.read().decode()
    # We print out first 30 characters of retrieved data
    print('Retrieved', len(data), 'characters', data[:30].replace('\n', ' '))
    count = count + 1

    try:
        # We deserialize the decoded URL to a Python object
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

        # We check status to see if we retrieved any data and break conection if failed
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    # Insert retrieved data into our Location database; Address is our input data, and Geodata is the geocoding data we retrieved
    cur.execute('''INSERT INTO hospital (zip_code, data)
            VALUES ( ?, ? );''', (memoryview(zip_code.encode()), memoryview(data.encode()) ) )
    db.commit()

    # if Count modulus equals 0 we suspend execution for 5 seconds
    if count % 10 == 0 :
        print('')
        print('Compiling Data...')
        time.sleep(5)


cur.close()
print("Run PlacesDump.py to read the data from the database and write it into a CSV file.")
