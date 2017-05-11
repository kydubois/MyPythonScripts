'''This programs opens a URL and searches through the html
find the <span> tag and then locates the numbers within the tag
finally it sums all the numbs and returns the total

Created for py4e Assignment Ch. 12, week 4
Developed by Kyle DuBois'''

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
