import sqlite3
import json
import csv

# We connect to our new database
db = sqlite3.connect('LIGEOCODE.sqlite')  # Make sure to update to new SQL database that you used in geoLIloader.py
cur = db.cursor()

# Selecting all columns from Locations table
cur.execute('SELECT * FROM Locations')

# Openning a new CSV file so we can write in it
fhand = open('LIGEOCODE.csv', 'w', newline='') # Make sure to update CSV file name
csvfhand = csv.writer(fhand)
# We create headers for our new CSV file
csvfhand.writerow(['Address','Latitude','Longitude'])  # Make sure to update headers if more needed
count = 0

for col in cur:
    #  We decode the Geodata column in our Locations table from bytestring to a string
    data = str(col[1].decode())
    try:
        # We deserialize the decoded string to a Python string object
        js = json.loads(str(data))
    except:
        continue

    if not('status' in js and js['status'] == 'OK'):
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]  # Pull out Latitude data from JSON string
    lng = js["results"][0]["geometry"]["location"]["lng"]  # Pull out Longitude data from JSON string
    if lat == 0 or lng == 0:
        continue  # Skiping Lat and Long data if blank
    address = js["results"][0]["formatted_address"]  # Pull out complete address from JSON string
    address = address.replace("'", "")
    # city = js["results"][0]["address_components"][1]["long_name"]
    # zipcode = js["results"][0]["address_components"][0]["long_name"]
    try:
        print(address, lat, lng)
        count = count + 1
        if count > 1:
            csvfhand.writerow([address,lat,lng])  # Make sure to update if needed
    except:
        continue

cur.close()
fhand.close()
print(count - 1, "records written to CSV file")
