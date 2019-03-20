import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Stats: ", r.status_code)

responseDict = r.json()
print(responseDict.keys())
print("Total repos: ", responseDict['total_count'])
print("Incomplete?: ", responseDict['incomplete_results'])

repoDicts = responseDict['items']
print('repositories returned: ', len(repoDicts))

repoDict = repoDicts[0]
print('\nKeys: ', len(repoDict))
print('Name: ', repoDict['name'])
print('Owner: ', repoDict['owner']['login'])
print('Repo: ', repoDict['html_url'])
print('Stars: ', repoDict['stargazers_count'])