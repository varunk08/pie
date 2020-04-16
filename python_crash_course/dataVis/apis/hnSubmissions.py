import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submissionIds = r.json()
#print(len(submissionIds))
submissionDicts = []
i = 0
for submissionId in submissionIds:
	url=('https://hacker-news.firebaseio.com/v0/item/' + str(submissionId) + '.json')
	submissionR = requests.get(url)
	print(str(i) + ': ' + str(submissionR.status_code))
	i += 1
	responseDict = submissionR.json()

	submissionDict = {
		'title': responseDict['title'],
		'link': 'http://news.ycombinator.com/item?id=' + str(submissionId),
		'comments': responseDict.get('descendants', 0)
	}
	submissionDicts.append(submissionDict)

submissionDicts = sorted(submissionDicts, key=itemgetter('comments'), reverse=False)
print(len(submissionDicts))
for submissionDict in submissionDicts:
	print("nTitle:", submissionDict['title'])
	print("DiscussionLink:", submissionDict['link'] )
	print("Comments:", submissionDict['comments'])