'''Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah

Week 4, Ch. 12, Assignment #2

Version 1.3, Developed by Kyle DuBois.'''

import urllib.request, urllib.parse, urllib.error
import bs4

url = input('Enter URL: ')
count = input('Enter count: ')
try:
    cou = int(count)
except:
    quit()
position = input('Enter position: ')
try:
    pos = int(position)
except:
    quit()

# loop through url a set number of time the user will input
printcounter = 0
for i in range(cou):
    html = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # retrieve all the anchor tags
    tags = soup('a')
    # looks for tag of first 3 urls
    for tag in tags[:(pos)]:
        # looks for third tag
        if (printcounter == (pos - 1)):
            url = tag.get('href', None)
            print('Retrieving: ', url)
            printcounter = 0
            continue
        printcounter +=1
