'''
Must run this script with api.py, bacth.py, abd init.py
script located in Github repository published by pembo13/brightlocal

Thsi script with retrieve all report and write associated information into a .CSV file
'''

import json
import pprint
import csv
from brightlocal import BrightLocalAPI, BrightLocalBatch



def testGetAllReports():
    with open('credentials.json', 'rb') as creds:
        credentials = json.load(creds)

        api_key = credentials['key'].encode('utf-8')
        api_secret = credentials['secret'].encode('utf-8')

        pass

    fhand = open('testGetAllReports.csv', 'w', newline='', encoding='utf-8')
    csvfhand = csv.writer(fhand)
    csvfhand.writerow(['Batch ID','Hospital Name','Campaign ID','Location ID'])

    # Set up API Wrappers
    api = BrightLocalAPI(key=api_key, secret=api_secret)
    batchapi = BrightLocalBatch(api=api)

    # Step 1: create a new batch
    batch_id = batchapi.create()

    print('Created Batch ID {}'.format(batch_id))
    csvfhand.writerow([batch_id,'','',''])

    # Step 2: Make GET request and retrieve results
    result = api.call(method='/v2/lsrc/get-all')

    pp = pprint.PrettyPrinter(indent=4)

    # pp.pprint(result['response']['results'])
    for item in result['response']['results']:
        campaign_id = item['campaign_id']
        location_id = item['location_id']
        hospname = item['name']
        print('Hosptial Name: ', hospname)
        print('Campaign ID: ', campaign_id)
        print('Location ID: ', location_id)
        print('')
        csvfhand.writerow(['',hospname,campaign_id,location_id])
        pass


    print('testGetAllReports.csv write with campaign information')

    fhand.close()
    return

testGetAllReports()
