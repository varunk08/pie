vehicles = ['scorpio', 'swift', 'bullet', 'subaru', 'polo']
print ("Your vehicles: ")
print(vehicles)

for vehicle in vehicles:
    print("Let's ride the " + vehicle)
    print(vehicle.title())
    print(vehicle.upper())
    print()

print("That's all the vehicles we have")


dates = ['coffee shop', 'down the road and trillium', 'the hideout', 'newbury street', '15 magnus ave sommerville']
for date in dates:
    print("Awesome time was during the date at: " + date.title())

topics = ['food', 'movies', 'books', 'places', 'politics', 'sexual orientation', 'gender identity', 'gender bias', 'religion', 'family']
num_topics = len(topics)
print("we discussed about " + format(num_topics) + " topics")
for topic in topics:
    print("We did discuss: " + topic.title())

for value in range(1,5):
    print(value)

squares = []
for num in range(1, 11):
    squares.append(num**2)
print(squares)
print(sum(squares))

twoPowers = [pow(2, value) for value in range(1, 11)]
print(twoPowers)

print("The last three topics we talked about were:")
for topic in topics[-3:]:
    print(topic.title())

femalesDated = ('sk', 'cl', 'kw', 'sb')
for gal in femalesDated:
    print("Thank you " + gal.upper())
