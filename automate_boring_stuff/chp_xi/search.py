#! python3
# Opens the first 5 search results for the search keywords specified

import requests, bs4, sys, webbrowser

print('Googling...')
res = requests.get('http://bing.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
print(len(res.text))

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a new browser tab for each top result
linkElems = soup.select("li.b_algo > h2 > a")
print(str(len(linkElems)))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open(linkElems[i].get('href'))