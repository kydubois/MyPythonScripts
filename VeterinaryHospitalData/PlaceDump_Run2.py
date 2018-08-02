import sqlite3
import json
import csv
import pprint as pp

# We connect to our new database
db = sqlite3.connect('HospitalData.sqlite')  # Make sure to update to new SQL database that was created in PlaceSearch_Run1.py
cur = db.cursor()

# Selecting all columns from Locations table
cur.execute('SELECT * FROM hospital;')

# Openning a new CSV file so we can write in it
fhand = open('HospitalData.csv', 'w', newline='') # Make sure to update CSV file name
csvfhand = csv.writer(fhand)
# We create headers for our new CSV file
csvfhand.writerow(['Place_id','Hospital','Address'])  # Make sure to update headers if more needed
count = 0

for col in cur:
    #  We decode the Geodata column in our Locations table from bytestring to a string
    data = str(col[1].decode())
    try:
        # We load the decoded JSON string into a Python dictionary
        js = json.loads(str(data))
    except:
        continue

    if not('status' in js and js['status'] == 'OK'):
        continue

    # pp.pprint(js["results"][0])

    for info in js["results"]:
        address = info["formatted_address"]
        place_id = info["place_id"]
        name = info["name"]
        print(name)
        print(address)
        print(place_id)
        print('')
        count +=1
        try:
            csvfhand.writerow([place_id,name,address])
        except:
            pass


cur.close()
fhand.close()
print(count, "records written to CSV file.  Run PlacesDetailsLoad.py to read the CSV data to obtain the Place Details and write that into a database.")
