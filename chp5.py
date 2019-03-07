chapter = "chapter 5 - if statements"
print(chapter.title())

countries_visited = ['uk', 'usa', 'hungary', 'india', 'sri lanka', 'qatar', 'germany', 'canada']
next_countries = ['thailand', 'japan', 'malaysia', 'singapore', 'chile', 'india', 'canada']
for country in next_countries:
    if country not in countries_visited:
        print("You need to visit " + country.title() + " next.")
    else:
        print("You've already visited " + country.title())

    