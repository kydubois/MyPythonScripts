'''The program will ask for a URL and use urllib to read the HTML from the data files, 
and parse the data, extracting numbers and compute the sum of the numbers in the file.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)

Developed by Kyle DuBois, Version 1.0'''

import urllib.request, urllib.parse, urllib.error
import bs4
import re
numList = list()

url = input('Enter - ')

html = urllib.request.urlopen(url).read()

# beautifulsoup makes reading the html easy
soup = bs4.BeautifulSoup(html, "html.parser")

tags = soup('span')

# retrieve all the digits in the tags
# using regex
nums = re.findall(b'class=.+>(\d+)', html)
for num in nums:
    #print(num)
    newNum = float(num)
    numList.append(newNum)

print(sum(numList))
