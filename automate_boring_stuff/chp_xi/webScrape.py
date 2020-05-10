#! python3

# webbrowser
# requests
# beautifulSoup
# selenium

import webbrowser

# Beautiful soup 4
import bs4

import requests
import logging

res = open('example.html')
soup = bs4.BeautifulSoup(res.read(), features="html.parser")

# select() returns a set
elements = soup.select('#author')

print(type(elements))
print(str(len(elements)))

print("Printing the elements")
print(str(elements[0]))
print()

# getText returns only the data in the tag.
print(elements[0].getText())

print (elements[0].attrs)

pElems = soup.select('p')
print(str(pElems[0]))
print()
print(pElems[0].getText())

print(len(pElems))
for elem in pElems:
	if (elem.get('class')) is not None:
		print(elem.attrs)
		print(elem.getText())