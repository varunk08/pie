import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from countryCode import getCountryCode

filename = 'population_data.json'
with open(filename) as f:
    popData = json.load(f)

ccPopulations = {}
for popDict in popData:
    if popDict['Year'] == '2010':
        countryName = popDict['Country Name']
        population = int(float(popDict['Value']))
        code = getCountryCode(countryName)
        if code:
            ccPopulations[code] = population

pops1, pops2, pops3 = {}, {}, {}
for cc, pop in ccPopulations.items():
	if pop < 10000000:
		pops1[cc] = pop
	elif pop < 1000000000:
		pops2[cc] = pop
	else:
		pops3[cc] = pop


wm_lightStyle = LightColorizedStyle
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World Populations"
wm.add('0-10m', pops1)
wm.add('10m-1bn', pops2)
wm.add('>1bn', pops3)
wm.render_to_file('worldPopulations.svg')
