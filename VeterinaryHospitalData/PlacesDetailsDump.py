import sqlite3
import json
import csv
import pprint as pp

# We connect to our new database
db = sqlite3.connect('HospitalDetails.sqlite')  # Make sure to update to new SQL database
cur = db.cursor()

# Selecting all columns from Locations table
cur.execute('SELECT * FROM hospital_dets;')

# Openning a new CSV file so we can write in it
fhand = open('HospitalDetails.csv', 'w', newline='') # Make sure to update CSV file name
csvfhand = csv.writer(fhand)
# We create headers for our new CSV file
csvfhand.writerow(['Hospital','Address','Country','Phone','Website','Google Maps Site','Avg. Google Rating','Hours of Operation'])  # Make sure to update headers if more needed
count = 0

for col in cur:

    #  We decode the Geodata column in our Locations table from bytestring to a string
    data = str(col[2].decode())
    try:
        # We load the decoded JSON string into a Python dictionary
        js = json.loads(str(data))
    except:
        continue

    if not('status' in js and js['status'] == 'OK'):
        continue

    # print(type(js))
    # keys = list(js.keys())
    # for key in keys:
    #     print(key)
    # pp.pprint(js["result"])

    address = js["result"]["formatted_address"]  # Pull out complete address from JSON string
    # address = address.replace(",", "")
    place_id = js["result"]["place_id"]
    name = js["result"]["name"]
    phonelist = []
    websitelist = []
    hoursofoper = []
    try:
        phone = js["result"]["formatted_phone_number"]
        phonelist.append(phone)
        website = js["result"]["website"]
        websitelist.append(website)
        googlemaps = js["result"]["url"]
        avgrate = js["result"]["rating"]
        # hoursop = js["result"]["opening_hours"]["weekday_text"]
        for hour in js["result"]["opening_hours"]["weekday_text"]:
            hoursofoper.append(hour)
        # addresscomps = js["result"]["address_components"]
        for comp in js["result"]["address_components"]:
            if comp["types"][0] == "country":
                country = comp["short_name"]
            else:
                pass
    except:
        pass
    try:
        print(name)
        print(address)
        print(country)
        phone = str(phonelist)
        print(phone[2:-2])
        website = str(websitelist)
        print(website[2:-2])
        print(googlemaps)
        print(avgrate)
        print(hoursofoper)
        print('')
        count = count + 1
        csvfhand.writerow([name,address,country,phone[2:-2],website[2:-2],googlemaps,avgrate,hoursofoper])  # Make sure to update if needed
    except:
        continue

cur.close()
fhand.close()
print(count -1, "records written to CSV file")
