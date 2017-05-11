'''Note - this code must run in Python 2.x and you must download
http://python-data.dr-chuck.net/known_by_Fikret.html
Practice position 3 and count 4. Will retrive name srquence:
Fikret, Montgomery, Mhairade, Butchi, and Anayah'''

import urllib.request, urllib.parse, urllib.error
import bs4
import re


url = input('Enter URL: ')
count = input('Enter Count: ')
try:
    cot = int(count)
except:
    print('Please enter a valid number')
    quit()
position = input('Enter Position: ')
try:
    pos = int(position)
except:
    print('Please enter a valid number')
    quit()


while i in rang(cot):
    html = urllib.request.urlopen(url).read()

    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        #print('TAG:',tag)
        if tag == pos:
            url = tag.get('href', None)
            print('Retrieving: ',url)
            continue
        #print 'Contents:',tag.contents[0]
        #print 'Attrs:',tag.attrs
