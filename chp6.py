print("Chapter 6 - Dictionaries")

countries_visited = ['uk', 'usa', 'hungary', 'india', 'sri lanka', 'qatar', 'germany', 'canada']

# countries and frequency of visit
countries = {}

for country in countries_visited:
    countries[country] = 1
    print(country.title() + " " + format(countries[country]))