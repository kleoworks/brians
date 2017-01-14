import re

# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
# import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url), "html.parser")

# print soup # print soup to see the result!!

# your code here to find all the links from the result
# and complete the challenges below


# find all the a tags in the html doc
a_tags = soup.find_all("a")

#PART 1 -- UNIQUE LIST
# loop through all a_tags found, search text for regex pattern using a capture group "()" to capture the link text
# store only the unique values when found
# sort the values and print the list
a_list = []

for element in range(len(a_tags)):
    match = re.search(r'href="([A-Za-z0-9-._~:/?#@!$&*+,;=`.]+)"', str(a_tags[element]))
    if match:
        #check if the found link is not in the list and add it
        if match.group(1) not in a_list:
            a_list.append(match.group(1))

a_list.sort()

for element in range(len(a_list)):
    print a_list[element]


#PART 2 -- DICTIONARY w/ COUNTER OF EACH TIME LINK WAS FOUND
a_dict = {}

for element in range(len(a_tags)):
    match = re.search(r'href="([A-Za-z0-9-._~:/?#@!$&*+,;=`.]+)"', str(a_tags[element]))
    if match:
        #check if the found link is not in the dict and add it
        if match.group(1) not in a_dict:
            a_dict[match.group(1)] = 1
        else:
            #update the counter
            a_dict[match.group(1)] += 1

for item in sorted(a_dict.items()):
    print item
