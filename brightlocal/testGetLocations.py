import json
import pprint
import csv
from brightlocal import BrightLocalAPI, BrightLocalBatch



def testGetLocations():

    count = 0

    with open('credentials.json', 'rb') as creds:
        credentials = json.load(creds)

        api_key = credentials['key'].encode('utf-8')
        api_secret = credentials['secret'].encode('utf-8')

        pass

    fhand = open('testGetLocations.csv', 'w', newline='', encoding='utf-8')
    csvfhand = csv.writer(fhand)
    csvfhand.writerow(['Batch ID','Hospital Name','Hospital Address','Hospital City','Hospital State','Hospital Zip'])

    # Set up API Wrappers
    api = BrightLocalAPI(key=api_key, secret=api_secret)
    batchapi = BrightLocalBatch(api=api)

    # Step 1: create a new batch
    batch_id = batchapi.create()

    print('Created Batch ID {}'.format(batch_id))

    pp = pprint.PrettyPrinter(indent=4)

    # Step 2: Make GET request and retrieve results
    with open('LocationID.csv') as fh:
        next(fh)
        for location_id in fh:
            print(str(location_id))
            result = api.call(method='/v1/clients-and-locations/locations/'+location_id,
            http_method=BrightLocalAPI.HTTP_METHOD_GET)

            pp.pprint(result)
            count += 1

#             if count == 1:
#                 break

    return

testGetLocations()
