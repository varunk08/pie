import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
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


wm = World()
wm.title = "World Populations"
wm.add('2010', ccPopulations)
wm.render_to_file('worldPopulations.svg')
