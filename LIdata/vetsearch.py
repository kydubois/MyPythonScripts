'''This program is used to lookup the number of Veterinary Hospitals within a certain zip code.

Enter the 5 digit zip code you want to lookup in the prompt when you run this program.
You will only get 1,000 requests per day with this API key.

Developed by Kyle DuBois,  Version 1.3,  3/28/2018'''

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = # Add your own Google Place Web Serivces API key here

serviceurl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter a zip code or city: ')
    if len(address) < 1:
        break

    # Create URL address using a dictionary that contains serviceurl, address, and api_key
    parms = dict()
    parms['query'] = address
    parms['type'] = 'veterinary_care'
    parms['key'] = api_key
    # print(parms)
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Connecting to: ', url)
    #  We open the URL, which can either be a string or a Request object
    uh = urllib.request.urlopen(url, context=ctx)
    # We decode the returned bytestring
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print('')

    try:
        # We deserialize the decoded URL to a Python object
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    count = 0
    for results in js["results"]:
        print(results.get("name"))
        print(results.get("formatted_address"))
        print('')
        count = count + 1
    print(count, 'record(s) found')
