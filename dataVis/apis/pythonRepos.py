import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status: ", r.status_code)

responseDict = r.json()
print('Keys: ')
print(responseDict.keys())
print("Total repos: ", responseDict['total_count'])
print("Incomplete?: ", responseDict['incomplete_results'])
repoDicts = responseDict['items']

names, plotDicts = [], []
for repoDict in repoDicts:
	names.append(repoDict['name'])

	description = repoDict['description']
	if not description:
		description = 'No description found.'

	plotDict = {
		'value' : repoDict['stargazers_count'],
		'label' : description,
		'xlink' : repoDict['html_url'],
	}
	plotDicts.append(plotDict)

myStyle = LS('#666633', base_style=LCS)
myStyle.title_font_size = 24
myStyle.label_font_size = 14
myStyle.major_font_size = 18

myConfig = pygal.Config()
myConfig.x_label_rotation = 45
myConfig.show_legend = False
myConfig.truncate_lable = 15
myConfig.show_y_guides = False
myConfig.width = 1000

chart = pygal.Bar(myConfig, style=myStyle)
chart.title = 'Most starred python projects on Github'
chart.x_labels = names

chart.add('', plotDicts)
chart.render_to_file('python_repos.svg')
