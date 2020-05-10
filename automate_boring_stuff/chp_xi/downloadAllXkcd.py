#! python3

# Downloads all xkcd comic images!

import requests, bs4, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	# Download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, features='html.parser')

	# Find the URL of the comic image
	comicElem = soup.select("#comic img")
	if comicElem == []:
		print("Could not find comic image")
	else:
		comicUrl = 'http:' + comicElem[0].get('src')

		if 'xkcd.com' in comicUrl:
			# Dowload the image
			res = requests.get(comicUrl)
			if res.status_code == requests.codes.ok:
				# Save the image to the 'xkcd' folder
				imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
				imageFile.close()
		
	# Get the Prev button's url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')